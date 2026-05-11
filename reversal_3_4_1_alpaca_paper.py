from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from pandas.errors import EmptyDataError
import requests

import reversal_3_3_live as live


VERSION = "3.4.1-alpaca-paper.2"
BASE_DIR = Path(__file__).resolve().parent
RESULT_DIR = BASE_DIR / "results" / "reversal_3_4_1_alpaca_paper"
STATE_PATH = RESULT_DIR / "alpaca_state.json"
EVENTS_PATH = RESULT_DIR / "alpaca_events.csv"
TRADES_PATH = RESULT_DIR / "alpaca_trades.csv"
POSITIONS_PATH = RESULT_DIR / "alpaca_positions.csv"
DASHBOARD_PATH = RESULT_DIR / "README.md"
ENV_PATH = BASE_DIR / ".secrets" / "alpaca_paper.env"

EVENT_COLUMNS = ["timestamp_et", "trade_date_et", "slot", "event_type", "detail"]
TRADE_COLUMNS = [
    "position_id",
    "ticker",
    "contract_symbol",
    "entry_timestamp_et",
    "exit_timestamp_et",
    "entry_trade_date_et",
    "exit_trade_date_et",
    "entry_option_price",
    "exit_option_price",
    "contracts",
    "allocated_cash",
    "proceeds",
    "pnl",
    "return_pct",
    "exit_reason",
    "alpaca_entry_order_id",
    "alpaca_exit_order_id",
]
POSITION_COLUMNS = [
    "position_id",
    "ticker",
    "asset_type",
    "execution_mode",
    "entry_mode",
    "contract_symbol",
    "expiry",
    "strike",
    "entry_timestamp",
    "entry_trade_date",
    "entry_slot",
    "entry_spot",
    "entry_option_price",
    "contracts",
    "allocated_cash",
    "planned_tp_day1",
    "planned_tp_day2",
    "planned_stop",
    "success_rate",
    "matched_signals",
    "current_drop_pct",
    "timing_score",
    "early_entry_score",
    "alpaca_entry_order_id",
    "alpaca_entry_client_order_id",
    "status",
    "asof_et",
    "current_option_price",
    "current_bid",
    "current_ask",
    "position_value",
    "unrealized_pnl",
    "unrealized_return_pct",
    "business_days_held",
]
CSV_COLUMNS = {
    EVENTS_PATH.name: EVENT_COLUMNS,
    TRADES_PATH.name: TRADE_COLUMNS,
    POSITIONS_PATH.name: POSITION_COLUMNS,
}

