# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 14:35:06 EDT`
Last processed slot: `manage_1430`

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

- Cash: `$30,222.25`
- Equity: `$30,222.25`
- Realized PnL: `$20,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM260717C00100000     17          2026-06-08         2026-06-09         9.25       8.325 -1572.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           83.33               18            1.48              0.86         82.81                69.62         0.675          pass              0.257             15.8                           0.367               -2.11             -0.127                                 ok            True                  False
  CTSH           93.55               31            0.66              0.25         52.88                51.28         0.571          pass              0.743             61.5                           0.489                1.60             -0.111                                 ok            True                  False
   WMT           80.95               21            1.07              0.90        119.45                36.35         0.563          pass              0.245             30.1                           0.435               -0.02              0.087                                 ok            True                  False
  TEAM           96.55               29            2.50              1.71         97.16                87.01         0.551          pass              0.757             58.5                           0.765               12.39              0.822                                 ok            True                  False
  CDNS           93.75               32            0.99              2.74        393.07                58.79         0.516          pass              0.796             77.2                           0.739                2.25              0.466                                 ok            True                   True
    ZS           71.43               14            3.51              3.17        127.89               157.94         0.845          pass              0.249             46.0                           0.630              -32.44             -1.879            downtrend_blocked_slope           False                  False
  DRAM          100.00               14            2.30              0.97         60.10               103.58         0.673          pass              0.712             72.6                           0.720               -2.28             -0.337            downtrend_blocked_slope           False                  False
  INTU           64.29               14            3.94              8.44        301.89               100.92         0.625          pass              0.137             15.9                           0.377               -3.58             -0.623 downtrend_blocked_slope_and_streak           False                  False
  CSCO          100.00                1            3.54              3.08        122.83                58.94         0.605          pass              0.573             37.6                           0.521                1.20              0.433                                 ok           False                  False
  MSFT           83.33                6            1.94              5.60        409.34                36.13         0.604          pass              0.268             39.6                           0.509               -2.96             -0.371            downtrend_blocked_slope           False                  False
  AVGO           85.00               20            2.00              5.56        394.22                69.53         0.550          pass              0.464             69.7                           0.841               -7.91             -0.953            downtrend_blocked_slope           False                  False
  PANW           75.00               12            2.83              5.27        264.07                58.75         0.539          pass              0.218             50.2                           0.684                0.80              0.357                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-09T12:00:03.055569-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:55:04.019844-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:50:02.014967-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:45:02.008648-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:40:06.401362-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:35:02.395564-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:30:02.013445-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:25:01.954572-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:20:06.212106-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T11:15:02.033784-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609143506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609143506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609143506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609143506)

</details>
