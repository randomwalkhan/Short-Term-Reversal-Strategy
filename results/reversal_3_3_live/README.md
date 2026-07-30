# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 11:40:02 EDT`
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

- Cash: `$33,222.25`
- Equity: `$33,222.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-30)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  FAST     option         option FAST260918C00045000     45          2026-07-29         2026-07-30         3.85       3.465 -1732.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   KDP           87.50               24            0.64              0.14         31.39                34.46         0.586          pass              0.548             65.2                           0.710                3.27              0.055                  ok            True                  False
   MAR          100.00               11            1.90              5.08        378.94                28.18         0.562          pass              0.590             42.4                           0.496                2.94              0.324                  ok            True                  False
  VRTX           83.33               12            1.93              6.53        480.53                33.19         0.557          pass              0.242             28.2                           0.423               -0.48             -0.033                  ok            True                  False
  AMGN           91.67               12            1.59              4.33        385.79                27.22         0.554          pass              0.483             34.4                           0.617                7.38              0.720                  ok            True                  False
  MNST           94.12               17            1.14              0.78         96.90                25.74         0.551          pass              0.672             64.6                           0.436               -1.93             -0.266                  ok            True                  False
  ABNB           95.24               21            1.74              1.86        152.21                40.20         0.541          pass              0.628             33.6                           0.389                2.60              0.076                  ok            True                  False
   HON           82.35               17            1.26              2.12        240.21                39.75         0.533          pass              0.221             19.4                           0.344                6.92              1.054                  ok            True                  False
  DASH           97.06               34            1.19              1.61        192.84                53.51         0.517          pass              0.763             50.3                           0.579                1.83             -0.031                  ok            True                  False
   AEP           82.35               17            1.21              1.10        128.93                20.00         0.517          pass              0.218             18.9                           0.213               -5.27             -0.168                  ok            True                  False
  IDXX           84.62               13            2.36              9.41        565.74                36.22         0.512          pass              0.235             13.6                           0.283                2.89             -0.044                  ok            True                  False
  ROST           88.46               26            0.89              1.56        251.29                27.49         0.511          pass              0.486             34.1                           0.459               13.04              1.043                  ok            True                  False
  PYPL           77.78                9            2.55              1.04         57.90                61.52         0.654          pass              0.102             12.1                           0.349                2.41              0.165                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-30T11:40:02.091678-04:00 early_entry_1140 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:35:05.117192-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:30:04.994647-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:25:01.766574-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:20:04.950564-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:15:04.858903-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:10:03.886706-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:05:04.940210-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:00:04.904053-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:55:01.879209-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730114002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730114002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730114002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730114002)

</details>
