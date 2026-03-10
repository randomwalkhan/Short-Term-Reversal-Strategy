# Coinbase Mean-Reversion Bot

This repository now contains two parts:

1. Research notebooks for reversal analysis.
2. A Coinbase Advanced Trade spot bot with backtesting, dry-run mode, and live execution support.

No strategy can honestly be described as "high win rate and stable" across all market regimes. The bot here is intentionally conservative: long-only spot trading, no leverage, no futures, no options, and no martingale.

## Important Security Step

Your Coinbase private key was pasted into chat. Treat it as compromised.

1. Revoke that API key in Coinbase immediately.
2. Create a new key with the minimum permissions needed for spot trading.
3. Put the replacement key in `.env`.
4. Never commit `.env` or private keys.

The official Coinbase SDK also warns against saving secrets directly in code.

## Strategy Choice

After reviewing public GitHub Coinbase bots and strategy repositories, this project does not blindly copy any "guaranteed profit" bot.

The selected approach is a moderate-risk spot mean-reversion strategy:

- Timeframe: `ONE_HOUR`
- Market: Coinbase spot pairs such as `BTC-USD`, `ETH-USD`, `SOL-USD`
- Direction: long only
- Entry filters:
  - close below the lower Bollinger Band
  - RSI oversold
  - `EMA50 > EMA200`
  - rising slow trend
  - ATR and volume filters
- Exit:
  - take profit near the Bollinger midline
  - stop loss at `1 x ATR`
  - maximum holding window
- Risk controls:
  - fixed fraction position sizing
  - minimum cash reserve
  - max one open position
  - cooldown after trades
  - daily realized loss cap

This design matches the reversal logic already present in the notebooks better than momentum-chasing Coinbase bots.

## GitHub References Reviewed

- Official Coinbase SDK: [coinbase/coinbase-advanced-py](https://github.com/coinbase/coinbase-advanced-py)
- Strategy library reference: [freqtrade/freqtrade-strategies](https://github.com/freqtrade/freqtrade-strategies)
- Example Coinbase automation bot reviewed but not adopted as-is:
  [albegonzalezp/coinbase_trader_bot](https://github.com/albegonzalezp/coinbase_trader_bot)

Why not copy the daily momentum bot directly:

- It chases recent winners instead of buying controlled pullbacks.
- It is less suitable for "moderate risk" spot trading.
- It has weaker risk controls than the bot implemented here.

## Project Layout

```text
coinbase_bot/
  backtest.py
  bot.py
  config.py
  exchange.py
  indicators.py
  state.py
  strategy.py
tests/
  test_strategy.py
Reversal2.0.ipynb
update_reversal_csv.ipynb
```

## Install

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configure

Create a local `.env` from the example:

```bash
cp .env.example .env
```

Set:

- `COINBASE_API_KEY`
- `COINBASE_API_SECRET`
- `BOT_PRODUCTS`
- risk values if you want to tune them

Live trading is disabled until you explicitly set:

```bash
COINBASE_ALLOW_LIVE_TRADING="true"
```

## Backtest First

Use Coinbase public candles:

```bash
python3 -m coinbase_bot.backtest --product BTC-USD --candles 500
```

Or use your own CSV:

```bash
python3 -m coinbase_bot.backtest --product BTC-USD --csv /path/to/candles.csv
```

The backtest is deliberately simple and should be used as a sanity check, not as proof that live performance will match.

## Dry Run

Dry-run does everything except place real orders:

```bash
python3 -m coinbase_bot.bot --mode dry-run
```

Continuous dry-run loop:

```bash
python3 -m coinbase_bot.bot --mode dry-run --loop --sleep-seconds 900
```

Dry-run state is written to:

```text
state/dry_run_state.json
```

## Live Trading

Only switch to live mode after:

1. Rotating the leaked API key.
2. Installing dependencies.
3. Running backtests.
4. Watching dry-run behavior for multiple days.
5. Reducing `BOT_PER_TRADE_QUOTE_FRACTION` if needed.

Then:

```bash
python3 -m coinbase_bot.bot --mode live
```

Continuous live loop:

```bash
python3 -m coinbase_bot.bot --mode live --loop --sleep-seconds 900
```

Live state is written to:

```text
state/live_state.json
```

The bot sends a market buy order with an attached bracket order using Coinbase Advanced Trade order APIs.

## Tests

```bash
python3 -m unittest discover -s tests
```

## Notebook Research

The original research notebooks are still here:

- `update_reversal_csv.ipynb`
- `Reversal2.0.ipynb`

They remain useful for signal research, but they are not execution code.

## Notes

- This bot assumes a dedicated quote balance and works best when you do not manually trade the same assets in the same account at the same time.
- If you want stronger execution guarantees, the next upgrade should be WebSocket-based order and fill reconciliation instead of REST polling only.
- If you want a safer rollout, start with only one product such as `BTC-USD`.
