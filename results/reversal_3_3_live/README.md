# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 10:15:04 EDT`
Last processed slot: `early_entry_1015`

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
  MDLZ          100.00               15            0.86              0.37         60.70                31.72         0.630          pass              0.639             47.5                           0.551                3.49              0.359                                 ok            True                  False
  AAPL           91.67               12            1.57              3.58        324.35                37.45         0.619          pass              0.452             21.7                           0.325                1.44              0.357                                 ok            True                  False
   KHC           88.89               18            0.52              0.09         25.92                31.13         0.618          pass              0.526             57.8                           0.583                4.64              0.496                                 ok            True                  False
   PEP           87.50               16            0.92              0.88        135.27                30.61         0.606          pass              0.396             31.7                           0.296               -2.51             -0.220                                 ok            True                  False
  ROST           84.21               19            1.28              2.13        237.30                31.02         0.549          pass              0.308             27.1                           0.241                6.60              0.877                                 ok            True                  False
  GILD           90.91               22            1.11              1.01        129.91                35.55         0.543          pass              0.566             47.1                           0.571               -4.41             -0.153                                 ok            True                  False
   ADP           96.55               29            0.56              0.96        242.71                36.25         0.541          pass              0.717             45.4                           0.237                0.19              0.066                                 ok            True                  False
   MAR          100.00               13            1.65              4.26        367.97                21.19         0.538          pass              0.581             35.6                           0.302               -2.35             -0.121                                 ok            True                  False
  SOXL           85.29               34            0.91              1.02        160.55               181.21         0.854          pass              0.648             87.2                           0.749              -17.11             -2.260            downtrend_blocked_slope           False                  False
  PYPL           89.74               39            0.34              0.13         55.45                61.85         0.634          pass              0.717             67.0                           0.635               22.07              2.345                                 ok           False                  False
  ISRG           70.00               10            2.78              6.64        337.84                68.45         0.602          pass              0.110             16.7                           0.262              -19.52             -2.282            downtrend_blocked_slope           False                  False
   KDP           92.86               28            0.38              0.08         30.17                36.78         0.583          pass              0.739             72.6                           0.647               -2.07             -0.331 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                              detail
2026-07-23T10:15:04.110282-04:00 early_entry_1015 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:10:06.093555-04:00 early_entry_1010 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00 early_entry_1005 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T10:05:02.098066-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "PYPL260821C00055000", "fill_price": 2.7675, "pnl": -1691.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-07-23T10:00:05.051160-04:00 early_entry_1000 early_entry_shadow                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T09:55:06.076284-04:00      manage_1000               exit   {"asset_type": "option", "contract_symbol": "AAPL260821C00325000", "fill_price": 9.765, "pnl": -1627.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "AAPL"}
2026-07-23T00:00:02.907448-04:00     data_refresh       data_refresh                                                                                                                                                                       {'saved': 93}
2026-07-22T15:10:06.070612-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-07-22T15:05:02.089739-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
2026-07-22T15:00:04.754101-04:00       entry_1500       slot_skipped                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723101504)

</details>
