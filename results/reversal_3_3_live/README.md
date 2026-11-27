# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 10:25:03 EST`
Last processed slot: `manage_1030`

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
  PANW           82.93               41            0.61              1.52        355.49                69.35         0.513            pass              0.592             87.6                           0.859                9.70              1.337                                 ok            True                  False
  NVDA           69.57               23            1.59              1.66        148.59               127.24         0.756            pass              0.280             39.4                           0.486              -11.59             -0.948 downtrend_blocked_slope_and_streak           False                  False
   KDP           88.24               34            0.36              0.09         35.59                47.31         0.578            pass              0.568             43.5                           0.369                0.23             -0.016                                 ok           False                  False
   CEG           89.74               39            0.65              1.07        234.82                66.73         0.555            pass              0.633             41.6                           0.270              -17.10             -2.034 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00               31            0.27              0.13         67.76                23.85         0.527            pass              0.785             64.0                           0.394                1.61              0.048                                 ok           False                  False
   AEP           96.30               27            0.08              0.07        127.56                16.32         0.525            pass              0.781             71.6                           0.499               -1.11             -0.131                                 ok           False                  False
  PAYX           74.19               31            0.16              0.13        118.43                28.65         0.510            pass              0.375             61.2                           0.310                2.71              0.112                                 ok           False                  False
  ROST           93.18               44            0.06              0.09        223.22                44.59         0.503            pass              0.883             93.8                           0.792               -5.95             -0.461                                 ok           False                  False
  ALNY           73.53               34            1.38              1.59        164.05               117.72         0.497 below_threshold              0.243             11.0                           0.137                3.71              0.200                                 ok           False                  False
  ORLY          100.00               21            1.17              0.79         96.35                21.83         0.493 below_threshold              0.541              6.2                           0.117                4.37              0.458                                 ok           False                  False
 GOOGL           81.82               33            0.37              0.70        272.80                60.73         0.478 below_threshold              0.452             67.4                           0.484               -8.91             -0.804            downtrend_blocked_slope           False                  False
  GOOG           81.82               33            0.35              0.67        270.69                57.96         0.470 below_threshold              0.445             65.5                           0.471               -8.58             -0.770            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-27T10:25:03.693968-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:20:04.818619-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:15:06.172355-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:10:04.653720-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:05:06.125532-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:00:04.055776-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T09:20:04.710561-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-26T16:10:21.376436-05:00      manage_1600       slot_skipped                                       {"reason": "already_processed"}
2026-11-26T15:54:23.516183-05:00      manage_1600      market_closed        {"holiday_name": "Thanksgiving Day", "reason": "nyse_holiday"}
2026-11-26T15:38:19.314719-05:00      manage_1530       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127102503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127102503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127102503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127102503)

</details>
