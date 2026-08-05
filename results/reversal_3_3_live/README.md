# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 11:55:03 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$31,840.75`
- Equity: `$31,840.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  GEHC           94.44               36            0.52              0.26         70.15                58.11         0.623          pass              0.710             29.8                           0.328               13.88              1.706                       ok            True                  False
  CTAS           83.33               12            1.69              2.41        202.62                37.77         0.602          pass              0.201             12.8                           0.279               -0.57             -0.135                       ok            True                  False
  MRVL           80.00               35            1.64              2.51        217.51               100.52         0.590          pass              0.391             55.1                           0.444                1.90              0.266                       ok            True                  False
  CPRT          100.00               10            2.62              0.54         29.17                38.86         0.553          pass              0.459              1.3                           0.171                5.37              0.580                       ok            True                  False
  MSFT           80.56               36            0.81              2.78        491.62                57.86         0.548          pass              0.330             29.1                           0.237               25.23              3.069                       ok            True                  False
   PEP           84.62               26            0.50              0.49        138.89                25.68         0.546          pass              0.406             40.7                           0.411                2.03              0.240                       ok            True                  False
  WDAY           82.35               34            1.25              1.50        170.64                70.04         0.525          pass              0.300              8.2                           0.172               27.73              2.859                       ok            True                  False
   ADP           95.45               22            1.20              2.27        269.65                35.53         0.517          pass              0.611             26.3                           0.231                9.98              1.111                       ok            True                  False
  DRAM           77.14               35            0.64              0.24         54.79               109.93         0.717          pass              0.490             83.9                           0.628               -5.59             -0.579 downtrend_blocked_streak           False                  False
  SOXL           79.31               29            4.33              4.24        138.08               182.46         0.673          pass              0.310             38.8                           0.491              -16.86             -1.863 downtrend_blocked_streak           False                  False
  AMAT           90.00               30            1.32              5.07        544.45                87.24         0.655          pass              0.630             54.9                           0.539               -2.62             -0.306 downtrend_blocked_streak           False                  False
  TMUS           81.82               11            2.13              2.64        176.08                55.59         0.637          pass              0.231             37.5                           0.728               -9.17             -0.434  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                         detail
2026-08-05T11:55:03.663510-04:00 early_entry_1155 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00      manage_1200               exit {"asset_type": "option", "contract_symbol": "PEP260918C00140000", "fill_price": 3.69, "pnl": -1640.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PEP"}
2026-08-05T11:45:04.673736-04:00 early_entry_1145 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:40:04.834796-04:00 early_entry_1140 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:35:01.719935-04:00 early_entry_1135 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:30:04.698899-04:00 early_entry_1130 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:25:03.699168-04:00 early_entry_1125 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:20:04.670230-04:00 early_entry_1120 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:15:01.663027-04:00 early_entry_1115 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805115503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805115503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805115503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805115503)

</details>
