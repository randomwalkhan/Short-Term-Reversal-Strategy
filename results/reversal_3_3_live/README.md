# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 12:10:01 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$31,411.75`
- Equity: `$31,411.75`
- Realized PnL: `$21,411.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260821C00290000      7          2026-07-17         2026-07-20        20.15      23.275 2187.5   15.508685 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WBD           83.33               12            1.14              0.21         26.78                20.40         0.566          pass              0.201             14.1                           0.369                1.70              0.369                                 ok            True                  False
  MNST          100.00               12            1.59              1.09         97.03                20.09         0.537          pass              0.522             18.4                           0.187               -1.46              0.114                                 ok            True                  False
   CSX           86.67               15            1.00              0.36         50.60                17.40         0.534          pass              0.276              3.8                           0.156                2.93              0.428                                 ok            True                  False
  ORLY           80.00               25            1.34              0.80         85.71                41.23         0.526          pass              0.221             22.8                           0.266                0.78             -0.007                                 ok            True                  False
  CTAS           85.00               20            1.41              2.01        203.59                36.07         0.520          pass              0.351             33.0                           0.597               13.09              1.522                                 ok            True                  False
  GILD           92.86               28            0.51              0.48        134.08                34.72         0.519          pass              0.650             45.2                           0.418                3.08              0.050                                 ok            True                  False
  BKNG           86.21               29            1.09              1.39        181.09                41.44         0.503          pass              0.505             54.2                           0.629               -0.73              0.174                                 ok            True                  False
  SBUX           88.46               26            0.81              0.60        105.23                24.88         0.501          pass              0.425             14.1                           0.221                2.48              0.271                                 ok            True                  False
  KLAC           89.47               38            0.30              0.44        212.56               107.27         0.708          pass              0.760             83.3                           0.679               -9.08             -0.563 downtrend_blocked_slope_and_streak           False                  False
  LRCX           91.67               36            0.21              0.46        313.10                96.49         0.671          pass              0.827             91.8                           0.748              -10.72             -0.868 downtrend_blocked_slope_and_streak           False                  False
   KHC           88.89               18            0.10              0.02         25.87                35.69         0.636          pass              0.622             89.4                           0.610                4.17              0.472                                 ok           False                  False
  ASML           94.44               36            0.11              1.31       1747.02                63.09         0.617          pass              0.887             88.8                           0.691               -4.35             -0.177                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-20T12:00:04.096666-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:55:01.102362-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:50:01.110550-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:45:01.103753-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "VRSK260821C00200000", "current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 68.7, "entry_ask": 9.6, "entry_bid": 8.6, "entry_mode": "early", "entry_option_price": 9.1, "hypothetical_budget": 15705.88, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 47.0, "option_spread_pct": 10.99, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.668, "shadow_only": true, "success_rate": 90.24, "ticker": "VRSK", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 68.7, "matched_signals": 41, "recovery_stability_score": 0.668, "success_rate": 90.24, "ticker": "VRSK", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-20T11:40:02.180070-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:35:01.099987-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "VRSK260821C00200000", "current_drop_pct": 0.57, "early_entry_score": 0.695, "early_reclaim_pct": 65.2, "entry_ask": 9.4, "entry_bid": 8.7, "entry_mode": "early", "entry_option_price": 9.05, "hypothetical_budget": 15705.88, "hypothetical_contracts": 17, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 47.0, "option_spread_pct": 7.73, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.692, "shadow_only": true, "success_rate": 89.74, "ticker": "VRSK", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.695, "early_reclaim_pct": 65.2, "matched_signals": 39, "recovery_stability_score": 0.692, "success_rate": 89.74, "ticker": "VRSK", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-20T11:30:02.147951-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:25:05.073932-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:20:01.956277-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T11:15:03.134685-04:00 early_entry_1115 early_entry_shadow                                  {"contract_symbol": "ADP260821C00250000", "current_drop_pct": 0.55, "early_entry_score": 0.785, "early_reclaim_pct": 67.0, "entry_ask": 13.2, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.35, "hypothetical_budget": 15705.88, "hypothetical_contracts": 12, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 640.0, "option_spread_pct": 13.77, "option_volume": 704.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.779, "shadow_only": true, "success_rate": 96.67, "ticker": "ADP", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.785, "early_reclaim_pct": 67.0, "matched_signals": 30, "recovery_stability_score": 0.779, "success_rate": 96.67, "ticker": "ADP", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720121001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720121001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720121001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720121001)

</details>
