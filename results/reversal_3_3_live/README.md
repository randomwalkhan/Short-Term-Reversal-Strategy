# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 10:00:06 EDT`
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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           80.00               25            4.79              5.08        149.27               120.87         0.561          pass              0.278             40.8                           0.271               42.68              4.607                                 ok            True                  False
   CEG           83.33               18            1.48              2.72        262.10                41.90         0.551          pass              0.283             28.6                           0.321               -1.96              0.017                                 ok            True                  False
  MPWR           85.71               28            1.44             13.80       1361.51                54.48         0.528          pass              0.512             62.4                           0.415               17.89              2.197                                 ok            True                  False
  NXPI           87.10               31            0.68              1.14        237.59                39.27         0.516          pass              0.617             78.6                           0.448                5.92              0.694                                 ok            True                  False
  AMAT           85.00               40            0.76              2.60        483.89                51.73         0.513          pass              0.618             77.8                           0.509               13.46              1.736                                 ok            True                  False
  PYPL           88.89               18            1.54              0.59         54.79                60.08         0.508          pass              0.520             59.8                           0.772                0.31              0.084                                 ok            True                  False
  MSFT          100.00               17            1.34              4.84        514.10                25.07         0.507          pass              0.649             50.5                           0.670                0.76              0.231                                 ok            True                  False
  UPRO           82.61               23            1.27              1.36        151.62                32.02         0.506          pass              0.291             28.1                           0.464                3.11              0.586                                 ok            True                  False
   STX           86.21               29            1.94             12.47        911.48                54.25         0.503          pass              0.447             35.0                           0.271               11.69              1.848                                 ok            True                  False
   TRI           88.00               25            1.93              1.34         98.42                56.74         0.565          pass              0.440             23.3                           0.244               -8.26             -0.556 downtrend_blocked_slope_and_streak           False                  False
  LRCX           79.55               44            0.52              1.15        314.72                61.39         0.529          pass              0.514             87.1                           0.574               14.78              1.855                                 ok           False                  False
  KLAC           74.29               35            0.92              1.21        187.40                50.67         0.506          pass              0.435             72.6                           0.575               10.11              1.398                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-09-28T10:00:06.220548-04:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T09:50:05.886543-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "MSTR261120C00160000", "fill_price": 15.9975, "pnl": -3555.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-28T03:00:06.642645-04:00     data_refresh       data_refresh                                                                                                                                                           {'saved': 92, 'empty': 1}
2026-09-26T02:55:04.179839-04:00   share_ext_0255      market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:50:05.866610-04:00   share_ext_0250      market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:45:06.222669-04:00   share_ext_0245      market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:40:05.820539-04:00   share_ext_0240      market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:35:05.219756-04:00   share_ext_0235      market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:30:04.108962-04:00   share_ext_0230      market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:25:06.088084-04:00   share_ext_0225      market_closed                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928100006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928100006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928100006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928100006)

</details>
