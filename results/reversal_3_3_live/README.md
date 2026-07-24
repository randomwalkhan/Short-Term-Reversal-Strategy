# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 15:55:02 EDT`
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

- Cash: `$17,668.00`
- Equity: `$34,418.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$375.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  GILD     option         option GILD260918C00130000       2026-07-24                   0     25     16375.0                 16750.0         6.55            6.7       129.9        129.51          bid_ask_mid                        6.7                bid_ask_mid                    True           375.0                   2.29         91.67               24              0.73         32.92           35.03                  35.55                1088.0           26.0               0.05                      ok
```

## Today's Closed Trades (2026-07-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00320000     13          2026-07-23         2026-07-24       11.225      13.675 3185.0   21.826281 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GILD           91.30               23            0.89              0.81        130.51                35.55         0.563            pass              0.499             18.1                           0.178               -0.10             -0.054                                 ok            True                  False
   HON           83.33               18            1.40              2.41        245.24                40.09         0.533            pass              0.351             51.9                           0.646                7.25              0.870                                 ok            True                  False
  ASML           95.24               21            2.70             34.12       1788.38                56.08         0.522            pass              0.594             22.8                           0.439               -2.40              0.051                                 ok            True                  False
  PANW           95.65               46            0.53              1.22        325.11                61.92         0.511            pass              0.819             55.8                           0.399               -0.62             -0.295                                 ok            True                  False
  META           72.22               18            1.73              7.33        602.96                54.86         0.597            pass              0.113              0.0                           0.183              -10.99             -1.093 downtrend_blocked_slope_and_streak           False                  False
  KLAC           78.57               14            4.30              6.59        215.91                98.03         0.589            pass              0.136             16.7                           0.381               -9.59             -0.816 downtrend_blocked_slope_and_streak           False                  False
   KDP           93.94               33            0.02              0.00         29.67                36.62         0.579            pass              0.872             96.3                           0.523               -6.33             -0.523 downtrend_blocked_slope_and_streak           False                  False
   WBD           94.12               17            0.69              0.13         25.90                21.83         0.561            pass              0.509             10.0                           0.097               -3.08             -0.613            downtrend_blocked_slope           False                  False
  CRWD           91.30               46            0.13              0.17        183.35                61.02         0.541            pass              0.808             84.2                           0.495               -2.14             -0.658 downtrend_blocked_slope_and_streak           False                  False
   APP           77.14               35            2.08              5.81        396.37                79.31         0.525            pass              0.309             30.0                           0.230              -22.96             -1.918            downtrend_blocked_slope           False                  False
  UPRO           87.18               39            0.16              0.15        136.06                34.86         0.505            pass              0.641             68.5                           0.428               -7.01             -0.644            downtrend_blocked_slope           False                  False
  MSTR           71.43               35            1.90              1.25         93.10                85.75         0.497 below_threshold              0.378             54.0                           0.383               -2.95              0.109                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-24T15:10:06.419772-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-24T15:05:03.522313-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-24T15:00:03.423809-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-24T14:55:06.458168-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-07-24T14:50:06.472791-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 16375.0, "asset_type": "option", "contract_symbol": "GILD260918C00130000", "contracts": 25, "early_entry_score": 0.558, "entry_mode": "regular", "entry_option_price": 6.55, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 1088.0, "option_spread_pct": 4.58, "option_volume": 26.0, "success_rate": 91.67, "ticker": "GILD", "timing_score": 0.567}
2026-07-24T14:50:06.472791-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-24", "training_samples": 5523, "window": 5}
2026-07-24T12:00:04.447749-04:00 early_entry_1200 early_entry_shadow        {"contract_symbol": "ASML260918C01790000", "current_drop_pct": 0.6, "early_entry_score": 0.84, "early_reclaim_pct": 78.1, "entry_ask": 155.4, "entry_bid": 151.0, "entry_mode": "early", "entry_option_price": 153.2, "hypothetical_budget": 17021.5, "hypothetical_contracts": 1, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 3.0, "option_spread_pct": 2.87, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.83, "shadow_only": true, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.58, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.84, "early_reclaim_pct": 78.1, "matched_signals": 35, "recovery_stability_score": 0.83, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.58, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-24T11:55:05.489069-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ASML260828C01785000", "current_drop_pct": 0.92, "early_entry_score": 0.781, "early_reclaim_pct": 66.4, "entry_ask": 129.0, "entry_bid": 115.0, "entry_mode": "early", "entry_option_price": 122.0, "hypothetical_budget": 17021.5, "hypothetical_contracts": 1, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 11.48, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.77, "shadow_only": true, "success_rate": 93.94, "ticker": "ASML", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.781, "early_reclaim_pct": 66.4, "matched_signals": 33, "recovery_stability_score": 0.77, "success_rate": 93.94, "ticker": "ASML", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-24T11:50:02.496150-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:45:02.490359-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724155502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724155502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724155502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724155502)

</details>
