# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 09:35:04 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           80.56               36            1.37              2.22        229.91                83.89         0.559              pass              0.276             10.7                           0.172               17.84              2.310                                 ok            True                  False
  NVDA           66.67               27            1.08              1.13        148.82               127.24         0.767              pass              0.234             14.8                           0.188              -11.13             -0.925 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           97.14               35            0.06              0.03         67.80                23.85         0.512              pass              0.894             92.0                           0.692                1.82              0.057                                 ok           False                  False
  GILD           90.91               33            0.81              1.01        176.31                34.85         0.489   below_threshold              0.635             47.3                           0.439                4.38              0.536                                 ok           False                  False
  PANW           77.78               18            3.51              8.75        352.39                69.35         0.484   below_threshold              0.106              1.6                           0.108                6.50              1.203                                 ok           False                  False
  VRSK           86.36               44            0.10              0.15        204.70                37.92         0.475   below_threshold              0.704             95.6                           0.583               -0.86             -0.258                                 ok           False                  False
  CRWD           87.50               40            1.31              1.92        208.48                67.60         0.449   below_threshold              0.500             18.4                           0.220              -10.14             -1.050            downtrend_blocked_slope           False                  False
  ORLY          100.00               37            0.44              0.30         96.56                21.83         0.438   below_threshold              0.772             49.4                           0.289                5.13              0.491                                 ok           False                  False
  VRTX             NaN                0           10.21             40.32        546.84                36.27           NaN no_signal_history                NaN              NaN                           0.062               -6.65             -0.038                                 ok           False                  False
  AAPL             NaN                0            0.00              0.00        357.92                28.52           NaN no_signal_history                NaN              NaN                           0.197                0.86              0.001                                 ok           False                  False
  ABNB             NaN                0            0.00              0.00        176.24                56.84           NaN no_signal_history                NaN              NaN                           0.628               -2.70             -0.738 downtrend_blocked_slope_and_streak           False                  False
  ADBE             NaN                0            0.00              0.00        235.80                33.21           NaN no_signal_history                NaN              NaN                           0.633               -1.15             -0.494                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127093504)

</details>
