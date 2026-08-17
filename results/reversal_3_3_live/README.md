# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 11:15:01 EDT`
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

- Cash: `$46,898.00`
- Equity: `$46,898.00`
- Realized PnL: `$36,898.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL260918C00140000      9          2026-08-14         2026-08-17         21.8        28.1 5670.0   28.899083 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ALNY           83.87               31            1.26              2.01        227.79               127.87         0.826          pass              0.494             56.0                           0.565                2.47              0.322                  ok            True                  False
  TEAM           80.65               31            2.54              2.88        160.98               128.53         0.759          pass              0.315             27.3                           0.402               52.44              5.013                  ok            True                  False
  SHOP           95.65               23            2.44              2.64        153.19                83.98         0.668          pass              0.619             21.8                           0.431               28.66              2.262                  ok            True                  False
  ABNB           94.74               19            1.62              2.09        183.17                64.74         0.668          pass              0.559             13.1                           0.356               20.21              2.459                  ok            True                  False
  TMUS           92.86               28            1.13              1.45        181.99                56.43         0.625          pass              0.533              2.6                           0.158                1.95              0.327                  ok            True                  False
 CMCSA           92.31               13            1.66              0.30         26.05                41.99         0.624          pass              0.411              0.0                           0.025                4.82              0.577                  ok            True                  False
  GEHC           95.00               20            1.59              0.82         73.34                52.52         0.623          pass              0.555              8.6                           0.173                6.62              0.711                  ok            True                  False
  BKNG           94.74               19            1.75              2.60        210.94                43.86         0.580          pass              0.531              6.8                           0.216                8.11              0.791                  ok            True                  False
  MDLZ           92.31               13            1.59              0.71         63.31                26.02         0.564          pass              0.410              1.9                           0.159                1.41              0.164                  ok            True                  False
   TRI           81.82               11            3.22              2.33        102.61                75.08         0.555          pass              0.121              3.3                           0.162               -1.31              0.020                  ok            True                  False
   LIN           81.25               16            1.43              4.82        480.68                26.03         0.536          pass              0.129              0.8                           0.224               -0.96             -0.169                  ok            True                  False
   ROP          100.00               17            1.91              5.33        397.06                41.77         0.528          pass              0.545             15.2                           0.178               -0.22              0.056                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-17T11:15:01.577044-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:10:01.687220-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:05:03.630999-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:00:04.689019-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:55:05.602923-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:50:05.567997-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:45:04.449129-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:40:04.617542-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:35:02.623158-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:30:06.068349-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817111501)

</details>
