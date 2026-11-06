# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 10:50:06 EST`
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

- Cash: `$123,162.80`
- Equity: `$123,162.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           92.31               13            1.15              0.30         36.76                35.93         0.581          pass              0.598             64.0                           0.625                5.15              0.596                                 ok            True                  False
 CMCSA           93.33               15            1.02              0.18         24.87                35.54         0.568          pass              0.667             73.7                           0.749                8.84              1.418                                 ok            True                  False
   KHC           84.62               13            1.86              0.33         25.18                36.03         0.535          pass              0.357             53.4                           0.674                0.20              0.335                                 ok            True                  False
  COST           80.95               21            0.69              5.14       1063.39                23.23         0.528          pass              0.359             69.3                           0.653                5.63              0.726                                 ok            True                  False
   PEP           84.21               19            0.96              0.96        142.30                27.68         0.522          pass              0.435             70.3                           0.681                4.11              0.655                                 ok            True                  False
  CTAS           94.44               18            1.19              1.89        225.60                27.57         0.512          pass              0.666             58.6                           0.623               -0.17              0.293                                 ok            True                  False
  FTNT           83.33               30            1.64              1.41        121.91                92.45         0.642          pass              0.360             24.4                           0.260              -33.05             -4.911 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.83               46            0.03              0.12        670.66                77.01         0.626          pass              0.960             99.2                           0.810               19.66              2.465                                 ok           False                  False
  MSTR           90.62               32            1.16              1.05        128.85                81.05         0.560          pass              0.665             59.6                           0.397              -12.47             -1.064            downtrend_blocked_slope           False                  False
  ISRG           85.71                7            2.34              7.69        465.23                42.48         0.560          pass              0.245             12.3                           0.128                1.16              0.360                                 ok           False                  False
  PAYX           75.00                4            2.08              1.74        118.75                35.22         0.557          pass              0.211             51.9                           0.627                0.14              0.520                                 ok           False                  False
   CSX           80.00                5            1.90              0.68         50.54                30.62         0.555          pass              0.092             12.3                           0.217               -1.82             -0.185                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-11-06T10:50:06.578402-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:45:05.896863-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:40:04.864524-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:35:02.947980-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:30:05.862007-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "MSFT261218C00535000", "current_drop_pct": 0.61, "early_entry_score": 0.823, "early_reclaim_pct": 79.4, "entry_ask": 21.65, "entry_bid": 21.1, "entry_mode": "early", "entry_option_price": 21.375, "hypothetical_budget": 61581.4, "hypothetical_contracts": 28, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 3628.0, "option_spread_pct": 2.57, "option_volume": 42.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.763, "shadow_only": true, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.509, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.823, "early_reclaim_pct": 79.4, "matched_signals": 30, "recovery_stability_score": 0.763, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.509, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:25:04.812264-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:20:05.873622-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                        {"contract_symbol": "MSFT261218C00535000", "current_drop_pct": 0.56, "early_entry_score": 0.828, "early_reclaim_pct": 81.0, "entry_ask": 19.7, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 19.15, "hypothetical_budget": 61581.4, "hypothetical_contracts": 32, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 3628.0, "option_spread_pct": 5.74, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.512, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.828, "early_reclaim_pct": 81.0, "matched_signals": 30, "recovery_stability_score": 0.749, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.512, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:15:06.200919-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:10:06.574666-05:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "IDXX261218C00670000", "current_drop_pct": 0.61, "early_entry_score": 0.88, "early_reclaim_pct": 80.4, "entry_ask": 31.1, "entry_bid": 25.9, "entry_mode": "early", "entry_option_price": 28.5, "hypothetical_budget": 61581.4, "hypothetical_contracts": 21, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 18.25, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.847, "shadow_only": true, "success_rate": 97.22, "ticker": "IDXX", "timing_score": 0.651, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.88, "early_reclaim_pct": 80.4, "matched_signals": 36, "recovery_stability_score": 0.847, "success_rate": 97.22, "ticker": "IDXX", "timing_score": 0.651, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 82.4, "matched_signals": 37, "recovery_stability_score": 0.911, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T10:05:04.744572-05:00 early_entry_1005 early_entry_shadow {"contract_symbol": "IDXX261218C00660000", "current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "entry_ask": 34.8, "entry_bid": 29.0, "entry_mode": "early", "entry_option_price": 31.9, "hypothetical_budget": 61581.4, "hypothetical_contracts": 19, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 18.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "matched_signals": 34, "recovery_stability_score": 0.776, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 72.0, "matched_signals": 39, "recovery_stability_score": 0.724, "success_rate": 89.74, "ticker": "TTWO", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106105006)

</details>
