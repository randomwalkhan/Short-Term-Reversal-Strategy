# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-22 09:30:04 EDT`
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
  QCOM           90.91               11            2.95              3.67        176.39                39.95         0.500 below_threshold              0.383             11.9                           0.193               -1.87             -0.053                                 ok            True                  False
   CEG           87.88               33            0.84              1.59        270.06                61.93         0.606            pass              0.618             64.8                           0.583               -5.82             -1.208 downtrend_blocked_slope_and_streak           False                  False
  SNPS           61.54               13            2.14              6.74        448.30                54.60         0.593            pass              0.079              0.0                           0.236              -11.29             -1.508 downtrend_blocked_slope_and_streak           False                  False
  CSCO           73.33               15            1.55              1.16        106.76                31.32         0.534            pass              0.094              2.4                           0.155               -8.09             -1.147 downtrend_blocked_slope_and_streak           False                  False
  DASH           86.84               38            1.01              1.31        183.89                51.42         0.496 below_threshold              0.500             27.2                           0.310               -4.76             -0.459            downtrend_blocked_slope           False                  False
  UPRO           85.71                7            2.60              2.76        150.84                26.42         0.490 below_threshold              0.270             23.0                           0.478               -3.30             -0.455            downtrend_blocked_slope           False                  False
  AMZN           64.71               17            1.67              3.06        261.06                27.43         0.485 below_threshold              0.168             24.4                           0.437                1.55              0.114                                 ok           False                  False
  NXPI           90.00               20            1.88              3.18        241.00                33.60         0.483 below_threshold              0.443             20.5                           0.214                2.92              0.572                                 ok           False                  False
  MSFT           94.12               34            0.27              1.00        532.52                21.62         0.481 below_threshold              0.811             75.3                           0.531                1.71             -0.026                                 ok           False                  False
  ABNB           82.35               17            1.84              2.27        175.97                26.45         0.476 below_threshold              0.197             13.2                           0.305                6.41              0.806                                 ok           False                  False
  MELI           79.55               44            0.42              5.42       1852.56                40.26         0.471 below_threshold              0.430             61.1                           0.630               -0.51             -0.148                                 ok           False                  False
  CDNS           64.29               14            2.47              5.64        323.65                37.11         0.470 below_threshold              0.074              0.0                           0.217               -8.83             -1.014 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261022093004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261022093004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261022093004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261022093004)

</details>
