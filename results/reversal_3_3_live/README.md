# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 12:20:06 EDT`
Last processed slot: `manage_1230`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
    ZS           97.78               45            0.26              0.36        199.27                78.48         0.629          pass              0.855             64.1                           0.462                0.73             -0.238                       ok           False                  False
  INTC           87.50               40            0.27              0.23        120.13                73.63         0.603          pass              0.726             88.5                           0.779               10.20              0.561                       ok           False                  False
   WBD           95.35               43            0.05              0.01         30.95                37.62         0.565          pass              0.731             25.0                           0.290                9.54              0.816                       ok           False                  False
  DRAM           79.41               34            0.48              0.20         60.27                53.77         0.562          pass              0.431             71.6                           0.553                3.96              0.094                       ok           False                  False
  CRWD           89.13               46            0.17              0.32        264.61                63.45         0.542          pass              0.773             91.6                           0.503                7.57              0.896                       ok           False                  False
   STX           88.89               36            0.32              2.09        921.44                53.17         0.540          pass              0.733             89.5                           0.755               14.56              0.991                       ok           False                  False
  ASML           82.86               35            0.45              5.74       1809.21                42.37         0.535          pass              0.476             59.8                           0.628               10.66              0.949                       ok           False                  False
  QCOM           92.68               41            0.01              0.01        184.04                56.29         0.532          pass              0.889             99.3                           0.748               -2.48             -0.213 downtrend_blocked_streak           False                  False
  MPWR           92.31               39            0.23              2.18       1346.29                50.40         0.532          pass              0.817             80.8                           0.692               15.09              1.143                       ok           False                  False
  AMGN            0.00                1            2.55              7.51        418.29                46.02         0.529          pass              0.068              5.0                           0.145                8.16              0.937                       ok           False                  False
  ABNB           82.61               23            1.38              1.55        159.99                40.44         0.513          pass              0.274             22.3                           0.310               -4.52             -0.519  downtrend_blocked_slope           False                  False
   XEL           84.62               26            0.24              0.12         70.43                18.32         0.503          pass              0.528             82.7                           0.605               -4.51             -0.427  downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001122006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001122006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001122006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001122006)

</details>
