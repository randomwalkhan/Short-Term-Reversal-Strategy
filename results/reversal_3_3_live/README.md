# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 10:45:04 EST`
Last processed slot: `early_entry_1045`

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

- Cash: `$111,239.80`
- Equity: `$111,239.80`
- Realized PnL: `$101,239.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  QCOM     option         option QCOM261218C00170000     52          2026-11-16         2026-11-17       11.125     10.0125 -5785.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           89.47               19            1.30              2.67        293.06                59.80         0.632          pass              0.389              4.5                           0.101               -7.07             -0.043                                 ok            True                  False
   KDP           95.83               24            0.74              0.19         35.50                46.38         0.595          pass              0.644             30.3                           0.249                1.66             -0.117                                 ok            True                  False
   CEG           88.24               17            2.33              4.52        275.88                60.48         0.590          pass              0.350              8.1                           0.209                3.18              1.238                                 ok            True                  False
  ABNB           85.19               27            1.21              1.57        185.52                54.56         0.590          pass              0.333              7.4                           0.241               10.17              0.760                                 ok            True                  False
  QCOM           83.33               12            2.89              3.41        167.06                68.75         0.589          pass              0.178              5.6                           0.185               -0.47              0.291                                 ok            True                  False
   CSX           80.00               15            1.48              0.54         51.80                34.26         0.577          pass              0.119              9.4                           0.203                1.06              0.254                                 ok            True                  False
  SBUX           88.24               17            0.98              0.75        108.40                31.47         0.569          pass              0.403             26.6                           0.171                3.36              0.198                                 ok            True                  False
   ADP           84.21               19            1.20              2.63        312.30                28.40         0.551          pass              0.295             22.6                           0.288                4.62              0.386                                 ok            True                  False
  ODFL           82.14               28            1.12              1.37        173.70                43.33         0.551          pass              0.232              0.0                           0.223               -3.01             -0.110                                 ok            True                  False
  META           80.77               26            1.31              5.73        623.96                41.97         0.528          pass              0.198              6.0                           0.139               -0.45              0.141                                 ok            True                  False
  AMZN           85.29               34            0.52              0.95        257.34                40.10         0.525          pass              0.469             38.4                           0.200                2.28              0.108                                 ok            True                  False
  SOXL           59.09               22            7.14              2.44         47.72               265.45         0.805          pass              0.182              7.2                           0.157              -38.07             -1.556 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-17T10:45:04.877729-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:40:03.860720-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:35:06.835467-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:30:03.912380-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:25:05.911595-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:20:06.716157-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:15:04.834585-05:00 early_entry_1015 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:10:04.914368-05:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:05:06.251834-05:00 early_entry_1005 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:00:06.465677-05:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117104504)

</details>
