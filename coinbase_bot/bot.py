from __future__ import annotations

import argparse
import logging
import time
import uuid
from datetime import datetime, timedelta

from coinbase_bot.config import BotConfig, load_config
from coinbase_bot.exchange import CoinbaseAdvancedClient, floor_to_increment
from coinbase_bot.indicators import build_signal_frame
from coinbase_bot.state import BotState, OpenPosition, utc_now
from coinbase_bot.strategy import evaluate_long_entry


LOGGER = logging.getLogger("coinbase_bot")


def _extract_order_id(payload: dict) -> str | None:
    for path in [
        ("success_response", "order_id"),
        ("order_id",),
        ("order", "order_id"),
    ]:
        cursor = payload
        try:
            for key in path:
                cursor = cursor[key]
            if cursor:
                return str(cursor)
        except (KeyError, TypeError):
            continue
    return None


def _state_path_for_mode(base_path: Path, live: bool) -> Path:
    if live:
        return base_path
    return base_path.with_name("dry_run_state.json")


def _compute_quote_size(available_balance: float, config: BotConfig) -> float:
    tradable = max(0.0, available_balance - config.min_cash_reserve)
    desired = available_balance * config.per_trade_quote_fraction
    return min(tradable, desired)


def _build_order_body(product_id: str, quote_size: str, take_profit: str, stop_price: str) -> dict:
    return {
        "client_order_id": str(uuid.uuid4()),
        "product_id": product_id,
        "side": "BUY",
        "order_configuration": {
            "market_market_ioc": {
                "quote_size": quote_size,
            }
        },
        "attached_order_configuration": {
            "trigger_bracket_gtc": {
                "limit_price": take_profit,
                "stop_trigger_price": stop_price,
            }
        },
    }


def _close_dry_run_position(state: BotState, position: OpenPosition, exit_price: float, reason: str) -> None:
    pnl = position.planned_quote_size * ((exit_price - position.entry_price) / position.entry_price)
    state.close_position(position.product_id, pnl, utc_now())
    LOGGER.info(
        "Dry-run exit %s at %.2f (%s), pnl %.2f",
        position.product_id,
        exit_price,
        reason,
        pnl,
    )


def _reconcile_dry_run_position(state: BotState, position: OpenPosition, signal_frame) -> bool:
    entry_time = datetime.fromisoformat(position.entry_time)
    since_entry = signal_frame[signal_frame["start"] >= entry_time]
    if since_entry.empty:
        return False

    for _, candle in since_entry.iterrows():
        if candle["low"] <= position.stop_price and candle["high"] >= position.take_profit_price:
            _close_dry_run_position(state, position, position.stop_price, "stop_hit_same_candle")
            return True
        if candle["low"] <= position.stop_price:
            _close_dry_run_position(state, position, position.stop_price, "stop_hit")
            return True
        if candle["high"] >= position.take_profit_price:
            _close_dry_run_position(state, position, position.take_profit_price, "take_profit_hit")
            return True

    if position.close_deadline:
        deadline = datetime.fromisoformat(position.close_deadline)
        latest_time = signal_frame.iloc[-1]["start"].to_pydatetime()
        if latest_time >= deadline:
            _close_dry_run_position(state, position, float(signal_frame.iloc[-1]["close"]), "max_hold")
            return True

    return False


def _reconcile_live_position(
    state: BotState,
    position: OpenPosition,
    client: CoinbaseAdvancedClient,
    base_currency: str,
) -> bool:
    remaining = client.get_available_balance(base_currency)
    if remaining > 0:
        return False

    fills = client.get_fills(position.product_id, start_time=datetime.fromisoformat(position.entry_time))
    sell_fills = [fill for fill in fills if str(fill.get("side", "")).upper() == "SELL"]
    pnl = 0.0
    if sell_fills:
        total_size = sum(float(fill.get("size", 0.0)) for fill in sell_fills)
        if total_size > 0:
            total_proceeds = sum(float(fill.get("price", 0.0)) * float(fill.get("size", 0.0)) for fill in sell_fills)
            avg_exit = total_proceeds / total_size
            pnl = position.planned_quote_size * ((avg_exit - position.entry_price) / position.entry_price)

    state.close_position(position.product_id, pnl, utc_now())
    LOGGER.info("Live position %s reconciled closed, pnl %.2f", position.product_id, pnl)
    return True


