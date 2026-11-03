# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 12:15:06 EST`
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

- Cash: `$136,446.55`
- Equity: `$136,446.55`
- Realized PnL: `$126,446.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     34          2026-11-02         2026-11-03        18.25       21.05 9520.0   15.342466 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           92.31               13            1.07              0.18         23.79                32.70         0.595          pass              0.524             38.7                           0.231                5.61              0.523                                 ok            True                  False
   KHC           83.33               12            1.85              0.32         24.79                33.68         0.561          pass              0.239             27.0                           0.424                2.69              0.153                                 ok            True                  False
   ROP           85.00               20            1.29              4.32        477.69                37.35         0.550          pass              0.397             47.2                           0.590               18.88              1.696                                 ok            True                  False
   EXC           81.25               16            1.01              0.33         46.31                22.18         0.532          pass              0.206             26.6                           0.188                6.86              0.721                                 ok            True                  False
   ADP           88.46               26            0.61              1.27        298.23                27.85         0.524          pass              0.601             72.0                           0.550                1.44             -0.171                                 ok            True                  False
  VRSK           80.00               20            1.59              2.25        200.54                37.47         0.524          pass              0.289             56.5                           0.545                3.89              0.168                                 ok            True                  False
  FAST           96.30               27            0.57              0.21         52.46                22.62         0.511          pass              0.698             44.4                           0.363                1.67              0.087                                 ok            True                  False
   XEL           86.36               22            0.64              0.36         79.18                19.18         0.508          pass              0.457             52.3                           0.519                2.79              0.290                                 ok            True                  False
  TMUS           55.56                9            2.24              2.51        159.08                68.40         0.650          pass              0.120             18.5                           0.205               -0.75              0.090                                 ok           False                  False
  MDLZ           87.50                8            1.50              0.70         66.08                28.20         0.592          pass              0.341             27.4                           0.190                2.18              0.240                                 ok           False                  False
   PEP           80.00                5            1.62              1.59        139.74                26.86         0.592          pass              0.111             17.2                           0.257                3.08              0.214                                 ok           False                  False
  MRVL           90.24               41            0.43              0.51        171.19                97.23         0.572          pass              0.775             81.7                           0.882              -29.01             -3.221 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-03T12:00:06.009720-05:00 early_entry_1200 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:55:04.283382-05:00 early_entry_1155 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:50:06.620716-05:00 early_entry_1150 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:45:05.991467-05:00 early_entry_1145 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:40:01.980819-05:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:35:05.840286-05:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:30:05.077695-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:25:04.545060-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:20:06.072141-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:15:01.990433-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103121506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103121506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103121506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103121506)

</details>
