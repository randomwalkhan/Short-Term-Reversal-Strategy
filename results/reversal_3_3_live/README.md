# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 11:20:04 EDT`
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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MNST     option         option MNST261016C00048000    140          2026-08-26         2026-08-27         1.95       1.755 -2730.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ABNB           93.75               32            0.70              0.92        187.67                62.05         0.664          pass              0.701             40.3                           0.335                0.88              0.356                      ok            True                  False
   MAR           96.30               27            0.65              1.63        357.97                33.81         0.564          pass              0.743             57.7                           0.553                1.28              0.111                      ok            True                  False
  MELI           97.22               36            0.57              7.72       1947.13                48.46         0.562          pass              0.736             35.7                           0.396                6.08              0.945                      ok            True                  False
  PCAR          100.00               14            1.56              1.41        128.62                19.19         0.534          pass              0.520             13.3                           0.284               -2.69             -0.149                      ok            True                  False
 CMCSA           94.44               18            1.42              0.27         27.08                26.47         0.515          pass              0.601             36.9                           0.523                2.43              0.471                      ok            True                  False
  BKNG           96.00               25            1.49              2.18        207.96                36.49         0.506          pass              0.667             38.7                           0.444               -3.54             -0.072                      ok            True                  False
  NFLX           83.33               18            1.98              1.13         80.98                32.24         0.506          pass              0.270             25.8                           0.470                2.06              0.502                      ok            True                  False
  MNST           71.43                7            2.19              0.73         47.50               551.93         1.000          pass              0.171             23.7                           0.529                0.18              0.335                      ok           False                  False
  INSM           88.00               25            1.63              1.42        123.78               110.38         0.799          pass              0.469             25.4                           0.444               -3.14             -0.321 downtrend_blocked_slope           False                  False
   WMT           90.91               11            1.50              1.10        103.87                39.06         0.626          pass              0.433             24.4                           0.453              -10.97             -1.323 downtrend_blocked_slope           False                  False
  MRVL           80.56               36            0.27              0.47        244.91                86.13         0.619          pass              0.485             78.2                           0.558               10.02              0.971                      ok           False                  False
  DRAM           78.38               37            0.27              0.11         56.34                86.64         0.618          pass              0.462             73.3                           0.342               -1.22             -0.296                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-27T11:20:04.659575-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:15:05.953915-04:00 early_entry_1115 early_entry_shadow  {"contract_symbol": "IDXX261016C00550000", "current_drop_pct": 0.51, "early_entry_score": 0.686, "early_reclaim_pct": 66.4, "entry_ask": 26.7, "entry_bid": 22.7, "entry_mode": "early", "entry_option_price": 24.7, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 16.19, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.686, "early_reclaim_pct": 66.4, "matched_signals": 38, "recovery_stability_score": 0.721, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T11:10:04.793952-04:00 early_entry_1110 early_entry_shadow                                                 {"contract_symbol": "INTU261016C00350000", "current_drop_pct": 0.64, "early_entry_score": 0.695, "early_reclaim_pct": 79.8, "entry_ask": 21.5, "entry_bid": 20.7, "entry_mode": "early", "entry_option_price": 21.1, "hypothetical_budget": 26394.05, "hypothetical_contracts": 12, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 792.0, "option_spread_pct": 3.79, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.575, "shadow_only": true, "success_rate": 88.89, "ticker": "INTU", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.695, "early_reclaim_pct": 79.8, "matched_signals": 36, "recovery_stability_score": 0.575, "success_rate": 88.89, "ticker": "INTU", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-27T11:05:01.915991-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:00:05.720063-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T10:55:01.790895-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "IDXX261016C00550000", "current_drop_pct": 0.56, "early_entry_score": 0.675, "early_reclaim_pct": 63.0, "entry_ask": 26.8, "entry_bid": 22.7, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 16.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.468, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.675, "early_reclaim_pct": 63.0, "matched_signals": 38, "recovery_stability_score": 0.632, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.468, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:50:01.751368-04:00 early_entry_1050 early_entry_shadow                    {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.53, "early_entry_score": 0.752, "early_reclaim_pct": 65.4, "entry_ask": 12.6, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 11.65, "hypothetical_budget": 26394.05, "hypothetical_contracts": 22, "matched_signals": 31, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 214.0, "option_spread_pct": 16.31, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.542, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.752, "early_reclaim_pct": 65.4, "matched_signals": 31, "recovery_stability_score": 0.633, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.542, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:45:02.873607-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "GEHC261002C00073000", "current_drop_pct": 0.53, "early_entry_score": 0.832, "early_reclaim_pct": 70.4, "entry_ask": 2.8, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.525, "hypothetical_budget": 26394.05, "hypothetical_contracts": 104, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 21.78, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.745, "shadow_only": true, "success_rate": 97.22, "ticker": "GEHC", "timing_score": 0.477, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.832, "early_reclaim_pct": 70.4, "matched_signals": 36, "recovery_stability_score": 0.745, "success_rate": 97.22, "ticker": "GEHC", "timing_score": 0.477, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:40:06.542712-04:00 early_entry_1040 early_entry_shadow       {"contract_symbol": "GEHC261002C00073000", "current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 67.3, "entry_ask": 2.8, "entry_bid": 2.2, "entry_mode": "early", "entry_option_price": 2.5, "hypothetical_budget": 26394.05, "hypothetical_contracts": 105, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.0, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.698, "shadow_only": true, "success_rate": 97.14, "ticker": "GEHC", "timing_score": 0.48, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.817, "early_reclaim_pct": 67.3, "matched_signals": 35, "recovery_stability_score": 0.698, "success_rate": 97.14, "ticker": "GEHC", "timing_score": 0.48, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T10:35:01.793771-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "GEHC261002C00073000", "current_drop_pct": 0.59, "early_entry_score": 0.809, "early_reclaim_pct": 66.9, "entry_ask": 2.75, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.45, "hypothetical_budget": 26394.05, "hypothetical_contracts": 107, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.49, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.652, "shadow_only": true, "success_rate": 97.06, "ticker": "GEHC", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.809, "early_reclaim_pct": 66.9, "matched_signals": 34, "recovery_stability_score": 0.652, "success_rate": 97.06, "ticker": "GEHC", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827112004)

</details>
