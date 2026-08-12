# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 11:20:01 EDT`
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
  TEAM           83.78               37            0.90              0.97        153.67               126.50         0.791          pass              0.565             68.2                           0.422               46.43              5.186                  ok            True                  False
  PYPL           91.30               23            1.12              0.46         58.80                59.96         0.679          pass              0.609             51.1                           0.401               -0.02              0.210                  ok            True                  False
  SHOP           96.30               27            1.77              1.89        151.80                81.89         0.661          pass              0.593              4.4                           0.242               16.05              2.885                  ok            True                  False
  ABNB          100.00               10            2.59              3.36        183.54                64.05         0.631          pass              0.501             12.5                           0.220               17.76              2.254                  ok            True                  False
 CMCSA           87.50               16            1.35              0.24         25.55                42.38         0.619          pass              0.349             15.9                           0.289                6.91              0.679                  ok            True                  False
  TMUS           88.57               35            0.57              0.71        178.28                55.82         0.603          pass              0.571             38.6                           0.358                2.44              0.273                  ok            True                  False
  GEHC           93.33               30            0.92              0.47         72.55                54.33         0.602          pass              0.734             61.5                           0.761                0.25              0.342                  ok            True                   True
   ROP          100.00               16            1.93              5.40        397.18                44.32         0.602          pass              0.564             21.3                           0.260                0.65              0.166                  ok            True                  False
  PAYX          100.00               13            1.51              1.28        120.75                33.26         0.577          pass              0.581             34.5                           0.551                2.69              0.369                  ok            True                  False
  FAST          100.00               20            0.65              0.24         52.28                25.01         0.576          pass              0.684             53.4                           0.516               11.53              1.203                  ok            True                  False
  DXCM           88.57               35            0.93              0.58         89.28                59.17         0.570          pass              0.653             67.1                           0.452               19.00              1.135                  ok            True                  False
   LIN           80.00               15            1.49              5.11        488.34                25.58         0.549          pass              0.093              1.6                           0.101               -5.00             -0.067                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-12T11:20:01.139516-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                  {"contract_symbol": "GEHC260925C00072000", "current_drop_pct": 0.92, "early_entry_score": 0.734, "early_reclaim_pct": 61.5, "entry_ask": 4.7, "entry_bid": 2.0, "entry_mode": "early", "entry_option_price": 3.35, "hypothetical_budget": 17549.0, "hypothetical_contracts": 52, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 80.6, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 93.33, "ticker": "GEHC", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.734, "early_reclaim_pct": 61.5, "matched_signals": 30, "recovery_stability_score": 0.761, "success_rate": 93.33, "ticker": "GEHC", "timing_score": 0.602, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T11:15:03.361027-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.54, "early_entry_score": 0.748, "early_reclaim_pct": 95.9, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 37, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.35, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.748, "early_reclaim_pct": 95.9, "matched_signals": 37, "recovery_stability_score": 0.748, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.35, "trend_health_status": "ok"}, {"current_drop_pct": 0.93, "early_entry_score": 0.732, "early_reclaim_pct": 60.9, "matched_signals": 30, "recovery_stability_score": 0.744, "success_rate": 93.33, "ticker": "GEHC", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T11:10:01.765274-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.62, "early_entry_score": 0.731, "early_reclaim_pct": 95.3, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 36, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 88.89, "ticker": "CTAS", "timing_score": 0.35, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.731, "early_reclaim_pct": 95.3, "matched_signals": 36, "recovery_stability_score": 0.715, "success_rate": 88.89, "ticker": "CTAS", "timing_score": 0.35, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T11:05:03.802537-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.8, "early_entry_score": 0.741, "early_reclaim_pct": 76.8, "entry_ask": 17.05, "entry_bid": 16.3, "entry_mode": "early", "entry_option_price": 16.675, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 4.5, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.568, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.439, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.741, "early_reclaim_pct": 76.8, "matched_signals": 40, "recovery_stability_score": 0.568, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.439, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T11:00:05.629703-04:00 early_entry_1100 early_entry_shadow                                           {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "entry_ask": 17.35, "entry_bid": 16.7, "entry_mode": "early", "entry_option_price": 17.025, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 3.82, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.596, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.737, "early_reclaim_pct": 75.5, "matched_signals": 40, "recovery_stability_score": 0.596, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.437, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.721, "early_reclaim_pct": 94.2, "matched_signals": 30, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:55:04.810521-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                 {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "entry_ask": 17.7, "entry_bid": 16.95, "entry_mode": "early", "entry_option_price": 17.325, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 4.33, "option_volume": 27.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.696, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.6, "matched_signals": 41, "recovery_stability_score": 0.696, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:50:01.775257-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                  {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "entry_ask": 17.55, "entry_bid": 16.45, "entry_mode": "early", "entry_option_price": 17.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.47, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.762, "early_reclaim_pct": 81.5, "matched_signals": 41, "recovery_stability_score": 0.789, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:45:05.750947-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:40:06.908628-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:35:08.326280-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812112001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812112001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812112001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812112001)

</details>
