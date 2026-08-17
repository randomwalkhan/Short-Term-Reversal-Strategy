# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 10:35:02 EDT`
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
  ALNY           83.87               31            1.27              2.04        227.78               127.87         0.825          pass              0.492             55.4                           0.694                2.45              0.321                  ok            True                  False
  TEAM           80.00               30            2.78              3.15        160.87               128.53         0.752          pass              0.270             20.5                           0.294               52.07              5.002                  ok            True                  False
  SHOP           94.74               19            2.73              2.95        153.05                83.98         0.673          pass              0.558             12.4                           0.272               28.28              2.248                  ok            True                  False
  ABNB           94.44               18            1.69              2.18        183.13                64.74         0.669          pass              0.527              7.2                           0.175               20.12              2.456                  ok            True                  False
 CMCSA           88.89               18            0.97              0.18         26.10                41.99         0.629          pass              0.457             34.6                           0.587                5.56              0.609                  ok            True                  False
  GEHC           91.30               23            1.22              0.63         73.42                52.52         0.620          pass              0.539             29.7                           0.604                7.01              0.728                  ok            True                  False
  AAPL           86.67               30            0.55              1.18        305.42                34.74         0.557          pass              0.396              9.9                           0.113                0.36             -0.152                  ok            True                  False
  BKNG           96.77               31            1.13              1.68        211.34                43.86         0.555          pass              0.605              3.0                           0.106                8.80              0.820                  ok            True                  False
  MDLZ           91.67               24            0.82              0.36         63.45                26.02         0.544          pass              0.561             34.2                           0.487                2.20              0.199                  ok            True                  False
   ROP          100.00               21            1.28              3.57        397.81                41.77         0.540          pass              0.657             43.2                           0.654                0.43              0.085                  ok            True                  False
   MAR           91.18               34            0.53              1.33        356.15                36.45         0.536          pass              0.673             53.9                           0.345                2.30              0.118                  ok            True                  False
   LIN           85.71               21            1.10              3.72        481.14                26.03         0.535          pass              0.315             11.8                           0.218               -0.63             -0.154                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-08-17T10:35:02.623158-04:00 early_entry_1035 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:30:06.068349-04:00 early_entry_1030 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:25:02.671318-04:00 early_entry_1025 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:20:02.783639-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:15:01.583460-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:10:05.798210-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:05:02.645350-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:00:05.950089-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T09:50:05.672730-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "SOXL260918C00140000", "fill_price": 28.1, "pnl": 5670.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.9, "ticker": "SOXL"}
2026-08-17T03:00:01.859006-04:00     data_refresh       data_refresh                                                                                                                                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817103502)

</details>
