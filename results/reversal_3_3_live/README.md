# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 10:05:05 EDT`
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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           91.89               37            0.53              4.04       1095.66                49.88         0.533            pass              0.735             61.6                           0.370                7.46              0.396                                 ok            True                  False
  PAYX           78.79               33            0.56              0.40        100.67                39.54         0.509            pass              0.354             50.0                           0.366              -13.66             -1.670 downtrend_blocked_slope_and_streak           False                  False
  ADBE           90.24               41            0.45              0.77        240.95                44.30         0.496 below_threshold              0.668             48.3                           0.344               -3.51             -0.354                                 ok           False                  False
  AMGN           87.50               40            0.13              0.38        407.11                47.14         0.492 below_threshold              0.693             81.3                           0.626                5.46              0.548                                 ok           False                  False
  VRSK           85.00               40            0.37              0.43        168.19                37.65         0.490 below_threshold              0.597             71.4                           0.518               -4.36             -0.414 downtrend_blocked_slope_and_streak           False                  False
  CTSH           92.00               25            1.64              0.70         60.58                46.07         0.485 below_threshold              0.548             26.5                           0.295                0.02             -0.046                                 ok           False                  False
  CHTR           77.78               45            0.22              0.17        111.30                50.16         0.485 below_threshold              0.484             78.6                           0.514              -13.30             -1.316            downtrend_blocked_slope           False                  False
   KHC           92.59               27            0.18              0.03         22.45                18.85         0.467 below_threshold              0.736             80.0                           0.648               -8.23             -0.874 downtrend_blocked_slope_and_streak           False                  False
  ISRG           91.67               24            1.30              3.64        399.68                28.38         0.465 below_threshold              0.513             20.6                           0.220                0.69              0.154                                 ok           False                  False
   ADP           90.48               21            1.09              2.02        263.10                23.86         0.461 below_threshold              0.478             26.5                           0.241               -3.74             -0.392 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           80.49               41            0.09              0.01         21.69                30.36         0.460 below_threshold              0.513             84.6                           0.473               -4.66             -0.591 downtrend_blocked_slope_and_streak           False                  False
   CEG           77.78                9            2.68              4.85        256.84                41.85         0.459 below_threshold              0.135             29.7                           0.244               -1.07             -0.192                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-02T10:05:05.705073-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:00:06.267323-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T09:20:04.739617-04:00     data_refresh       data_refresh                                                                                    {'saved': 92, 'empty': 1}
2026-10-01T15:10:06.086305-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T15:05:04.536150-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T15:00:06.279684-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T14:55:05.658187-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T14:50:05.514279-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-10-01T14:50:05.514279-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-01", "training_samples": 5895, "window": 5}
2026-10-01T12:00:06.030645-04:00 early_entry_1200 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002100505)

</details>
