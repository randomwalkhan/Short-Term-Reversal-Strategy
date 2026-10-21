# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 10:05:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  MDLZ           90.00               10            0.94              0.42         63.81                19.17         0.579            pass              0.356             10.4                           0.154                6.75              0.704                       ok            True                  False
  DASH           80.95               21            2.06              2.76        190.49                49.85         0.522            pass              0.151              0.0                           0.223               -1.84             -0.175                       ok            True                  False
  MSFT           96.30               27            0.50              1.86        531.07                21.62         0.510            pass              0.748             61.2                           0.587               -0.10              0.003                       ok            True                  False
  INTU           88.24               34            0.54              1.26        334.75                37.42         0.503            pass              0.600             56.7                           0.469               12.72              1.294                       ok            True                  False
   KHC           89.66               29            0.65              0.11         23.78                25.26         0.501            pass              0.575             46.9                           0.580                7.72              0.789                       ok            True                  False
  TMUS           63.64               11            1.83              2.02        156.88                56.37         0.617            pass              0.229             53.6                           0.760               -7.63             -0.422  downtrend_blocked_slope           False                  False
   KDP           96.43               28            0.35              0.08         34.59                29.04         0.548            pass              0.826             83.6                           0.511               13.00              1.293                       ok           False                  False
 CMCSA          100.00                3            2.30              0.36         22.21                21.50         0.535            pass              0.470              5.5                           0.118                4.32              0.685                       ok           False                  False
  DXCM          100.00                3            3.16              1.90         84.93                29.22         0.506            pass              0.451              0.0                           0.197               -1.51              0.078 downtrend_blocked_streak           False                  False
  MELI           75.68               37            0.75              9.88       1875.26                40.36         0.495 below_threshold              0.312             27.6                           0.272               -0.40             -0.113                       ok           False                  False
  IDXX           89.47               19            1.75              6.85        555.00                24.93         0.491 below_threshold              0.362              0.0                           0.250                8.19              1.022                       ok           False                  False
  GEHC           72.73               11            1.99              0.98         69.81                23.16         0.487 below_threshold              0.055              0.0                           0.257                6.43              0.839                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-21T10:05:06.311663-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T10:00:05.535793-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-21T09:20:05.984665-04:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-10-20T15:10:05.817672-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T15:05:04.338456-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T15:00:02.391381-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:55:05.300060-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:50:06.260078-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-10-20T14:50:06.260078-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-20", "training_samples": 6130, "window": 5}
2026-10-20T12:00:03.885046-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021100506)

</details>
