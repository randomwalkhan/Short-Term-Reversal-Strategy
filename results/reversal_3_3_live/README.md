# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 14:15:04 EDT`
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

- Cash: `$69,741.10`
- Equity: `$69,741.10`
- Realized PnL: `$59,741.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261009C00135000     34          2026-09-09         2026-09-10        10.85       9.765 -3689.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            2.42              2.25        131.74               104.12         0.628          pass              0.330             44.5                           0.284                5.11              0.555                                 ok            True                  False
   KHC          100.00               12            0.59              0.10         24.57                28.60         0.613          pass              0.657             60.8                           0.474                0.27             -0.095                                 ok            True                  False
   STX           85.19               27            2.44             15.15        879.43                74.71         0.528          pass              0.432             42.5                           0.690                2.11              0.518                                 ok            True                  False
   AEP           90.91               22            0.52              0.46        124.47                16.58         0.508          pass              0.599             59.2                           0.484                0.54              0.194                                 ok            True                  False
   KDP           84.00               25            1.09              0.25         31.97                29.72         0.500          pass              0.334             25.7                           0.240               -1.49              0.055                                 ok            True                  False
  WDAY           91.18               34            0.80              1.04        185.60                77.13         0.644          pass              0.670             49.3                           0.277               -3.25             -0.529 downtrend_blocked_slope_and_streak           False                  False
  AMGN          100.00                1            2.27              6.22        388.61                44.45         0.642          pass              0.491              9.0                           0.260              -13.16             -1.260 downtrend_blocked_slope_and_streak           False                  False
   EXC           92.86               14            0.47              0.14         43.64                15.30         0.562          pass              0.564             46.1                           0.576               -1.19              0.014                                 ok           False                  False
   TRI           97.06               34            0.51              0.35         96.83                52.79         0.552          pass              0.687             23.8                           0.137               -5.82             -0.734 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               15            1.40              7.94        804.25                27.92         0.533          pass              0.584             32.4                           0.305               -2.27              0.036           downtrend_blocked_streak           False                  False
  INTU           97.06               34            0.72              1.57        313.27                48.73         0.530          pass              0.750             45.7                           0.253               -9.88             -1.305 downtrend_blocked_slope_and_streak           False                  False
    ZS           96.43               28            2.09              2.43        165.06                64.27         0.529          pass              0.605             10.9                           0.092               -4.51             -1.190            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-10T12:00:03.311742-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:55:04.274439-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "entry_ask": 5.8, "entry_bid": 4.7, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 20.95, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "matched_signals": 37, "recovery_stability_score": 0.651, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:50:01.152194-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "entry_ask": 5.7, "entry_bid": 4.8, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 17.14, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "matched_signals": 41, "recovery_stability_score": 0.674, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.67, "early_reclaim_pct": 66.3, "matched_signals": 32, "recovery_stability_score": 0.576, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:45:04.259583-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "entry_ask": 5.9, "entry_bid": 4.4, "entry_mode": "early", "entry_option_price": 5.15, "hypothetical_budget": 34870.55, "hypothetical_contracts": 67, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 29.13, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:40:01.104202-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                       {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "entry_ask": 5.8, "entry_bid": 5.2, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 10.91, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:35:01.128582-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:30:05.235557-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "entry_ask": 6.0, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.39, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.653, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "matched_signals": 37, "recovery_stability_score": 0.653, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:25:01.128031-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "entry_ask": 5.8, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.45, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.84, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "matched_signals": 37, "recovery_stability_score": 0.629, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:20:01.183708-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                        {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "entry_ask": 5.7, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 5.35, "hypothetical_budget": 34870.55, "hypothetical_contracts": 65, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.08, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.687, "early_reclaim_pct": 73.3, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:15:01.146533-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                         {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "entry_ask": 6.2, "entry_bid": 5.4, "entry_mode": "early", "entry_option_price": 5.8, "hypothetical_budget": 34870.55, "hypothetical_contracts": 60, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 13.79, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.705, "early_reclaim_pct": 74.7, "matched_signals": 38, "recovery_stability_score": 0.61, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910141504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910141504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910141504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910141504)

</details>
