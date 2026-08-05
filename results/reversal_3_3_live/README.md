# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 12:05:02 EDT`
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
  MRVL           80.00               35            1.14              1.75        217.84               100.52         0.625          pass              0.436             68.8                           0.430                2.42              0.289                       ok            True                  False
  CTAS           85.71               14            1.63              2.32        202.66                37.77         0.597          pass              0.287             16.2                           0.390               -0.51             -0.132                       ok            True                  False
  MSFT           80.56               36            0.79              2.74        491.64                57.86         0.548          pass              0.333             30.2                           0.243               25.25              3.069                       ok            True                  False
  WDAY           82.86               35            1.05              1.26        170.74                70.04         0.533          pass              0.372             25.3                           0.222               27.99              2.868                       ok            True                  False
  CPRT           83.33               12            2.45              0.50         29.18                38.86         0.520          pass              0.196             13.8                           0.232                5.56              0.588                       ok            True                  False
   ADP           95.83               24            1.00              1.89        269.81                35.53         0.517          pass              0.661             38.5                           0.332               10.20              1.120                       ok            True                  False
  DRAM           77.14               35            0.40              0.15         54.82               109.93         0.730          pass              0.509             89.9                           0.604               -5.37             -0.568 downtrend_blocked_streak           False                  False
  SOXL           81.25               32            3.36              3.29        138.49               182.46         0.719          pass              0.409             52.5                           0.444              -16.02             -1.817 downtrend_blocked_streak           False                  False
  AMAT           90.62               32            1.13              4.33        544.76                87.24         0.656          pass              0.680             61.5                           0.480               -2.43             -0.297 downtrend_blocked_streak           False                  False
  TMUS           81.82               11            2.13              2.65        176.08                55.59         0.637          pass              0.231             37.3                           0.690               -9.17             -0.434  downtrend_blocked_slope           False                  False
  GEHC           94.44               36            0.48              0.24         70.16                58.11         0.625          pass              0.725             34.6                           0.354               13.92              1.707                       ok           False                  False
  LRCX           86.67               30            1.51              3.36        316.30                92.33         0.625          pass              0.557             61.3                           0.549               -1.99             -0.112 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                         detail
2026-08-05T12:00:04.693066-04:00 early_entry_1200 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00      manage_1200               exit {"asset_type": "option", "contract_symbol": "PEP260918C00140000", "fill_price": 3.69, "pnl": -1640.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PEP"}
2026-08-05T11:45:04.673736-04:00 early_entry_1145 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:40:04.834796-04:00 early_entry_1140 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:35:01.719935-04:00 early_entry_1135 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:30:04.698899-04:00 early_entry_1130 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:25:03.699168-04:00 early_entry_1125 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:20:04.670230-04:00 early_entry_1120 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805120502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805120502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805120502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805120502)

</details>
