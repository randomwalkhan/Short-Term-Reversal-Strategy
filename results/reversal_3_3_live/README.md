# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 11:35:05 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           93.75               16            0.65              0.11         24.38                22.04         0.546            pass              0.515             17.9                           0.239               -2.33             -0.133                                 ok            True                  False
   PEP          100.00               11            0.87              0.79        129.41                15.76         0.554            pass              0.571             36.4                           0.364               -6.54             -0.641 downtrend_blocked_slope_and_streak           False                  False
  CHTR           90.32               31            1.63              1.47        127.54                64.18         0.541            pass              0.578             36.3                           0.560              -17.05             -1.430 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.30               37            0.59              1.03        248.48                46.23         0.526            pass              0.839             68.7                           0.393               -7.15             -0.449            downtrend_blocked_slope           False                  False
   ADP           95.24               21            0.66              1.26        270.68                22.01         0.524            pass              0.691             55.0                           0.511               -2.33              0.127           downtrend_blocked_streak           False                  False
  WDAY           95.45               44            0.13              0.18        193.79                50.60         0.517            pass              0.918             88.8                           0.636               -1.11              0.332                                 ok           False                  False
  TMUS           94.74               19            1.09              1.28        167.63                33.56         0.511            pass              0.717             71.1                           0.715               -8.36             -0.869            downtrend_blocked_slope           False                  False
  VRSK           85.71               14            2.31              2.84        174.19                39.25         0.497 below_threshold              0.260             10.4                           0.218               -7.52             -0.276            downtrend_blocked_slope           False                  False
  INTU          100.00               35            0.73              1.56        302.52                42.64         0.495 below_threshold              0.834             72.5                           0.534               -9.54             -0.594 downtrend_blocked_slope_and_streak           False                  False
  PAYX           85.00               20            1.06              0.86        115.77                23.92         0.494 below_threshold              0.361             37.2                           0.579               -5.59             -0.201           downtrend_blocked_streak           False                  False
   BKR           94.87               39            0.10              0.04         57.23                30.72         0.492 below_threshold              0.912             91.0                           0.736               -9.94             -1.331 downtrend_blocked_slope_and_streak           False                  False
  SBUX           71.43                7            1.72              1.15         95.34                22.99         0.489 below_threshold              0.124             25.2                           0.252               -9.85             -0.847 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-21T11:35:05.882163-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:30:05.864479-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:25:04.810284-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:20:06.298711-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:15:05.659477-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:10:04.948141-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:05:05.847856-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:00:03.910998-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:55:06.015379-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:50:06.524394-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921113505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921113505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921113505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921113505)

</details>
