# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 09:35:04 EDT`
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
  MSFT           96.15               26            0.68              2.52        531.87                21.62         0.506            pass              0.671             37.8                           0.340                1.29             -0.045                                 ok            True                  False
   CEG           80.95               21            1.95              3.69        269.16                61.93         0.601            pass              0.224             21.6                           0.329               -6.88             -1.259 downtrend_blocked_slope_and_streak           False                  False
  SNPS           70.00               10            2.44              7.69        447.89                54.60         0.596            pass              0.119             19.9                           0.261              -11.56             -1.522 downtrend_blocked_slope_and_streak           False                  False
  CSCO           76.47               17            1.37              1.03        106.82                31.32         0.536            pass              0.154             17.9                           0.323               -7.92             -1.138 downtrend_blocked_slope_and_streak           False                  False
  UPRO           87.50                8            2.35              2.50        150.95                26.42         0.500            pass              0.342             30.5                           0.554               -3.05             -0.443            downtrend_blocked_slope           False                  False
  QCOM           92.00               25            1.66              2.07        177.07                39.95         0.497 below_threshold              0.621             50.3                           0.565               -0.57              0.007                                 ok           False                  False
  FAST           94.44               18            1.33              0.49         52.28                19.95         0.495 below_threshold              0.508              6.7                           0.200                2.57              0.215                                 ok           False                  False
  DXCM           87.50               16            1.76              0.99         79.84                36.58         0.493 below_threshold              0.381             30.5                           0.270               -6.59             -0.439 downtrend_blocked_slope_and_streak           False                  False
  NVDA           73.33               15            1.73              2.68        220.82                25.09         0.488 below_threshold              0.180             32.7                           0.557               -5.35             -0.613            downtrend_blocked_slope           False                  False
  AVGO           60.00               10            2.55              6.04        335.21                36.08         0.486 below_threshold              0.145             32.0                           0.583               -8.60             -0.984            downtrend_blocked_slope           False                  False
   BKR           92.86               28            0.98              0.38         55.84                24.70         0.480 below_threshold              0.565             17.9                           0.257               -1.51             -0.156                                 ok           False                  False
  AMZN           64.71               17            1.78              3.27        260.97                27.43         0.478 below_threshold              0.152             19.2                           0.384                1.43              0.109                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022093504)

</details>
