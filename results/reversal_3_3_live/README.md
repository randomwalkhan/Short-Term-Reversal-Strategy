# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 09:40:05 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NVDA           69.23               26            1.41              1.47        148.67               127.24         0.757            pass              0.203              7.0                           0.077              -11.43             -0.940 downtrend_blocked_slope_and_streak           False                  False
  MCHP           88.89               36            0.23              0.09         57.61                90.80         0.664            pass              0.618             47.1                           0.314               -6.58             -0.608            downtrend_blocked_slope           False                  False
  ASML           72.73               33            0.44              3.97       1301.38                72.71         0.602            pass              0.213              0.0                           0.150              -13.34             -1.379            downtrend_blocked_slope           False                  False
   KDP           88.89               36            0.27              0.07         35.60                47.31         0.575            pass              0.564             32.1                           0.225                0.32             -0.011                                 ok           False                  False
    ZS           84.44               45            0.41              0.66        230.58                83.89         0.565            pass              0.601             75.4                           0.392               18.99              2.354                                 ok           False                  False
  ISRG           86.84               38            0.37              1.10        426.71                50.77         0.542            pass              0.434              3.4                           0.258               -3.25             -0.418           downtrend_blocked_streak           False                  False
  ALNY           80.85               47            0.22              0.26        164.62               117.72         0.502            pass              0.485             70.7                           0.394                4.92              0.253                                 ok           False                  False
  CRWD           87.80               41            0.63              0.92        208.90                67.60         0.485 below_threshold              0.644             62.6                           0.351               -9.52             -1.019            downtrend_blocked_slope           False                  False
  VRSK           85.00               40            0.35              0.51        204.54                37.92         0.483 below_threshold              0.636             84.8                           0.590               -1.11             -0.269                                 ok           False                  False
  FTNT           85.71               42            0.78              0.74        134.64                96.72         0.476 below_threshold              0.404              1.4                           0.072                3.37              0.605                                 ok           False                  False
   WMT           92.50               40            0.04              0.04        131.92                24.82         0.473 below_threshold              0.865             94.7                           0.650                4.52              0.423                                 ok           False                  False
  PANW           69.23               13            4.07             10.14        351.79                69.35         0.466 below_threshold              0.068              0.5                           0.100                5.89              1.176                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127094005)

</details>
