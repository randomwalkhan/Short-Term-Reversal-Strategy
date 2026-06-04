# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-04 09:39:00 EDT`
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

- Cash: `$34,571.75`
- Equity: `$34,571.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  QCOM           94.12               17            2.40              4.19        248.21                96.24         0.652          pass              0.667             59.5                           0.598               20.50              1.369                      ok            True                  False
  CSCO           92.31               13            1.54              1.36        125.92                54.61         0.632          pass              0.463             17.2                           0.237                8.92              0.853                      ok            True                  False
   ADI          100.00               10            2.40              7.35        434.52                44.48         0.559          pass              0.510             17.9                           0.197                7.61              0.915                      ok            True                  False
   WDC           96.88               32            0.99              4.13        592.34                59.52         0.532          pass              0.840             80.0                           0.786               27.98              2.334                      ok            True                   True
  ASML           95.45               22            2.19             26.46       1715.02                50.96         0.516          pass              0.626             31.4                           0.495                8.93              0.806                      ok            True                  False
  SNPS           92.86               28            1.31              4.58        496.06                43.50         0.510          pass              0.569             18.5                           0.199               -1.49             -0.439                      ok            True                  False
  UPRO           93.75               32            0.53              0.55        147.48                29.41         0.509          pass              0.774             69.8                           0.700                4.33              0.567                      ok            True                   True
  CDNS           94.59               37            0.62              1.76        407.25                45.02         0.506          pass              0.826             68.6                           0.358               15.56              1.574                      ok            True                  False
    ZS           82.22               45            0.22              0.20        134.28               161.85         0.860          pass              0.609             87.8                           0.440              -23.14             -2.933 downtrend_blocked_slope           False                  False
  INSM           79.55               44            0.16              0.12        103.81               108.54         0.750          pass              0.559             94.8                           0.563               -3.91             -0.484 downtrend_blocked_slope           False                  False
  MRVL          100.00                7            5.23             11.04        296.92               116.52         0.578          pass              0.566             36.0                           0.554               53.04              4.797                      ok           False                  False
   CEG           81.08               37            0.29              0.55        267.01                55.72         0.567          pass              0.493             75.9                           0.446               -5.26             -0.930 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-06-04T09:22:28.092024-04:00     data_refresh   data_refresh                                                                                                {'saved': 93}
2026-06-03T15:10:03.976623-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T15:05:05.758809-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T15:00:06.248089-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T14:55:06.012322-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-06-03T14:50:06.341439-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T14:50:06.341439-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-03", "training_samples": 5182, "window": 5}
2026-06-03T12:00:06.118457-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:55:01.593242-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-06-03T11:50:05.337681-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260604093900)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260604093900)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260604093900)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260604093900)

</details>
