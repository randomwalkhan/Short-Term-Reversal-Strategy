# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 10:30:06 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           91.30               23            3.11              3.65        165.77               109.59         0.686          pass              0.457              0.0                           0.177               22.17              2.792                                 ok            True                  False
  PYPL           88.89               18            1.54              0.57         52.65                57.12         0.629          pass              0.427             24.5                           0.211               -0.18             -0.186                                 ok            True                  False
  NVDA           91.30               23            1.49              2.38        227.85                44.57         0.578          pass              0.481             11.7                           0.148                0.92              0.448                                 ok            True                  False
  ADSK           81.48               27            1.59              2.44        218.57                55.47         0.549          pass              0.208              0.0                           0.213                4.60              0.284                                 ok            True                  False
  UPRO           88.24               17            1.76              1.89        152.93                31.44         0.526          pass              0.354             11.7                           0.192                2.61              0.469                                 ok            True                  False
  ADBE           94.87               39            0.14              0.23        238.15                47.75         0.546          pass              0.809             54.7                           0.351               -6.65             -0.625            downtrend_blocked_slope           False                  False
   XEL           88.89                9            0.92              0.47         71.86                15.29         0.546          pass              0.407             38.4                           0.619               -5.54             -0.547 downtrend_blocked_slope_and_streak           False                  False
  MRVL           78.12               32            1.99              3.66        260.79                69.87         0.544          pass              0.230              9.8                           0.120                9.41              1.459                                 ok           False                  False
   WBD           92.68               41            0.10              0.02         30.82                38.24         0.540          pass              0.853             86.9                           0.617               10.36              1.013                                 ok           False                  False
   CEG           75.00               20            1.29              2.39        262.44                42.63         0.525          pass              0.228             36.3                           0.429              -11.52             -1.173 downtrend_blocked_slope_and_streak           False                  False
   KHC           93.75               16            0.96              0.16         23.93                22.23         0.520          pass              0.598             46.5                           0.499               -3.41             -0.218           downtrend_blocked_streak           False                  False
  ALNY           84.09               44            0.06              0.10        251.61                45.04         0.513          pass              0.632             90.6                           0.572               -2.52             -0.146                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-23T10:30:06.224797-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:25:06.407969-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:20:05.981567-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:15:04.258896-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:10:06.450659-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "entry_ask": 5.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 41.86, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.742, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "matched_signals": 33, "recovery_stability_score": 0.742, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:05:05.428675-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:00:05.505875-04:00 early_entry_1000 early_entry_shadow  {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "entry_ask": 5.3, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 35735.4, "hypothetical_contracts": 78, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 32.97, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "matched_signals": 33, "recovery_stability_score": 0.713, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T09:35:04.357346-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923103006)

</details>
