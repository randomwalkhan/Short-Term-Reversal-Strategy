# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 14:30:01 EDT`
Last processed slot: `manage_1430`

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
  MSTR           81.82               22            3.83              3.67        135.37               103.17         0.599          pass              0.302             37.8                           0.375               -0.94              0.176                                 ok            True                  False
  TEAM          100.00               37            0.85              1.14        192.28                63.46         0.562          pass              0.851             71.7                           0.561               -1.56             -0.268                                 ok            True                   True
  TMUS           95.65               23            0.91              1.17        182.40                25.87         0.514          pass              0.615             25.8                           0.207                0.44             -0.168                                 ok            True                  False
  MSFT          100.00               18            1.37              4.83        503.34                22.76         0.508          pass              0.540             11.9                           0.293               -1.73             -0.133                                 ok            True                  False
  AAPL           88.00               25            0.80              1.87        332.28                23.75         0.506          pass              0.495             43.6                           0.527                4.28              0.317                                 ok            True                  False
  AMGN           95.00               20            0.88              2.35        380.49                45.29         0.613          pass              0.660             44.1                           0.505              -12.04             -1.895 downtrend_blocked_slope_and_streak           False                  False
  PYPL           92.11               38            0.21              0.08         54.00                58.07         0.611          pass              0.817             82.3                           0.750                2.63              0.038                                 ok           False                  False
  DRAM           81.08               37            0.03              0.01         54.80                66.30         0.610          pass              0.556             95.3                           0.589               -3.72              0.057                                 ok           False                  False
   WMT           86.11               36            0.33              0.26        108.97                40.03         0.558          pass              0.568             58.5                           0.561                3.67              0.241                                 ok           False                  False
    MU           87.18               39            0.08              0.50        923.82                57.16         0.557          pass              0.673             77.7                           0.406               -3.69             -0.108           downtrend_blocked_streak           False                  False
  ADBE           96.30               27            1.19              2.21        264.65                49.46         0.550          pass              0.755             62.1                           0.487              -10.37             -1.343 downtrend_blocked_slope_and_streak           False                  False
   EXC           91.67               12            0.54              0.16         42.65                14.63         0.546          pass              0.550             57.0                           0.688               -1.89             -0.199           downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915143001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915143001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915143001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915143001)

</details>
