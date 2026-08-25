# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 10:50:06 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$30,388.00`
- Equity: `$57,185.50`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$-517.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 26797.5        30.35          29.78      310.66        310.29          bid_ask_mid                      29.78                bid_ask_mid                    True          -517.5                  -1.89          87.5               32              1.06         63.04           63.15                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.35               34            1.20              1.44        170.71               115.46         0.773          pass              0.477             58.8                           0.497                9.87              1.104                  ok            True                  False
  GEHC           96.77               31            0.82              0.43         74.01                49.18         0.597          pass              0.722             40.8                           0.530                1.14              0.221                  ok            True                  False
   TRI           90.91               11            2.92              2.22        107.67                67.11         0.596          pass              0.394             12.4                           0.131                1.24              0.400                  ok            True                  False
  DXCM           88.24               34            0.68              0.43         90.87                50.36         0.581          pass              0.583             48.3                           0.427                1.02              0.103                  ok            True                  False
  WDAY           80.00               30            2.08              2.90        197.91                78.88         0.567          pass              0.288             32.7                           0.236                7.58              0.731                  ok            True                  False
   KHC           86.36               22            1.19              0.21         25.58                37.91         0.555          pass              0.397             30.7                           0.402                2.90              0.354                  ok            True                  False
  PAYX          100.00               25            0.64              0.57        125.77                34.31         0.543          pass              0.731             58.9                           0.573                3.22              0.333                  ok            True                  False
  FAST          100.00               21            0.87              0.31         51.15                22.00         0.541          pass              0.639             37.3                           0.394               -2.95             -0.216                  ok            True                  False
   KDP           85.00               20            1.49              0.34         32.36                31.66         0.518          pass              0.255              1.0                           0.077                9.75              0.884                  ok            True                  False
  MDLZ           90.91               22            1.25              0.57         64.46                26.88         0.511          pass              0.520             32.5                           0.606                3.42              0.380                  ok            True                  False
   ROP          100.00               20            1.54              4.48        413.59                32.18         0.502          pass              0.703             62.0                           0.372                2.41              0.476                  ok            True                  False
  INTU           82.61               23            2.42              6.27        367.23                48.36         0.502          pass              0.256             16.7                           0.251                7.29              0.902                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-08-25T10:50:06.625543-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:45:01.788012-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "DXCM261002C00091000", "current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "entry_ask": 5.0, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 4.15, "hypothetical_budget": 15194.0, "hypothetical_contracts": 36, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 40.96, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.59, "shadow_only": true, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "matched_signals": 38, "recovery_stability_score": 0.59, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T10:40:03.785417-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:35:02.544392-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:30:01.796364-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:25:02.779045-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:20:01.784831-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:15:01.792883-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:10:01.860034-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:05:04.691112-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825105006)

</details>
