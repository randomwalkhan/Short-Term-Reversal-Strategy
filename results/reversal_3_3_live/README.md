# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 11:20:04 EDT`
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

- Cash: `$33,370.75`
- Equity: `$33,370.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SOXL     option         option SOXL260717C00270000      2          2026-06-04         2026-06-05        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  PANW           89.66               29            1.25              2.44        278.20                60.15         0.557          pass              0.595             51.9                           0.361                9.03              1.326                       ok            True                  False
  CTSH           92.59               27            0.96              0.36         53.25                51.38         0.551          pass              0.680             58.5                           0.354                0.27              0.155                       ok            True                  False
  WDAY           86.21               29            2.01              2.08        147.02                69.97         0.545          pass              0.382             11.6                           0.298               13.11              1.925                       ok            True                  False
  TEAM           95.45               22            3.61              2.56        100.40                86.36         0.522          pass              0.532              0.0                           0.203               14.54              1.807                       ok            True                  False
  FTNT          100.00               24            1.55              1.62        148.98                44.88         0.518          pass              0.672             42.3                           0.466               10.02              1.475                       ok            True                  False
    ZS           80.77               26            1.87              1.77        134.50               157.69         0.877          pass              0.237              7.3                           0.134              -27.22             -2.290  downtrend_blocked_slope           False                  False
  MELI           95.12               41            0.28              3.20       1633.41                60.42         0.605          pass              0.878             72.4                           0.403               -2.06             -0.293  downtrend_blocked_slope           False                  False
  CSCO          100.00                3            3.40              3.09        128.68                55.20         0.581          pass              0.510             17.2                           0.394                4.30              0.810                       ok           False                  False
   ADI          100.00                5            2.96              8.87        424.96                45.54         0.552          pass              0.527             24.0                           0.273                5.08              0.387                       ok           False                  False
  META           77.78                9            2.18              9.59        623.46                30.98         0.513          pass              0.073              7.2                           0.223                1.07              0.036                       ok           False                  False
   CEG           75.00               20            2.57              4.76        262.55                55.63         0.508          pass              0.146              9.3                           0.136               -9.81             -1.407  downtrend_blocked_slope           False                  False
  AVGO          100.00                1            4.97             14.58        412.66                65.35         0.505          pass              0.465              4.9                           0.121               -3.88             -0.077 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-06-05T11:20:04.824659-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:15:04.845440-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:10:06.011587-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:05:02.012867-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                 {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.77, "early_entry_score": 0.749, "early_reclaim_pct": 70.2, "entry_ask": 17.7, "entry_bid": 16.7, "entry_mode": "early", "entry_option_price": 17.2, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 5.81, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.631, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.749, "early_reclaim_pct": 70.2, "matched_signals": 36, "recovery_stability_score": 0.631, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:00:03.928468-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                  {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.71, "early_entry_score": 0.758, "early_reclaim_pct": 72.8, "entry_ask": 17.8, "entry_bid": 17.0, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 4.6, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.548, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.758, "early_reclaim_pct": 72.8, "matched_signals": 36, "recovery_stability_score": 0.619, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.548, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T10:55:02.043885-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:50:04.031385-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:45:02.885647-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:40:02.027944-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.81, "early_entry_score": 0.745, "early_reclaim_pct": 69.0, "entry_ask": 18.2, "entry_bid": 16.75, "entry_mode": "early", "entry_option_price": 17.475, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 8.3, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.738, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.541, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.745, "early_reclaim_pct": 69.0, "matched_signals": 36, "recovery_stability_score": 0.738, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.541, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T10:35:05.997480-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "DASH260717C00160000", "current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "entry_ask": 11.75, "entry_bid": 10.75, "entry_mode": "early", "entry_option_price": 11.25, "hypothetical_budget": 16685.38, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 157.0, "option_spread_pct": 8.89, "option_volume": 14.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.812, "early_reclaim_pct": 75.5, "matched_signals": 41, "recovery_stability_score": 0.584, "success_rate": 92.68, "ticker": "DASH", "timing_score": 0.473, "trend_health_status": "ok"}, {"current_drop_pct": 0.66, "early_entry_score": 0.776, "early_reclaim_pct": 74.8, "matched_signals": 37, "recovery_stability_score": 0.742, "success_rate": 91.89, "ticker": "PANW", "timing_score": 0.545, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605112004)

</details>
