# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 11:30:05 EDT`
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
  INTC           87.18               39            0.60              0.50        120.01                73.63         0.589          pass              0.668             74.9                           0.666                9.84              0.547                       ok            True                  False
  ASML           81.82               33            0.55              6.93       1808.70                42.37         0.542          pass              0.370             38.0                           0.350               10.56              0.944                       ok            True                  False
   STX           88.24               34            0.91              5.88        919.82                53.17         0.514          pass              0.643             70.6                           0.706               13.89              0.964                       ok            True                  False
    MU           89.66               29            1.37             10.18       1060.75                49.56         0.503          pass              0.631             65.6                           0.720                7.48              0.492                       ok            True                  False
  NXPI           87.10               31            0.76              1.27        236.99                38.88         0.501          pass              0.439             19.9                           0.272                3.41              0.349                       ok            True                  False
    ZS           97.87               47            0.16              0.22        199.32                78.48         0.624          pass              0.895             77.5                           0.405                0.83             -0.233                       ok           False                  False
  AMGN           50.00                6            1.98              5.83        419.01                46.02         0.592          pass              0.093             11.2                           0.113                8.79              0.964                       ok           False                  False
  DRAM           80.00               35            0.39              0.16         60.29                53.77         0.563          pass              0.454             77.0                           0.607                4.06              0.098                       ok           False                  False
   WBD           95.56               45            0.03              0.01         30.95                37.62         0.555          pass              0.806             50.0                           0.395                9.56              0.817                       ok           False                  False
  MPWR           92.31               39            0.24              2.29       1346.24                50.40         0.531          pass              0.814             79.9                           0.498               15.08              1.142                       ok           False                  False
  QCOM           92.68               41            0.12              0.15        183.97                56.29         0.525          pass              0.844             84.3                           0.603               -2.59             -0.219 downtrend_blocked_streak           False                  False
  SHOP           87.23               47            0.04              0.04        148.28                58.67         0.518          pass              0.740             98.4                           0.488               15.27              1.317                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-10-01T11:30:05.726555-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:25:06.486320-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.79, "early_entry_score": 0.671, "early_reclaim_pct": 66.9, "entry_ask": 9.8, "entry_bid": 9.55, "entry_mode": "early", "entry_option_price": 9.675, "hypothetical_budget": 40682.15, "hypothetical_contracts": 42, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 2.58, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.596, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.671, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.563, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.596, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:20:05.846567-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "GILD261106C00148000", "current_drop_pct": 0.55, "early_entry_score": 0.795, "early_reclaim_pct": 75.8, "entry_ask": 7.55, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 6.675, "hypothetical_budget": 40682.15, "hypothetical_contracts": 60, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.795, "early_reclaim_pct": 75.8, "matched_signals": 33, "recovery_stability_score": 0.597, "success_rate": 93.94, "ticker": "GILD", "timing_score": 0.423, "trend_health_status": "ok"}, {"current_drop_pct": 1.25, "early_entry_score": 0.671, "early_reclaim_pct": 68.5, "matched_signals": 31, "recovery_stability_score": 0.662, "success_rate": 90.32, "ticker": "MU", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T11:15:05.398029-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "GILD261106C00148000", "current_drop_pct": 0.6, "early_entry_score": 0.776, "early_reclaim_pct": 73.4, "entry_ask": 7.55, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 6.675, "hypothetical_budget": 40682.15, "hypothetical_contracts": 60, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.22, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.776, "early_reclaim_pct": 73.4, "matched_signals": 32, "recovery_stability_score": 0.593, "success_rate": 93.75, "ticker": "GILD", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T11:10:04.424751-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                    {"contract_symbol": "FTNT261120C00180000", "current_drop_pct": 0.56, "early_entry_score": 0.744, "early_reclaim_pct": 73.3, "entry_ask": 15.6, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 15.3, "hypothetical_budget": 40682.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 176.0, "option_spread_pct": 3.92, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.578, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.744, "early_reclaim_pct": 73.3, "matched_signals": 42, "recovery_stability_score": 0.578, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T11:05:05.459722-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:00:05.415565-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:55:06.231186-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:50:06.456306-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:45:05.877463-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001113005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001113005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001113005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001113005)

</details>
