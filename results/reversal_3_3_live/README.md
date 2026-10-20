# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 10:25:04 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   ADP     option         option ADP261120C00290000     70          2026-10-19         2026-10-20          9.3        11.2 13300.0   20.430108 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           90.00               30            0.88              1.62        262.49                59.49         0.576            pass              0.629             57.2                           0.639              -13.16             -1.439 downtrend_blocked_slope_and_streak           False                  False
  SNPS           83.87               31            0.77              2.44        453.53                54.29         0.566            pass              0.522             74.1                           0.860              -10.71             -1.325 downtrend_blocked_slope_and_streak           False                  False
  META           81.82               11            1.89              9.34        701.44                40.24         0.537            pass              0.245             45.3                           0.738               -6.33             -0.384 downtrend_blocked_slope_and_streak           False                  False
    ZS           93.33               45            0.12              0.18        212.45                62.14         0.529            pass              0.894             95.1                           0.841                0.01             -0.265                                 ok           False                  False
  DRAM           80.56               36            0.39              0.13         48.27                49.05         0.496 below_threshold              0.510             90.8                           0.929              -19.12             -2.655 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.30               27            0.50              1.88        532.72                21.83         0.488 below_threshold              0.757             65.1                           0.735                0.29              0.074                                 ok           False                  False
   LIN           79.17               24            0.68              2.40        502.41                13.47         0.470 below_threshold              0.140              0.0                           0.170                2.05              0.374                                 ok           False                  False
  CDNS           83.33               36            0.66              1.51        325.21                37.22         0.467 below_threshold              0.538             76.4                           0.871               -9.97             -1.244 downtrend_blocked_slope_and_streak           False                  False
  PANW           84.21               38            1.20              2.91        345.70                55.73         0.456 below_threshold              0.542             66.0                           0.794              -18.36             -2.198 downtrend_blocked_slope_and_streak           False                  False
   BKR           93.55               31            0.79              0.31         55.68                25.31         0.452 below_threshold              0.697             50.0                           0.464               -3.08             -0.234                                 ok           False                  False
  IDXX           92.68               41            0.37              1.43        555.18                25.12         0.448 below_threshold              0.621             12.8                           0.121                7.44              1.011                                 ok           False                  False
  ASML           79.41               34            0.46              5.33       1644.83                29.62         0.448 below_threshold              0.437             77.3                           0.812              -10.61             -1.231            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-10-20T10:25:04.152080-04:00 early_entry_1025 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:20:05.290913-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:15:05.434773-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:10:06.028828-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:05:04.298275-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:00:02.343877-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T09:50:06.258363-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "ADP261120C00290000", "fill_price": 11.2, "pnl": 13300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.43, "ticker": "ADP"}
2026-10-20T00:00:06.202426-04:00     data_refresh       data_refresh                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-10-19T15:10:06.181493-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-10-19T15:07:09.479134-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020102504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020102504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020102504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020102504)

</details>
