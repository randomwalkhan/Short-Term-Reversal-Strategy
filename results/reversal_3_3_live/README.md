# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 10:55:05 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           86.96               23            1.07              0.18         23.75                25.26         0.505            pass              0.391             22.7                           0.417                7.26              0.769                      ok            True                  False
  INTU           87.50               32            0.76              1.77        334.53                37.42         0.502            pass              0.514             39.1                           0.261               12.47              1.284                      ok            True                  False
  TMUS           55.56                9            2.56              2.83        156.54                56.37         0.577            pass              0.163             35.2                           0.464               -8.31             -0.456 downtrend_blocked_slope           False                  False
  GILD           88.89                9            1.73              1.90        155.70                26.70         0.536            pass              0.421             43.5                           0.634                4.73              0.594                      ok           False                  False
  MDLZ           50.00                2            1.88              0.84         63.63                19.17         0.514            pass              0.082             10.1                           0.215                5.73              0.660                      ok           False                  False
  DASH           84.85               33            1.33              1.79        190.90                49.85         0.496 below_threshold              0.458             42.0                           0.382               -1.11             -0.141                      ok           False                  False
 CMCSA           75.00                4            2.17              0.34         22.21                21.50         0.495 below_threshold              0.164             38.2                           0.566                4.47              0.692                      ok           False                  False
  MSFT           93.55               31            0.37              1.37        531.28                21.62         0.490 below_threshold              0.765             71.5                           0.674                0.03              0.009                      ok           False                  False
  AVGO           82.50               40            0.05              0.12        334.32                36.72         0.487 below_threshold              0.591             91.8                           0.618              -11.24             -1.195 downtrend_blocked_slope           False                  False
  GEHC           78.95               19            1.38              0.68         69.94                23.16         0.481 below_threshold              0.218             36.6                           0.438                7.10              0.868                      ok           False                  False
  REGN           82.86               35            0.65              3.67        805.91                31.32         0.480 below_threshold              0.381             29.9                           0.280                8.10              0.916                      ok           False                  False
  ALNY           80.00               35            1.15              1.86        229.91                41.48         0.470 below_threshold              0.294             26.8                           0.282                1.63              0.258                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-10-21T10:55:05.589543-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                          {"contract_symbol": "ABNB261120C00175000", "current_drop_pct": 0.52, "early_entry_score": 0.752, "early_reclaim_pct": 69.9, "entry_ask": 11.05, "entry_bid": 8.7, "entry_mode": "early", "entry_option_price": 9.875, "hypothetical_budget": 72415.9, "hypothetical_contracts": 73, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 728.0, "option_spread_pct": 23.8, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.452, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.752, "early_reclaim_pct": 69.9, "matched_signals": 37, "recovery_stability_score": 0.682, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:50:05.866905-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.67, "early_entry_score": 0.768, "early_reclaim_pct": 63.7, "entry_ask": 31.9, "entry_bid": 27.6, "entry_mode": "early", "entry_option_price": 29.75, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 14.45, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.768, "early_reclaim_pct": 63.7, "matched_signals": 40, "recovery_stability_score": 0.721, "success_rate": 92.5, "ticker": "IDXX", "timing_score": 0.431, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.753, "early_reclaim_pct": 70.3, "matched_signals": 37, "recovery_stability_score": 0.699, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.452, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:45:05.723673-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.8, "entry_ask": 32.1, "entry_bid": 26.1, "entry_mode": "early", "entry_option_price": 29.1, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 20.62, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.75, "early_reclaim_pct": 61.8, "matched_signals": 39, "recovery_stability_score": 0.722, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:40:06.184950-04:00 early_entry_1040 early_entry_shadow   {"contract_symbol": "IDXX261120C00550000", "current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 60.9, "entry_ask": 32.1, "entry_bid": 26.1, "entry_mode": "early", "entry_option_price": 29.1, "hypothetical_budget": 72415.9, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 22.0, "option_spread_pct": 20.62, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.748, "early_reclaim_pct": 60.9, "matched_signals": 39, "recovery_stability_score": 0.69, "success_rate": 92.31, "ticker": "IDXX", "timing_score": 0.433, "trend_health_status": "ok"}, {"current_drop_pct": 0.59, "early_entry_score": 0.74, "early_reclaim_pct": 66.0, "matched_signals": 37, "recovery_stability_score": 0.653, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:35:02.510761-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:30:05.461967-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                           {"contract_symbol": "ABNB261120C00175000", "current_drop_pct": 0.55, "early_entry_score": 0.747, "early_reclaim_pct": 68.1, "entry_ask": 11.05, "entry_bid": 8.8, "entry_mode": "early", "entry_option_price": 9.925, "hypothetical_budget": 72415.9, "hypothetical_contracts": 72, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 728.0, "option_spread_pct": 22.67, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.576, "shadow_only": true, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.45, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.747, "early_reclaim_pct": 68.1, "matched_signals": 37, "recovery_stability_score": 0.576, "success_rate": 91.89, "ticker": "ABNB", "timing_score": 0.45, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-21T10:25:04.556585-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:20:05.382566-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:15:01.464955-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:10:06.281776-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021105505)

</details>
