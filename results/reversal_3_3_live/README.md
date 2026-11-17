# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 10:55:05 EST`
Last processed slot: `manage_1100`

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

- Cash: `$111,239.80`
- Equity: `$111,239.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   TXN           85.71               14            1.81              3.73        292.61                59.80         0.621          pass              0.285             14.7                           0.211               -7.56             -0.067                  ok            True                  False
   KDP           94.12               17            1.03              0.26         35.47                46.38         0.619          pass              0.497              3.9                           0.122                1.37             -0.130                  ok            True                  False
   ADI           90.32               31            1.01              2.70        382.01                67.56         0.606          pass              0.556             26.6                           0.245               -9.64             -0.160                  ok            True                  False
  AVGO           81.08               37            0.60              1.40        332.80                71.99         0.603          pass              0.429             53.3                           0.252               -0.22              1.015                  ok            True                  False
  QCOM           80.00               10            3.14              3.70        166.93                68.75         0.578          pass              0.096             12.8                           0.205               -0.73              0.279                  ok            True                  False
  SBUX           81.82               11            1.41              1.07        108.26                31.47         0.573          pass              0.112              0.0                           0.170                2.91              0.178                  ok            True                  False
   CEG           81.82               11            3.08              5.99        275.25                60.48         0.566          pass              0.142             10.0                           0.202                2.38              1.203                  ok            True                  False
   ADP           82.35               17            1.24              2.73        312.26                28.40         0.559          pass              0.224             19.6                           0.215                4.57              0.384                  ok            True                  False
  FAST           90.00               10            1.23              0.48         54.91                19.71         0.554          pass              0.322              0.0                           0.163                4.01              0.523                  ok            True                  False
  AMZN           81.82               22            1.31              2.36        256.74                40.10         0.543          pass              0.213             10.0                           0.182                1.47              0.072                  ok            True                  False
  PYPL           88.24               17            1.39              0.57         58.58                28.48         0.537          pass              0.320              0.0                           0.210               -0.34             -0.122                  ok            True                  False
  AAPL           96.43               28            0.55              1.37        352.19                27.81         0.536          pass              0.600              8.9                           0.178                5.78              0.468                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-17T10:55:05.881265-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:50:06.221076-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:45:04.877729-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:40:03.860720-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:35:06.835467-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:30:03.912380-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:25:05.911595-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:20:06.716157-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:15:04.834585-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:10:04.914368-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117105505)

</details>
