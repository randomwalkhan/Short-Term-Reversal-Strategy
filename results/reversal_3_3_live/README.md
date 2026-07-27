# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-27 12:35:04 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$36,793.00`
- Equity: `$36,793.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  GILD     option         option GILD260918C00130000     25          2026-07-24         2026-07-27         6.55        7.65 2750.0   16.793893 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               14            0.93              0.53         81.44                20.22         0.568            pass              0.515             10.6                           0.259                0.53              0.141                                 ok            True                  False
  MPWR           82.86               35            1.16             10.84       1329.16                65.61         0.512            pass              0.499             68.3                           0.650                2.09              0.292                                 ok            True                  False
  DRAM           76.92               26            2.92              1.09         52.73                97.77         0.555            pass              0.305             47.6                           0.561               -9.87             -0.563            downtrend_blocked_slope           False                  False
   EXC           95.65               23            0.46              0.15         47.46                24.01         0.552            pass              0.770             76.1                           0.413                0.47              0.128                                 ok           False                  False
   CSX          100.00                2            2.52              0.94         52.83                24.65         0.545            pass              0.517             20.9                           0.498                4.53              0.536                                 ok           False                  False
   WBD           88.24               17            0.85              0.15         25.70                22.96         0.538            pass              0.493             57.7                           0.356               -5.68             -0.828            downtrend_blocked_slope           False                  False
  PANW           95.65               46            0.28              0.63        323.52                61.51         0.528            pass              0.760             35.7                           0.221               -2.24             -0.773 downtrend_blocked_slope_and_streak           False                  False
  CSCO           89.74               39            0.13              0.10        114.13                39.56         0.523            pass              0.775             89.9                           0.791               -4.38             -0.208                                 ok           False                  False
   TXN           88.57               35            0.75              1.47        278.95                50.69         0.509            pass              0.640             64.5                           0.600               -7.06             -0.723            downtrend_blocked_slope           False                  False
   AEP           78.95               19            1.04              0.99        135.12                20.37         0.503            pass              0.143             10.8                           0.252               -1.11             -0.011                                 ok           False                  False
  KLAC           84.62               13            5.04              7.43        207.34                94.03         0.501            pass              0.280             29.1                           0.453              -10.05             -0.886 downtrend_blocked_slope_and_streak           False                  False
   WDC           94.44               18            5.03             18.30        511.96               113.75         0.494 below_threshold              0.626             46.1                           0.656              -11.14             -0.120                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-27T12:00:02.583905-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:55:01.558921-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:50:05.732067-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:45:02.697826-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:40:04.711421-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:35:01.677814-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:30:01.582772-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:25:02.749051-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:20:01.767844-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:15:01.581718-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260727123504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260727123504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260727123504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260727123504)

</details>
