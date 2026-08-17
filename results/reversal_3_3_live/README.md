# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-17 10:10:05 EDT`
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
  ALNY           84.62               26            1.58              2.52        227.57               127.87         0.833          pass              0.447             44.8                           0.624                2.14              0.307                  ok            True                  False
  TEAM           80.65               31            2.17              2.46        161.16               128.53         0.774          pass              0.348             37.9                           0.554               53.02              5.031                  ok            True                  False
  SHOP           95.65               23            2.41              2.61        153.20                83.98         0.670          pass              0.622             22.7                           0.263               28.70              2.263                  ok            True                  False
  ABNB           96.55               29            1.11              1.43        183.45                64.74         0.649          pass              0.638             15.4                           0.222               20.83              2.482                  ok            True                  False
  GEHC           95.24               21            1.40              0.72         73.38                52.52         0.628          pass              0.595             19.5                           0.260                6.82              0.720                  ok            True                  False
 CMCSA           88.24               17            1.26              0.23         26.08                41.99         0.619          pass              0.357              9.6                           0.131                5.25              0.596                  ok            True                  False
  PAYX          100.00               11            1.84              1.57        121.35                35.05         0.583          pass              0.517             17.5                           0.189                1.79              0.355                  ok            True                  False
  BKNG           96.88               32            0.91              1.36        211.48                43.86         0.563          pass              0.628              8.5                           0.184                9.03              0.829                  ok            True                  False
  MDLZ           90.48               21            1.09              0.49         63.40                26.02         0.545          pass              0.443             12.0                           0.179                1.92              0.186                  ok            True                  False
   ROP          100.00               15            2.02              5.65        396.92                41.77         0.533          pass              0.517             10.1                           0.179               -0.33              0.051                  ok            True                  False
   LIN           86.96               23            1.02              3.46        481.26                26.03         0.532          pass              0.325              0.0                           0.162               -0.55             -0.151                  ok            True                  False
   XEL          100.00               26            0.58              0.32         79.03                16.04         0.522          pass              0.686             42.5                           0.421                1.31              0.221                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-08-17T10:10:05.798210-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:05:02.645350-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:00:05.950089-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T09:50:05.672730-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "SOXL260918C00140000", "fill_price": 28.1, "pnl": 5670.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.9, "ticker": "SOXL"}
2026-08-17T03:00:01.859006-04:00     data_refresh       data_refresh                                                                                                                                                                         {'saved': 93}
2026-08-15T02:55:03.720107-04:00   share_ext_0255      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:50:05.933577-04:00   share_ext_0250      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:45:06.097367-04:00   share_ext_0245      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:40:01.513034-04:00   share_ext_0240      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
2026-08-15T02:35:02.859847-04:00   share_ext_0235      market_closed                                                                                                                                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260817101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260817101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260817101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260817101005)

</details>
