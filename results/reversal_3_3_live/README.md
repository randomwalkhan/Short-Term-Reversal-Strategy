# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-30 11:35:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KDP           86.96               23            0.67              0.15         31.39                34.46         0.590          pass              0.522             63.5                           0.695                3.24              0.053                      ok            True                  False
   MAR          100.00               11            1.94              5.18        378.90                28.18         0.560          pass              0.586             41.2                           0.459                2.90              0.322                      ok            True                  False
  VRTX           81.82               11            2.05              6.92        480.36                33.19         0.554          pass              0.182             23.9                           0.302               -0.60             -0.039                      ok            True                  False
  ABNB           95.24               21            1.58              1.69        152.29                40.20         0.551          pass              0.648             39.8                           0.481                2.77              0.083                      ok            True                  False
   HON           82.35               17            1.19              2.00        240.26                39.75         0.538          pass              0.235             24.0                           0.366                7.00              1.057                      ok            True                  False
  AMGN           93.75               16            1.48              4.02        385.92                27.22         0.537          pass              0.578             39.1                           0.634                7.50              0.725                      ok            True                  False
   AEP           82.35               17            1.20              1.09        128.93                20.00         0.517          pass              0.221             19.9                           0.211               -5.25             -0.168                      ok            True                  False
  IDXX           83.33               12            2.48              9.88        565.53                36.22         0.509          pass              0.181              9.3                           0.253                2.77             -0.049                      ok            True                  False
  PCAR           86.96               23            1.26              1.18        133.36                29.38         0.508          pass              0.416             31.1                           0.439                6.65              0.912                      ok            True                  False
  DASH           97.30               37            1.06              1.44        192.91                53.51         0.506          pass              0.797             55.6                           0.554                1.96             -0.025                      ok            True                  False
  ISRG           78.57               28            1.02              2.51        352.02                72.57         0.662          pass              0.324             46.0                           0.431              -10.14             -0.980 downtrend_blocked_slope           False                  False
  PYPL           77.78                9            2.48              1.01         57.92                61.52         0.659          pass              0.110             14.7                           0.379                2.49              0.169                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-30T11:35:05.117192-04:00 early_entry_1135 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:30:04.994647-04:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:25:01.766574-04:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:20:04.950564-04:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:15:04.858903-04:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:10:03.886706-04:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:05:04.940210-04:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T11:00:04.904053-04:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:55:01.879209-04:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-30T10:50:01.107758-04:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260730113505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260730113505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260730113505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260730113505)

</details>
