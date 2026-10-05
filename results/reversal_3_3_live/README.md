# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 14:10:06 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$88,586.80`
- Equity: `$88,586.80`
- Realized PnL: `$78,586.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-05)

```text
ticker asset_type execution_mode        instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
    ZS     option         option ZS261120C00200000     27          2026-10-02         2026-10-05        14.85      17.525 7222.5   18.013468 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           85.71               21            2.20              1.50         96.98                53.36         0.525            pass              0.318             13.2                           0.253                0.04              0.020                                 ok            True                  False
  NXPI           87.50               32            0.68              1.16        243.16                37.68         0.513            pass              0.596             65.9                           0.707                4.13              0.370                                 ok            True                  False
  MRVL           83.33               36            0.77              1.47        271.66                54.74         0.512            pass              0.473             53.2                           0.456                4.98              0.471                                 ok            True                  False
    MU           90.91               33            1.03              7.72       1071.58                50.82         0.505            pass              0.624             42.9                           0.341                1.91              0.038                                 ok            True                  False
  SOXL           86.11               36            0.23              0.26        163.60               114.85         0.774            pass              0.694             93.4                           0.790               15.16              1.040                                 ok           False                  False
  INTC           84.38               32            1.90              1.59        118.65                74.20         0.550            pass              0.500             60.4                           0.600               -3.87             -0.532            downtrend_blocked_slope           False                  False
  AMAT           84.62               39            0.44              1.66        539.33                49.71         0.546            pass              0.559             62.7                           0.546               15.82              1.639                                 ok           False                  False
  ASML           84.21               38            0.17              2.25       1866.34                42.39         0.545            pass              0.623             89.7                           0.755                8.93              0.865                                 ok           False                  False
  AMGN           87.80               41            0.09              0.25        402.93                47.11         0.533            pass              0.743             94.0                           0.675                2.42              0.140                                 ok           False                  False
  LRCX           81.40               43            0.37              0.90        347.11                57.64         0.527            pass              0.524             77.9                           0.786               14.65              1.453                                 ok           False                  False
  QCOM           88.00               25            1.81              2.34        183.87                56.36         0.522            pass              0.437             23.7                           0.282               -6.54             -0.962 downtrend_blocked_slope_and_streak           False                  False
  TMUS           88.89               36            0.28              0.32        163.50                31.57         0.495 below_threshold              0.676             72.1                           0.369               -1.26             -0.134                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-10-05T12:00:06.148315-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                           {"contract_symbol": "ADI261120C00410000", "current_drop_pct": 0.7, "early_entry_score": 0.678, "early_reclaim_pct": 61.4, "entry_ask": 25.9, "entry_bid": 24.0, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 44293.4, "hypothetical_contracts": 17, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 228.0, "option_spread_pct": 7.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.669, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.678, "early_reclaim_pct": 61.4, "matched_signals": 33, "recovery_stability_score": 0.669, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-05T11:55:05.965880-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                         {"contract_symbol": "ADI261120C00410000", "current_drop_pct": 0.67, "early_entry_score": 0.696, "early_reclaim_pct": 63.0, "entry_ask": 25.9, "entry_bid": 24.0, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 44293.4, "hypothetical_contracts": 17, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 228.0, "option_spread_pct": 7.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.716, "shadow_only": true, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.696, "early_reclaim_pct": 63.0, "matched_signals": 34, "recovery_stability_score": 0.716, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-05T11:50:06.228563-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-05T11:45:06.909696-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                          {"contract_symbol": "ADI261120C00410000", "current_drop_pct": 0.64, "early_entry_score": 0.701, "early_reclaim_pct": 64.4, "entry_ask": 26.2, "entry_bid": 24.0, "entry_mode": "early", "entry_option_price": 25.1, "hypothetical_budget": 44293.4, "hypothetical_contracts": 17, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 228.0, "option_spread_pct": 8.76, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.711, "shadow_only": true, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.701, "early_reclaim_pct": 64.4, "matched_signals": 34, "recovery_stability_score": 0.711, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-05T11:40:05.908683-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "MCHP261120C00080000", "current_drop_pct": 0.55, "early_entry_score": 0.727, "early_reclaim_pct": 64.6, "entry_ask": 6.9, "entry_bid": 6.8, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 44293.4, "hypothetical_contracts": 64, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1154.0, "option_spread_pct": 1.46, "option_volume": 120.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.727, "early_reclaim_pct": 64.6, "matched_signals": 36, "recovery_stability_score": 0.602, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.491, "trend_health_status": "ok"}, {"current_drop_pct": 0.68, "early_entry_score": 0.681, "early_reclaim_pct": 62.4, "matched_signals": 33, "recovery_stability_score": 0.67, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-05T11:35:05.040233-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-05T11:30:06.121387-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.51, "early_entry_score": 0.87, "early_reclaim_pct": 90.5, "entry_ask": 1.3, "entry_bid": 1.25, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 44293.4, "hypothetical_contracts": 347, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 4139.0, "option_spread_pct": 3.92, "option_volume": 86.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.38, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.87, "early_reclaim_pct": 90.5, "matched_signals": 34, "recovery_stability_score": 0.707, "success_rate": 97.06, "ticker": "FAST", "timing_score": 0.38, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.679, "early_reclaim_pct": 61.9, "matched_signals": 33, "recovery_stability_score": 0.605, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-05T11:25:04.991240-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.64, "early_entry_score": 0.85, "early_reclaim_pct": 88.2, "entry_ask": 1.35, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 44293.4, "hypothetical_contracts": 347, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 4139.0, "option_spread_pct": 11.76, "option_volume": 86.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.384, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.85, "early_reclaim_pct": 88.2, "matched_signals": 32, "recovery_stability_score": 0.687, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.384, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-05T11:20:05.108684-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                      {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.67, "early_entry_score": 0.848, "early_reclaim_pct": 87.6, "entry_ask": 1.35, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 44293.4, "hypothetical_contracts": 347, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 4139.0, "option_spread_pct": 11.76, "option_volume": 86.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.383, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.848, "early_reclaim_pct": 87.6, "matched_signals": 32, "recovery_stability_score": 0.701, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.383, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-05T11:15:06.725790-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                      {"contract_symbol": "FAST261120C00052500", "current_drop_pct": 0.67, "early_entry_score": 0.848, "early_reclaim_pct": 87.6, "entry_ask": 1.35, "entry_bid": 1.2, "entry_mode": "early", "entry_option_price": 1.275, "hypothetical_budget": 44293.4, "hypothetical_contracts": 347, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 4139.0, "option_spread_pct": 11.76, "option_volume": 86.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.719, "shadow_only": true, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.383, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.848, "early_reclaim_pct": 87.6, "matched_signals": 32, "recovery_stability_score": 0.719, "success_rate": 96.88, "ticker": "FAST", "timing_score": 0.383, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005141006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005141006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005141006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005141006)

</details>
