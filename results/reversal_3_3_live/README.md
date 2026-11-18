# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 11:50:04 EST`
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

- Cash: `$105,918.80`
- Equity: `$105,918.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP261218C00400000     17          2026-11-17         2026-11-18         31.3       28.17 -5321.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   APP           90.91               44            0.82              2.28        397.96               121.47         0.760            pass              0.736             56.3                           0.483               45.61              2.275                       ok            True                  False
   ADI           87.50               24            1.34              3.59        382.13                67.50         0.628            pass              0.398             13.9                           0.223               -6.82              0.095                       ok            True                  False
   BKR           84.00               25            0.90              0.30         47.33                58.51         0.627            pass              0.335             22.0                           0.290               -5.24             -0.047                       ok            True                  False
   TXN           84.62               13            1.90              3.94        294.17                59.80         0.622            pass              0.234              9.7                           0.223               -6.83              0.147                       ok            True                  False
  VRSK           80.95               21            1.64              2.35        204.30                46.89         0.562            pass              0.261             35.4                           0.545                2.07              0.167                       ok            True                  False
   WMT           85.00               20            0.93              0.83        127.17                25.55         0.540            pass              0.410             51.8                           0.505               -2.19             -0.005                       ok            True                  False
   CEG           90.91               33            1.28              2.39        267.04                61.66         0.536            pass              0.630             44.1                           0.403                7.87              1.125                       ok            True                  False
  META           83.33               30            0.82              3.54        617.35                41.87         0.534            pass              0.398             41.0                           0.462               -2.57              0.011                       ok            True                  False
   ADP           90.32               31            0.51              1.09        307.82                28.72         0.524            pass              0.644             58.7                           0.656                1.05              0.204                       ok            True                  False
   LIN           86.36               22            0.87              3.14        513.77                18.95         0.500 below_threshold              0.411             37.0                           0.562               -2.69             -0.103                       ok            True                  False
  SOXL           61.54               26            3.22              1.11         48.60               265.73         0.920            pass              0.314             38.5                           0.229              -28.78             -0.508  downtrend_blocked_slope           False                  False
  INTC           67.86               28            2.14              0.83         54.82               143.31         0.808            pass              0.296             31.8                           0.314               -7.35             -0.133 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          detail
2026-11-18T11:50:04.203803-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                 {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "entry_ask": 6.3, "entry_bid": 5.7, "entry_mode": "early", "entry_option_price": 6.0, "hypothetical_budget": 52959.4, "hypothetical_contracts": 88, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 10.0, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "matched_signals": 39, "recovery_stability_score": 0.7, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:45:05.124213-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "entry_ask": 6.1, "entry_bid": 5.6, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 52959.4, "hypothetical_contracts": 90, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 8.55, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "matched_signals": 39, "recovery_stability_score": 0.694, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:40:04.319584-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:35:02.338548-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "APP261218C00400000", "current_drop_pct": 0.53, "early_entry_score": 0.793, "early_reclaim_pct": 71.7, "entry_ask": 26.4, "entry_bid": 25.2, "entry_mode": "early", "entry_option_price": 25.8, "hypothetical_budget": 52959.4, "hypothetical_contracts": 20, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1251.0, "option_spread_pct": 4.65, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 91.3, "ticker": "APP", "timing_score": 0.764, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.793, "early_reclaim_pct": 71.7, "matched_signals": 46, "recovery_stability_score": 0.559, "success_rate": 91.3, "ticker": "APP", "timing_score": 0.764, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:30:05.127022-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:25:05.812808-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:20:05.157588-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:15:04.160916-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:10:06.093723-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "APP261218C00400000", "current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "entry_ask": 27.1, "entry_bid": 25.2, "entry_mode": "early", "entry_option_price": 26.15, "hypothetical_budget": 52959.4, "hypothetical_contracts": 20, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 1251.0, "option_spread_pct": 7.27, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "matched_signals": 44, "recovery_stability_score": 0.563, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:05:06.391620-05:00 early_entry_1105 early_entry_shadow {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "entry_ask": 22.2, "entry_bid": 21.85, "entry_mode": "early", "entry_option_price": 22.025, "hypothetical_budget": 52959.4, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 1.59, "option_volume": 159.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "matched_signals": 32, "recovery_stability_score": 0.634, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.767, "early_reclaim_pct": 71.4, "matched_signals": 37, "recovery_stability_score": 0.606, "success_rate": 91.89, "ticker": "CEG", "timing_score": 0.552, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118115004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118115004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118115004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118115004)

</details>
