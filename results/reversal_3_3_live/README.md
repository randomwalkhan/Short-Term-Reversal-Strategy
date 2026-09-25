# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 12:15:06 EDT`
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

- Cash: `$73,553.30`
- Equity: `$73,553.30`
- Realized PnL: `$63,553.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-25)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  SOXL     option         option SOXL261030C00145000     16          2026-09-24         2026-09-25       20.275      23.775 5600.0   17.262639 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.64              1.85        160.82               109.71         0.720          pass              0.684             45.2                           0.513               21.38              2.828                                 ok            True                  False
  CRWD           86.11               36            1.68              3.04        258.37                96.70         0.665          pass              0.527             41.4                           0.345               22.24              2.076                                 ok            True                  False
   TRI           86.67               30            1.25              0.88         99.94                57.78         0.556          pass              0.590             74.3                           0.540                3.51             -0.127                                 ok            True                  False
  FTNT           85.00               20            2.49              3.11        177.34                58.17         0.543          pass              0.326             23.8                           0.234                9.68              1.065                                 ok            True                  False
  SHOP           87.50               32            1.28              1.30        144.60                62.63         0.513          pass              0.566             56.0                           0.739               11.27              1.326                                 ok            True                  False
  PANW           62.50               16            3.27              8.93        386.09                80.20         0.589          pass              0.157             19.2                           0.168               11.42              1.183                                 ok           False                  False
  TEAM          100.00               42            0.13              0.18        192.53                57.21         0.576          pass              0.926             89.6                           0.488                7.12              0.661                                 ok           False                  False
   KHC           92.86               14            1.05              0.17         23.79                23.05         0.540          pass              0.474             16.9                           0.369               -3.20             -0.351            downtrend_blocked_slope           False                  False
    MU           90.24               41            0.00              0.04       1080.51                50.28         0.536          pass              0.825             99.3                           0.672               10.79              1.794                                 ok           False                  False
   XEL           94.12               17            0.68              0.33         69.42                16.48         0.526          pass              0.608             44.0                           0.631               -7.64             -0.761 downtrend_blocked_slope_and_streak           False                  False
  CHTR           82.76               29            1.95              1.61        116.86                64.78         0.518          pass              0.395             47.7                           0.777              -18.00             -2.541 downtrend_blocked_slope_and_streak           False                  False
   EXC           93.75               16            0.65              0.18         40.12                15.59         0.516          pass              0.592             44.7                           0.456               -7.95             -0.785 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-09-25T12:00:04.925096-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:55:06.011160-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:50:06.515187-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:45:06.706431-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:40:06.045824-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:35:03.999797-04:00 early_entry_1135 early_entry_shadow   {"contract_symbol": "CRWD261120C00260000", "current_drop_pct": 0.85, "early_entry_score": 0.695, "early_reclaim_pct": 70.4, "entry_ask": 21.8, "entry_bid": 21.15, "entry_mode": "early", "entry_option_price": 21.475, "hypothetical_budget": 36776.65, "hypothetical_contracts": 17, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 689.0, "option_spread_pct": 3.03, "option_volume": 191.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 88.1, "ticker": "CRWD", "timing_score": 0.679, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.695, "early_reclaim_pct": 70.4, "matched_signals": 42, "recovery_stability_score": 0.698, "success_rate": 88.1, "ticker": "CRWD", "timing_score": 0.679, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-25T11:30:05.086082-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:25:05.020755-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:20:06.150324-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-25T11:15:04.659630-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "MSTR261120C00160000", "current_drop_pct": 0.74, "early_entry_score": 0.847, "early_reclaim_pct": 71.6, "entry_ask": 17.3, "entry_bid": 17.0, "entry_mode": "early", "entry_option_price": 17.15, "hypothetical_budget": 36776.65, "hypothetical_contracts": 21, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2435.0, "option_spread_pct": 1.75, "option_volume": 1951.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.835, "shadow_only": true, "success_rate": 94.44, "ticker": "MSTR", "timing_score": 0.734, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.847, "early_reclaim_pct": 71.6, "matched_signals": 36, "recovery_stability_score": 0.835, "success_rate": 94.44, "ticker": "MSTR", "timing_score": 0.734, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925121506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925121506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925121506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925121506)

</details>
