# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 13:05:06 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
 CMCSA           91.67               12            1.19              0.20         23.78                32.70         0.593          pass              0.478             31.5                           0.263                5.48              0.517                  ok            True                  False
  MDLZ           90.91               11            1.39              0.64         66.10                28.20         0.584          pass              0.454             32.8                           0.370                2.30              0.245                  ok            True                  False
   KHC           83.33               12            1.85              0.32         24.79                33.68         0.561          pass              0.239             27.0                           0.514                2.69              0.153                  ok            True                  False
   EXC           83.33               18            0.93              0.30         46.32                22.18         0.527          pass              0.293             32.8                           0.393                6.95              0.725                  ok            True                  False
  FAST           96.00               25            0.60              0.22         52.46                22.62         0.521          pass              0.677             41.7                           0.335                1.65              0.086                  ok            True                  False
   ROP           89.29               28            1.01              3.41        478.08                37.35         0.521          pass              0.595             58.3                           0.664               19.20              1.709                  ok            True                  False
  VRSK           80.00               20            1.65              2.33        200.50                37.47         0.521          pass              0.283             54.9                           0.572                3.82              0.165                  ok            True                  False
   ADP           89.66               29            0.51              1.06        298.32                27.85         0.513          pass              0.665             76.6                           0.684                1.54             -0.166                  ok            True                  False
  TMUS           55.56                9            2.45              2.75        158.97                68.40         0.638          pass              0.095             10.5                           0.172               -0.97              0.080                  ok           False                  False
   PEP           75.00                4            1.76              1.73        139.68                26.86         0.585          pass              0.088              9.9                           0.177                2.93              0.207                  ok           False                  False
  PAYX           77.78               27            0.04              0.03        115.48                35.36         0.561          pass              0.465             98.6                           0.785                3.55             -0.021                  ok           False                  False
   CSX           70.00               10            1.45              0.53         51.39                27.65         0.548          pass              0.108             17.6                           0.359                5.80              0.570                  ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103130506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103130506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103130506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103130506)

</details>
