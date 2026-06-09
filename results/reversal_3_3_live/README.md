# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 11:00:04 EDT`
Last processed slot: `manage_1100`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           82.14               28            1.61             10.73        944.68               111.98         0.693          pass              0.364             39.2                           0.291                4.25              0.172                      ok            True                  False
  TEAM           93.33               30            1.97              1.35         97.31                87.01         0.613          pass              0.666             38.5                           0.228               13.00              0.847                      ok            True                  False
  PANW           85.00               20            2.00              3.74        264.73                58.75         0.592          pass              0.339             26.5                           0.216                1.65              0.395                      ok            True                  False
   WDC           96.30               27            1.80              6.63        524.09                73.41         0.548          pass              0.711             47.6                           0.336               -1.34              0.035                      ok            True                  False
   WMT           87.10               31            0.52              0.44        119.64                36.35         0.542          pass              0.556             57.5                           0.464                0.54              0.112                      ok            True                  False
   STX           95.24               21            1.91             11.74        871.74                63.66         0.528          pass              0.649             40.9                           0.311                1.68              0.108                      ok            True                  False
  WDAY           83.33               12            3.95              3.98        142.06                70.13         0.510          pass              0.209             18.5                           0.274               11.34              1.255                      ok            True                  False
    ZS           77.78               18            2.92              2.64        128.12               157.94         0.875          pass              0.199             19.3                           0.231              -32.03             -1.852 downtrend_blocked_slope           False                  False
  DRAM          100.00               20            0.35              0.15         60.46               103.58         0.806          pass              0.779             77.2                           0.407               -0.33             -0.247                      ok           False                  False
  INTU           79.17               24            1.75              3.74        303.91               100.92         0.732          pass              0.278             37.0                           0.203               -1.37             -0.520                      ok           False                  False
  SOXL           95.00               20            3.71              5.50        209.08               192.77         0.717          pass              0.674             45.3                           0.309               -9.83             -0.668 downtrend_blocked_slope           False                  False
   TRI           90.32               31            0.15              0.09         83.14                69.62         0.684          pass              0.754             90.2                           0.384               -0.79             -0.067                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-09T11:00:04.007300-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:55:02.016087-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:50:06.282559-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:45:01.973366-04:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:40:03.961827-04:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:35:06.798530-04:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:30:02.001966-04:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:25:06.878160-04:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:20:02.039126-04:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-09T10:15:04.004316-04:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609110004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609110004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609110004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609110004)

</details>
