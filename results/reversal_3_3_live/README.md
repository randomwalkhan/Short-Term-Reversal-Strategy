# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 10:25:02 EDT`
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

- Cash: `$30,858.00`
- Equity: `$30,858.00`
- Realized PnL: `$20,858.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  AAPL     option         option AAPL260821C00325000     15          2026-07-22         2026-07-23       10.850      9.7650 -1627.50       -10.0 stop_loss_hit_at_scan
  PYPL     option         option PYPL260821C00055000     55          2026-07-21         2026-07-23        3.075      2.7675 -1691.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           86.21               29            0.88              0.34         55.36                61.85         0.659          pass              0.402             14.8                           0.297               21.40              2.320                                 ok            True                  False
  MDLZ          100.00               10            1.25              0.53         60.63                31.72         0.637          pass              0.536             24.0                           0.338                3.09              0.341                                 ok            True                  False
  AAPL           92.31               13            1.37              3.13        324.55                37.45         0.626          pass              0.506             31.6                           0.559                1.64              0.366                                 ok            True                  False
   KHC           92.31               13            1.14              0.21         25.87                31.13         0.615          pass              0.433              7.8                           0.234                3.99              0.468                                 ok            True                  False
   PEP           84.62               13            1.14              1.08        135.19                30.61         0.607          pass              0.250             15.3                           0.225               -2.73             -0.230                                 ok            True                  False
  ROST           81.25               16            1.38              2.31        237.22                31.02         0.559          pass              0.192             21.0                           0.291                6.49              0.872                                 ok            True                  False
  GILD           90.91               22            1.07              0.97        129.92                35.55         0.546          pass              0.573             49.1                           0.687               -4.37             -0.151                                 ok            True                  False
   ADP           96.15               26            0.79              1.34        242.54                36.25         0.545          pass              0.632             23.5                           0.212               -0.03              0.056                                 ok            True                  False
  PAYX          100.00               28            0.77              0.60        110.48                34.17         0.538          pass              0.635             20.6                           0.239                3.42              0.416                                 ok            True                  False
   MAR          100.00               12            1.81              4.69        367.79                21.19         0.534          pass              0.554             29.2                           0.288               -2.52             -0.129                                 ok            True                  False
   KDP           90.48               21            0.78              0.16         30.13                36.78         0.599          pass              0.545             44.0                           0.422               -2.46             -0.349 downtrend_blocked_slope_and_streak           False                  False
  ISRG           83.33                6            3.50              8.34        337.12                68.45         0.593          pass              0.148              0.0                           0.198              -20.11             -2.316            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-07-23T10:25:02.098761-04:00 early_entry_1025 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:20:02.100648-04:00 early_entry_1020 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:15:04.110282-04:00 early_entry_1015 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:10:06.093555-04:00 early_entry_1010 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00 early_entry_1005 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260821C00055000", "fill_price": 2.7675, "pnl": -1691.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-07-23T10:00:05.051160-04:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T09:55:06.076284-04:00      manage_1000               exit   {"asset_type": "option", "contract_symbol": "AAPL260821C00325000", "fill_price": 9.765, "pnl": -1627.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AAPL"}
2026-07-23T00:00:02.907448-04:00     data_refresh       data_refresh                                                                                                                                                                       {'saved': 93}
2026-07-22T15:10:06.070612-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723102502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723102502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723102502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723102502)

</details>
