# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-12 10:45:05 EDT`
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
  TEAM           83.78               37            0.83              0.89        153.70               126.50         0.794          pass              0.572             70.6                           0.470               46.53              5.189                  ok            True                  False
  PYPL           91.67               24            1.08              0.45         58.81                59.96         0.675          pass              0.630             52.6                           0.517                0.02              0.211                  ok            True                  False
  SHOP           96.88               32            1.43              1.53        151.95                81.89         0.653          pass              0.666             18.1                           0.250               16.45              2.901                  ok            True                  False
  ABNB          100.00               10            2.55              3.30        183.57                64.05         0.633          pass              0.505             14.1                           0.203               17.82              2.256                  ok            True                  False
  GEHC           95.24               21            1.58              0.81         72.40                54.33         0.620          pass              0.637             33.9                           0.351               -0.42              0.311                  ok            True                  False
 CMCSA           88.24               17            1.29              0.23         25.55                42.38         0.617          pass              0.387             19.5                           0.271                6.97              0.682                  ok            True                  False
  ISRG           84.85               33            0.84              2.36        400.22                69.94         0.605          pass              0.394             16.8                           0.318               12.72              1.314                  ok            True                  False
   ROP          100.00               16            1.92              5.38        397.19                44.32         0.603          pass              0.565             21.6                           0.237                0.66              0.166                  ok            True                  False
  DXCM           88.89               36            0.74              0.46         89.33                59.17         0.576          pass              0.689             73.8                           0.433               19.22              1.143                  ok            True                  False
  FAST          100.00               18            0.87              0.32         52.24                25.01         0.575          pass              0.624             37.7                           0.256               11.28              1.193                  ok            True                  False
  PAYX          100.00               12            1.69              1.43        120.69                33.26         0.573          pass              0.551             26.9                           0.372                2.51              0.361                  ok            True                  False
   LIN           83.33               18            1.28              4.39        488.65                25.58         0.550          pass              0.212              4.9                           0.186               -4.79             -0.057                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-08-12T10:45:05.750947-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:40:06.908628-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:35:08.326280-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:30:06.810656-04:00 early_entry_1030 early_entry_shadow                                                          {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "entry_ask": 16.5, "entry_bid": 15.5, "entry_mode": "early", "entry_option_price": 16.0, "hypothetical_budget": 17549.0, "hypothetical_contracts": 10, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.25, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.838, "shadow_only": true, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 78.3, "matched_signals": 40, "recovery_stability_score": 0.838, "success_rate": 90.0, "ticker": "ZS", "timing_score": 0.443, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.72, "early_reclaim_pct": 94.1, "matched_signals": 30, "recovery_stability_score": 0.734, "success_rate": 90.0, "ticker": "CTAS", "timing_score": 0.379, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:25:01.823569-04:00 early_entry_1025 early_entry_shadow                                                      {"contract_symbol": "ZS260918C00175000", "current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "entry_ask": 16.5, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 15.95, "hypothetical_budget": 17549.0, "hypothetical_contracts": 11, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 692.0, "option_spread_pct": 6.9, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.843, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.757, "early_reclaim_pct": 80.1, "matched_signals": 41, "recovery_stability_score": 0.843, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.441, "trend_health_status": "ok"}, {"current_drop_pct": 0.59, "early_entry_score": 0.746, "early_reclaim_pct": 95.5, "matched_signals": 37, "recovery_stability_score": 0.717, "success_rate": 89.19, "ticker": "CTAS", "timing_score": 0.347, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-12T10:20:04.811080-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "CTAS260925C00205000", "current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "entry_ask": 10.3, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 8.2, "hypothetical_budget": 17549.0, "hypothetical_contracts": 21, "matched_signals": 34, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 31.0, "option_spread_pct": 51.22, "option_volume": 125.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.779, "early_reclaim_pct": 94.8, "matched_signals": 34, "recovery_stability_score": 0.643, "success_rate": 91.18, "ticker": "CTAS", "timing_score": 0.362, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-12T10:15:04.787408-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:10:02.811881-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:05:01.817084-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-12T10:00:04.707045-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "REGN260918C00790000", "current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "entry_ask": 32.7, "entry_bid": 25.0, "entry_mode": "early", "entry_option_price": 28.85, "hypothetical_budget": 17549.0, "hypothetical_contracts": 6, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 45.0, "option_spread_pct": 26.69, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.816, "early_reclaim_pct": 62.7, "matched_signals": 38, "recovery_stability_score": 0.62, "success_rate": 94.74, "ticker": "REGN", "timing_score": 0.484, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.698, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.591, "success_rate": 88.89, "ticker": "DXCM", "timing_score": 0.581, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260812104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260812104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260812104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260812104505)

</details>
