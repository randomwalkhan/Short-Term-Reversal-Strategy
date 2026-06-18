# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-18 10:50:01 EDT`
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

- Cash: `$26,514.50`
- Equity: `$26,514.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-18)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           95.24               21            0.97              0.41         60.68                21.28         0.523          pass              0.563             12.6                           0.200               -1.18             -0.158                                 ok            True                  False
  VRTX           93.33               15            1.64              5.26        456.73                24.55         0.511          pass              0.459              6.4                           0.169                2.20              0.297                                 ok            True                  False
    ZS           79.07               43            0.21              0.19        124.30               152.31         0.875          pass              0.570             94.1                           0.918               -8.24             -0.517 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                3            0.93              0.15         23.14                27.50         0.693          pass              0.529             19.8                           0.216                4.15              0.391                                 ok           False                  False
  INTU           74.42               43            0.35              0.65        268.80                98.62         0.686          pass              0.540             90.6                           0.800              -11.20             -1.224 downtrend_blocked_slope_and_streak           False                  False
  AMGN           83.33                6            1.80              4.30        339.82                27.62         0.576          pass              0.165              6.3                           0.125               -2.92             -0.124           downtrend_blocked_streak           False                  False
  WDAY           81.08               37            0.96              0.82        121.48                69.08         0.547          pass              0.483             73.0                           0.583              -18.42             -2.072 downtrend_blocked_slope_and_streak           False                  False
  GILD           85.71                7            2.01              1.77        124.69                29.17         0.547          pass              0.221              4.7                           0.102               -4.22             -0.254 downtrend_blocked_slope_and_streak           False                  False
  COST           66.67               15            1.08              7.31        962.46                23.27         0.538          pass              0.206             39.5                           0.487               -1.77             -0.052                                 ok           False                  False
   WMT           89.19               37            0.34              0.28        118.01                34.58         0.524          pass              0.650             57.4                           0.478               -0.01              0.037                                 ok           False                  False
   HON           82.86               35            0.47              0.75        228.29                41.75         0.521          pass              0.435             46.7                           0.231                4.55              0.819                                 ok           False                  False
  ADBE           79.07               43            0.22              0.30        196.15                56.59         0.503          pass              0.530             93.1                           0.897              -24.21             -2.997 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-18T10:50:01.439897-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:45:03.283549-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:40:01.292114-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:35:03.329239-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:30:02.323229-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "entry_ask": 9.9, "entry_bid": 7.35, "entry_mode": "early", "entry_option_price": 8.625, "hypothetical_budget": 13257.25, "hypothetical_contracts": 15, "matched_signals": 43, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 29.57, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.893, "early_reclaim_pct": 81.6, "matched_signals": 43, "recovery_stability_score": 0.694, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-18T10:25:02.315380-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:20:06.081546-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:15:06.113244-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:10:05.150482-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-18T10:05:02.276759-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FTNT260724C00143000", "current_drop_pct": 0.68, "early_entry_score": 0.881, "early_reclaim_pct": 77.6, "entry_ask": 9.5, "entry_bid": 5.95, "entry_mode": "early", "entry_option_price": 7.725, "hypothetical_budget": 13257.25, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 45.95, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.741, "shadow_only": true, "success_rate": 97.56, "ticker": "FTNT", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.881, "early_reclaim_pct": 77.6, "matched_signals": 41, "recovery_stability_score": 0.741, "success_rate": 97.56, "ticker": "FTNT", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260618105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260618105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260618105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260618105001)

</details>
