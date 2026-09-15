# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 14:00:02 EDT`
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
  MSTR           80.00               25            3.41              3.27        135.54               103.17         0.604          pass              0.294             44.6                           0.579               -0.51              0.196                                 ok            True                  False
  TEAM          100.00               37            0.80              1.08        192.31                63.46         0.565          pass              0.856             73.1                           0.469               -1.52             -0.266                                 ok            True                  False
  TMUS           95.65               23            0.89              1.14        182.41                25.87         0.515          pass              0.620             27.4                           0.224                0.46             -0.167                                 ok            True                  False
  MSFT          100.00               17            1.40              4.96        503.28                22.76         0.513          pass              0.507              3.0                           0.088               -1.77             -0.135                                 ok            True                  False
  AAPL           88.00               25            0.80              1.86        332.28                23.75         0.506          pass              0.495             43.8                           0.611                4.28              0.317                                 ok            True                  False
  PYPL           91.43               35            0.40              0.15         53.97                58.07         0.616          pass              0.734             66.9                           0.570                2.44              0.030                                 ok           False                  False
  AMGN           95.24               21            0.85              2.26        380.53                45.29         0.609          pass              0.673             46.3                           0.498              -12.00             -1.894 downtrend_blocked_slope_and_streak           False                  False
  DRAM           81.08               37            0.06              0.02         54.79                66.30         0.608          pass              0.537             89.1                           0.554               -3.75              0.056                                 ok           False                  False
   WMT           85.29               34            0.41              0.31        108.95                40.03         0.564          pass              0.506             49.4                           0.398                3.59              0.237                                 ok           False                  False
   EXC          100.00               11            0.68              0.20         42.63                14.63         0.552          pass              0.599             45.8                           0.674               -2.03             -0.205           downtrend_blocked_streak           False                  False
   PEP           87.50               16            0.43              0.41        136.17                16.22         0.542          pass              0.485             63.5                           0.713               -2.23             -0.240                                 ok           False                  False
  REGN           90.00               10            1.75              9.70        789.58                29.50         0.542          pass              0.408             29.0                           0.453               -2.40             -0.615 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-15T12:00:02.459407-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                 {"contract_symbol": "VRSK261016C00185000", "current_drop_pct": 0.81, "early_entry_score": 0.714, "early_reclaim_pct": 92.0, "entry_ask": 7.4, "entry_bid": 6.3, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 52, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.06, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.865, "shadow_only": true, "success_rate": 88.57, "ticker": "VRSK", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.714, "early_reclaim_pct": 92.0, "matched_signals": 35, "recovery_stability_score": 0.865, "success_rate": 88.57, "ticker": "VRSK", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T11:55:01.104674-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T11:50:04.267935-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T11:45:05.768336-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                {"contract_symbol": "ISRG261030C00375000", "current_drop_pct": 0.52, "early_entry_score": 0.68, "early_reclaim_pct": 78.3, "entry_ask": 23.2, "entry_bid": 19.4, "entry_mode": "early", "entry_option_price": 21.3, "hypothetical_budget": 36158.05, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 50.0, "option_spread_pct": 17.84, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.878, "shadow_only": true, "success_rate": 88.57, "ticker": "ISRG", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.68, "early_reclaim_pct": 78.3, "matched_signals": 35, "recovery_stability_score": 0.878, "success_rate": 88.57, "ticker": "ISRG", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T11:40:01.137697-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                            {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 0.81, "early_entry_score": 0.855, "early_reclaim_pct": 72.7, "entry_ask": 14.5, "entry_bid": 13.2, "entry_mode": "early", "entry_option_price": 13.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 9.39, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.727, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.855, "early_reclaim_pct": 72.7, "matched_signals": 37, "recovery_stability_score": 0.727, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:35:02.119957-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "CTSH261016C00065000", "current_drop_pct": 0.54, "early_entry_score": 0.872, "early_reclaim_pct": 84.2, "entry_ask": 2.85, "entry_bid": 2.7, "entry_mode": "early", "entry_option_price": 2.775, "hypothetical_budget": 36158.05, "hypothetical_contracts": 130, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 712.0, "option_spread_pct": 5.41, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.872, "early_reclaim_pct": 84.2, "matched_signals": 35, "recovery_stability_score": 0.627, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "matched_signals": 35, "recovery_stability_score": 0.694, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T11:30:02.213843-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                            {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.17, "early_entry_score": 0.793, "early_reclaim_pct": 60.8, "entry_ask": 14.5, "entry_bid": 13.2, "entry_mode": "early", "entry_option_price": 13.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 9.39, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.573, "top_candidates": [{"current_drop_pct": 1.17, "early_entry_score": 0.793, "early_reclaim_pct": 60.8, "matched_signals": 33, "recovery_stability_score": 0.687, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.573, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:25:01.146077-04:00 early_entry_1125 early_entry_shadow                           {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.53, "early_entry_score": 0.89, "early_reclaim_pct": 78.1, "entry_ask": 13.9, "entry_bid": 13.0, "entry_mode": "early", "entry_option_price": 13.45, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 6.69, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.628, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.89, "early_reclaim_pct": 78.1, "matched_signals": 39, "recovery_stability_score": 0.703, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.628, "trend_health_status": "ok"}, {"current_drop_pct": 1.13, "early_entry_score": 0.798, "early_reclaim_pct": 62.2, "matched_signals": 33, "recovery_stability_score": 0.762, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.576, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:20:04.224010-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                 {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.59, "early_entry_score": 0.882, "early_reclaim_pct": 75.4, "entry_ask": 13.8, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 13.325, "hypothetical_budget": 36158.05, "hypothetical_contracts": 27, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 7.13, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.624, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.882, "early_reclaim_pct": 75.4, "matched_signals": 39, "recovery_stability_score": 0.715, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.624, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:15:01.103562-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "entry_ask": 13.2, "entry_bid": 12.4, "entry_mode": "early", "entry_option_price": 12.8, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 6.25, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.805, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "matched_signals": 35, "recovery_stability_score": 0.805, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915140002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915140002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915140002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915140002)

</details>
