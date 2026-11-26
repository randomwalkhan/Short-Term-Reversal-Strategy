# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-26 13:52:15 EST`
Last processed slot: `manage_1400`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-26)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot    event_type                                                         detail
2026-11-26T13:52:15.125563-05:00 manage_1400 market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T13:36:19.297790-05:00 manage_1330  slot_skipped                                {"reason": "already_processed"}
2026-11-26T13:20:06.113819-05:00 manage_1330 market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T13:15:06.250648-05:00      manual market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T13:10:38.030914-05:00 manage_1300  slot_skipped                                {"reason": "already_processed"}
2026-11-26T13:08:13.836178-05:00 manage_1300  slot_skipped                                {"reason": "already_processed"}
2026-11-26T12:50:44.329934-05:00 manage_1300 market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T12:35:18.345099-05:00 manage_1230  slot_skipped                                {"reason": "already_processed"}
2026-11-26T12:26:27.805585-05:00 manage_1230 market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T12:11:07.096021-05:00 manage_1200  slot_skipped                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261126135215)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261126135215)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261126135215)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261126135215)

</details>
