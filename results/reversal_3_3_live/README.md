# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 11:05:01 EDT`
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

- Cash: `$17,620.25`
- Equity: `$27,135.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$140.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9515.0        46.88          47.58      660.72        661.98          bid_ask_mid                      47.58                bid_ask_mid                    True           140.0                   1.49         81.82               22              1.27         53.38           53.69                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   ADP          100.00               10            1.72              3.03        249.75                31.20         0.579          pass              0.610             50.7                           0.598                9.67              0.840                  ok            True                  False
  AAPL           96.30               27            0.56              1.24        316.78                35.57         0.576          pass              0.791             73.3                           0.634               12.00              1.128                  ok            True                  False
  GILD           89.47               19            0.97              0.90        131.02                32.97         0.572          pass              0.476             35.4                           0.332                3.00              0.408                  ok            True                  False
  QCOM           84.38               32            0.72              0.93        183.58                63.33         0.564          pass              0.540             73.3                           0.668               -3.21              0.152                  ok            True                  False
  PYPL           81.82               11            1.82              0.61         47.39                33.27         0.563          pass              0.199             29.1                           0.301                5.42              0.638                  ok            True                  False
  AMGN           94.44               18            1.06              2.67        359.30                21.45         0.548          pass              0.590             32.1                           0.393               -1.09             -0.084                  ok            True                  False
  PAYX          100.00               29            0.55              0.43        110.57                31.82         0.535          pass              0.837             85.6                           0.742               10.35              0.966                  ok            True                  False
  CTAS           88.00               25            0.99              1.27        183.21                31.28         0.530          pass              0.502             45.2                           0.350                7.60              0.646                  ok            True                  False
  PCAR           84.62               26            0.95              0.83        123.91                31.62         0.528          pass              0.359             25.3                           0.238                2.91              0.398                  ok            True                  False
  TMUS           87.10               31            0.76              1.00        187.98                37.13         0.525          pass              0.487             35.1                           0.394                7.48              1.024                  ok            True                  False
  IDXX           87.50               16            2.16              8.52        560.56                34.15         0.508          pass              0.408             39.2                           0.659                3.01              0.532                  ok            True                  False
   KHC           88.89                9            0.97              0.17         25.16                36.18         0.662          pass              0.435             44.1                           0.570                3.29              0.330                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-07-14T11:05:01.389220-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T11:00:04.389185-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:55:01.316217-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:50:01.398804-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "DASH260814C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "entry_ask": 13.75, "entry_bid": 11.3, "entry_mode": "early", "entry_option_price": 12.525, "hypothetical_budget": 8810.13, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 19.56, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.826, "shadow_only": true, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.889, "early_reclaim_pct": 81.1, "matched_signals": 45, "recovery_stability_score": 0.826, "success_rate": 95.56, "ticker": "DASH", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:45:05.382640-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:40:02.394699-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:35:01.379704-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:30:01.227428-04:00 early_entry_1030 early_entry_shadow                 {"contract_symbol": "DASH260821C00190000", "current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "entry_ask": 14.35, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 8810.13, "hypothetical_contracts": 6, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 268.0, "option_spread_pct": 20.35, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:25:01.405128-04:00 early_entry_1025 early_entry_shadow    {"contract_symbol": "VRSK260821C00190000", "current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "entry_ask": 12.0, "entry_bid": 9.5, "entry_mode": "early", "entry_option_price": 10.75, "hypothetical_budget": 8810.13, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 23.26, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "matched_signals": 37, "recovery_stability_score": 0.655, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:20:04.363539-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714110501)

</details>
