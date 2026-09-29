# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-29 12:15:05 EDT`
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

- Cash: `$78,758.30`
- Equity: `$78,758.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-29)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261120C00270000     24          2026-09-28         2026-09-29         14.4       18.05 8760.0   25.347222 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MSTR           92.59               27            2.56              2.82        155.93                99.69         0.645          pass              0.562             16.0                           0.408               18.14              2.105                      ok            True                  False
    ZS           97.37               38            1.29              1.80        198.62                81.58         0.573          pass              0.764             40.1                           0.331                1.51              0.336                      ok            True                  False
  QCOM           90.32               31            0.73              0.96        187.07                57.69         0.539          pass              0.493              7.8                           0.160               -0.90              0.372                      ok            True                  False
  PYPL           91.67               24            1.11              0.42         54.10                35.54         0.519          pass              0.473              5.5                           0.151               -0.25              0.206                      ok            True                  False
   KDP           94.74               19            1.00              0.22         31.37                25.35         0.503          pass              0.704             66.8                           0.682               -0.38              0.043                      ok            True                  False
  CRWD           89.13               46            0.20              0.36        259.10                71.98         0.595          pass              0.759             85.3                           0.462                6.70              0.833                      ok           False                  False
   WBD           95.00               40            0.11              0.02         30.89                38.06         0.578          pass              0.868             70.1                           0.679               10.11              1.217                      ok           False                  False
  AMGN           86.11               36            0.32              0.95        417.72                46.33         0.574          pass              0.606             70.8                           0.391               10.95              1.217                      ok           False                  False
   TRI           85.19               27            1.62              1.11         96.86                56.59         0.559          pass              0.364             19.0                           0.168               -6.69             -0.335 downtrend_blocked_slope           False                  False
  TMUS           76.92               13            1.54              1.80        165.68                33.31         0.547          pass              0.166             30.4                           0.559               -9.19             -0.692 downtrend_blocked_slope           False                  False
  MPWR           87.18               39            0.20              1.90       1350.38                52.17         0.538          pass              0.702             87.6                           0.519               18.03              1.995                      ok           False                  False
  CTAS           80.00                5            1.90              2.67        199.44                21.05         0.528          pass              0.074              7.1                           0.212               -1.10             -0.026                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-29T12:00:02.521898-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.71, "early_entry_score": 0.849, "early_reclaim_pct": 85.5, "entry_ask": 2.4, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.275, "hypothetical_budget": 39379.15, "hypothetical_contracts": 173, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 10.99, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.386, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.849, "early_reclaim_pct": 85.5, "matched_signals": 33, "recovery_stability_score": 0.603, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.386, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:55:06.341077-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.72, "early_entry_score": 0.848, "early_reclaim_pct": 85.3, "entry_ask": 2.35, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.25, "hypothetical_budget": 39379.15, "hypothetical_contracts": 175, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 8.89, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.385, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.848, "early_reclaim_pct": 85.3, "matched_signals": 33, "recovery_stability_score": 0.577, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.385, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:50:06.042061-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.82, "early_entry_score": 0.829, "early_reclaim_pct": 83.3, "entry_ask": 2.4, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.275, "hypothetical_budget": 39379.15, "hypothetical_contracts": 173, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 10.99, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 96.77, "ticker": "FAST", "timing_score": 0.39, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.829, "early_reclaim_pct": 83.3, "matched_signals": 31, "recovery_stability_score": 0.556, "success_rate": 96.77, "ticker": "FAST", "timing_score": 0.39, "trend_health_status": "ok"}, {"current_drop_pct": 0.86, "early_entry_score": 0.711, "early_reclaim_pct": 61.4, "matched_signals": 42, "recovery_stability_score": 0.711, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:45:05.362745-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:40:04.530036-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:35:05.300798-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:30:04.434130-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                        {"contract_symbol": "FTNT261120C00175000", "current_drop_pct": 0.84, "early_entry_score": 0.713, "early_reclaim_pct": 62.1, "entry_ask": 15.8, "entry_bid": 15.25, "entry_mode": "early", "entry_option_price": 15.525, "hypothetical_budget": 39379.15, "hypothetical_contracts": 25, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 71.0, "option_spread_pct": 3.54, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.472, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.713, "early_reclaim_pct": 62.1, "matched_signals": 42, "recovery_stability_score": 0.731, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.472, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:25:05.375211-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:20:05.555943-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-29T11:15:04.210610-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260929121505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260929121505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260929121505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260929121505)

</details>
