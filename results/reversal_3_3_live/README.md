# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 09:50:04 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DXCM           85.71               42            0.51              0.30         84.71                47.84         0.504          pass              0.447             14.7                           0.205                3.70              0.303                                 ok            True                  False
  PANW           80.00               35            1.34              3.35        354.70                69.35         0.501          pass              0.435             72.7                           0.581                8.89              1.304                                 ok            True                  False
  NVDA           69.57               23            1.58              1.65        148.59               127.24         0.756          pass              0.281             39.6                           0.279              -11.58             -0.948 downtrend_blocked_slope_and_streak           False                  False
  LRCX           67.50               40            0.18              0.23        184.91               114.86         0.679          pass              0.525             85.6                           0.410              -21.00             -2.134            downtrend_blocked_slope           False                  False
  AMAT           67.57               37            0.39              0.85        310.81               107.91         0.666          pass              0.444             65.7                           0.366              -18.51             -1.916            downtrend_blocked_slope           False                  False
  MCHP           87.10               31            0.65              0.26         57.54                90.80         0.662          pass              0.515             40.0                           0.285               -6.97             -0.627            downtrend_blocked_slope           False                  False
  ASML           72.73               33            0.51              4.64       1301.09                72.71         0.593          pass              0.337             41.6                           0.277              -13.40             -1.382            downtrend_blocked_slope           False                  False
   KDP           90.00               40            0.03              0.01         35.63                47.31         0.566          pass              0.802             92.9                           0.576                0.56             -0.001                                 ok           False                  False
   CEG           87.80               41            0.40              0.66        235.00                66.73         0.561          pass              0.467              1.0                           0.017              -16.90             -2.022 downtrend_blocked_slope_and_streak           False                  False
  ISRG           86.11               36            0.59              1.76        426.43                50.77         0.535          pass              0.496             35.3                           0.275               -3.46             -0.428           downtrend_blocked_streak           False                  False
   AEP           96.30               27            0.09              0.08        127.56                16.32         0.525          pass              0.713             48.9                           0.222               -1.11             -0.132                                 ok           False                  False
  ALNY           75.00               36            0.97              1.11        164.25               117.72         0.517          pass              0.225              0.0                           0.208                4.14              0.219                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127095004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127095004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127095004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127095004)

</details>
