# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 13:10:03 EDT`
Last processed slot: `manage_1300`

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
  CRWD           86.11               36            1.58              2.31        207.87                89.85         0.631            pass              0.475             25.1                           0.265               -9.83             -0.922            downtrend_blocked_slope           False                  False
  AMGN          100.00               21            0.81              2.16        381.55                44.93         0.628            pass              0.621             28.4                           0.299              -13.18             -1.554 downtrend_blocked_slope_and_streak           False                  False
    ZS           97.73               44            0.18              0.21        163.39                64.41         0.548            pass              0.922             89.0                           0.417              -12.88             -1.596            downtrend_blocked_slope           False                  False
   EXC           94.74               19            0.25              0.08         43.36                15.10         0.544            pass              0.722             71.6                           0.365               -0.60              0.010                                 ok           False                  False
  TEAM           94.74               38            0.76              0.96        179.16                63.98         0.543            pass              0.788             51.2                           0.328               -4.00             -0.731            downtrend_blocked_slope           False                  False
  PANW           61.90               21            2.78              6.60        335.66                67.54         0.512            pass              0.177             17.6                           0.264              -14.05             -1.503            downtrend_blocked_slope           False                  False
  REGN          100.00               22            1.22              6.78        790.35                28.70         0.496 below_threshold              0.591             20.6                           0.331               -2.99             -0.169           downtrend_blocked_streak           False                  False
   WBD           91.67               24            0.73              0.14         28.14                12.44         0.494 below_threshold              0.454              0.0                           0.252               -3.06             -0.292 downtrend_blocked_slope_and_streak           False                  False
   ROP          100.00               34            0.36              0.97        388.17                26.95         0.493 below_threshold              0.824             71.7                           0.608               -8.40             -1.084 downtrend_blocked_slope_and_streak           False                  False
  FTNT           84.00               25            2.16              2.40        157.82                53.57         0.491 below_threshold              0.288             10.6                           0.115              -10.05             -0.909            downtrend_blocked_slope           False                  False
  VRTX           97.62               42            0.06              0.21        514.47                30.09         0.487 below_threshold              0.916             89.1                           0.565               -6.08             -0.673 downtrend_blocked_slope_and_streak           False                  False
   CEG           95.00               40            0.13              0.27        285.85                34.28         0.487 below_threshold              0.674              8.3                           0.097                1.12              0.499                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911131003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911131003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911131003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911131003)

</details>
