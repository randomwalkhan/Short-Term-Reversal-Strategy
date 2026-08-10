# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$31,073.00`
- Equity: `$31,073.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  PYPL     option         option PYPL260918C00060000     94          2026-08-07         2026-08-10        1.725      1.5525 -1621.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           83.78               37            1.01              1.06        148.62               133.30         0.798          pass              0.549             62.9                           0.440               53.92              3.904                  ok            True                  False
  SOXL           80.65               31            3.59              3.52        138.74               179.06         0.700          pass              0.313             28.8                           0.275                5.52              2.571                  ok            True                  False
  LRCX           87.10               31            1.17              2.54        310.26                90.05         0.650          pass              0.508             38.0                           0.330                5.52              1.423                  ok            True                  False
  PYPL           93.94               33            0.79              0.33         58.93                60.12         0.648          pass              0.726             45.3                           0.413                4.52              0.343                  ok            True                  False
  TMUS           90.91               22            1.26              1.57        176.52                55.81         0.647          pass              0.572             45.3                           0.607               -1.28             -0.162                  ok            True                  False
  AMAT           89.29               28            1.68              6.34        536.42                85.88         0.637          pass              0.506             25.0                           0.278                2.55              1.262                  ok            True                  False
 CMCSA           90.91               11            1.75              0.31         25.23                44.15         0.630          pass              0.432             23.9                           0.298                9.28              0.754                  ok            True                  False
  BKNG           95.00               20            1.72              2.58        213.31                46.72         0.561          pass              0.610             29.2                           0.379               12.82              1.027                  ok            True                  False
  MDLZ           91.67               12            1.64              0.72         62.30                30.17         0.561          pass              0.433             17.6                           0.307                1.51             -0.037                  ok            True                  False
  ORLY           90.62               32            0.95              0.62         93.26                35.75         0.508          pass              0.628             49.0                           0.674                2.26              0.423                  ok            True                  False
   PEP           80.00               25            0.73              0.71        138.71                22.07         0.506          pass              0.256             35.0                           0.486               -1.28             -0.277                  ok            True                  False
  MCHP           82.61               23            3.02              1.79         83.92                76.06         0.501          pass              0.233              8.9                           0.185                5.43              0.901                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-08-10T11:15:01.972299-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "HON260911C00245000", "current_drop_pct": 0.65, "early_entry_score": 0.688, "early_reclaim_pct": 70.3, "entry_ask": 9.4, "entry_bid": 6.7, "entry_mode": "early", "entry_option_price": 8.05, "hypothetical_budget": 15536.5, "hypothetical_contracts": 19, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 33.54, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 90.62, "ticker": "HON", "timing_score": 0.475, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.688, "early_reclaim_pct": 70.3, "matched_signals": 32, "recovery_stability_score": 0.713, "success_rate": 90.62, "ticker": "HON", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T11:10:06.738408-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:05:04.768952-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:00:02.784116-04:00 early_entry_1100 early_entry_shadow                           {"contract_symbol": "TMUS260918C00175000", "current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "entry_ask": 7.0, "entry_bid": 6.5, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 15536.5, "hypothetical_contracts": 23, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 971.0, "option_spread_pct": 7.41, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "matched_signals": 33, "recovery_stability_score": 0.827, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T10:55:01.620992-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:50:05.624699-04:00 early_entry_1050 early_entry_shadow                                          {"contract_symbol": "PYPL260918C00060000", "current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "entry_ask": 1.59, "entry_bid": 1.52, "entry_mode": "early", "entry_option_price": 1.555, "hypothetical_budget": 15536.5, "hypothetical_contracts": 99, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 8780.0, "option_spread_pct": 4.5, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:45:01.632821-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:40:02.921350-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "PYPL260918C00060000", "fill_price": 1.5525, "pnl": -1621.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810111501)

</details>
