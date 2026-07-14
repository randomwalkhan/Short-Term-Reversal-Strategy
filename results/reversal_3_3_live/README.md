# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-14 10:30:01 EDT`
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

- Cash: `$17,620.25`
- Equity: `$27,040.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$45.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  META     option         option META260821C00660000       2026-07-13                   1      2      9375.0                  9420.0        46.88           47.1      660.72        658.83          bid_ask_mid                       47.1                bid_ask_mid                    True            45.0                   0.48         81.82               22              1.27         53.38            55.3                  55.99                7322.0         1343.0               0.02                      ok
```

## Today's Closed Trades (2026-07-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   PEP           88.89               18            0.79              0.77        138.16                30.22         0.596          pass              0.362              3.9                           0.220               -0.93             -0.092                                 ok            True                  False
  AAPL           95.65               23            0.75              1.66        316.60                35.57         0.591          pass              0.739             64.3                           0.650               11.78              1.120                                 ok            True                  False
  GILD           86.36               22            0.86              0.79        131.06                32.97         0.555          pass              0.434             42.9                           0.390                3.12              0.413                                 ok            True                  False
  AMGN           94.12               17            1.14              2.87        359.22                21.45         0.550          pass              0.559             27.1                           0.275               -1.17             -0.087                                 ok            True                  False
  PYPL           81.25               16            1.51              0.50         47.43                33.27         0.548          pass              0.251             41.0                           0.412                5.75              0.652                                 ok            True                  False
  PAYX          100.00               25            0.85              0.66        110.47                31.82         0.542          pass              0.788             77.9                           0.593               10.02              0.952                                 ok            True                  False
  QCOM           81.48               27            1.62              2.08        183.09                63.33         0.538          pass              0.327             40.0                           0.369               -4.09              0.111                                 ok            True                  False
  CTAS           89.66               29            0.77              0.99        183.32                31.28         0.518          pass              0.607             57.1                           0.621                7.84              0.655                                 ok            True                  False
  IDXX           90.00               10            2.94             11.60        559.24                34.15         0.506          pass              0.369             17.3                           0.234                2.19              0.496                                 ok            True                  False
   KHC           88.89                9            0.85              0.15         25.17                36.18         0.668          pass              0.457             50.9                           0.520                3.41              0.335                                 ok           False                  False
  MDLZ          100.00                6            1.32              0.55         59.62                31.17         0.648          pass              0.524             19.8                           0.290               -0.97              0.027                                 ok           False                  False
   KDP           81.82               11            1.22              0.27         31.14                34.17         0.612          pass              0.201             28.3                           0.322               -7.85             -0.770 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-14T10:30:01.227428-04:00 early_entry_1030 early_entry_shadow                               {"contract_symbol": "DASH260821C00190000", "current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "entry_ask": 14.35, "entry_bid": 11.7, "entry_mode": "early", "entry_option_price": 13.025, "hypothetical_budget": 8810.13, "hypothetical_contracts": 6, "matched_signals": 44, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 268.0, "option_spread_pct": 20.35, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.873, "early_reclaim_pct": 75.7, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 95.45, "ticker": "DASH", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:25:01.405128-04:00 early_entry_1025 early_entry_shadow                  {"contract_symbol": "VRSK260821C00190000", "current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "entry_ask": 12.0, "entry_bid": 9.5, "entry_mode": "early", "entry_option_price": 10.75, "hypothetical_budget": 8810.13, "hypothetical_contracts": 8, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 23.26, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.711, "early_reclaim_pct": 79.9, "matched_signals": 37, "recovery_stability_score": 0.655, "success_rate": 89.19, "ticker": "VRSK", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-14T10:20:04.363539-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:15:01.411533-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:10:01.422460-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:05:01.368977-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-14T10:00:02.374246-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "SNPS260814C00430000", "current_drop_pct": 0.59, "early_entry_score": 0.736, "early_reclaim_pct": 81.0, "entry_ask": 0.0, "entry_bid": 0.0, "entry_mode": "early", "entry_option_price": 30.45, "hypothetical_budget": 8810.13, "hypothetical_contracts": 2, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "option_open_interest": 3.0, "option_spread_pct": null, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.763, "shadow_only": true, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.394, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.736, "early_reclaim_pct": 81.0, "matched_signals": 39, "recovery_stability_score": 0.763, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.394, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T15:10:07.483451-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T15:05:06.913203-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
2026-07-13T15:00:09.058779-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260714103001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260714103001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260714103001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260714103001)

</details>
