# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 14:45:04 EDT`
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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  META     option         option META261120C00735000      8          2026-09-30         2026-10-01       48.425     43.5825 -3874.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           97.87               47            0.04              0.05        199.40                78.48         0.631            pass              0.948             95.1                           0.481                0.95             -0.228                                 ok           False                  False
   WBD           95.35               43            0.06              0.01         30.94                37.62         0.562            pass              0.656              0.0                           0.189                9.53              0.815                                 ok           False                  False
  AMGN            0.00                2            2.31              6.81        418.59                46.02         0.536            pass              0.115             20.3                           0.476                8.43              0.948                                 ok           False                  False
  ASML           85.00               40            0.07              0.88       1811.29                42.37         0.532            pass              0.668             93.8                           0.753               11.09              0.966                                 ok           False                  False
  QCOM           92.68               41            0.08              0.10        184.00                56.29         0.528            pass              0.861             90.0                           0.464               -2.55             -0.217           downtrend_blocked_streak           False                  False
  NFLX           68.75               16            1.82              0.89         69.20                37.25         0.498 below_threshold              0.176             28.7                           0.313               -9.29             -0.751            downtrend_blocked_slope           False                  False
   XEL           86.67               30            0.11              0.05         70.46                18.32         0.491 below_threshold              0.637             92.3                           0.671               -4.38             -0.420            downtrend_blocked_slope           False                  False
  TMUS           84.00               25            1.05              1.20        162.57                33.48         0.490 below_threshold              0.380             41.5                           0.276               -3.05             -0.248                                 ok           False                  False
   PEP           76.92               13            0.82              0.72        126.41                14.74         0.488 below_threshold              0.069              0.0                           0.250               -5.97             -0.433            downtrend_blocked_slope           False                  False
  ABNB           87.18               39            0.50              0.56        160.41                40.44         0.480 below_threshold              0.649             71.9                           0.704               -3.66             -0.479                                 ok           False                  False
  MDLZ           96.55               29            0.12              0.05         57.80                16.32         0.470 below_threshold              0.836             87.3                           0.521               -6.09             -0.523 downtrend_blocked_slope_and_streak           False                  False
  PANW           78.38               37            1.44              4.01        395.59                66.50         0.468 below_threshold              0.360             44.3                           0.481                4.40              0.677                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-01T12:00:06.030645-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:55:01.414923-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "STX261030C00915000", "current_drop_pct": 0.54, "early_entry_score": 0.696, "early_reclaim_pct": 82.7, "entry_ask": 80.1, "entry_bid": 67.5, "entry_mode": "early", "entry_option_price": 73.8, "hypothetical_budget": 40682.15, "hypothetical_contracts": 5, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 25.0, "option_spread_pct": 17.07, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.696, "early_reclaim_pct": 82.7, "matched_signals": 35, "recovery_stability_score": 0.75, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T11:50:04.589481-04:00 early_entry_1150 early_entry_shadow                                            {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.7, "early_entry_score": 0.683, "early_reclaim_pct": 70.7, "entry_ask": 10.25, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 10.175, "hypothetical_budget": 40682.15, "hypothetical_contracts": 39, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 1.47, "option_volume": 55.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.683, "early_reclaim_pct": 70.7, "matched_signals": 36, "recovery_stability_score": 0.627, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.602, "trend_health_status": "ok"}, {"current_drop_pct": 0.75, "early_entry_score": 0.674, "early_reclaim_pct": 75.8, "matched_signals": 35, "recovery_stability_score": 0.757, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:45:02.515296-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:40:06.090435-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                   {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.77, "early_entry_score": 0.673, "early_reclaim_pct": 67.8, "entry_ask": 10.25, "entry_bid": 10.05, "entry_mode": "early", "entry_option_price": 10.15, "hypothetical_budget": 40682.15, "hypothetical_contracts": 40, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 1.97, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.673, "early_reclaim_pct": 67.8, "matched_signals": 36, "recovery_stability_score": 0.661, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:35:06.431749-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:30:05.726555-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:25:06.486320-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.79, "early_entry_score": 0.671, "early_reclaim_pct": 66.9, "entry_ask": 9.8, "entry_bid": 9.55, "entry_mode": "early", "entry_option_price": 9.675, "hypothetical_budget": 40682.15, "hypothetical_contracts": 42, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 2.58, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.596, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.671, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.563, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.596, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:20:05.846567-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "GILD261106C00148000", "current_drop_pct": 0.55, "early_entry_score": 0.795, "early_reclaim_pct": 75.8, "entry_ask": 7.55, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 6.675, "hypothetical_budget": 40682.15, "hypothetical_contracts": 60, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.795, "early_reclaim_pct": 75.8, "matched_signals": 33, "recovery_stability_score": 0.597, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.423, "trend_health_status": "ok"}, {"current_drop_pct": 1.25, "early_entry_score": 0.671, "early_reclaim_pct": 68.5, "matched_signals": 31, "recovery_stability_score": 0.662, "success_rate": 90.32, "ticker": "MU", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T11:15:05.398029-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "GILD261106C00148000", "current_drop_pct": 0.6, "early_entry_score": 0.776, "early_reclaim_pct": 73.4, "entry_ask": 7.55, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 6.675, "hypothetical_budget": 40682.15, "hypothetical_contracts": 60, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.776, "early_reclaim_pct": 73.4, "matched_signals": 32, "recovery_stability_score": 0.593, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001144504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001144504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001144504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001144504)

</details>
