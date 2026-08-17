# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 13:10:01 EDT`
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
  ALNY           84.62               26            1.75              2.81        227.45               127.87         0.827          pass              0.428             38.6                           0.295                1.96              0.299                  ok            True                  False
  TEAM           80.65               31            2.53              2.87        160.99               128.53         0.759          pass              0.316             27.7                           0.244               52.46              5.014                  ok            True                  False
  ABNB          100.00               14            1.97              2.53        182.97                64.74         0.682          pass              0.522              9.0                           0.324               19.78              2.443                  ok            True                  False
  SHOP           92.86               14            3.39              3.66        152.75                83.98         0.660          pass              0.446              3.4                           0.232               27.42              2.218                  ok            True                  False
  GEHC           93.75               16            1.89              0.98         73.27                52.52         0.625          pass              0.481              3.8                           0.208                6.28              0.697                  ok            True                  False
  TMUS           90.91               22            1.63              2.08        181.72                56.43         0.622          pass              0.459              8.7                           0.317                1.44              0.304                  ok            True                  False
 CMCSA           90.00               10            2.08              0.38         26.02                41.99         0.605          pass              0.386             19.6                           0.434                4.38              0.558                  ok            True                  False
  DXCM           85.71               28            1.28              0.80         89.41                54.82         0.561          pass              0.517             62.7                           0.426                1.48              0.672                  ok            True                  False
  UPRO           80.00               30            0.69              0.76        156.30                39.51         0.557          pass              0.194              1.8                           0.177                6.30              0.429                  ok            True                  False
  AAPL           85.71               28            0.70              1.49        305.29                34.74         0.555          pass              0.414             28.6                           0.380                0.21             -0.159                  ok            True                  False
   ROP          100.00               18            1.62              4.54        397.40                41.77         0.538          pass              0.593             28.6                           0.597                0.07              0.069                  ok            True                  False
  DASH          100.00               38            0.71              1.07        216.56                46.91         0.523          pass              0.779             46.7                           0.278                7.48              0.673                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-08-17T12:00:04.607418-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:55:01.576813-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:50:04.389347-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:45:01.690104-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:40:05.536828-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:35:03.481570-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:30:06.396920-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:25:02.640154-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:20:04.561969-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:15:01.577044-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817131001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817131001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817131001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817131001)

</details>
