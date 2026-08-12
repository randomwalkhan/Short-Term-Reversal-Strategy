# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 10:35:08 EDT`
Last processed slot: `manage_1030`

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
  PYPL           91.67               24            1.08              0.45         58.81                59.96         0.675          pass              0.630             52.6                           0.471                0.02              0.211                  ok            True                  False
  SHOP           97.06               34            1.34              1.44        151.99                81.89         0.647          pass              0.694             23.2                           0.275               16.56              2.905                  ok            True                  False
  ABNB          100.00               10            2.47              3.19        183.61                64.05         0.638          pass              0.514             16.8                           0.184               17.91              2.260                  ok            True                  False
  GEHC           95.45               22            1.34              0.68         72.46                54.33         0.629          pass              0.675             44.0                           0.624               -0.17              0.322                  ok            True                  False
  TMUS           90.62               32            0.71              0.88        178.21                55.82         0.616          pass              0.564             24.1                           0.304                2.30              0.267                  ok            True                  False
 CMCSA           88.24               17            1.33              0.24         25.55                42.38         0.615          pass              0.379             17.1                           0.231                6.93              0.680                  ok            True                  False
   ROP          100.00               12            2.17              6.05        396.91                44.32         0.614          pass              0.510             11.8                           0.223                0.41              0.155                  ok            True                  False
  FAST          100.00               16            1.02              0.37         52.22                25.01         0.578          pass              0.578             26.7                           0.198               11.11              1.186                  ok            True                  False
  PAYX          100.00               12            1.76              1.49        120.66                33.26         0.568          pass              0.542             23.9                           0.382                2.44              0.358                  ok            True                  False
  MDLZ           92.00               25            0.65              0.28         61.66                29.90         0.563          pass              0.636             53.2                           0.611               -2.69             -0.200                  ok            True                  False
   ADP          100.00               18            1.66              3.15        269.74                32.74         0.557          pass              0.549             13.3                           0.318                1.03              0.115                  ok            True                  False
   LIN           83.33               18            1.21              4.16        488.75                25.58         0.556          pass              0.198              0.0                           0.236               -4.73             -0.054                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-08-12T10:35:08.326280-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:30:06.810656-04:00 early_entry_1030 early_entry_shadow                                                          {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "entry_ask": 16.5, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.25, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.838, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "matched_signals": 40, "recovery_stability_score": 0.838, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.72, "early_reclaim_pct": 94.1, "matched_signals": 30, "recovery_stability_score": 0.734, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.379, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:25:01.823569-04:00 early_entry_1025 early_entry_shadow                                                      {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "entry_ask": 16.5, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 15.95, "hypothetical_budget": 17549.0, "hypothetical_contracts": 11, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.9, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.843, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "matched_signals": 41, "recovery_stability_score": 0.843, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "trend_health_status": "ok"}, {"current_drop_pct": 0.59, "early_entry_score": 0.746, "early_reclaim_pct": 95.5, "matched_signals": 37, "recovery_stability_score": 0.717, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.347, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:20:04.811080-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "matched_signals": 34, "recovery_stability_score": 0.643, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T10:15:04.787408-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:10:02.811881-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:05:01.817084-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:00:04.707045-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "REGN260918C00790000", "current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "entry_ask": 32.7, "entry_bid": 25.0, "entry_mode": "early", "entry_option_price": 28.85, "hypothetical_budget": 17549.0, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 45.0, "option_spread_pct": 26.69, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "matched_signals": 38, "recovery_stability_score": 0.62, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.698, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.591, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T09:50:02.620693-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"asset_type": "option", "contract_symbol": "LRCX260918C00310000", "fill_price": 34.9, "pnl": 4025.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 29.98, "ticker": "LRCX"}
2026-08-12T09:35:01.769154-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812103508)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812103508)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812103508)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812103508)

</details>
