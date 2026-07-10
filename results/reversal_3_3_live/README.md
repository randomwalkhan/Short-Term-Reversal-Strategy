# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-10 15:40:02 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$26,995.25`
- Equity: `$26,995.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  GILD     option         option GILD260821C00135000     24          2026-07-09         2026-07-10         5.85       5.265 -1404.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           81.25               32            1.22             11.75       1369.09                84.23         0.629          pass              0.453             70.1                           0.752               -5.48             -0.217                                 ok            True                  False
  DRAM           83.33               24            1.58              0.71         64.05               119.54         0.790          pass              0.463             67.1                           0.625              -17.62             -2.062            downtrend_blocked_slope           False                  False
    MU           82.86               35            0.19              1.29        991.09               119.39         0.788          pass              0.607             95.1                           0.664              -18.43             -2.339            downtrend_blocked_slope           False                  False
  LRCX           94.44               36            0.27              0.67        352.88               104.85         0.728          pass              0.912             93.6                           0.734              -12.35             -2.046 downtrend_blocked_slope_and_streak           False                  False
  ASML           91.18               34            0.37              4.74       1802.22                72.45         0.663          pass              0.770             82.0                           0.587               -2.37             -0.506            downtrend_blocked_slope           False                  False
  MRVL           92.59               27            2.40              4.08        241.52               107.78         0.648          pass              0.658             48.2                           0.652              -15.58             -2.144            downtrend_blocked_slope           False                  False
  INTC           89.66               29            2.11              1.67        111.83                93.93         0.598          pass              0.604             53.2                           0.599              -17.09             -2.277            downtrend_blocked_slope           False                  False
  QCOM           83.87               31            1.20              1.61        190.42                71.74         0.571          pass              0.473             57.4                           0.624               -7.85             -0.366           downtrend_blocked_streak           False                  False
  AVGO           87.50               40            0.16              0.44        400.92                53.79         0.547          pass              0.719             88.3                           0.651                5.69              0.688                                 ok           False                  False
  CPRT           90.00               10            2.38              0.47         28.13                43.96         0.524          pass              0.356             12.3                           0.230               -7.97             -0.522            downtrend_blocked_slope           False                  False
  CTSH           70.83               24            1.80              0.55         43.17                63.93         0.524          pass              0.226             26.8                           0.451                8.86              1.164                                 ok           False                  False
  VRTX           87.50                8            2.04              7.10        493.46                34.73         0.508          pass              0.301             16.6                           0.357                1.28              0.236                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-07-10T15:10:08.910811-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T15:05:06.429039-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T15:00:09.226035-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T14:55:05.716481-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-07-10T14:50:05.489745-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
2026-07-10T14:50:05.489745-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-10", "training_samples": 5470, "window": 5}
2026-07-10T11:47:54.272841-04:00 early_entry_1145 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T11:19:23.277635-04:00 early_entry_1115 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:46:53.268563-04:00 early_entry_1045 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-10T10:03:01.269450-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260710154002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260710154002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260710154002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260710154002)

</details>
