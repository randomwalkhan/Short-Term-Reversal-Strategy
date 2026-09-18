# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 11:50:03 EDT`
Last processed slot: `manage_1200`

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

## Today's Closed Trades (2026-09-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   WMT     option         option WMT261023C00108000    127          2026-09-17         2026-09-18        2.565        3.05 6159.5   18.908382 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           97.44               39            0.64              0.89        197.09                82.85         0.633          pass              0.878             73.7                           0.586               10.35              1.881                                 ok            True                   True
   KHC           93.75               16            0.51              0.09         24.69                21.70         0.547          pass              0.697             78.4                           0.776               -1.66             -0.108                                 ok            True                  False
  CTSH          100.00               15            2.44              1.06         61.43                39.55         0.528          pass              0.523             12.5                           0.237               -6.61             -0.011                                 ok            True                  False
  CRWD           77.78               18            3.14              5.40        243.38                97.92         0.628          pass              0.202             28.5                           0.500               10.70              1.749                                 ok           False                  False
  PYPL           94.12               34            0.57              0.21         52.85                57.74         0.611          pass              0.767             56.5                           0.445               -7.13             -0.428            downtrend_blocked_slope           False                  False
  MRVL           78.95               38            0.86              1.44        240.14                74.50         0.586          pass              0.357             37.1                           0.372               14.30              0.790                                 ok           False                  False
   TRI           90.91               11            3.09              2.15         98.56                55.72         0.564          pass              0.386             10.8                           0.370              -13.73             -0.629 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00                6            1.23              0.37         42.48                15.46         0.563          pass              0.480              7.9                           0.250               -4.52             -0.468 downtrend_blocked_slope_and_streak           False                  False
  ADSK           84.85               33            0.75              1.14        218.15                55.63         0.556          pass              0.448             36.6                           0.484               -8.64             -0.057           downtrend_blocked_streak           False                  False
  ADBE           96.15               26            1.41              2.49        251.60                46.08         0.540          pass              0.665             34.9                           0.318              -12.82             -0.810 downtrend_blocked_slope_and_streak           False                  False
   ADP           95.45               22            0.61              1.16        271.74                22.18         0.533          pass              0.716             60.8                           0.511               -3.96             -0.037           downtrend_blocked_streak           False                  False
   AEP           66.67                6            1.21              1.03        121.18                17.28         0.527          pass              0.098             15.0                           0.209               -3.66             -0.429 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-18T11:50:03.921219-04:00 early_entry_1150 early_entry_shadow                           {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.64, "early_entry_score": 0.878, "early_reclaim_pct": 73.7, "entry_ask": 14.2, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 13.525, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 9.98, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.633, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.878, "early_reclaim_pct": 73.7, "matched_signals": 39, "recovery_stability_score": 0.586, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.633, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:45:06.412302-04:00 early_entry_1145 early_entry_shadow                             {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 78.6, "entry_ask": 14.2, "entry_bid": 12.8, "entry_mode": "early", "entry_option_price": 13.5, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 10.37, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.893, "early_reclaim_pct": 78.6, "matched_signals": 39, "recovery_stability_score": 0.633, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:40:04.871951-04:00 early_entry_1140 early_entry_shadow                          {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.67, "early_entry_score": 0.874, "early_reclaim_pct": 72.5, "entry_ask": 14.2, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.425, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 11.55, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.659, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.631, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.874, "early_reclaim_pct": 72.5, "matched_signals": 39, "recovery_stability_score": 0.659, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.631, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:35:05.972190-04:00 early_entry_1135 early_entry_shadow                          {"contract_symbol": "ZS261030C00200000", "current_drop_pct": 0.53, "early_entry_score": 0.893, "early_reclaim_pct": 78.4, "entry_ask": 14.2, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.425, "hypothetical_budget": 35735.4, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 112.0, "option_spread_pct": 11.55, "option_volume": 65.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.757, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.893, "early_reclaim_pct": 78.4, "matched_signals": 39, "recovery_stability_score": 0.757, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.639, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-18T11:30:04.777867-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:25:04.772895-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:20:06.499852-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:15:06.591225-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T11:10:04.781289-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ZS261023C00195000", "current_drop_pct": 0.57, "early_entry_score": 0.887, "early_reclaim_pct": 76.6, "entry_ask": 13.95, "entry_bid": 12.5, "entry_mode": "early", "entry_option_price": 13.225, "hypothetical_budget": 35735.4, "hypothetical_contracts": 27, "matched_signals": 39, "option_liquidity_status": "low_open_interest", "option_open_interest": 97.0, "option_spread_pct": 10.96, "option_volume": 40.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.817, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.637, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.887, "early_reclaim_pct": 76.6, "matched_signals": 39, "recovery_stability_score": 0.817, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.637, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T11:05:05.479852-04:00 early_entry_1105 early_entry_shadow  {"contract_symbol": "ZS261023C00195000", "current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "entry_ask": 13.95, "entry_bid": 12.45, "entry_mode": "early", "entry_option_price": 13.2, "hypothetical_budget": 35735.4, "hypothetical_contracts": 27, "matched_signals": 38, "option_liquidity_status": "low_open_interest", "option_open_interest": 97.0, "option_spread_pct": 11.36, "option_volume": 40.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.842, "early_reclaim_pct": 64.3, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.626, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918115003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918115003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918115003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918115003)

</details>
