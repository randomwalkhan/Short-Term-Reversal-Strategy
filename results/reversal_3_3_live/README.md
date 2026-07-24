# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 11:15:02 EDT`
Last processed slot: `early_entry_1115`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           89.47               19            3.57             22.84        903.57               102.76         0.617            pass              0.482             35.8                           0.636               -3.25              0.358                                 ok            True                  False
   WDC           90.00               20            4.51             17.64        550.74               114.14         0.580            pass              0.485             31.2                           0.649               -8.49             -0.260                                 ok            True                  False
  GILD           92.59               27            0.52              0.48        130.66                35.55         0.563            pass              0.661             51.9                           0.382                0.27             -0.037                                 ok            True                  False
  ASML           93.10               29            1.48             18.64       1795.01                56.08         0.558            pass              0.669             45.8                           0.658               -1.17              0.108                                 ok            True                  False
   HON           83.33               18            1.22              2.10        245.37                40.09         0.554            pass              0.330             44.2                           0.288                7.44              0.879                                 ok            True                  False
  KLAC           84.62               26            2.03              3.11        217.40                98.03         0.683            pass              0.439             46.8                           0.544               -7.44             -0.709 downtrend_blocked_slope_and_streak           False                  False
  PYPL           90.00               40            0.16              0.06         55.97                61.86         0.620            pass              0.811             94.0                           0.788               20.70              1.887                                 ok           False                  False
  LRCX           84.62               26            2.19              4.91        317.68                88.87         0.609            pass              0.437             48.9                           0.588              -10.72             -0.964 downtrend_blocked_slope_and_streak           False                  False
  AMAT           89.47               19            2.96             11.67        557.80                96.41         0.592            pass              0.490             39.5                           0.550               -9.36             -0.832 downtrend_blocked_slope_and_streak           False                  False
   APP           80.49               41            1.28              3.58        397.32                79.31         0.546            pass              0.438             56.8                           0.780              -22.34             -1.881            downtrend_blocked_slope           False                  False
  MSTR           75.61               41            1.00              0.66         93.35                85.75         0.525            pass              0.480             75.7                           0.897               -2.06              0.150                                 ok           False                  False
  GEHC           87.50               24            1.29              0.56         61.75                33.38         0.495 below_threshold              0.504             53.8                           0.575               -5.43             -0.529 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-24T11:15:02.420314-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:10:02.431913-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:05:02.376412-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:00:05.423763-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:55:02.424626-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:50:02.430847-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:45:05.925719-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:40:02.342835-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:35:04.435807-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T10:30:02.438509-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724111502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724111502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724111502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724111502)

</details>
