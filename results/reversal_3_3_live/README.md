# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 10:20:02 EDT`
Last processed slot: `manage_1030`

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
  ALNY           86.11               36            0.96              1.53        227.99               127.87         0.821          pass              0.618             66.5                           0.799                2.78              0.335                  ok            True                  False
  TEAM           80.65               31            1.99              2.25        161.25               128.53         0.782          pass              0.365             43.2                           0.688               53.31              5.039                  ok            True                  False
  SHOP           95.65               23            2.37              2.56        153.22                83.98         0.672          pass              0.626             24.1                           0.362               28.76              2.265                  ok            True                  False
  ABNB           95.00               20            1.48              1.91        183.24                64.74         0.672          pass              0.559              8.4                           0.217               20.37              2.465                  ok            True                  False
 CMCSA           88.24               17            1.05              0.19         26.10                41.99         0.629          pass              0.418             29.5                           0.427                5.48              0.605                  ok            True                  False
  GEHC           91.30               23            1.23              0.64         73.42                52.52         0.619          pass              0.537             28.9                           0.501                7.00              0.727                  ok            True                  False
  BKNG           96.77               31            0.97              1.44        211.44                43.86         0.565          pass              0.636             13.1                           0.198                8.98              0.827                  ok            True                  False
  MDLZ           90.48               21            0.97              0.43         63.42                26.02         0.551          pass              0.472             21.5                           0.246                2.04              0.192                  ok            True                  False
  WDAY           85.19               27            2.18              3.04        197.38                90.03         0.542          pass              0.411             34.9                           0.524               17.75              1.863                  ok            True                  False
   LIN           85.00               20            1.12              3.80        481.11                26.03         0.538          pass              0.284             10.0                           0.131               -0.66             -0.156                  ok            True                  False
   ROP          100.00               18            1.70              4.75        397.30                41.77         0.534          pass              0.580             24.4                           0.287               -0.01              0.066                  ok            True                  False
   TRI           88.89               27            2.20              1.60        102.93                75.08         0.533          pass              0.499             31.7                           0.451               -0.28              0.068                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-08-17T10:20:02.783639-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:15:01.583460-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:10:05.798210-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:05:02.645350-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:00:05.950089-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T09:50:05.672730-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "SOXL260918C00140000", "fill_price": 28.1, "pnl": 5670.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.9, "ticker": "SOXL"}
2026-08-17T03:00:01.859006-04:00     data_refresh       data_refresh                                                                                                                                                                         {'saved': 93}
2026-08-15T02:55:03.720107-04:00   share_ext_0255      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:50:05.933577-04:00   share_ext_0250      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:45:06.097367-04:00   share_ext_0245      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817102002)

</details>
