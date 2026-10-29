# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-29 11:05:05 EDT`
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

- Cash: `$123,336.80`
- Equity: `$123,336.80`
- Realized PnL: `$113,336.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-29)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261218C00110000     90          2026-10-28         2026-10-29        7.275      6.5475 -6547.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           89.29               28            2.03              2.06        144.28                71.12         0.571          pass              0.584             53.2                           0.614               -6.00             -0.043                                 ok            True                  False
   ROP           88.57               35            0.52              1.59        439.98                39.09         0.523          pass              0.590             47.3                           0.441               14.63              1.750                                 ok            True                  False
  UPRO           82.61               23            1.27              1.34        150.56                30.20         0.515          pass              0.317             36.5                           0.474               -1.52             -0.011                                 ok            True                  False
  ADBE           84.00               25            1.74              3.04        248.46                41.65         0.505          pass              0.408             50.3                           0.381               -2.48              0.011                                 ok            True                  False
  SOXL           68.18               22            4.83              3.63        105.80               137.18         0.626          pass              0.289             49.0                           0.632               -4.83              0.009                                 ok           False                  False
  MPWR           65.22               23            1.60             13.57       1205.41                59.53         0.573          pass              0.321             59.1                           0.657               -4.59             -0.535            downtrend_blocked_slope           False                  False
  CSCO           76.19               21            1.03              0.80        109.95                35.33         0.548          pass              0.220             30.7                           0.322               -0.64              0.243                                 ok           False                  False
  NVDA           76.00               25            0.66              1.00        214.95                30.56         0.538          pass              0.324             56.7                           0.631               -1.51             -0.088                                 ok           False                  False
  MELI           78.57               28            1.56             18.21       1665.28                48.85         0.531          pass              0.304             43.5                           0.433              -11.30             -1.364 downtrend_blocked_slope_and_streak           False                  False
  AVGO           54.55               11            2.46              6.05        349.22                43.15         0.530          pass              0.160             33.6                           0.580               -0.34              0.221                                 ok           False                  False
   LIN           75.00                8            1.31              4.66        506.16                14.48         0.522          pass              0.104             17.2                           0.192                1.68              0.209                                 ok           False                  False
   ADP           93.33               30            0.35              0.70        285.07                29.33         0.518          pass              0.631             30.1                           0.286               -0.45              0.073                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-29T11:05:05.678206-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "INTU261204C00325000", "current_drop_pct": 0.53, "early_entry_score": 0.707, "early_reclaim_pct": 87.8, "entry_ask": 27.9, "entry_bid": 22.5, "entry_mode": "early", "entry_option_price": 25.2, "hypothetical_budget": 61668.4, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 21.43, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.582, "shadow_only": true, "success_rate": 88.57, "ticker": "INTU", "timing_score": 0.48, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.707, "early_reclaim_pct": 87.8, "matched_signals": 35, "recovery_stability_score": 0.582, "success_rate": 88.57, "ticker": "INTU", "timing_score": 0.48, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-29T11:05:05.678206-04:00      manage_1100               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "CSCO261218C00110000", "fill_price": 6.5475, "pnl": -6547.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSCO"}
2026-10-29T11:00:06.462507-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "QCOM261218C00185000", "current_drop_pct": 0.85, "early_entry_score": 0.75, "early_reclaim_pct": 62.8, "entry_ask": 12.1, "entry_bid": 11.75, "entry_mode": "early", "entry_option_price": 11.925, "hypothetical_budget": 32204.65, "hypothetical_contracts": 27, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 3107.0, "option_spread_pct": 2.94, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.75, "early_reclaim_pct": 62.8, "matched_signals": 32, "recovery_stability_score": 0.605, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.479, "trend_health_status": "ok"}, {"current_drop_pct": 0.63, "early_entry_score": 0.699, "early_reclaim_pct": 85.5, "matched_signals": 35, "recovery_stability_score": 0.552, "success_rate": 88.57, "ticker": "INTU", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:55:05.704456-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:50:05.735637-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:45:05.600888-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:40:05.590194-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "QCOM261218C00190000", "current_drop_pct": 0.9, "early_entry_score": 0.744, "early_reclaim_pct": 60.9, "entry_ask": 10.15, "entry_bid": 9.6, "entry_mode": "early", "entry_option_price": 9.875, "hypothetical_budget": 32204.65, "hypothetical_contracts": 32, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 1786.0, "option_spread_pct": 5.57, "option_volume": 811.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.744, "early_reclaim_pct": 60.9, "matched_signals": 32, "recovery_stability_score": 0.662, "success_rate": 93.75, "ticker": "QCOM", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:35:05.458266-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:30:06.113309-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-29T10:25:05.571151-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261029110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261029110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261029110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261029110505)

</details>
