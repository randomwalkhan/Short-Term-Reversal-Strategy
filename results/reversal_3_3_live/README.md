# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 09:30:05 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ          100.00               24            0.53              0.25         67.70                23.85         0.559            pass              0.549              0.0                           0.179                1.34              0.036                      ok            True                  False
  PANW           80.00               20            2.60              6.49        353.36                69.35         0.534            pass              0.170             16.8                           0.238                7.50              1.245                      ok            True                  False
  GILD           87.50               24            1.15              1.42        176.13                34.85         0.526            pass              0.346              0.0                           0.250                4.02              0.521                      ok            True                  False
   ROP           84.38               32            0.70              2.38        482.07                31.75         0.501            pass              0.313              0.0                           0.350                0.38             -0.076                      ok            True                  False
  INSM           85.71               49            0.02              0.02        170.30                97.01         0.697            pass              0.690             89.4                           0.703               44.22              4.307                      ok           False                  False
   TRI           85.00               40            0.12              0.09        109.31                57.66         0.591            pass              0.392              0.0                           0.250                0.60              0.003                      ok           False                  False
   KDP           88.24               34            0.36              0.09         35.59                47.31         0.581            pass              0.438              0.0                           0.272                0.23             -0.016                      ok           False                  False
  PAYX           69.23               26            0.41              0.34        118.34                28.65         0.527            pass              0.159              0.0                           0.283                2.45              0.101                      ok           False                  False
  VRSK           81.25               32            0.86              1.23        204.23                37.92         0.511            pass              0.231              0.0                           0.217               -1.61             -0.292 downtrend_blocked_slope           False                  False
  CTAS           96.55               29            0.39              0.62        227.38                19.75         0.501            pass              0.577              0.0                           0.350               -0.11              0.041                      ok           False                  False
  CRWD           89.58               48            0.10              0.15        209.24                67.60         0.491 below_threshold              0.505              0.0                           0.177               -9.04             -0.994 downtrend_blocked_slope           False                  False
  ORLY          100.00               32            0.63              0.42         96.51                21.83         0.458 below_threshold              0.679             28.8                           0.299                4.94              0.483                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127093005)

</details>
