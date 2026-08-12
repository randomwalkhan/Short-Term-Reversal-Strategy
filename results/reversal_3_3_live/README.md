# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 11:15:03 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$35,098.00`
- Equity: `$35,098.00`
- Realized PnL: `$25,098.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-12)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  LRCX     option         option LRCX260918C00310000      5          2026-08-10         2026-08-12        26.85        34.9 4025.0   29.981378 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           82.86               35            1.03              1.11        153.60               126.50         0.793          pass              0.513             63.5                           0.349               46.24              5.180                  ok            True                  False
  PYPL           92.00               25            1.03              0.43         58.82                59.96         0.673          pass              0.652             54.8                           0.552                0.07              0.214                  ok            True                  False
  SHOP           96.43               28            1.68              1.79        151.84                81.89         0.662          pass              0.603              5.5                           0.189               16.16              2.889                  ok            True                  False
  ABNB          100.00               10            2.48              3.21        183.60                64.05         0.637          pass              0.512             16.2                           0.275               17.89              2.259                  ok            True                  False
 CMCSA           93.33               15            1.40              0.25         25.54                42.38         0.630          pass              0.488             12.2                           0.260                6.84              0.676                  ok            True                  False
  TMUS           90.91               33            0.69              0.86        178.22                55.82         0.612          pass              0.583             25.9                           0.293                2.32              0.268                  ok            True                  False
  GEHC           93.33               30            0.93              0.48         72.55                54.33         0.601          pass              0.732             60.9                           0.744                0.24              0.341                  ok            True                   True
   ROP          100.00               16            2.02              5.65        397.08                44.32         0.597          pass              0.553             17.7                           0.219                0.56              0.162                  ok            True                  False
  DXCM           88.89               36            0.61              0.38         89.37                59.17         0.584          pass              0.703             78.2                           0.530               19.37              1.149                  ok            True                  False
  PAYX          100.00               12            1.67              1.41        120.69                33.26         0.574          pass              0.554             27.8                           0.364                2.53              0.362                  ok            True                  False
  FAST          100.00               23            0.59              0.22         52.29                25.01         0.560          pass              0.715             57.5                           0.523               11.59              1.206                  ok            True                  False
   LIN           81.25               16            1.46              5.00        488.39                25.58         0.546          pass              0.139              3.6                           0.132               -4.97             -0.066                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-12T11:15:03.361027-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.54, "early_entry_score": 0.748, "early_reclaim_pct": 95.9, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 37, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.35, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.748, "early_reclaim_pct": 95.9, "matched_signals": 37, "recovery_stability_score": 0.748, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.35, "trend_health_status": "ok"}, {"current_drop_pct": 0.93, "early_entry_score": 0.732, "early_reclaim_pct": 60.9, "matched_signals": 30, "recovery_stability_score": 0.744, "success_rate": 93.33, "ticker": "GEHC", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T11:10:01.765274-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.62, "early_entry_score": 0.731, "early_reclaim_pct": 95.3, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 36, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 88.89, "ticker": "CTAS", "timing_score": 0.35, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.731, "early_reclaim_pct": 95.3, "matched_signals": 36, "recovery_stability_score": 0.715, "success_rate": 88.89, "ticker": "CTAS", "timing_score": 0.35, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T11:05:03.802537-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.8, "early_entry_score": 0.741, "early_reclaim_pct": 76.8, "entry_ask": 17.05, "entry_bid": 16.3, "entry_mode": "early", "entry_option_price": 16.675, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 4.5, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.568, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.741, "early_reclaim_pct": 76.8, "matched_signals": 40, "recovery_stability_score": 0.568, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.439, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T11:00:05.629703-04:00 early_entry_1100 early_entry_shadow                                           {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "entry_ask": 17.35, "entry_bid": 16.7, "entry_mode": "early", "entry_option_price": 17.025, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 3.82, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.596, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "matched_signals": 40, "recovery_stability_score": 0.596, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.721, "early_reclaim_pct": 94.2, "matched_signals": 30, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:55:04.810521-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                 {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "entry_ask": 17.7, "entry_bid": 16.95, "entry_mode": "early", "entry_option_price": 17.325, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 4.33, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "matched_signals": 41, "recovery_stability_score": 0.696, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:50:01.775257-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                  {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "entry_ask": 17.55, "entry_bid": 16.45, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.47, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "matched_signals": 41, "recovery_stability_score": 0.789, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:45:05.750947-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:40:06.908628-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:35:08.326280-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:30:06.810656-04:00 early_entry_1030 early_entry_shadow                                              {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "entry_ask": 16.5, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.25, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.838, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "matched_signals": 40, "recovery_stability_score": 0.838, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.72, "early_reclaim_pct": 94.1, "matched_signals": 30, "recovery_stability_score": 0.734, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.379, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812111503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812111503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812111503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812111503)

</details>
