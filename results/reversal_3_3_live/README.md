# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 11:25:03 EST`
Last processed slot: `manage_1130`

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

- Cash: `$96,129.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   MAR           91.67               24            0.53              1.55        413.38                25.25         0.527          pass              0.559             33.9                           0.307               -0.95             -0.105                                 ok            True                  False
  INTC           60.87               23            3.13              1.22         55.20               141.91         0.755          pass              0.304             47.1                           0.346               -4.10             -0.904 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                3            5.96             15.82        372.24               122.37         0.698          pass              0.502             10.8                           0.288               -8.90             -0.719 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.73               44            0.13              0.63        689.38                78.44         0.690          pass              0.857             62.6                           0.388                1.88             -0.026                                 ok           False                  False
  FTNT           70.00               20            2.38              2.19        130.52                96.17         0.673          pass              0.221             29.0                           0.420                7.99              0.686                                 ok           False                  False
  MCHP           75.00               16            3.08              1.26         57.93                78.21         0.562          pass              0.177             26.8                           0.417               -2.88             -0.479            downtrend_blocked_slope           False                  False
  QCOM           71.43                7            3.49              3.96        160.31                69.46         0.560          pass              0.057              0.4                           0.171               -5.48             -0.837 downtrend_blocked_slope_and_streak           False                  False
  CSCO           69.23               13            1.97              1.31         94.14                50.60         0.557          pass              0.094              6.0                           0.172               -1.09             -0.400                                 ok           False                  False
   TXN          100.00                2            4.28              8.55        282.08                59.73         0.538          pass              0.501             15.9                           0.381               -1.38             -0.401                                 ok           False                  False
  UPRO          100.00                3            4.44              3.67        116.32                72.20         0.535          pass              0.476              7.6                           0.183              -12.63             -1.683 downtrend_blocked_slope_and_streak           False                  False
  MSFT           94.74               19            1.26              4.41        496.41                37.07         0.529          pass              0.681             58.5                           0.363               -7.10             -0.846            downtrend_blocked_slope           False                  False
  NXPI           88.89                9            2.94              5.18        249.54                49.35         0.521          pass              0.303              4.7                           0.159               -1.58             -0.400 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-20T11:25:03.911005-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:20:05.063742-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:15:06.465652-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:10:05.768872-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:05:06.071133-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:00:06.033769-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:55:04.962322-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:50:06.269299-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:45:05.890117-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T10:40:06.786688-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120112503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120112503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120112503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120112503)

</details>
