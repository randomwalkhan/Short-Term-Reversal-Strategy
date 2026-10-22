# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 09:40:04 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FAST           93.33               15            1.49              0.55         52.26                19.95         0.501            pass              0.450              3.7                           0.074                2.42              0.208                                 ok            True                  False
   CEG           80.95               21            1.94              3.68        269.16                61.93         0.601            pass              0.225             22.0                           0.306               -6.87             -1.259 downtrend_blocked_slope_and_streak           False                  False
  SNPS           57.14                7            2.97              9.39        447.17                54.60         0.568            pass              0.070              4.4                           0.101              -12.05             -1.547 downtrend_blocked_slope_and_streak           False                  False
  CSCO           80.00               20            1.08              0.81        106.91                31.32         0.540            pass              0.226             35.2                           0.477               -7.65             -1.125 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.67               30            0.46              1.72        532.21                21.62         0.496 below_threshold              0.755             57.5                           0.388                1.51             -0.035                                 ok           False                  False
  UPRO           87.50                8            2.45              2.60        150.90                26.42         0.494 below_threshold              0.332             27.5                           0.580               -3.15             -0.448            downtrend_blocked_slope           False                  False
   BKR           83.33               12            2.00              0.78         55.66                24.70         0.493 below_threshold              0.152              0.0                           0.030               -2.52             -0.202                                 ok           False                  False
  AMZN           50.00                4            2.60              4.77        260.32                27.43         0.489 below_threshold              0.049              0.0                           0.269                0.59              0.070                                 ok           False                  False
  NVDA           73.33               15            1.72              2.67        220.82                25.09         0.488 below_threshold              0.181             32.9                           0.614               -5.35             -0.612            downtrend_blocked_slope           False                  False
  AVGO           60.00               10            2.58              6.11        335.18                36.08         0.484 below_threshold              0.142             31.3                           0.651               -8.63             -0.985            downtrend_blocked_slope           False                  False
  QCOM           91.30               23            2.10              2.61        176.84                39.95         0.481 below_threshold              0.548             37.3                           0.570               -1.01             -0.013                                 ok           False                  False
  NXPI           92.59               27            1.17              1.98        241.51                33.60         0.480 below_threshold              0.679             60.7                           0.719                3.66              0.605                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                        detail
2026-10-22T09:20:05.053527-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                     {'saved': 91, 'empty': 2}
2026-10-21T15:10:06.687584-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-10-21T15:05:05.870739-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-10-21T15:00:05.576532-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-10-21T14:55:05.525520-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-10-21T14:50:04.709155-04:00       entry_1500           entry_skipped                                                                                                                                                                                                        {"reason": "no_trade_after_option_and_timing_filters"}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.216, "option_liquidity_status": "no_two_sided_quote,wide_spread", "option_open_interest": 112.0, "option_spread_pct": null, "option_volume": 63.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.504}
2026-10-21T14:50:04.709155-04:00       entry_1500 entry_candidate_skipped   {"early_entry_score": 0.255, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 40.0, "option_spread_pct": 10.41, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "MELI", "timing_score": 0.508}
2026-10-21T14:50:04.709155-04:00       entry_1500          timing_overlay                                                                                                                                                  {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-21", "training_samples": 6158, "window": 5}
2026-10-21T12:00:03.696470-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022094004)

</details>
