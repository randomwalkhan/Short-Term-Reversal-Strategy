# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 11:40:01 EDT`
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

- Cash: `$32,694.50`
- Equity: `$32,694.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  INTC     option         option INTC260918C00100000     15          2026-08-06         2026-08-07       11.175     10.0575 -1676.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           94.12               34            0.64              0.27         59.66                59.52         0.648            pass              0.679             25.7                           0.292                5.78              0.479                                 ok            True                  False
  TMUS           92.59               27            1.01              1.27        179.42                57.01         0.627            pass              0.644             44.2                           0.314               -1.08             -0.154                                 ok            True                  False
  PCAR           96.88               32            0.51              0.48        131.86                29.35         0.513            pass              0.721             40.9                           0.232               -0.65             -0.149                                 ok            True                  False
  INSM           61.54               13            3.08              2.86        131.33               110.04         0.717            pass              0.106              4.7                           0.155               20.15              1.448                                 ok           False                  False
    MU           79.41               34            0.92              5.68        879.04               110.38         0.658            pass              0.455             76.4                           0.875               -5.17              0.209                                 ok           False                  False
  ALNY           88.37               43            0.33              0.50        215.90               128.30         0.621            pass              0.747             87.2                           0.629              -20.74             -3.036            downtrend_blocked_slope           False                  False
  DRAM           78.12               32            2.26              0.82         51.09               108.98         0.607            pass              0.376             56.3                           0.803               -5.50              0.341                                 ok           False                  False
   CSX           93.10               29            0.42              0.15         50.64                29.04         0.536            pass              0.729             66.4                           0.699               -5.16             -0.300 downtrend_blocked_slope_and_streak           False                  False
   MAR           93.75               32            0.55              1.39        359.08                38.09         0.521            pass              0.738             57.6                           0.420               -4.47             -0.852 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.77               31            0.44              0.83        273.15                34.67         0.514            pass              0.847             85.2                           0.503                8.89              0.704                                 ok           False                  False
 GOOGL           80.43               46            0.31              0.77        357.42                51.28         0.501            pass              0.479             72.3                           0.685               11.54              1.365                                 ok           False                  False
  GOOG           83.33               48            0.26              0.66        356.34                50.46         0.500 below_threshold              0.559             73.3                           0.677               11.47              1.333                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-08-07T11:40:01.565358-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.0, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.648, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.0, "matched_signals": 37, "recovery_stability_score": 0.648, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:35:06.439574-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.66, "early_entry_score": 0.705, "early_reclaim_pct": 82.7, "entry_ask": 4.1, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.9, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 10.26, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.705, "early_reclaim_pct": 82.7, "matched_signals": 36, "recovery_stability_score": 0.658, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:30:01.519424-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.69, "early_entry_score": 0.703, "early_reclaim_pct": 82.1, "entry_ask": 4.1, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.9, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 10.26, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.703, "early_reclaim_pct": 82.1, "matched_signals": 36, "recovery_stability_score": 0.58, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:25:01.515249-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:20:02.542614-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:15:01.509027-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:10:02.535508-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.6, "early_entry_score": 0.724, "early_reclaim_pct": 84.3, "entry_ask": 4.1, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 7.59, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.611, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.724, "early_reclaim_pct": 84.3, "matched_signals": 37, "recovery_stability_score": 0.611, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}, {"current_drop_pct": 0.52, "early_entry_score": 0.67, "early_reclaim_pct": 71.5, "matched_signals": 35, "recovery_stability_score": 0.675, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:05:03.367045-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.68, "early_entry_score": 0.704, "early_reclaim_pct": 82.3, "entry_ask": 4.1, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 7.59, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.704, "early_reclaim_pct": 82.3, "matched_signals": 36, "recovery_stability_score": 0.617, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:00:05.487197-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:55:05.454765-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807114001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807114001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807114001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807114001)

</details>
