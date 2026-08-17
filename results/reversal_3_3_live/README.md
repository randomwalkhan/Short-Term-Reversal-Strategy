# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 10:00:05 EDT`
Last processed slot: `manage_1000`

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
  SHOP           94.74               19            2.85              3.08        153.00                83.98         0.668          pass              0.534              4.9                           0.123               28.13              2.243                  ok            True                  False
  ABNB           96.77               31            0.97              1.25        183.53                64.74         0.646          pass              0.683             26.1                           0.279               21.00              2.489                  ok            True                  False
 CMCSA           88.24               17            1.32              0.24         26.08                41.99         0.616          pass              0.344              5.5                           0.083                5.19              0.593                  ok            True                  False
  GEHC           95.00               20            1.74              0.90         73.31                52.52         0.615          pass              0.528              0.0                           0.157                6.45              0.704                  ok            True                  False
  PAYX          100.00               12            1.81              1.55        121.36                35.05         0.579          pass              0.527             18.7                           0.157                1.82              0.356                  ok            True                  False
  BKNG           97.06               34            0.63              0.93        211.66                43.86         0.568          pass              0.722             35.2                           0.269                9.35              0.842                  ok            True                  False
  MDLZ           90.48               21            0.97              0.43         63.42                26.02         0.551          pass              0.472             21.5                           0.234                2.04              0.192                  ok            True                  False
   ROP          100.00               16            1.96              5.47        396.99                41.77         0.534          pass              0.494              0.1                           0.049               -0.27              0.054                  ok            True                  False
   TRI           85.71               21            2.74              1.98        102.76                75.08         0.532          pass              0.324             15.1                           0.159               -0.82              0.043                  ok            True                  False
  ISRG           86.49               37            0.53              1.48        393.88                39.79         0.523          pass              0.564             53.1                           0.425                4.53              0.816                  ok            True                  False
  CHTR           88.89               18            2.93              3.16        152.91                52.98         0.514          pass              0.357              5.0                           0.069                3.92              0.207                  ok            True                  False
   XEL          100.00               28            0.56              0.31         79.04                16.04         0.511          pass              0.706             45.0                           0.485                1.34              0.222                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-08-17T10:00:05.950089-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T09:50:05.672730-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "SOXL260918C00140000", "fill_price": 28.1, "pnl": 5670.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.9, "ticker": "SOXL"}
2026-08-17T03:00:01.859006-04:00     data_refresh       data_refresh                                                                                                                                                                         {'saved': 93}
2026-08-15T02:55:03.720107-04:00   share_ext_0255      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:50:05.933577-04:00   share_ext_0250      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:45:06.097367-04:00   share_ext_0245      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:40:01.513034-04:00   share_ext_0240      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:35:02.859847-04:00   share_ext_0235      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:30:02.424773-04:00   share_ext_0230      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:25:41.575248-04:00   share_ext_0225      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817100005)

</details>
