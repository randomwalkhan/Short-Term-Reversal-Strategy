# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 09:55:04 EST`
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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DXCM           83.78               37            0.67              0.40         84.67                47.84         0.522            pass              0.378             14.9                           0.183                3.54              0.295                                 ok            True                  False
  NVDA           69.57               23            1.57              1.64        148.60               127.24         0.757            pass              0.283             40.1                           0.277              -11.57             -0.947 downtrend_blocked_slope_and_streak           False                  False
   KDP           88.57               35            0.34              0.08         35.59                47.31         0.576            pass              0.496             14.3                           0.157                0.25             -0.015                                 ok           False                  False
   CEG           88.64               44            0.14              0.24        235.18                66.73         0.559            pass              0.697             70.2                           0.362              -16.68             -2.010 downtrend_blocked_slope_and_streak           False                  False
  REGN           89.36               47            0.08              0.55        981.63                56.75         0.557            pass              0.759             84.5                           0.483                3.25              0.297                                 ok           False                  False
  ROST           91.43               35            0.57              0.89        222.88                44.59         0.528            pass              0.592             22.6                           0.213               -6.43             -0.485            downtrend_blocked_slope           False                  False
  ISRG           86.84               38            0.52              1.54        426.52                50.77         0.528            pass              0.552             43.3                           0.297               -3.39             -0.424           downtrend_blocked_streak           False                  False
   AEP           96.30               27            0.15              0.14        127.53                16.32         0.521            pass              0.605             13.3                           0.101               -1.18             -0.134                                 ok           False                  False
  ALNY           75.68               37            0.91              1.05        164.28               117.72         0.513            pass              0.293             20.6                           0.218                4.20              0.222                                 ok           False                  False
  MDLZ           97.06               34            0.13              0.06         67.78                23.85         0.512            pass              0.857             82.0                           0.569                1.74              0.054                                 ok           False                  False
  PANW           81.08               37            1.21              3.01        354.85                69.35         0.498 below_threshold              0.485             75.5                           0.729                9.04              1.310                                 ok           False                  False
  GILD           90.91               33            0.85              1.06        176.29                34.85         0.487 below_threshold              0.627             44.8                           0.365                4.33              0.534                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot    event_type                                                         detail
2026-11-27T09:20:04.710561-05:00 data_refresh  data_refresh                                      {'saved': 91, 'empty': 2}
2026-11-26T16:10:21.376436-05:00  manage_1600  slot_skipped                                {"reason": "already_processed"}
2026-11-26T15:54:23.516183-05:00  manage_1600 market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:38:19.314719-05:00  manage_1530  slot_skipped                                {"reason": "already_processed"}
2026-11-26T15:27:17.895294-05:00  manage_1530 market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:11:16.077658-05:00   entry_1500  slot_skipped                                {"reason": "already_processed"}
2026-11-26T14:56:03.145316-05:00   entry_1500  slot_skipped                                {"reason": "already_processed"}
2026-11-26T14:52:31.871596-05:00   entry_1500 market_closed {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T14:35:06.546537-05:00  manage_1430  slot_skipped                                {"reason": "already_processed"}
2026-11-26T14:34:41.057855-05:00  manage_1430  slot_skipped                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127095504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127095504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127095504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127095504)

</details>
