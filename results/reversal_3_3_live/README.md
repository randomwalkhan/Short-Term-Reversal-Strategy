# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 11:50:02 EDT`
Last processed slot: `manage_1200`

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
  CRWD           86.49               37            1.47              2.14        207.94                89.85         0.632            pass              0.508             30.6                           0.477               -9.72             -0.917            downtrend_blocked_slope           False                  False
  AMGN           96.43               28            0.57              1.53        381.81                44.93         0.596            pass              0.727             49.1                           0.556              -12.98             -1.543 downtrend_blocked_slope_and_streak           False                  False
  TEAM           94.29               35            1.09              1.37        178.98                63.98         0.541            pass              0.693             30.2                           0.434               -4.32             -0.746            downtrend_blocked_slope           False                  False
   EXC           95.65               23            0.09              0.03         43.38                15.10         0.530            pass              0.808             89.5                           0.630               -0.45              0.018                                 ok           False                  False
  PANW           61.90               21            2.78              6.60        335.66                67.54         0.512            pass              0.177             17.6                           0.391              -14.05             -1.503            downtrend_blocked_slope           False                  False
  REGN          100.00               22            1.22              6.79        790.35                28.70         0.496 below_threshold              0.591             20.6                           0.289               -2.99             -0.169           downtrend_blocked_streak           False                  False
  FTNT           86.21               29            1.75              1.95        158.02                53.57         0.494 below_threshold              0.424             27.6                           0.364               -9.67             -0.890            downtrend_blocked_slope           False                  False
   ROP          100.00               36            0.16              0.44        388.39                26.95         0.492 below_threshold              0.884             87.2                           0.820               -8.22             -1.075 downtrend_blocked_slope_and_streak           False                  False
   WDC           80.00               30            1.80              5.81        458.44                66.80         0.491 below_threshold              0.345             54.3                           0.506               -2.00              0.250           downtrend_blocked_streak           False                  False
  VRTX           97.50               40            0.22              0.78        514.23                30.09         0.490 below_threshold              0.828             59.6                           0.510               -6.23             -0.680 downtrend_blocked_slope_and_streak           False                  False
   BKR          100.00                7            2.56              1.06         58.94                30.11         0.481 below_threshold              0.492             14.6                           0.315               -6.81             -0.505            downtrend_blocked_slope           False                  False
   KDP           88.57               35            0.21              0.05         31.44                30.75         0.476 below_threshold              0.684             80.3                           0.790               -1.52             -0.096           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-09-11T11:50:02.882708-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:45:05.865744-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:40:01.913291-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:35:01.868483-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:30:06.647893-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:25:02.875572-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:20:01.270402-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:15:02.705141-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:10:04.829349-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-11T11:05:04.651905-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911115002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911115002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911115002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911115002)

</details>
