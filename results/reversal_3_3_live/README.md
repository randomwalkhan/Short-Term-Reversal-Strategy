# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 11:45:05 EDT`
Last processed slot: `early_entry_1145`

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

- Cash: `$72,316.10`
- Equity: `$72,316.10`
- Realized PnL: `$62,316.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-15)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   EXC     option         option EXC261016C00043000    400          2026-09-14         2026-09-15         0.95       0.855 -3800.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           93.75               32            0.63              0.24         53.93                58.07         0.622          pass              0.719             47.7                           0.470                2.20              0.019                                 ok            True                  False
  MSTR           80.77               26            3.25              3.11        135.61               103.17         0.608          pass              0.330             47.3                           0.751               -0.33              0.204                                 ok            True                  False
   PEP           87.50               16            0.51              0.48        136.13                16.22         0.536          pass              0.463             56.6                           0.655               -2.31             -0.243                                 ok            True                  False
  TMUS           96.00               25            0.66              0.84        182.54                25.87         0.518          pass              0.691             46.5                           0.314                0.70             -0.156                                 ok            True                  False
  AAPL           87.50               24            0.93              2.17        332.15                23.75         0.504          pass              0.447             34.6                           0.376                4.15              0.311                                 ok            True                  False
   CSX           80.00               20            0.55              0.19         48.83                18.06         0.502          pass              0.298             60.3                           0.650               -3.70             -0.157                                 ok            True                  False
  AMGN           95.00               20            0.90              2.42        380.46                45.29         0.611          pass              0.656             42.6                           0.691              -12.06             -1.896 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.98               47            0.02              0.06        373.91                81.04         0.606          pass              0.636             98.7                           0.723               -2.17              0.076                                 ok           False                  False
  TEAM          100.00               37            0.47              0.63        192.50                63.46         0.591          pass              0.892             84.4                           0.817               -1.18             -0.250                                 ok           False                  False
   WMT           85.29               34            0.38              0.29        108.96                40.03         0.566          pass              0.518             53.4                           0.348                3.62              0.239                                 ok           False                  False
  SNPS           66.67                9            2.99              7.99        378.01                61.31         0.554          pass              0.093             12.4                           0.403              -15.83             -1.300            downtrend_blocked_slope           False                  False
   EXC          100.00                9            0.91              0.27         42.60                14.63         0.550          pass              0.506             17.0                           0.253               -2.26             -0.216           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-15T11:45:05.768336-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                {"contract_symbol": "ISRG261030C00375000", "current_drop_pct": 0.52, "early_entry_score": 0.68, "early_reclaim_pct": 78.3, "entry_ask": 23.2, "entry_bid": 19.4, "entry_mode": "early", "entry_option_price": 21.3, "hypothetical_budget": 36158.05, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 50.0, "option_spread_pct": 17.84, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.878, "shadow_only": true, "success_rate": 88.57, "ticker": "ISRG", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.68, "early_reclaim_pct": 78.3, "matched_signals": 35, "recovery_stability_score": 0.878, "success_rate": 88.57, "ticker": "ISRG", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T11:40:01.137697-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                            {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 0.81, "early_entry_score": 0.855, "early_reclaim_pct": 72.7, "entry_ask": 14.5, "entry_bid": 13.2, "entry_mode": "early", "entry_option_price": 13.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 9.39, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.727, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.855, "early_reclaim_pct": 72.7, "matched_signals": 37, "recovery_stability_score": 0.727, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:35:02.119957-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "CTSH261016C00065000", "current_drop_pct": 0.54, "early_entry_score": 0.872, "early_reclaim_pct": 84.2, "entry_ask": 2.85, "entry_bid": 2.7, "entry_mode": "early", "entry_option_price": 2.775, "hypothetical_budget": 36158.05, "hypothetical_contracts": 130, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 712.0, "option_spread_pct": 5.41, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.872, "early_reclaim_pct": 84.2, "matched_signals": 35, "recovery_stability_score": 0.627, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "matched_signals": 35, "recovery_stability_score": 0.694, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T11:30:02.213843-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                            {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.17, "early_entry_score": 0.793, "early_reclaim_pct": 60.8, "entry_ask": 14.5, "entry_bid": 13.2, "entry_mode": "early", "entry_option_price": 13.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 9.39, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.573, "top_candidates": [{"current_drop_pct": 1.17, "early_entry_score": 0.793, "early_reclaim_pct": 60.8, "matched_signals": 33, "recovery_stability_score": 0.687, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.573, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:25:01.146077-04:00 early_entry_1125 early_entry_shadow                           {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.53, "early_entry_score": 0.89, "early_reclaim_pct": 78.1, "entry_ask": 13.9, "entry_bid": 13.0, "entry_mode": "early", "entry_option_price": 13.45, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 6.69, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.628, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.89, "early_reclaim_pct": 78.1, "matched_signals": 39, "recovery_stability_score": 0.703, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.628, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.798, "early_reclaim_pct": 62.2, "matched_signals": 33, "recovery_stability_score": 0.762, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.576, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:20:04.224010-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                 {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.59, "early_entry_score": 0.882, "early_reclaim_pct": 75.4, "entry_ask": 13.8, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 13.325, "hypothetical_budget": 36158.05, "hypothetical_contracts": 27, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 7.13, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.624, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.882, "early_reclaim_pct": 75.4, "matched_signals": 39, "recovery_stability_score": 0.715, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.624, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:15:01.103562-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "entry_ask": 13.2, "entry_bid": 12.4, "entry_mode": "early", "entry_option_price": 12.8, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 6.25, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.805, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "matched_signals": 35, "recovery_stability_score": 0.805, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:10:01.228919-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                              {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.02, "early_entry_score": 0.821, "early_reclaim_pct": 65.8, "entry_ask": 13.4, "entry_bid": 12.3, "entry_mode": "early", "entry_option_price": 12.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 8.56, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.775, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.57, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.821, "early_reclaim_pct": 65.8, "matched_signals": 35, "recovery_stability_score": 0.775, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.57, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:05:02.271330-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                             {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.16, "early_entry_score": 0.795, "early_reclaim_pct": 61.3, "entry_ask": 13.1, "entry_bid": 12.1, "entry_mode": "early", "entry_option_price": 12.6, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 7.94, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.708, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.574, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.795, "early_reclaim_pct": 61.3, "matched_signals": 33, "recovery_stability_score": 0.708, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.574, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:00:05.317059-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                             {"contract_symbol": "GILD261016C00150000", "current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "entry_ask": 3.1, "entry_bid": 2.74, "entry_mode": "early", "entry_option_price": 2.92, "hypothetical_budget": 36158.05, "hypothetical_contracts": 123, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 529.0, "option_spread_pct": 12.33, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.576, "shadow_only": true, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "matched_signals": 37, "recovery_stability_score": 0.576, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915114505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915114505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915114505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915114505)

</details>
