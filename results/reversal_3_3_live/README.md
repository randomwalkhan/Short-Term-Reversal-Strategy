# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 10:05:06 EST`
Last processed slot: `manage_1000`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           92.86               28            1.19              5.81        696.06                74.33         0.673            pass              0.569             13.1                           0.217               21.79              2.453                                 ok            True                  False
  FTNT           55.56                9            3.39              3.07        128.08                91.87         0.652            pass              0.150             28.1                           0.453              -27.73             -4.573 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           81.25               16            1.41              2.85        287.71                52.55         0.620            pass              0.135              0.0                           0.150              -12.14             -1.687            downtrend_blocked_slope           False                  False
  GOOG           80.00               15            1.48              2.97        286.03                51.02         0.610            pass              0.094              0.0                           0.150              -11.75             -1.630            downtrend_blocked_slope           False                  False
  MSFT          100.00                5            2.18              8.46        552.17                33.48         0.575            pass              0.477              6.4                           0.092                4.34              0.243                                 ok           False                  False
  AMZN           66.67               15            1.90              3.53        264.52                42.79         0.529            pass              0.091              1.6                           0.043                4.23              0.354                                 ok           False                  False
   BKR           83.33               18            1.64              0.57         49.62                49.30         0.526            pass              0.268             24.4                           0.248               -8.52             -1.163 downtrend_blocked_slope_and_streak           False                  False
  INTC           66.67                3            8.13              3.31         56.85               128.90         0.523            pass              0.077              8.2                           0.132              -37.38             -5.830            downtrend_blocked_slope           False                  False
  ISRG           95.12               41            0.29              0.98        481.68                40.52         0.502            pass              0.857             68.9                           0.422                8.30              0.466                                 ok           False                  False
  BKNG           73.33               15            2.24              2.68        169.82                46.70         0.501            pass              0.100              5.7                           0.084                3.75              0.594                                 ok           False                  False
   KHC           91.89               37            0.31              0.06         25.42                36.26         0.500 below_threshold              0.727             60.0                           0.385                1.08              0.201                                 ok           False                  False
  DXCM           86.11               36            0.93              0.57         88.23                45.01         0.494 below_threshold              0.440             18.0                           0.212               11.93              1.302                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-11-05T10:05:06.545963-05:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:00:05.848004-05:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T09:20:04.622994-05:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-11-04T15:10:06.129182-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:05:06.426407-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T15:00:04.760681-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:55:04.187352-05:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-11-04T14:50:05.817314-05:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-11-04T14:50:05.817314-05:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-04", "training_samples": 6270, "window": 5}
2026-11-04T12:00:04.108894-05:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105100506)

</details>
