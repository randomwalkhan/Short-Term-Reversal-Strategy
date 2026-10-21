# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-21 09:50:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MDLZ           90.00               10            0.93              0.42         63.81                19.17         0.579            pass              0.358             11.2                           0.251                6.76              0.704                      ok            True                  False
  GILD           91.30               23            1.11              1.21        155.99                26.70         0.505            pass              0.532             31.1                           0.371                5.40              0.623                      ok            True                  False
   KHC           88.89               27            0.76              0.13         23.78                25.26         0.505            pass              0.515             37.9                           0.317                7.60              0.784                      ok            True                  False
  TMUS           63.64               11            1.92              2.12        156.84                56.37         0.612            pass              0.222             51.4                           0.745               -7.71             -0.426 downtrend_blocked_slope           False                  False
   KDP           96.67               30            0.29              0.07         34.60                29.04         0.540            pass              0.846             86.3                           0.679               13.06              1.295                      ok           False                  False
 CMCSA           80.00                5            1.79              0.28         22.24                21.50         0.528            pass              0.133             26.6                           0.253                4.87              0.709                      ok           False                  False
  INTU           89.19               37            0.26              0.62        335.03                37.42         0.505            pass              0.712             78.8                           0.755               13.03              1.306                      ok           False                  False
  MRVL           92.31               39            0.24              0.41        240.25                55.63         0.503            pass              0.776             68.0                           0.368              -15.73             -2.048 downtrend_blocked_slope           False                  False
  DASH           87.80               41            0.79              1.06        191.22                49.85         0.488 below_threshold              0.632             58.3                           0.615               -0.56             -0.117                      ok           False                  False
  MSFT           94.12               34            0.16              0.58        531.62                21.62         0.486 below_threshold              0.849             88.0                           0.700                0.24              0.019                      ok           False                  False
  MELI           80.00               45            0.24              3.10       1878.17                40.36         0.484 below_threshold              0.480             77.3                           0.746                0.12             -0.090                      ok           False                  False
  SBUX           87.50               32            0.81              0.56         99.13                24.55         0.473 below_threshold              0.443             16.5                           0.236                5.33              0.822                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261021095006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261021095006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261021095006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261021095006)

</details>
