# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 12:55:03 EST`
Last processed slot: `manage_1300`

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
  IDXX           96.55               29            1.16              5.59        687.26                78.44         0.708          pass              0.626              9.4                           0.156                0.83             -0.073                                 ok            True                  False
  AAPL          100.00               19            1.03              2.51        348.13                27.12         0.548          pass              0.566             17.0                           0.277                1.03              0.043                                 ok            True                  False
   MAR           93.33               15            1.15              3.32        412.62                25.25         0.544          pass              0.502             19.5                           0.319               -1.56             -0.133                                 ok            True                  False
  ODFL           88.89               36            0.71              0.87        173.46                43.88         0.503          pass              0.536             25.1                           0.260                4.65              0.410                                 ok            True                  False
   APP          100.00                3            5.42             14.37        372.86               122.37         0.726          pass              0.530             19.0                           0.259               -8.37             -0.693 downtrend_blocked_slope_and_streak           False                  False
  INTC           63.64               11            5.20              2.03         54.85               141.91         0.712          pass              0.115             12.3                           0.315               -6.14             -1.002 downtrend_blocked_slope_and_streak           False                  False
  FTNT           50.00               10            3.55              3.27        130.06                96.17         0.631          pass              0.113             16.6                           0.381                6.69              0.631                                 ok           False                  False
  ABNB           90.00               40            0.37              0.45        172.60                57.19         0.542          pass              0.714             64.2                           0.335               -9.39             -0.875 downtrend_blocked_slope_and_streak           False                  False
  GOOG           86.84               38            0.07              0.13        270.97                53.33         0.530          pass              0.708             95.3                           0.422               -4.61             -0.593            downtrend_blocked_slope           False                  False
  FAST           75.00                4            1.87              0.69         52.38                22.02         0.528          pass              0.073              6.8                           0.184               -2.44             -0.330 downtrend_blocked_slope_and_streak           False                  False
  MSFT           92.31               13            1.87              6.52        495.50                37.07         0.526          pass              0.517             38.6                           0.338               -7.67             -0.874            downtrend_blocked_slope           False                  False
  ISRG           87.88               33            0.71              2.04        406.37                45.14         0.520          pass              0.476             20.1                           0.181              -10.70             -1.227 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-20T12:00:03.900140-05:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:55:04.983316-05:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:50:06.003914-05:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:45:06.435631-05:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:40:06.030121-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:35:06.036427-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:30:06.242321-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:25:03.911005-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:20:05.063742-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:15:06.465652-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120125503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120125503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120125503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120125503)

</details>
