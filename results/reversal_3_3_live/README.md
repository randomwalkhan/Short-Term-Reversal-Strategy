# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-17 13:35:06 EST`
Last processed slot: `manage_1330`

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
   APP           94.44               18            2.82              8.20        411.70               119.50         0.781          pass              0.684             55.7                           0.781               64.35              4.178                  ok            True                  False
  IDXX           96.15               26            1.24              6.06        698.05                77.90         0.725          pass              0.608              9.8                           0.132                2.97              0.330                  ok            True                  False
   ROP           84.21               19            1.24              4.21        481.92                41.88         0.603          pass              0.367             44.7                           0.598                0.87             -0.069                  ok            True                  False
 GOOGL           82.14               28            0.86              1.72        282.98                55.10         0.594          pass              0.397             53.4                           0.552                0.44              0.182                  ok            True                  False
  GOOG           82.14               28            0.97              1.92        280.44                53.19         0.581          pass              0.377             47.4                           0.448                0.09              0.115                  ok            True                  False
  QCOM           87.88               33            0.96              1.13        168.03                68.75         0.579          pass              0.641             73.3                           0.706                1.50              0.380                  ok            True                  False
   CEG           88.89               18            2.29              4.46        275.91                60.48         0.578          pass              0.447             33.0                           0.334                3.21              1.239                  ok            True                  False
   ADP           85.00               20            1.12              2.46        312.38                28.40         0.550          pass              0.342             28.9                           0.554                4.70              0.390                  ok            True                  False
  ODFL           83.87               31            0.92              1.13        173.81                43.33         0.542          pass              0.425             42.7                           0.380               -2.81             -0.101                  ok            True                  False
  INSM           84.44               45            0.54              0.46        122.68                61.88         0.538          pass              0.627             84.8                           0.795               17.02              1.505                  ok            True                  False
  META           83.87               31            0.68              3.00        625.12                41.97         0.535          pass              0.497             66.7                           0.728                0.18              0.169                  ok            True                  False
   CSX           82.76               29            0.80              0.29         51.91                34.26         0.534          pass              0.424             56.8                           0.643                1.76              0.286                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-11-17T12:00:06.286293-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:55:01.833366-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:50:06.047053-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:45:03.924491-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                 {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "entry_ask": 23.75, "entry_bid": 21.55, "entry_mode": "early", "entry_option_price": 22.65, "hypothetical_budget": 55619.9, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 9.71, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.8, "early_reclaim_pct": 75.7, "matched_signals": 32, "recovery_stability_score": 0.589, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-17T11:40:06.599969-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:35:05.679790-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "PYPL261218C00057500", "current_drop_pct": 0.51, "early_entry_score": 0.843, "early_reclaim_pct": 65.9, "entry_ask": 3.05, "entry_bid": 2.78, "entry_mode": "early", "entry_option_price": 2.915, "hypothetical_budget": 55619.9, "hypothetical_contracts": 190, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3814.0, "option_spread_pct": 9.26, "option_volume": 43.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.843, "early_reclaim_pct": 65.9, "matched_signals": 40, "recovery_stability_score": 0.562, "success_rate": 95.0, "ticker": "PYPL", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-17T11:30:05.827440-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:25:01.808669-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.62, "early_entry_score": 0.786, "early_reclaim_pct": 71.0, "entry_ask": 23.65, "entry_bid": 21.25, "entry_mode": "early", "entry_option_price": 22.45, "hypothetical_budget": 55619.9, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 10.69, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.592, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.786, "early_reclaim_pct": 71.0, "matched_signals": 32, "recovery_stability_score": 0.632, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-17T11:20:04.857658-05:00 early_entry_1120 early_entry_shadow {"contract_symbol": "PYPL261218C00057500", "current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 61.1, "entry_ask": 2.89, "entry_bid": 2.59, "entry_mode": "early", "entry_option_price": 2.74, "hypothetical_budget": 55619.9, "hypothetical_contracts": 202, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3814.0, "option_spread_pct": 10.95, "option_volume": 43.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.809, "early_reclaim_pct": 61.1, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 94.74, "ticker": "PYPL", "timing_score": 0.461, "trend_health_status": "ok"}, {"current_drop_pct": 0.61, "early_entry_score": 0.786, "early_reclaim_pct": 71.2, "matched_signals": 32, "recovery_stability_score": 0.705, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.592, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-17T11:15:06.470113-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261117133506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261117133506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261117133506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261117133506)

</details>
