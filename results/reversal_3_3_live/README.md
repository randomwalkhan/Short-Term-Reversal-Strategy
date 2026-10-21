# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 10:20:05 EDT`
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
  MSFT           96.00               25            0.64              2.37        530.86                21.62         0.513            pass              0.703             50.7                           0.327               -0.24             -0.003                      ok            True                  False
   KHC           85.71               21            1.30              0.22         23.74                25.26         0.502            pass              0.290              4.6                           0.243                7.01              0.759                      ok            True                  False
  INTU           88.24               34            0.60              1.40        334.69                37.42         0.500 below_threshold              0.586             52.0                           0.339               12.65              1.291                      ok            True                  False
  TMUS           50.00                8            2.94              3.24        156.36                56.37         0.555            pass              0.132             25.6                           0.286               -8.67             -0.474 downtrend_blocked_slope           False                  False
  MDLZ           75.00                4            1.58              0.71         63.69                19.17         0.552            pass              0.068              4.3                           0.164                6.06              0.674                      ok           False                  False
   KDP           96.43               28            0.36              0.09         34.59                29.04         0.547            pass              0.823             82.9                           0.559               12.98              1.292                      ok           False                  False
  DXCM          100.00                3            2.71              1.62         85.04                29.22         0.530            pass              0.509             18.6                           0.187               -1.04              0.100                      ok           False                  False
  GILD           83.33                6            2.17              2.38        155.49                26.70         0.522            pass              0.229             29.2                           0.275                4.26              0.574                      ok           False                  False
 CMCSA          100.00                3            2.91              0.46         22.16                21.50         0.496 below_threshold              0.456              2.3                           0.103                3.68              0.657                      ok           False                  False
  AVGO           83.33               36            0.43              1.00        333.94                36.72         0.488 below_threshold              0.405             31.2                           0.262              -11.57             -1.212 downtrend_blocked_slope           False                  False
  DASH           87.18               39            0.94              1.27        191.13                49.85         0.486 below_threshold              0.610             58.9                           0.527               -0.72             -0.124                      ok           False                  False
  MELI           79.55               44            0.30              3.94       1877.81                40.36         0.486 below_threshold              0.462             71.1                           0.596                0.06             -0.093                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-21T10:20:05.382566-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:15:01.464955-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:10:06.281776-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:05:06.311663-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:00:05.535793-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T09:20:05.984665-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-20T15:10:05.817672-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-20T15:05:04.338456-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-20T15:00:02.391381-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-20T14:55:05.300060-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021102005)

</details>