STRATEGY_CAPITAL_CAP = float(os.getenv("ALPACA_PAPER_STRATEGY_CAPITAL_CAP", str(live.INITIAL_CAPITAL)))
FINAL_ORDER_STATES = {"filled", "canceled", "expired", "rejected", "replaced", "done_for_day"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=f"Run Reversal {VERSION} with Alpaca paper execution.")
    parser.add_argument("--now", default=None)
    parser.add_argument("--force-slot", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-git-publish", action="store_true")
    return parser.parse_args()


def load_env() -> None:
    if not ENV_PATH.exists():
        raise FileNotFoundError(f"Missing Alpaca paper env file: {ENV_PATH}")
    for line in ENV_PATH.read_text().splitlines():
        if not line or line.strip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


class AlpacaPaperClient:
    def __init__(self) -> None:
        load_env()
        self.base_url = os.environ.get("ALPACA_PAPER_BASE_URL", "https://paper-api.alpaca.markets/v2").rstrip("/")
        self.headers = {
            "APCA-API-KEY-ID": os.environ["ALPACA_PAPER_API_KEY"],
            "APCA-API-SECRET-KEY": os.environ["ALPACA_PAPER_API_SECRET"],
            "Content-Type": "application/json",
        }

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        response = requests.request(method, self.base_url + path, headers=self.headers, timeout=30, **kwargs)
        if not response.ok:
            raise RuntimeError(f"Alpaca {method} {path} failed: {response.status_code} {response.text[:500]}")
        return response.json() if response.text else {}

    def account(self) -> dict[str, Any]:
        return self.request("GET", "/account")

    def clock(self) -> dict[str, Any]:
        return self.request("GET", "/clock")

    def order(self, order_id: str) -> dict[str, Any]:
        return self.request("GET", f"/orders/{order_id}")

    def submit_order(self, payload: dict[str, Any]) -> dict[str, Any]:
        return self.request("POST", "/orders", json=payload)

    def option_contract(self, symbol: str) -> dict[str, Any]:
        return self.request("GET", f"/options/contracts/{symbol}")


def ensure_dirs() -> None:
    RESULT_DIR.mkdir(parents=True, exist_ok=True)


def load_state() -> dict[str, Any]:
    if STATE_PATH.exists():
        state = json.loads(STATE_PATH.read_text())
    else:
        state = {"version": VERSION, "positions": [], "blocked_trade_dates": [], "start_date": live.LIVE_START_DATE}
    state.setdefault("version", VERSION)
    state.setdefault("positions", [])
    state.setdefault("blocked_trade_dates", [])
    return state


def save_state(state: dict[str, Any]) -> None:
    state["version"] = VERSION
    STATE_PATH.write_text(json.dumps(state, indent=2, sort_keys=True))


def load_csv(path: Path) -> pd.DataFrame:
    if path.exists() and path.stat().st_size:
        try:
            return pd.read_csv(path)
        except EmptyDataError:
            return pd.DataFrame(columns=CSV_COLUMNS.get(path.name, []))
    return pd.DataFrame(columns=CSV_COLUMNS.get(path.name, []))


def save_csv(path: Path, df: pd.DataFrame) -> None:
    df.to_csv(path, index=False)


def append_event(events_df: pd.DataFrame, now_et: pd.Timestamp, slot: str | None, event_type: str, detail: dict[str, Any]) -> pd.DataFrame:
    row = {
        "timestamp_et": now_et.isoformat(),
        "trade_date_et": now_et.date().isoformat(),
        "slot": slot or "manual",
        "event_type": event_type,
        "detail": json.dumps(detail, ensure_ascii=False, sort_keys=True),
    }
    return pd.concat([events_df, pd.DataFrame([row])], ignore_index=True)


def has_entry_today(state: dict[str, Any], trades_df: pd.DataFrame, events_df: pd.DataFrame, trade_date: str) -> bool:
    if trade_date in set(map(str, state.get("blocked_trade_dates", []))):
        return True
    return live.has_entry_on_trade_date(state, trades_df, events_df, trade_date)


def round_price(value: float) -> str:
    return f"{max(float(value), 0.01):.2f}"


def choose_alpaca_order_prices(selected: pd.Series) -> tuple[float, float]:
    bid = float(selected.get("bid", np.nan))
    ask = float(selected.get("ask", np.nan))
    mark = float(selected.get("mark_price", np.nan))
    entry_limit = ask if np.isfinite(ask) and ask > 0 else mark
    reference_price = mark if np.isfinite(mark) and mark > 0 else entry_limit
    return float(entry_limit), float(reference_price)


def find_entry_candidate(summary_df: pd.DataFrame, entry_mode: str) -> pd.Series | None:
    if summary_df.empty:
        return None
    col = "early_entry_candidate" if entry_mode == "early" else "call_candidate"
    candidates = summary_df[summary_df[col].fillna(False)].copy()
    if candidates.empty:
        return None
    if entry_mode == "early":
        candidates = candidates.sort_values(
            ["early_entry_score", "success_rate_%", "matched_signals", "current_drop_%"],
            ascending=[False, False, False, False],
            na_position="last",
        )
    return candidates.iloc[0]


def submit_entry(
    client: AlpacaPaperClient,
    state: dict[str, Any],
    events_df: pd.DataFrame,
    now_et: pd.Timestamp,
    slot: str,
    summary_df: pd.DataFrame,
    entry_mode: str,
    dry_run: bool,
) -> tuple[dict[str, Any], pd.DataFrame]:
    candidate = find_entry_candidate(summary_df, entry_mode)
    if candidate is None:
        return state, append_event(events_df, now_et, slot, "entry_skipped", {"reason": "no_candidate", "entry_mode": entry_mode})

    ticker = str(candidate["ticker"])
    spot = float(candidate["live_price_raw"])
    try:
        calls = live.fetch_call_candidates(ticker, spot=spot)
        selected = calls.iloc[0]
        liquid, liquidity_status = live.assess_option_entry_liquidity(selected)
        if not liquid:
            return state, append_event(
                events_df,
                now_et,
                slot,
                "entry_skipped",
                {
                    "ticker": ticker,
                    "reason": "no_trade_low_option_liquidity",
                    "option_liquidity_status": liquidity_status,
                    "entry_mode": entry_mode,
                },
            )
        contract_symbol = str(selected["contractSymbol"])
        contract = client.option_contract(contract_symbol)
        if not contract.get("tradable", False):
            return state, append_event(events_df, now_et, slot, "entry_skipped", {"ticker": ticker, "reason": "alpaca_option_not_tradable", "contract_symbol": contract_symbol})
    except Exception as exc:
        return state, append_event(events_df, now_et, slot, "entry_skipped", {"ticker": ticker, "reason": "option_selection_failed", "error": str(exc)[:300]})

    account = client.account()
    cash = float(account.get("cash", 0))
    portfolio_value = float(account.get("portfolio_value", 0))
    strategy_equity = min(portfolio_value, STRATEGY_CAPITAL_CAP)
    budget = min(cash, strategy_equity * live.TARGET_POSITION_WEIGHT)
    entry_limit, reference_price = choose_alpaca_order_prices(selected)
    contracts = int(budget // (entry_limit * 100))
    if contracts <= 0:
        return state, append_event(events_df, now_et, slot, "entry_skipped", {"ticker": ticker, "reason": "insufficient_cash", "budget": round(budget, 2), "entry_limit": entry_limit})

    payload = {
        "symbol": contract_symbol,
        "qty": str(contracts),
        "side": "buy",
        "type": "limit",
        "time_in_force": "day",
        "limit_price": round_price(entry_limit),
        "client_order_id": f"rev-{now_et.strftime('%Y%m%d%H%M%S')}-{ticker}-{entry_mode}".lower(),
    }
    if dry_run:
        return state, append_event(events_df, now_et, slot, "entry_dry_run", {"ticker": ticker, "payload": {**payload, "limit_price": payload["limit_price"]}})

    order = client.submit_order(payload)
    position = {
        "position_id": f"{ticker}_{now_et.strftime('%Y%m%dT%H%M%S')}",
        "ticker": ticker,
        "asset_type": "option",
        "execution_mode": "alpaca_paper_option",
        "entry_mode": entry_mode,
        "contract_symbol": contract_symbol,
        "expiry": pd.Timestamp(selected["expiry"]).date().isoformat(),
        "strike": float(selected["strike"]),
        "entry_timestamp": now_et.isoformat(),
        "entry_trade_date": now_et.date().isoformat(),
        "entry_slot": slot,
        "entry_spot": spot,
        "entry_option_price": reference_price,
        "contracts": contracts,
        "allocated_cash": reference_price * 100 * contracts,
        "planned_tp_day1": reference_price * (1 + live.DAY1_TAKE_PROFIT_PCT),
        "planned_tp_day2": reference_price * (1 + live.DAY2_TAKE_PROFIT_PCT),
        "planned_stop": reference_price * (1 - live.STOP_LOSS_PCT),
        "success_rate": float(candidate["success_rate_%"]),
        "matched_signals": int(candidate["matched_signals"]),
        "current_drop_pct": float(candidate["current_drop_%"]),
        "timing_score": float(candidate.get("timing_score", np.nan)) if pd.notna(candidate.get("timing_score")) else np.nan,
        "early_entry_score": float(candidate.get("early_entry_score", np.nan)) if pd.notna(candidate.get("early_entry_score")) else np.nan,
        "alpaca_entry_order_id": order["id"],
        "alpaca_entry_client_order_id": order.get("client_order_id"),
        "status": "entry_submitted",
    }
    state["positions"].append(position)
    return state, append_event(
        events_df,
        now_et,
        slot,
        "entry_order_submitted",
        {
            "ticker": ticker,
            "contract_symbol": contract_symbol,
            "contracts": contracts,
            "limit_price": payload["limit_price"],
            "entry_mode": entry_mode,
            "alpaca_order_id": order["id"],
        },
    )


def reconcile_orders(
    client: AlpacaPaperClient,
    state: dict[str, Any],
    trades_df: pd.DataFrame,
    events_df: pd.DataFrame,
    now_et: pd.Timestamp,
) -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame]:
    remaining = []
    for pos in state.get("positions", []):
        status = str(pos.get("status", "open"))
        if status == "entry_submitted":
            order = client.order(pos["alpaca_entry_order_id"])
            order_status = str(order.get("status", ""))
            if order_status == "filled":
                filled_price = float(order.get("filled_avg_price") or pos["entry_option_price"])
                filled_qty = int(float(order.get("filled_qty") or pos["contracts"]))
                pos["status"] = "open"
                pos["entry_option_price"] = filled_price
                pos["contracts"] = filled_qty
                pos["allocated_cash"] = filled_price * 100 * filled_qty
                pos["planned_tp_day1"] = filled_price * (1 + live.DAY1_TAKE_PROFIT_PCT)
                pos["planned_tp_day2"] = filled_price * (1 + live.DAY2_TAKE_PROFIT_PCT)
                pos["planned_stop"] = filled_price * (1 - live.STOP_LOSS_PCT)
                events_df = append_event(events_df, now_et, pos.get("entry_slot"), "entry_filled", {"ticker": pos["ticker"], "contract_symbol": pos["contract_symbol"], "filled_price": filled_price, "contracts": filled_qty})
                remaining.append(pos)
            elif order_status in FINAL_ORDER_STATES:
                events_df = append_event(events_df, now_et, pos.get("entry_slot"), "entry_not_filled", {"ticker": pos["ticker"], "contract_symbol": pos["contract_symbol"], "status": order_status})
            else:
                remaining.append(pos)
        elif status == "exit_submitted":
            order = client.order(pos["alpaca_exit_order_id"])
            order_status = str(order.get("status", ""))
            if order_status == "filled":
                exit_price = float(order.get("filled_avg_price") or pos.get("exit_reference_price") or 0)
                proceeds = exit_price * 100 * int(pos["contracts"])
                pnl = proceeds - float(pos["entry_option_price"]) * 100 * int(pos["contracts"])
                trade = {
                    "position_id": pos["position_id"],
                    "ticker": pos["ticker"],
                    "contract_symbol": pos["contract_symbol"],
                    "entry_timestamp_et": pos["entry_timestamp"],
                    "exit_timestamp_et": now_et.isoformat(),
                    "entry_trade_date_et": pos["entry_trade_date"],
                    "exit_trade_date_et": now_et.date().isoformat(),
                    "entry_option_price": pos["entry_option_price"],
                    "exit_option_price": exit_price,
                    "contracts": pos["contracts"],
                    "allocated_cash": pos["allocated_cash"],
                    "proceeds": proceeds,
                    "pnl": pnl,
                    "return_pct": pnl / float(pos["allocated_cash"]) * 100 if float(pos["allocated_cash"]) > 0 else np.nan,
                    "exit_reason": pos.get("exit_reason"),
                    "alpaca_entry_order_id": pos.get("alpaca_entry_order_id"),
                    "alpaca_exit_order_id": pos.get("alpaca_exit_order_id"),
                }
                trades_df = pd.concat([trades_df, pd.DataFrame([trade])], ignore_index=True)
                events_df = append_event(events_df, now_et, "exit", "exit_filled", {"ticker": pos["ticker"], "contract_symbol": pos["contract_symbol"], "exit_price": exit_price, "pnl": round(pnl, 2), "reason": pos.get("exit_reason")})
            elif order_status in FINAL_ORDER_STATES:
                pos["status"] = "open"
                pos.pop("alpaca_exit_order_id", None)
                events_df = append_event(events_df, now_et, "exit", "exit_not_filled", {"ticker": pos["ticker"], "contract_symbol": pos["contract_symbol"], "status": order_status})
                remaining.append(pos)
            else:
                remaining.append(pos)
        else:
            remaining.append(pos)
    state["positions"] = remaining
    return state, trades_df, events_df


def mark_positions(state: dict[str, Any], now_et: pd.Timestamp) -> pd.DataFrame:
    rows = []
    for pos in state.get("positions", []):
        if pos.get("status") not in {"open", "exit_submitted"}:
            rows.append({**pos, "current_option_price": np.nan, "unrealized_pnl": np.nan, "unrealized_return_pct": np.nan})
            continue
        quote = live.fetch_contract_quote(pos["ticker"], pos["expiry"], pos["contract_symbol"], pos["strike"])
        current_price = float(quote["mark_price"])
        value = current_price * 100 * int(pos["contracts"])
        pnl = value - float(pos["entry_option_price"]) * 100 * int(pos["contracts"])
        rows.append({
            **pos,
            "asof_et": now_et.isoformat(),
            "current_option_price": current_price,
            "current_bid": quote.get("bid"),
            "current_ask": quote.get("ask"),
            "position_value": value,
            "unrealized_pnl": pnl,
            "unrealized_return_pct": pnl / float(pos["allocated_cash"]) * 100 if float(pos["allocated_cash"]) > 0 else np.nan,
            "business_days_held": live.business_days_since(pos["entry_trade_date"], now_et.date().isoformat()),
        })
    if not rows:
        return pd.DataFrame(columns=POSITION_COLUMNS)
    return pd.DataFrame(rows)


def submit_exits(
    client: AlpacaPaperClient,
    state: dict[str, Any],
    events_df: pd.DataFrame,
    now_et: pd.Timestamp,
    slot: str | None,
    dry_run: bool,
) -> tuple[dict[str, Any], pd.DataFrame]:
    if not slot or not slot.startswith("manage_"):
        return state, events_df
    for pos in state.get("positions", []):
        if pos.get("status") != "open":
            continue
        quote = live.fetch_contract_quote(pos["ticker"], pos["expiry"], pos["contract_symbol"], pos["strike"])
        current = float(quote["mark_price"])
        bid = float(quote.get("bid", np.nan))
        business_days_held = live.business_days_since(pos["entry_trade_date"], now_et.date().isoformat())
        target = float(pos["planned_tp_day1"] if business_days_held <= 1 else pos["planned_tp_day2"])
        reason = None
        if current <= float(pos["planned_stop"]):
            reason = "stop_loss_hit_at_scan"
        elif current >= target:
            reason = "take_profit_day1_hit_at_scan" if business_days_held <= 1 else "take_profit_day2_hit_at_scan"
        elif business_days_held >= 2 and slot == "manage_1600":
            reason = "time_exit_at_4pm_scan"
        if reason is None:
            continue
        limit_price = bid if np.isfinite(bid) and bid > 0 else current
        payload = {
            "symbol": pos["contract_symbol"],
            "qty": str(int(pos["contracts"])),
            "side": "sell",
            "type": "limit",
            "time_in_force": "day",
            "limit_price": round_price(limit_price),
            "client_order_id": f"rev-exit-{now_et.strftime('%Y%m%d%H%M%S')}-{pos['ticker']}".lower(),
        }
        if dry_run:
            events_df = append_event(events_df, now_et, slot, "exit_dry_run", {"ticker": pos["ticker"], "reason": reason, "payload": payload})
            continue
        order = client.submit_order(payload)
        pos["status"] = "exit_submitted"
        pos["alpaca_exit_order_id"] = order["id"]
        pos["exit_reason"] = reason
        pos["exit_reference_price"] = limit_price
        events_df = append_event(events_df, now_et, slot, "exit_order_submitted", {"ticker": pos["ticker"], "contract_symbol": pos["contract_symbol"], "reason": reason, "limit_price": payload["limit_price"], "alpaca_order_id": order["id"]})
    return state, events_df


def render_dashboard(account: dict[str, Any], positions_df: pd.DataFrame, trades_df: pd.DataFrame, events_df: pd.DataFrame, now_et: pd.Timestamp, slot: str | None) -> None:
    lines = [
        f"# Reversal {VERSION}",
        "",
        f"Latest checkpoint (ET): `{now_et.strftime('%Y-%m-%d %H:%M:%S %Z')}`",
        f"Last slot: `{slot or 'manual'}`",
        "",
        "## Alpaca Paper Account",
        "",
        f"- Status: `{account.get('status')}`",
        f"- Cash: `${float(account.get('cash', 0)):,.2f}`",
        f"- Portfolio value: `${float(account.get('portfolio_value', 0)):,.2f}`",
        f"- Strategy capital cap: `${STRATEGY_CAPITAL_CAP:,.2f}`",
        f"- Options level: `{account.get('options_trading_level', account.get('options_approved_level', 'unknown'))}`",
        "",
        "## Open / Pending Positions",
        "",
        live.format_table(positions_df, columns=["ticker", "status", "entry_mode", "contract_symbol", "contracts", "entry_option_price", "current_option_price", "position_value", "unrealized_pnl", "unrealized_return_pct", "business_days_held"], max_rows=20),
        "",
        "## Closed Trades",
        "",
        live.format_table(trades_df.tail(20), columns=["ticker", "contract_symbol", "entry_trade_date_et", "exit_trade_date_et", "entry_option_price", "exit_option_price", "contracts", "pnl", "return_pct", "exit_reason"], max_rows=20),
        "",
        "## Recent Events",
        "",
        live.format_table(events_df.tail(20).sort_values("timestamp_et", ascending=False), columns=["timestamp_et", "slot", "event_type", "detail"], max_rows=20),
    ]
    DASHBOARD_PATH.write_text("\n".join(lines))


def maybe_git_publish(now_et: pd.Timestamp, skip: bool) -> None:
    if skip:
        return
    try:
        subprocess.run(["git", "add", str(RESULT_DIR.relative_to(BASE_DIR)), "reversal_3_4_1_alpaca_paper.py", ".gitignore"], cwd=BASE_DIR, check=True)
        if subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=BASE_DIR).returncode == 0:
            return
        subprocess.run(["git", "commit", "-m", f"Update Reversal Alpaca paper {now_et.strftime('%Y-%m-%d %H:%M ET')}"], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
    except Exception as exc:
        print(f"git publish skipped/failed: {exc}")


def run_cycle(args: argparse.Namespace) -> dict[str, Any]:
    ensure_dirs()
    now_et = live.now_et_from_arg(args.now)
    slot = live.slot_key_for_timestamp(now_et, args.force_slot)
    early_slot = live.early_entry_slot_key_for_timestamp(now_et)
    effective_slot = slot or early_slot
    closure_detail = live.market_closure_reason(now_et)

    client = AlpacaPaperClient()
    state = load_state()
    events_df = load_csv(EVENTS_PATH)
    trades_df = load_csv(TRADES_PATH)

    state, trades_df, events_df = reconcile_orders(client, state, trades_df, events_df, now_et)

    no_action_slot = effective_slot is None or str(effective_slot).startswith("share_ext_")
    if not state.get("positions") and (closure_detail is not None or no_action_slot):
        account = client.account()
        return {
            "timestamp_et": now_et.isoformat(),
            "slot": effective_slot,
            "open_or_pending_positions": 0,
            "alpaca_cash": round(float(account.get("cash", 0)), 2),
            "alpaca_portfolio_value": round(float(account.get("portfolio_value", 0)), 2),
            "dry_run": bool(args.dry_run),
            "skipped": "no_action_window",
        }

    if closure_detail is None:
        state, events_df = submit_exits(client, state, events_df, now_et, slot, args.dry_run)

    if closure_detail is None and early_slot and not has_entry_today(state, trades_df, events_df, now_et.date().isoformat()):
        summary, _, _ = live.screen_live_candidates(live.build_universe(), now_et=now_et)
        state, events_df = submit_entry(client, state, events_df, now_et, early_slot, summary, "early", args.dry_run)
    elif closure_detail is None and slot == "entry_1500" and not has_entry_today(state, trades_df, events_df, now_et.date().isoformat()):
        summary, _, _ = live.screen_live_candidates(live.build_universe(), now_et=now_et)
        state, events_df = submit_entry(client, state, events_df, now_et, slot, summary, "regular", args.dry_run)
    elif closure_detail is not None:
        events_df = append_event(events_df, now_et, effective_slot, "market_closed", closure_detail)

    account = client.account()
    positions_df = mark_positions(state, now_et)

    if not args.dry_run:
        save_state(state)
        save_csv(EVENTS_PATH, events_df)
        save_csv(TRADES_PATH, trades_df)
        save_csv(POSITIONS_PATH, positions_df)
        render_dashboard(account, positions_df, trades_df, events_df, now_et, effective_slot)
        maybe_git_publish(now_et, args.skip_git_publish)

    return {
        "timestamp_et": now_et.isoformat(),
        "slot": effective_slot,
        "open_or_pending_positions": len(state.get("positions", [])),
        "alpaca_cash": round(float(account.get("cash", 0)), 2),
        "alpaca_portfolio_value": round(float(account.get("portfolio_value", 0)), 2),
        "dry_run": bool(args.dry_run),
    }


def main() -> None:
    result = run_cycle(parse_args())
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
