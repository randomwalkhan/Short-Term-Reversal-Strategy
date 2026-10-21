# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 10:25:04 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MSFT           96.30               27            0.53              1.97        531.02                21.62         0.508            pass              0.741             58.8                           0.457               -0.13              0.002                      ok            True                  False
   KHC           85.71               21            1.24              0.21         23.74                25.26         0.506            pass              0.304              9.2                           0.232                7.07              0.762                      ok            True                  False
  TMUS           55.56                9            2.54              2.81        156.55                56.37         0.578            pass              0.165             35.6                           0.413               -8.30             -0.455 downtrend_blocked_slope           False                  False
   KDP           96.30               27            0.42              0.10         34.59                29.04         0.550            pass              0.809             80.1                           0.552               12.92              1.289                      ok           False                  False
  GILD           87.50                8            2.08              2.28        155.53                26.70         0.521            pass              0.348             32.1                           0.335                4.36              0.578                      ok           False                  False
  DXCM          100.00                3            2.92              1.75         84.99                29.22         0.518            pass              0.489             12.3                           0.161               -1.26              0.090                      ok           False                  False
 CMCSA          100.00                3            2.53              0.40         22.19                21.50         0.517            pass              0.501             16.3                           0.224                4.08              0.675                      ok           False                  False
  MDLZ           50.00                2            1.92              0.86         63.62                19.17         0.513            pass              0.054              0.8                           0.154                5.69              0.658                      ok           False                  False
  INTU           88.57               35            0.46              1.09        334.82                37.42         0.502            pass              0.633             62.6                           0.372               12.80              1.297                      ok           False                  False
  DASH           87.80               41            0.66              0.89        191.29                49.85         0.492 below_threshold              0.671             71.2                           0.695               -0.44             -0.111                      ok           False                  False
  MELI           80.00               45            0.15              2.01       1878.64                40.36         0.489 below_threshold              0.505             85.3                           0.698                0.21             -0.086                      ok           False                  False
  AVGO           81.58               38            0.23              0.53        334.14                36.72         0.487 below_threshold              0.468             63.5                           0.362              -11.39             -1.203 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-21T10:25:04.556585-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:20:05.382566-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:15:01.464955-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:10:06.281776-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:05:06.311663-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:00:05.535793-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T09:20:05.984665-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-20T15:10:05.817672-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-20T15:05:04.338456-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-20T15:00:02.391381-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021102504)

</details>
