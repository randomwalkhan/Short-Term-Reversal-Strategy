# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 10:45:05 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$33,222.25`
- Equity: `$33,222.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   CSX           92.31               13            1.23              0.44         50.55                28.82         0.584          pass              0.450             14.4                           0.195                1.39              0.262                  ok            True                  False
   KDP           82.35               17            1.32              0.29         31.33                34.46         0.578          pass              0.251             27.8                           0.356                2.56              0.023                  ok            True                  False
  ABNB           93.75               16            1.92              2.06        152.13                40.20         0.560          pass              0.543             26.7                           0.221                2.41              0.067                  ok            True                  False
  MNST           94.12               17            1.04              0.71         96.93                25.74         0.557          pass              0.682             67.8                           0.417               -1.83             -0.261                  ok            True                  False
  VRTX           81.82               11            2.07              7.01        480.33                33.19         0.553          pass              0.179             22.9                           0.256               -0.63             -0.040                  ok            True                  False
  AMGN           90.91               11            1.88              5.10        385.45                27.22         0.542          pass              0.420             22.7                           0.351                7.07              0.707                  ok            True                  False
   HON           82.35               17            1.29              2.18        240.19                39.75         0.532          pass              0.196             11.0                           0.162                6.88              1.053                  ok            True                  False
  DXCM           84.62               26            1.54              0.81         74.79                45.20         0.515          pass              0.388             35.6                           0.524               -0.19             -0.317                  ok            True                  False
  PCAR           88.46               26            1.05              0.98        133.45                29.38         0.511          pass              0.400              5.4                           0.205                6.88              0.922                  ok            True                  False
  ROST           88.46               26            0.90              1.59        251.28                27.49         0.510          pass              0.482             32.9                           0.313               13.02              1.042                  ok            True                  False
  DASH           96.97               33            1.40              1.90        192.72                53.51         0.509          pass              0.728             41.2                           0.303                1.61             -0.041                  ok            True                  False
  PYPL           77.78                9            2.45              1.00         57.92                61.52         0.664          pass              0.072              1.7                           0.047                2.52              0.170                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-30T10:45:05.898000-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:40:01.919519-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:35:01.875503-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:30:03.673843-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:25:02.736575-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:20:02.940055-04:00 early_entry_1020 early_entry_shadow                               {"contract_symbol": "DASH260918C00195000", "current_drop_pct": 0.73, "early_entry_score": 0.859, "early_reclaim_pct": 69.5, "entry_ask": 16.05, "entry_bid": 14.75, "entry_mode": "early", "entry_option_price": 15.4, "hypothetical_budget": 16611.13, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 7694.0, "option_spread_pct": 8.44, "option_volume": 53.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.757, "shadow_only": true, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.859, "early_reclaim_pct": 69.5, "matched_signals": 41, "recovery_stability_score": 0.757, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-30T10:15:03.914804-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.864, "early_reclaim_pct": 71.6, "matched_signals": 43, "recovery_stability_score": 0.762, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:10:02.887573-04:00 early_entry_1010 early_entry_shadow           {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.729, "shadow_only": true, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.865, "early_reclaim_pct": 71.9, "matched_signals": 43, "recovery_stability_score": 0.729, "success_rate": 97.67, "ticker": "DASH", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:05:01.868497-04:00 early_entry_1005 early_entry_shadow             {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "entry_ask": 18.6, "entry_bid": 15.95, "entry_mode": "early", "entry_option_price": 17.275, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 379.0, "option_spread_pct": 15.34, "option_volume": 91.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.681, "shadow_only": true, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.855, "early_reclaim_pct": 68.2, "matched_signals": 40, "recovery_stability_score": 0.681, "success_rate": 97.5, "ticker": "DASH", "timing_score": 0.506, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-30T10:00:05.892455-04:00 early_entry_1000 early_entry_shadow                                    {"contract_symbol": "DASH260918C00190000", "current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "entry_ask": 18.65, "entry_bid": 17.3, "entry_mode": "early", "entry_option_price": 17.975, "hypothetical_budget": 16611.13, "hypothetical_contracts": 9, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 379.0, "option_spread_pct": 7.51, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.857, "early_reclaim_pct": 68.9, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 97.56, "ticker": "DASH", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730104505)

</details>
