# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 11:45:02 EDT`
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

- Cash: `$34,043.00`
- Equity: `$34,043.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00320000     13          2026-07-23         2026-07-24       11.225      13.675 3185.0   21.826281 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           89.47               19            3.74             23.91        903.11               102.76         0.606          pass              0.472             32.8                           0.489               -3.42              0.350                                 ok            True                  False
  ASML           93.10               29            1.24             15.64       1796.30                56.08         0.575          pass              0.697             54.5                           0.714               -0.93              0.119                                 ok            True                  False
   WDC           90.00               20            4.66             18.20        550.50               114.14         0.570          pass              0.477             29.1                           0.588               -8.63             -0.267                                 ok            True                  False
   HON           83.33               18            1.38              2.37        245.25                40.09         0.543          pass              0.307             36.8                           0.288                7.27              0.871                                 ok            True                  False
  KLAC           85.71               28            1.76              2.69        217.58                98.03         0.689          pass              0.503             53.9                           0.694               -7.19             -0.697 downtrend_blocked_slope_and_streak           False                  False
  LRCX           85.19               27            1.72              3.86        318.13                88.87         0.635          pass              0.494             59.8                           0.764              -10.29             -0.943 downtrend_blocked_slope_and_streak           False                  False
  PYPL           90.00               40            0.25              0.10         55.96                61.86         0.614          pass              0.800             90.7                           0.724               20.60              1.883                                 ok           False                  False
  AMAT           90.00               20            2.66             10.48        558.31                96.41         0.607          pass              0.531             45.7                           0.576               -9.07             -0.817 downtrend_blocked_slope_and_streak           False                  False
  PANW           95.65               46            0.09              0.20        325.54                61.92         0.550          pass              0.908             84.3                           0.492               -0.17             -0.275                                 ok           False                  False
  GILD           93.75               32            0.31              0.29        130.74                35.55         0.545          pass              0.781             71.1                           0.698                0.48             -0.028                                 ok           False                  False
  MSTR           75.61               41            0.90              0.59         93.38                85.75         0.533          pass              0.488             78.2                           0.823               -1.96              0.155                                 ok           False                  False
   APP           78.95               38            1.80              5.03        396.71                79.31         0.527          pass              0.358             39.5                           0.541              -22.74             -1.905            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-24T11:45:02.490359-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:40:02.395425-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:35:03.478911-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:30:02.536091-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:25:02.429701-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:20:02.438945-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:15:02.420314-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:10:02.431913-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:05:02.376412-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:00:05.423763-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724114502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724114502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724114502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724114502)

</details>
