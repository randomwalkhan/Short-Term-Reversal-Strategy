# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 09:45:06 EDT`
Last processed slot: `manual`

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
  SOXL           80.65               31            3.69              3.92        150.27               119.42         0.642          pass              0.279             19.1                           0.231               16.35              2.493                                 ok            True                  False
  DRAM           82.76               29            1.45              0.64         63.39                51.34         0.565          pass              0.323             22.0                           0.276                1.90              0.656                                 ok            True                  False
  ADSK           81.82               33            0.92              1.42        219.01                55.47         0.562          pass              0.258              0.0                           0.223                5.31              0.315                                 ok            True                  False
  INTC           82.86               35            1.66              1.44        123.24                67.82         0.530          pass              0.388             30.9                           0.348               14.65              2.106                                 ok            True                  False
  QCOM           90.91               33            0.65              0.90        197.89                46.97         0.505          pass              0.653             52.6                           0.436               11.67              1.055                                 ok            True                  False
  UPRO           80.65               31            0.73              0.78        153.40                31.44         0.504          pass              0.208              0.0                           0.211                3.69              0.517                                 ok            True                  False
  NVDA           91.89               37            0.10              0.17        228.80                44.57         0.588          pass              0.811             84.9                           0.783                2.33              0.511                                 ok           False                  False
   XEL           88.89                9            0.92              0.47         71.86                15.29         0.547          pass              0.322             10.1                           0.127               -5.54             -0.547 downtrend_blocked_slope_and_streak           False                  False
   WBD           92.68               41            0.09              0.02         30.82                38.24         0.540          pass              0.857             88.2                           0.663               10.37              1.013                                 ok           False                  False
  CHTR           84.85               33            1.62              1.33        116.69                65.60         0.531          pass              0.336              0.0                           0.190              -13.84             -2.032 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.24               17            0.48              0.44        131.00                15.28         0.531          pass              0.331              3.8                           0.168               -4.49             -0.602 downtrend_blocked_slope_and_streak           False                  False
   CEG           72.22               18            1.53              2.83        262.25                42.63         0.519          pass              0.179             24.5                           0.227              -11.73             -1.184 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                 detail
2026-09-23T09:35:04.357346-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.621, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.01, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.504}
2026-09-22T14:50:01.294026-04:00   entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-22", "training_samples": 5799, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923094506)

</details>