def run_cycle(config: BotConfig, live: bool) -> None:
    state_path = _state_path_for_mode(config.state_path, live)
    state = BotState.load(state_path)
    client = CoinbaseAdvancedClient(require_auth=True)
    now = utc_now()

    for product_id in config.product_ids:
        try:
            product = client.get_product(product_id)
            candles = client.fetch_candles(product_id, config.granularity, config.lookback_candles)
            signal_frame = build_signal_frame(candles, config.strategy)
            position = state.position_for(product_id)

            if position is not None:
                was_closed = (
                    _reconcile_live_position(state, position, client, product.base_currency)
                    if live
                    else _reconcile_dry_run_position(state, position, signal_frame)
                )
                if not was_closed:
                    LOGGER.info("Position already open for %s, skipping new entry", product_id)
                    continue

            if state.open_position_count() >= config.max_open_positions:
                LOGGER.info("Max open positions reached, skipping %s", product_id)
                continue

            cooldown_seconds = config.strategy.cooldown_candles * config.granularity_seconds
            if state.in_cooldown(product_id, now, cooldown_seconds):
                LOGGER.info("%s still in cooldown", product_id)
                continue

            if state.realized_loss_today(now) >= config.max_daily_loss_quote:
                LOGGER.warning("Daily loss limit reached, no new positions will be opened")
                break

            decision = evaluate_long_entry(signal_frame, config.strategy, reference_price=product.price)
            if decision.action != "BUY":
                LOGGER.info("%s: %s", product_id, decision.reason)
                continue

            available_balance = client.get_available_balance(config.quote_currency)
            quote_size_value = _compute_quote_size(available_balance, config)
            if quote_size_value < max(config.min_quote_order_size, product.quote_min_size):
                LOGGER.info("%s: insufficient free %s balance for a new trade", product_id, config.quote_currency)
                continue

            quote_size = floor_to_increment(quote_size_value, product.quote_increment)
            take_profit = floor_to_increment(float(decision.take_profit_price), product.quote_increment)
            stop_price = floor_to_increment(float(decision.stop_price), product.quote_increment)
            order_body = _build_order_body(product_id, quote_size, take_profit, stop_price)

            if live:
                if not config.allow_live_trading:
                    raise RuntimeError("COINBASE_ALLOW_LIVE_TRADING is false")
                if product.trading_disabled:
                    LOGGER.warning("%s is currently not tradable on Coinbase", product_id)
                    continue
                if config.preview_live_orders:
                    preview = client.preview_order(order_body)
                    LOGGER.info("Preview accepted for %s: %s", product_id, preview)
                response = client.create_order(order_body)
                order_id = _extract_order_id(response)
                LOGGER.info("Live BUY submitted for %s: %s", product_id, response)
            else:
                order_id = None
                LOGGER.info("Dry-run BUY %s with payload %s", product_id, order_body)

            state.open_position(
                OpenPosition(
                    product_id=product_id,
                    entry_time=now.isoformat(),
                    entry_price=float(decision.entry_price),
                    stop_price=float(decision.stop_price),
                    take_profit_price=float(decision.take_profit_price),
                    planned_quote_size=float(quote_size),
                    client_order_id=order_body["client_order_id"],
                    exchange_order_id=order_id,
                    dry_run=not live,
                    close_deadline=(now + timedelta(
                        seconds=config.strategy.max_hold_candles * config.granularity_seconds
                    )).isoformat(),
                )
            )
            LOGGER.info(
                "Opened %s position on %s at %.2f, tp %.2f, stop %.2f, rr %.2f",
                "live" if live else "dry-run",
                product_id,
                decision.entry_price,
                decision.take_profit_price,
                decision.stop_price,
                decision.reward_risk or 0.0,
            )
        except Exception as exc:
            LOGGER.exception("Failed processing %s: %s", product_id, exc)

    state.save(state_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Coinbase spot mean-reversion bot.")
    parser.add_argument("--mode", choices=["dry-run", "live"], default="dry-run")
    parser.add_argument("--loop", action="store_true", help="Run continuously instead of a single cycle.")
    parser.add_argument(
        "--sleep-seconds",
        type=int,
        default=300,
        help="Delay between cycles when --loop is enabled.",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    config = load_config()
    try:
        if args.loop:
            while True:
                run_cycle(config, live=args.mode == "live")
                LOGGER.info("Sleeping for %s seconds before the next cycle", args.sleep_seconds)
                time.sleep(args.sleep_seconds)
        else:
            run_cycle(config, live=args.mode == "live")
    except Exception as exc:
        LOGGER.error("%s", exc)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
