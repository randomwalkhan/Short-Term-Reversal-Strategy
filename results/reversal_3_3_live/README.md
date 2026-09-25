# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-25 14:00:05 EDT`
Last processed slot: `manage_1400`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.71              1.94        160.78               109.71         0.716            pass              0.676             42.7                           0.483               21.28              2.825                                 ok            True                  False
  CRWD           86.11               36            1.68              3.05        258.36                96.70         0.665            pass              0.526             41.2                           0.324               22.24              2.076                                 ok            True                  False
   TRI           84.00               25            1.75              1.23         99.79                57.78         0.552            pass              0.453             63.8                           0.380                2.98             -0.150                                 ok            True                  False
  FTNT           83.33               24            2.14              2.67        177.52                58.17         0.538            pass              0.340             34.6                           0.529               10.07              1.082                                 ok            True                  False
  WDAY           94.59               37            0.50              0.67        190.70                49.78         0.529            pass              0.873             83.6                           0.483                2.67              0.237                                 ok            True                  False
  SHOP           82.61               23            1.94              1.97        144.32                62.63         0.522            pass              0.309             33.5                           0.349               10.53              1.296                                 ok            True                  False
  PANW           61.90               21            2.81              7.66        386.64                80.20         0.586            pass              0.224             30.8                           0.544               11.96              1.205                                 ok           False                  False
  TEAM          100.00               39            0.43              0.58        192.36                57.21         0.575            pass              0.852             66.9                           0.443                6.80              0.647                                 ok           False                  False
   KHC           90.91               11            1.36              0.23         23.76                23.05         0.534            pass              0.394             14.5                           0.324               -3.51             -0.366            downtrend_blocked_slope           False                  False
   XEL           95.00               20            0.38              0.19         69.48                16.48         0.527            pass              0.725             68.5                           0.716               -7.37             -0.748 downtrend_blocked_slope_and_streak           False                  False
  NFLX           78.12               32            0.84              0.42         71.54                37.57         0.506            pass              0.254             18.9                           0.226               -8.11             -1.163 downtrend_blocked_slope_and_streak           False                  False
  INTC           79.31               29            2.42              2.16        126.46                68.53         0.498 below_threshold              0.273             32.2                           0.304               20.75              2.949                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260925140005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260925140005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260925140005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260925140005)

</details>
