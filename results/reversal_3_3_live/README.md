# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 11:05:01 EDT`
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
- Equity: `$57,455.50`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$-247.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 27067.5        30.35          30.08      310.66        311.22          bid_ask_mid                      30.08                bid_ask_mid                    True          -247.5                  -0.91          87.5               32              1.06         63.04            62.7                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.35               34            1.36              1.63        170.63               115.46         0.766          pass              0.459             53.2                           0.500                9.68              1.097                  ok            True                  False
  GEHC           97.30               37            0.58              0.30         74.06                49.18         0.575          pass              0.812             58.3                           0.648                1.39              0.232                  ok            True                  False
  WDAY           82.14               28            2.38              3.31        197.73                78.88         0.565          pass              0.303             23.0                           0.266                7.25              0.717                  ok            True                  False
   KHC           86.36               22            1.09              0.20         25.59                37.91         0.560          pass              0.415             36.4                           0.554                3.00              0.359                  ok            True                  False
  PAYX          100.00               23            0.85              0.75        125.69                34.31         0.543          pass              0.678             45.7                           0.324                3.00              0.324                  ok            True                  False
  FAST          100.00               21            0.90              0.32         51.14                22.00         0.539          pass              0.633             35.2                           0.472               -2.98             -0.217                  ok            True                  False
  MDLZ           94.44               18            1.39              0.63         64.43                26.88         0.533          pass              0.567             25.0                           0.414                3.27              0.374                  ok            True                  False
  SBUX           81.82               11            1.22              0.92        107.10                20.57         0.528          pass              0.219             37.1                           0.283                0.12             -0.118                  ok            True                  False
  AAPL           85.29               34            0.53              1.14        309.85                32.89         0.520          pass              0.402             16.4                           0.221                1.25              0.253                  ok            True                  False
   KDP           83.33               18            1.68              0.38         32.35                31.66         0.515          pass              0.194              0.0                           0.190                9.54              0.876                  ok            True                  False
  BKNG           97.37               38            0.54              0.81        213.01                41.51         0.508          pass              0.704             22.3                           0.297               -0.31             -0.027                  ok            True                  False
  MNST           92.11               38            0.22              0.08         48.89               552.55         1.000          pass              0.803             64.5                           0.370                7.20              0.669                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-25T11:05:01.855398-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T11:00:02.779478-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "GEHC261002C00074000", "current_drop_pct": 0.53, "early_entry_score": 0.83, "early_reclaim_pct": 62.1, "entry_ask": 3.5, "entry_bid": 2.3, "entry_mode": "early", "entry_option_price": 2.9, "hypothetical_budget": 15194.0, "hypothetical_contracts": 52, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 26.0, "option_spread_pct": 41.38, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.642, "shadow_only": true, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.573, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.83, "early_reclaim_pct": 62.1, "matched_signals": 38, "recovery_stability_score": 0.642, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.573, "trend_health_status": "ok"}, {"current_drop_pct": 0.97, "early_entry_score": 0.809, "early_reclaim_pct": 75.9, "matched_signals": 30, "recovery_stability_score": 0.568, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T10:55:04.743815-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:50:06.625543-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:45:01.788012-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "DXCM261002C00091000", "current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "entry_ask": 5.0, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 4.15, "hypothetical_budget": 15194.0, "hypothetical_contracts": 36, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 40.96, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.59, "shadow_only": true, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.681, "early_reclaim_pct": 61.6, "matched_signals": 38, "recovery_stability_score": 0.59, "success_rate": 89.47, "ticker": "DXCM", "timing_score": 0.568, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T10:40:03.785417-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:35:02.544392-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:30:01.796364-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:25:02.779045-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T10:20:01.784831-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825110501)

</details>
