# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 16:05:04 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-22)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-22T15:10:06.051324-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00       entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_trade_after_option_and_timing_filters"}
2026-09-22T14:50:01.294026-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.621, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.01, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.504}
2026-09-22T14:50:01.294026-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"early_entry_score": 0.689, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 24.88, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.507}
2026-09-22T14:50:01.294026-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-22", "training_samples": 5799, "window": 5}
2026-09-22T12:00:04.192622-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.559, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:55:04.534124-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922160504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922160504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922160504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922160504)

</details>
