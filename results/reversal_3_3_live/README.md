# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 14:45:02 EDT`
Last processed slot: `manual`

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
   PEP           86.36               22            0.74              0.70        135.35                30.61         0.576          pass              0.451             47.9                           0.460               -2.33             -0.211                                 ok            True                  False
  MPWR           83.33               36            0.96              9.40       1394.42                64.79         0.547          pass              0.530             71.0                           0.537                0.79              0.252                                 ok            True                  False
  PAYX          100.00               30            0.60              0.46        110.54                34.17         0.533          pass              0.741             51.5                           0.628                3.59              0.424                                 ok            True                  False
   MAR          100.00               11            2.05              5.31        367.53                21.19         0.526          pass              0.519             19.9                           0.273               -2.75             -0.140                                 ok            True                  False
  CTSH           86.11               36            0.86              0.26         43.07                49.36         0.505          pass              0.593             68.6                           0.775               -1.36              0.056                                 ok            True                  False
  SOXL           84.62               26            4.59              5.17        158.77               181.21         0.705          pass              0.405             35.1                           0.411              -20.19             -2.433            downtrend_blocked_slope           False                  False
  LRCX           88.89               36            0.26              0.59        319.04                89.02         0.687          pass              0.752             90.9                           0.628               -9.83             -1.155 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00                5            1.83              0.78         60.53                31.72         0.627          pass              0.503             13.6                           0.374                2.48              0.314                                 ok           False                  False
  AAPL           87.50                8            1.79              4.09        324.14                37.45         0.627          pass              0.295             10.7                           0.189                1.21              0.346                                 ok           False                  False
   KDP           90.00               10            1.62              0.34         30.05                36.78         0.608          pass              0.370             14.0                           0.267               -3.29             -0.388 downtrend_blocked_slope_and_streak           False                  False
  ASML           94.29               35            0.39              4.89       1799.76                56.20         0.601          pass              0.847             79.7                           0.572               -0.52              0.030                                 ok           False                  False
  ISRG           63.64               11            2.55              6.08        338.08                68.45         0.601          pass              0.152             28.3                           0.545              -19.33             -2.272            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-23T12:00:02.078304-04:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:55:05.041109-04:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:50:02.063008-04:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:45:02.073454-04:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:40:05.071726-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:35:03.088888-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:30:02.112498-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:25:02.129403-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:20:01.968002-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-23T11:15:04.121471-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723144502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723144502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723144502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723144502)

</details>
