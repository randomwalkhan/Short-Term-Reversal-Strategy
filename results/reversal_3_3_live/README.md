# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 11:20:01 EDT`
Last processed slot: `manage_1130`

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
- Equity: `$57,343.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$-360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 26955.0        30.35          29.95      310.66        313.68          bid_ask_mid                      29.95                bid_ask_mid                    True          -360.0                  -1.32          87.5               32              1.06         63.04           59.31                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  TEAM           81.82               33            1.65              1.97        170.48               115.46         0.757          pass              0.408             43.4                           0.312                9.37              1.084                      ok            True                  False
   TRI           90.00               10            3.02              2.30        107.64                67.11         0.595          pass              0.354              9.4                           0.174                1.13              0.395                      ok            True                  False
  DXCM           88.57               35            0.63              0.40         90.89                50.36         0.578          pass              0.609             52.0                           0.477                1.07              0.105                      ok            True                  False
  GEHC           97.37               38            0.54              0.28         74.07                49.18         0.572          pass              0.827             61.2                           0.673                1.43              0.234                      ok            True                   True
  WDAY           82.14               28            2.36              3.29        197.74                78.88         0.566          pass              0.304             23.6                           0.244                7.27              0.718                      ok            True                  False
  PAYX          100.00               21            0.90              0.79        125.67                34.31         0.552          pass              0.657             42.6                           0.319                2.95              0.322                      ok            True                  False
   KHC           85.71               21            1.34              0.24         25.57                37.91         0.551          pass              0.346             21.6                           0.273                2.74              0.347                      ok            True                  False
  FAST          100.00               18            1.05              0.38         51.12                22.00         0.549          pass              0.580             23.9                           0.293               -3.13             -0.224                      ok            True                  False
  MDLZ           93.33               15            1.70              0.77         64.37                26.88         0.533          pass              0.467              8.3                           0.176                2.95              0.359                      ok            True                  False
   KDP           83.33               18            1.65              0.37         32.35                31.66         0.517          pass              0.210              5.3                           0.149                9.58              0.877                      ok            True                  False
  MNST           92.31               39            0.12              0.04         48.90               552.55         1.000          pass              0.863             80.6                           0.409                7.31              0.674                      ok           False                  False
  AMAT           90.62               32            0.91              3.10        482.86                81.86         0.660          pass              0.547             16.9                           0.185               -8.63             -1.186 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-25T11:20:01.845673-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "GEHC261002C00074000", "current_drop_pct": 0.54, "early_entry_score": 0.827, "early_reclaim_pct": 61.2, "entry_ask": 3.5, "entry_bid": 2.3, "entry_mode": "early", "entry_option_price": 2.9, "hypothetical_budget": 15194.0, "hypothetical_contracts": 52, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 26.0, "option_spread_pct": 41.38, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.572, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.827, "early_reclaim_pct": 61.2, "matched_signals": 38, "recovery_stability_score": 0.673, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.572, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.81, "early_reclaim_pct": 76.5, "matched_signals": 30, "recovery_stability_score": 0.73, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:15:01.710634-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 0.98, "early_entry_score": 0.808, "early_reclaim_pct": 75.8, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.697, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.808, "early_reclaim_pct": 75.8, "matched_signals": 30, "recovery_stability_score": 0.697, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:10:04.748235-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 0.86, "early_entry_score": 0.823, "early_reclaim_pct": 78.7, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.823, "early_reclaim_pct": 78.7, "matched_signals": 31, "recovery_stability_score": 0.665, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:05:01.855398-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T11:00:02.779478-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "GEHC261002C00074000", "current_drop_pct": 0.53, "early_entry_score": 0.83, "early_reclaim_pct": 62.1, "entry_ask": 3.5, "entry_bid": 2.3, "entry_mode": "early", "entry_option_price": 2.9, "hypothetical_budget": 15194.0, "hypothetical_contracts": 52, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 26.0, "option_spread_pct": 41.38, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.573, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.83, "early_reclaim_pct": 62.1, "matched_signals": 38, "recovery_stability_score": 0.642, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.573, "trend_health_status": "ok"}, {"current_drop_pct": 0.97, "early_entry_score": 0.809, "early_reclaim_pct": 75.9, "matched_signals": 30, "recovery_stability_score": 0.568, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T10:55:04.743815-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:50:06.625543-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:45:01.788012-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "DXCM261002C00091000", "current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "entry_ask": 5.0, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 4.15, "hypothetical_budget": 15194.0, "hypothetical_contracts": 36, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 40.96, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.59, "shadow_only": true, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "matched_signals": 38, "recovery_stability_score": 0.59, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T10:40:03.785417-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:35:02.544392-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825112001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825112001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825112001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825112001)

</details>
