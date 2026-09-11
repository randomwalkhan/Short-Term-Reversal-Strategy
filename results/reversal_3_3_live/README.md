# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 14:10:01 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-11)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  MSTR     option         option MSTR261016C00130000     30          2026-09-10         2026-09-11       11.525       13.65 6375.0   18.438178 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               18            0.96              2.56        381.37                44.93         0.637            pass              0.562             14.9                           0.280              -13.31             -1.561 downtrend_blocked_slope_and_streak           False                  False
  CRWD           86.11               36            1.60              2.33        207.86                89.85         0.630            pass              0.472             24.4                           0.289               -9.84             -0.923            downtrend_blocked_slope           False                  False
   PEP           90.91               22            0.03              0.03        136.64                17.04         0.561            pass              0.691             87.9                           0.391               -1.18             -0.181                                 ok           False                  False
    MU           87.50               40            0.22              1.48        976.78                56.22         0.547            pass              0.691             78.9                           0.433                4.27              0.731                                 ok           False                  False
  TEAM           94.74               38            0.83              1.04        179.12                63.98         0.539            pass              0.775             47.0                           0.349               -4.06             -0.734            downtrend_blocked_slope           False                  False
   EXC           95.65               23            0.12              0.03         43.38                15.10         0.529            pass              0.800             86.8                           0.505               -0.47              0.017                                 ok           False                  False
  REGN          100.00               17            1.35              7.47        790.06                28.70         0.520            pass              0.536             12.6                           0.280               -3.11             -0.175           downtrend_blocked_streak           False                  False
  PANW           65.22               23            2.63              6.22        335.82                67.54         0.513            pass              0.205             22.3                           0.346              -13.91             -1.496            downtrend_blocked_slope           False                  False
  WDAY           95.45               44            0.07              0.09        185.05                76.08         0.510            pass              0.911             86.7                           0.475               -4.45             -0.873 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.55               29            0.44              0.31         99.09                21.90         0.502            pass              0.647             23.5                           0.158               -7.91             -0.934 downtrend_blocked_slope_and_streak           False                  False
   WBD           91.30               23            0.74              0.15         28.14                12.44         0.499 below_threshold              0.438              0.0                           0.203               -3.08             -0.292 downtrend_blocked_slope_and_streak           False                  False
  MELI          100.00               37            0.45              6.06       1903.64                37.18         0.495 below_threshold              0.744             38.3                           0.337               -1.72             -0.325 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-11T12:00:03.003315-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:55:01.842224-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:50:02.882708-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:45:05.865744-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:40:01.913291-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:35:01.868483-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:30:06.647893-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:25:02.875572-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:20:01.270402-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:15:02.705141-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911141001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911141001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911141001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911141001)

</details>
