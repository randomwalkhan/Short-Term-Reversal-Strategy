# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-11 13:45:04 EDT`
Last processed slot: `manual`

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
  AMGN          100.00               19            0.88              2.35        381.46                44.93         0.636            pass              0.589             21.9                           0.240              -13.25             -1.557 downtrend_blocked_slope_and_streak           False                  False
  CRWD           85.71               35            1.73              2.53        207.77                89.85         0.627            pass              0.436             17.9                           0.264               -9.97             -0.929            downtrend_blocked_slope           False                  False
  TEAM           94.74               38            0.67              0.84        179.21                63.98         0.549            pass              0.806             57.3                           0.439               -3.91             -0.726            downtrend_blocked_slope           False                  False
    ZS           97.78               45            0.11              0.13        163.43                64.41         0.547            pass              0.935             93.4                           0.544              -12.81             -1.592            downtrend_blocked_slope           False                  False
   EXC           95.24               21            0.16              0.05         43.37                15.10         0.538            pass              0.772             81.6                           0.545               -0.52              0.014                                 ok           False                  False
  REGN          100.00               17            1.35              7.52        790.04                28.70         0.519            pass              0.535             12.0                           0.202               -3.12             -0.176           downtrend_blocked_streak           False                  False
  PANW           65.00               20            2.92              6.92        335.52                67.54         0.514            pass              0.159             13.6                           0.251              -14.17             -1.509            downtrend_blocked_slope           False                  False
  WDAY           95.24               42            0.30              0.39        184.92                76.08         0.508            pass              0.778             42.5                           0.287               -4.67             -0.884 downtrend_blocked_slope_and_streak           False                  False
  MELI          100.00               35            0.56              7.42       1903.06                37.18         0.503            pass              0.634              5.7                           0.175               -1.82             -0.329 downtrend_blocked_slope_and_streak           False                  False
   WBD           91.67               24            0.69              0.14         28.14                12.44         0.496 below_threshold              0.475              7.1                           0.302               -3.03             -0.290 downtrend_blocked_slope_and_streak           False                  False
  FTNT           84.62               26            2.03              2.25        157.88                53.57         0.494 below_threshold              0.327             16.1                           0.250               -9.93             -0.903            downtrend_blocked_slope           False                  False
   ROP          100.00               34            0.42              1.16        388.08                26.95         0.488 below_threshold              0.807             66.1                           0.584               -8.46             -1.088 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260911134504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260911134504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260911134504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260911134504)

</details>
