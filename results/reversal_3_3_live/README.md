# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 11:50:02 EDT`
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

- Cash: `$85,238.30`
- Equity: `$85,238.30`
- Realized PnL: `$75,238.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261120C00155000     24          2026-09-29         2026-09-30         15.9        18.6 6480.0   16.981132 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  DRAM           83.33               30            0.97              0.42         61.11                54.99         0.589          pass              0.395             38.0                           0.370                9.70              0.607                  ok            True                  False
  ASML           81.82               33            0.55              7.07       1831.36                42.72         0.555          pass              0.413             51.7                           0.518               13.86              1.186                  ok            True                  False
  PYPL           88.24               17            1.38              0.52         53.67                34.93         0.542          pass              0.361             13.4                           0.246                0.83              0.274                  ok            True                  False
  MRVL           82.35               34            1.10              2.03        262.40                56.16         0.535          pass              0.453             58.8                           0.738               13.35              0.999                  ok            True                  False
  MPWR           85.19               27            1.50             14.20       1347.91                52.13         0.526          pass              0.394             30.0                           0.360               16.22              1.598                  ok            True                  False
  NXPI           84.62               26            1.12              1.85        235.68                39.17         0.510          pass              0.478             65.7                           0.476                6.78              0.545                  ok            True                  False
  ALNY           82.05               39            0.70              1.25        253.53                45.82         0.505          pass              0.412             37.8                           0.224                5.40              0.615                  ok            True                  False
  SOXL           86.11               36            0.21              0.21        146.91               117.21         0.768          pass              0.690             92.4                           0.577               41.19              2.938                  ok           False                  False
  MSTR           94.59               37            0.37              0.41        154.50                99.32         0.687          pass              0.872             78.1                           0.639               22.12              1.393                  ok           False                  False
   WBD           95.24               42            0.05              0.01         30.85                37.86         0.558          pass              0.866             70.0                           0.746                9.85              1.041                  ok           False                  False
  AMAT           85.00               40            0.31              1.11        511.54                51.71         0.556          pass              0.617             76.2                           0.437               22.88              2.010                  ok           False                  False
  META           86.84               38            0.27              1.39        738.19                54.80         0.554          pass              0.690             88.6                           0.854                9.52              0.979                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-09-30T11:50:02.063648-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T11:45:06.112899-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T11:40:05.681416-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T11:35:01.055595-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T11:30:05.967635-04:00 early_entry_1130 early_entry_shadow                 {"contract_symbol": "MSTR261120C00155000", "current_drop_pct": 0.6, "early_entry_score": 0.81, "early_reclaim_pct": 64.7, "entry_ask": 15.55, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 15.425, "hypothetical_budget": 42619.15, "hypothetical_contracts": 27, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1873.0, "option_spread_pct": 1.62, "option_volume": 182.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.684, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.81, "early_reclaim_pct": 64.7, "matched_signals": 35, "recovery_stability_score": 0.551, "success_rate": 94.29, "ticker": "MSTR", "timing_score": 0.684, "trend_health_status": "ok"}, {"current_drop_pct": 0.5, "early_entry_score": 0.729, "early_reclaim_pct": 61.2, "matched_signals": 37, "recovery_stability_score": 0.713, "success_rate": 91.89, "ticker": "ADI", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-30T11:25:06.141633-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.745, "early_reclaim_pct": 62.4, "entry_ask": 8.1, "entry_bid": 7.7, "entry_mode": "early", "entry_option_price": 7.9, "hypothetical_budget": 42619.15, "hypothetical_contracts": 53, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 4833.0, "option_spread_pct": 5.06, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.639, "shadow_only": true, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.745, "early_reclaim_pct": 62.4, "matched_signals": 32, "recovery_stability_score": 0.639, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T11:20:05.483552-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-30T11:15:04.128412-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.53, "early_entry_score": 0.76, "early_reclaim_pct": 63.5, "entry_ask": 8.1, "entry_bid": 7.7, "entry_mode": "early", "entry_option_price": 7.9, "hypothetical_budget": 42619.15, "hypothetical_contracts": 53, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 4833.0, "option_spread_pct": 5.06, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.76, "early_reclaim_pct": 63.5, "matched_signals": 33, "recovery_stability_score": 0.712, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.439, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-30T11:10:05.136975-04:00 early_entry_1110 early_entry_shadow               {"contract_symbol": "MSTR261120C00155000", "current_drop_pct": 0.54, "early_entry_score": 0.843, "early_reclaim_pct": 68.7, "entry_ask": 15.3, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.2, "hypothetical_budget": 42619.15, "hypothetical_contracts": 28, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1873.0, "option_spread_pct": 1.32, "option_volume": 85.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 94.59, "ticker": "MSTR", "timing_score": 0.677, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.843, "early_reclaim_pct": 68.7, "matched_signals": 37, "recovery_stability_score": 0.592, "success_rate": 94.59, "ticker": "MSTR", "timing_score": 0.677, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.694, "early_reclaim_pct": 66.4, "matched_signals": 39, "recovery_stability_score": 0.665, "success_rate": 89.74, "ticker": "DXCM", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-30T11:05:05.139754-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "GILD261120C00150000", "current_drop_pct": 0.54, "early_entry_score": 0.745, "early_reclaim_pct": 62.4, "entry_ask": 8.1, "entry_bid": 7.5, "entry_mode": "early", "entry_option_price": 7.8, "hypothetical_budget": 42619.15, "hypothetical_contracts": 54, "matched_signals": 32, "option_liquidity_status": "low_volume", "option_open_interest": 4833.0, "option_spread_pct": 7.69, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.686, "shadow_only": true, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.745, "early_reclaim_pct": 62.4, "matched_signals": 32, "recovery_stability_score": 0.686, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.443, "trend_health_status": "ok"}, {"current_drop_pct": 0.51, "early_entry_score": 0.717, "early_reclaim_pct": 69.9, "matched_signals": 40, "recovery_stability_score": 0.704, "success_rate": 90.0, "ticker": "DXCM", "timing_score": 0.412, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930115002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930115002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930115002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930115002)

</details>
