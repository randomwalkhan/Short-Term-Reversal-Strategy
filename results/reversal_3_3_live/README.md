# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 11:25:06 EDT`
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

- Cash: `$128,734.80`
- Equity: `$128,734.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261120C00115000    115          2026-10-14         2026-10-15         5.85       5.265 -6727.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           90.00               30            1.56              2.42        219.75                59.94         0.523            pass              0.633             60.1                           0.487                9.34              1.363                                 ok            True                  False
  META           86.11               36            0.26              1.36        736.96                55.15         0.577            pass              0.668             91.2                           0.835                1.33              0.188                                 ok           False                  False
  SNPS           75.00                8            2.66              8.93        476.10                52.37         0.568            pass              0.206             49.9                           0.745               -4.76             -0.259 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.89                9            2.91              5.70        277.10                59.82         0.557            pass              0.388             31.8                           0.561                4.82              0.741                                 ok           False                  False
  CDNS           80.00               20            1.49              3.45        327.98                37.41         0.506            pass              0.308             63.7                           0.786               -7.47             -0.805 downtrend_blocked_slope_and_streak           False                  False
   AEP           57.14                7            1.43              1.26        125.59                12.92         0.482 below_threshold              0.085             12.4                           0.263                3.82              0.540                                 ok           False                  False
  NVDA           84.62               13            1.84              2.86        220.08                25.52         0.474 below_threshold              0.346             51.7                           0.678               -5.91             -0.733 downtrend_blocked_slope_and_streak           False                  False
  CRWD           84.21               19            2.68              4.67        247.29                48.36         0.474 below_threshold              0.308             29.5                           0.458               -8.82             -0.902 downtrend_blocked_slope_and_streak           False                  False
  INTC           85.71               14            3.82              2.62         97.00                68.27         0.471 below_threshold              0.387             53.7                           0.813              -21.36             -2.398            downtrend_blocked_slope           False                  False
  AVGO           85.71               28            1.45              3.51        344.74                35.83         0.456 below_threshold              0.489             56.9                           0.639               -0.70             -0.305                                 ok           False                  False
    MU           90.24               41            0.26              1.67        913.41                50.57         0.453 below_threshold              0.806             95.7                           0.800              -16.90             -1.882 downtrend_blocked_slope_and_streak           False                  False
   XEL           88.57               35            0.13              0.07         75.33                17.56         0.453 below_threshold              0.639             66.1                           0.421                6.68              0.660                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-15T11:25:06.119732-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:20:05.131214-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:15:06.283716-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "entry_ask": 15.15, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.525, "hypothetical_budget": 64367.4, "hypothetical_contracts": 44, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 8.61, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "matched_signals": 35, "recovery_stability_score": 0.665, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:10:05.939660-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "entry_ask": 14.15, "entry_bid": 13.6, "entry_mode": "early", "entry_option_price": 13.875, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.96, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "top_candidates": [{"current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:05:05.115302-04:00 early_entry_1105 early_entry_shadow   {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "entry_ask": 14.0, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 13.775, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.27, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "matched_signals": 35, "recovery_stability_score": 0.632, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:00:05.305512-04:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "entry_ask": 14.45, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 64367.4, "hypothetical_contracts": 45, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.43, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "matched_signals": 35, "recovery_stability_score": 0.571, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:55:05.229160-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:50:05.707569-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:45:06.384302-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:40:06.514457-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015112506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015112506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015112506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015112506)

</details>
