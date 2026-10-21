# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 09:45:06 EDT`
Last processed slot: `manual`

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
  MDLZ           92.86               14            0.73              0.33         63.85                19.17         0.574            pass              0.436              3.1                           0.121                6.98              0.713                      ok            True                  False
   KHC           87.50               24            0.99              0.16         23.77                25.26         0.507            pass              0.401             18.9                           0.221                7.39              0.775                      ok            True                  False
  GILD           92.00               25            1.00              1.09        156.04                26.70         0.501            pass              0.584             37.8                           0.508                5.52              0.628                      ok            True                  False
  TMUS           60.00               10            2.29              2.53        156.67                56.37         0.592            pass              0.185             42.0                           0.607               -8.06             -0.444 downtrend_blocked_slope           False                  False
   KDP           96.43               28            0.40              0.10         34.59                29.04         0.545            pass              0.817             80.8                           0.728               12.93              1.290                      ok           False                  False
 CMCSA           75.00                4            2.06              0.32         22.22                21.50         0.512            pass              0.098             15.6                           0.208                4.58              0.697                      ok           False                  False
  DASH           89.13               46            0.14              0.19        191.59                49.85         0.500 below_threshold              0.771             92.5                           0.817                0.08             -0.087                      ok           False                  False
  MSFT           93.55               31            0.29              1.06        531.41                21.62         0.495 below_threshold              0.784             77.8                           0.594                0.11              0.013                      ok           False                  False
  MELI           80.00               45            0.13              1.74       1878.75                40.36         0.491 below_threshold              0.511             87.2                           0.802                0.23             -0.085                      ok           False                  False
   PEP           83.33               36            0.07              0.06        133.99                22.26         0.475 below_threshold              0.590             93.4                           0.844                8.24              0.753                      ok           False                  False
   ROP           88.89               36            0.51              1.42        397.60                26.56         0.473 below_threshold              0.641             61.0                           0.611               10.49              1.028                      ok           False                  False
  CTAS           94.44               36            0.45              0.69        216.74                24.03         0.466 below_threshold              0.740             45.1                           0.653                9.56              0.925                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-21T09:20:05.984665-04:00     data_refresh       data_refresh                                                                                    {'saved': 91, 'empty': 2}
2026-10-20T15:10:05.817672-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T15:05:04.338456-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T15:00:02.391381-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:55:05.300060-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-20T14:50:06.260078-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-10-20T14:50:06.260078-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-20", "training_samples": 6130, "window": 5}
2026-10-20T12:00:03.885046-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:40:09.833456-04:00 early_entry_1140 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:35:07.546342-04:00 early_entry_1135 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021094506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021094506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021094506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021094506)

</details>
