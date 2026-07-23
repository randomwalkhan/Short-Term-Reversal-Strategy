# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-23 14:10:02 EDT`
Last processed slot: `manage_1400`

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
  ASML           94.29               35            0.66              8.30       1798.30                56.20         0.583          pass              0.803             65.6                           0.322               -0.79              0.017                                 ok            True                  False
   PEP           86.36               22            0.76              0.72        135.34                30.61         0.575          pass              0.447             46.6                           0.410               -2.35             -0.212                                 ok            True                  False
   ADP           96.55               29            0.56              0.96        242.71                36.25         0.540          pass              0.730             49.6                           0.665                0.19              0.066                                 ok            True                  False
  MPWR           82.86               35            1.23             12.04       1393.29                64.79         0.534          pass              0.485             62.9                           0.328                0.52              0.240                                 ok            True                  False
  PAYX          100.00               30            0.61              0.47        110.54                34.17         0.532          pass              0.739             50.7                           0.687                3.59              0.424                                 ok            True                  False
   MAR          100.00               12            1.94              5.01        367.65                21.19         0.526          pass              0.539             24.3                           0.375               -2.64             -0.135                                 ok            True                  False
  KLAC           89.19               37            0.44              0.67        214.40                97.72         0.726          pass              0.745             82.4                           0.416               -6.88             -0.895 downtrend_blocked_slope_and_streak           False                  False
  LRCX           87.10               31            0.67              1.49        318.65                89.02         0.689          pass              0.629             77.1                           0.360              -10.19             -1.174 downtrend_blocked_slope_and_streak           False                  False
  SOXL           83.33               24            5.06              5.71        158.54               181.21         0.685          pass              0.336             28.4                           0.220              -20.58             -2.455            downtrend_blocked_slope           False                  False
  AAPL           87.50                8            1.78              4.06        324.15                37.45         0.628          pass              0.297             11.4                           0.208                1.23              0.347                                 ok           False                  False
  MDLZ          100.00                5            1.91              0.82         60.51                31.72         0.622          pass              0.491              9.7                           0.344                2.39              0.310                                 ok           False                  False
   KDP           92.86               14            1.42              0.30         30.07                36.78         0.598          pass              0.503             24.5                           0.507               -3.09             -0.378 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260723141002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260723141002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260723141002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260723141002)

</details>
