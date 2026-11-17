# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 11:10:04 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  IDXX           97.06               34            0.87              4.27        698.82                77.90         0.706          pass              0.675             14.8                           0.196                3.35              0.347                  ok            True                  False
  FTNT           83.33               42            0.73              0.63        123.00                92.89         0.663          pass              0.557             67.2                           0.734               -4.48             -0.084                  ok            True                  False
   KDP           92.31               13            1.34              0.33         35.44                46.38         0.620          pass              0.431              6.9                           0.152                1.05             -0.144                  ok            True                  False
  QCOM           84.00               25            1.39              1.64        167.82                68.75         0.597          pass              0.451             61.4                           0.655                1.06              0.361                  ok            True                  False
 GOOGL           80.77               26            1.00              1.98        282.87                55.10         0.597          pass              0.325             46.2                           0.565                0.31              0.176                  ok            True                  False
   AEP          100.00               12            0.54              0.49        129.13                17.11         0.593          pass              0.572             33.2                           0.297               -0.18              0.155                  ok            True                  False
  MDLZ           95.45               22            0.53              0.25         67.43                29.55         0.587          pass              0.677             46.2                           0.299                3.17              0.198                  ok            True                  False
   CEG           88.89               18            2.27              4.41        275.93                60.48         0.580          pass              0.450             33.7                           0.426                3.24              1.241                  ok            True                  False
  GOOG           82.14               28            1.01              1.99        280.41                53.19         0.578          pass              0.371             45.5                           0.464                0.05              0.114                  ok            True                  False
   CSX           83.33               18            1.23              0.45         51.84                34.26         0.576          pass              0.300             33.3                           0.404                1.32              0.266                  ok            True                  False
  SBUX           84.62               13            1.28              0.97        108.30                31.47         0.570          pass              0.253             17.7                           0.173                3.05              0.184                  ok            True                  False
  FAST           90.91               11            1.14              0.44         54.92                19.71         0.554          pass              0.400             15.8                           0.199                4.11              0.527                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-17T11:10:04.744524-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:05:05.736370-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:00:04.828714-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:55:05.881265-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:50:06.221076-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:45:04.877729-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:40:03.860720-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:35:06.835467-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:30:03.912380-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:25:05.911595-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117111004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117111004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117111004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117111004)

</details>
