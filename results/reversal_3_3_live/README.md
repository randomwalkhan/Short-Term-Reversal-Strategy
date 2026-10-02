# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 10:30:04 EDT`
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
   TRI           87.88               33            0.93              0.64         99.08                57.35         0.518            pass              0.654             79.6                           0.458                4.29              0.316                                 ok            True                  False
  AMGN           84.85               33            0.52              1.49        406.63                47.14         0.505            pass              0.414             27.1                           0.239                5.05              0.530                                 ok            True                  False
   WBD           95.65               46            0.00              0.00         30.95                37.65         0.552            pass              0.937             94.0                           0.567               11.33              0.523                                 ok           False                  False
  SNPS           80.95               42            0.31              1.07        490.08                58.70         0.536            pass              0.455             58.5                           0.305               27.03              1.972                                 ok           False                  False
    MU           92.31               39            0.36              2.80       1096.19                49.88         0.531            pass              0.795             73.4                           0.616                7.64              0.404                                 ok           False                  False
  PAYX           77.42               31            0.71              0.50        100.62                39.54         0.509            pass              0.300             36.3                           0.398              -13.79             -1.677 downtrend_blocked_slope_and_streak           False                  False
  ADBE           86.67               30            1.35              2.28        240.30                44.30         0.496 below_threshold              0.378              5.8                           0.078               -4.38             -0.395            downtrend_blocked_slope           False                  False
  CTSH           89.47               19            2.07              0.88         60.50                46.07         0.493 below_threshold              0.384              7.4                           0.240               -0.42             -0.065                                 ok           False                  False
   ADP           80.00               10            1.51              2.79        262.76                23.86         0.489 below_threshold              0.054              1.6                           0.158               -4.15             -0.411 downtrend_blocked_slope_and_streak           False                  False
  GILD           94.74               19            1.06              1.10        147.03                19.81         0.482 below_threshold              0.544             14.2                           0.220               -2.78             -0.254 downtrend_blocked_slope_and_streak           False                  False
  VRSK           83.33               30            1.34              1.58        167.70                37.65         0.482 below_threshold              0.280              3.3                           0.108               -5.29             -0.458 downtrend_blocked_slope_and_streak           False                  False
   CEG           84.21               19            1.53              2.77        257.73                41.85         0.477 below_threshold              0.399             59.8                           0.758                0.10             -0.139                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-02T10:30:04.822821-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:25:06.818366-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:20:07.304982-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:15:06.003196-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:10:02.761986-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:05:05.705073-04:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:00:06.267323-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T09:20:04.739617-04:00     data_refresh       data_refresh                                             {'saved': 92, 'empty': 1}
2026-10-01T15:10:06.086305-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
2026-10-01T15:05:04.536150-04:00       entry_1500       slot_skipped                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002103004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002103004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002103004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002103004)

</details>
