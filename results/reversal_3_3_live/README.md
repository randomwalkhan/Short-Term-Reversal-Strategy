# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 10:30:06 EDT`
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
  ALNY           83.33               30            1.29              2.07        227.76               127.87         0.828          pass              0.469             54.8                           0.716                2.44              0.320                  ok            True                  False
  TEAM           80.65               31            2.49              2.83        161.01               128.53         0.761          pass              0.320             28.7                           0.427               52.52              5.016                  ok            True                  False
  ABNB           94.74               19            1.58              2.04        183.19                64.74         0.672          pass              0.530              3.2                           0.161               20.25              2.461                  ok            True                  False
  SHOP           95.65               23            2.42              2.61        153.20                83.98         0.669          pass              0.621             22.5                           0.392               28.69              2.263                  ok            True                  False
 CMCSA           88.24               17            1.05              0.19         26.10                41.99         0.629          pass              0.418             29.5                           0.528                5.48              0.605                  ok            True                  False
  GEHC           91.30               23            1.26              0.65         73.41                52.52         0.618          pass              0.533             27.7                           0.484                6.98              0.727                  ok            True                  False
  BKNG           96.88               32            0.94              1.39        211.46                43.86         0.560          pass              0.659             18.8                           0.243                9.01              0.828                  ok            True                  False
  MDLZ           91.30               23            0.84              0.37         63.45                26.02         0.548          pass              0.540             32.3                           0.439                2.18              0.198                  ok            True                  False
   ROP          100.00               19            1.50              4.19        397.54                41.77         0.539          pass              0.614             33.3                           0.428                0.20              0.075                  ok            True                  False
   TRI           88.89               27            2.21              1.60        102.92                75.08         0.533          pass              0.498             31.6                           0.488               -0.28              0.067                  ok            True                  False
   LIN           86.96               23            1.01              3.43        481.27                26.03         0.530          pass              0.382             18.9                           0.276               -0.54             -0.150                  ok            True                  False
  CHTR           89.47               19            2.61              2.82        153.06                52.98         0.522          pass              0.445             26.7                           0.478                4.26              0.222                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-08-17T10:30:06.068349-04:00 early_entry_1030 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:25:02.671318-04:00 early_entry_1025 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:20:02.783639-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:15:01.583460-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:10:05.798210-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:05:02.645350-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:00:05.950089-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T09:50:05.672730-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "SOXL260918C00140000", "fill_price": 28.1, "pnl": 5670.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.9, "ticker": "SOXL"}
2026-08-17T03:00:01.859006-04:00     data_refresh       data_refresh                                                                                                                                                                         {'saved': 93}
2026-08-15T02:55:03.720107-04:00   share_ext_0255      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817103006)

</details>
