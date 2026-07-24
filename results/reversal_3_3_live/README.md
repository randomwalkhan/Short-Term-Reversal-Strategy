# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 11:05:02 EDT`
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
  PYPL           86.67               30            0.58              0.23         55.90                61.86         0.652          pass              0.611             78.3                           0.562               20.20              1.868                                 ok            True                  False
   STX           89.47               19            4.11             26.25        902.11               102.76         0.581          pass              0.449             26.2                           0.500               -3.79              0.333                                 ok            True                  False
  GILD           91.30               23            0.78              0.71        130.55                35.55         0.571          pass              0.519             24.5                           0.289                0.01             -0.049                                 ok            True                  False
  ASML           92.31               26            1.88             23.68       1792.85                56.08         0.550          pass              0.583             31.1                           0.469               -1.57              0.089                                 ok            True                  False
   HON           83.33               18            1.33              2.29        245.29                40.09         0.546          pass              0.314             39.1                           0.215                7.32              0.874                                 ok            True                  False
  KLAC           84.00               25            2.61              4.00        217.02                98.03         0.652          pass              0.367             31.6                           0.520               -7.99             -0.736 downtrend_blocked_slope_and_streak           False                  False
  LRCX           81.82               22            2.94              6.57        316.96                88.87         0.581          pass              0.281             31.5                           0.526              -11.40             -0.999 downtrend_blocked_slope_and_streak           False                  False
  AMAT           88.24               17            3.63             14.31        556.67                96.41         0.557          pass              0.399             25.8                           0.463               -9.98             -0.863 downtrend_blocked_slope_and_streak           False                  False
  PANW           95.65               46            0.18              0.42        325.45                61.92         0.544          pass              0.858             67.8                           0.445               -0.27             -0.279                                 ok           False                  False
   WDC           94.12               17            5.52             21.57        549.06               114.14         0.534          pass              0.524             15.9                           0.409               -9.46             -0.308            downtrend_blocked_slope           False                  False
   APP           79.49               39            1.64              4.59        396.89                79.31         0.532          pass              0.381             44.8                           0.689              -22.62             -1.897            downtrend_blocked_slope           False                  False
  CRWD           91.30               46            0.43              0.55        183.18                61.02         0.520          pass              0.701             49.0                           0.431               -2.43             -0.672 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-24T11:05:02.376412-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:00:05.423763-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:55:02.424626-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:50:02.430847-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:45:05.925719-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:40:02.342835-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:35:04.435807-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:30:02.438509-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:25:03.433473-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:20:04.356287-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724110502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724110502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724110502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724110502)

</details>
