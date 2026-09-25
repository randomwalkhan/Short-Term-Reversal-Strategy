# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 12:50:06 EDT`
Last processed slot: `manage_1300`

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
  MSTR           93.10               29            2.20              2.49        160.54               109.71         0.691          pass              0.624             26.3                           0.295               20.68              2.802                                 ok            True                  False
  CRWD           85.29               34            1.74              3.17        258.31                96.70         0.671          pass              0.485             38.9                           0.392               22.16              2.073                                 ok            True                  False
   TRI           84.00               25            1.77              1.24         99.79                57.78         0.551          pass              0.452             63.5                           0.457                2.96             -0.151                                 ok            True                  False
  FTNT           85.00               20            2.52              3.15        177.32                58.17         0.542          pass              0.323             23.0                           0.375                9.65              1.064                                 ok            True                  False
  SHOP           82.61               23            1.97              2.00        144.30                62.63         0.520          pass              0.305             32.4                           0.276               10.49              1.294                                 ok            True                  False
  INTC           80.65               31            2.16              1.93        126.56                68.53         0.503          pass              0.326             39.6                           0.501               21.08              2.961                                 ok            True                  False
  PANW           53.85               13            3.51              9.58        385.81                80.20         0.583          pass              0.118             13.4                           0.250               11.15              1.172                                 ok           False                  False
  TEAM          100.00               39            0.47              0.64        192.34                57.21         0.572          pass              0.842             63.7                           0.500                6.76              0.645                                 ok           False                  False
   KHC           92.31               13            1.28              0.21         23.77                23.05         0.531          pass              0.406              1.6                           0.094               -3.42             -0.362            downtrend_blocked_slope           False                  False
   XEL           94.44               18            0.58              0.28         69.44                16.48         0.526          pass              0.648             52.4                           0.608               -7.55             -0.757 downtrend_blocked_slope_and_streak           False                  False
    MU           90.24               41            0.20              1.55       1079.87                50.28         0.524          pass              0.738             70.7                           0.481               10.57              1.785                                 ok           False                  False
   CEG           83.33               36            0.37              0.69        261.33                42.14         0.521          pass              0.349             11.7                           0.241               -8.86             -0.738 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925125006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925125006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925125006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925125006)

</details>
