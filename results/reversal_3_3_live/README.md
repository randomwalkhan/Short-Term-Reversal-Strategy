# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 11:45:03 EDT`
Last processed slot: `early_entry_1145`

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

- Cash: `$33,222.25`
- Equity: `$33,222.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   KDP           86.96               23            0.67              0.15         31.39                34.46         0.590          pass              0.522             63.5                           0.711                3.24              0.053                  ok            True                  False
   XEL          100.00               14            0.89              0.49         78.54                19.80         0.579          pass              0.505              6.7                           0.123               -2.64              0.016                  ok            True                  False
   MAR          100.00               13            1.50              4.01        379.40                28.18         0.575          pass              0.641             54.5                           0.689                3.36              0.343                  ok            True                  False
  VRTX           84.62               13            1.64              5.56        480.95                33.19         0.570          pass              0.317             38.9                           0.490               -0.19             -0.020                  ok            True                  False
  MNST           94.12               17            1.02              0.69         96.93                25.74         0.559          pass              0.684             68.5                           0.469               -1.81             -0.260                  ok            True                  False
  ABNB           95.45               22            1.55              1.66        152.30                40.20         0.547          pass              0.657             40.9                           0.552                2.80              0.084                  ok            True                  False
  AMGN           94.12               17            1.35              3.67        386.07                27.22         0.539          pass              0.610             44.4                           0.668                7.64              0.731                  ok            True                  False
   HON           83.33               18            1.10              1.86        240.32                39.75         0.538          pass              0.284             29.3                           0.442                7.09              1.061                  ok            True                  False
   AEP           82.35               17            1.22              1.11        128.92                20.00         0.516          pass              0.215             18.1                           0.221               -5.28             -0.169                  ok            True                  False
  ORLY           80.00               25            1.42              0.90         90.24                45.72         0.512          pass              0.366             71.4                           0.859                4.19              0.629                  ok            True                  False
  DASH           97.22               36            1.11              1.50        192.89                53.51         0.509          pass              0.785             53.5                           0.623                1.91             -0.027                  ok            True                  False
  ROST           89.29               28            0.75              1.32        251.39                27.49         0.507          pass              0.551             44.2                           0.608               13.19              1.049                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-30T11:45:03.023708-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:40:02.091678-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:35:05.117192-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:30:04.994647-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:25:01.766574-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:20:04.950564-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:15:04.858903-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:10:03.886706-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:05:04.940210-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:00:04.904053-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730114503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730114503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730114503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730114503)

</details>
