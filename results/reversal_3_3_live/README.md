# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 12:45:06 EDT`
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
  PYPL           94.12               34            0.51              0.19         53.95                58.07         0.618          pass              0.771             57.7                           0.704                2.32              0.025                                 ok            True                  False
  MSTR           80.00               25            3.69              3.54        135.42               103.17         0.588          pass              0.279             40.1                           0.484               -0.80              0.183                                 ok            True                  False
  TMUS           95.65               23            0.79              1.02        182.46                25.87         0.521          pass              0.645             35.4                           0.269                0.56             -0.163                                 ok            True                  False
  AAPL           87.50               24            0.97              2.25        332.11                23.75         0.502          pass              0.439             31.9                           0.365                4.11              0.309                                 ok            True                  False
  DRAM           81.08               37            0.16              0.06         54.77                66.30         0.602          pass              0.485             71.9                           0.498               -3.85              0.051                                 ok           False                  False
  AMGN           96.15               26            0.58              1.56        380.83                45.29         0.597          pass              0.755             63.0                           0.711              -11.77             -1.882 downtrend_blocked_slope_and_streak           False                  False
   WMT           84.85               33            0.46              0.35        108.93                40.03         0.566          pass              0.467             42.5                           0.393                3.53              0.235                                 ok           False                  False
    MU           87.18               39            0.00              0.02        924.02                57.16         0.561          pass              0.738             99.2                           0.563               -3.62             -0.104           downtrend_blocked_streak           False                  False
   PEP          100.00               12            0.78              0.75        136.02                16.22         0.556          pass              0.567             32.7                           0.233               -2.58             -0.256            downtrend_blocked_slope           False                  False
   EXC          100.00                6            1.16              0.35         42.57                14.63         0.552          pass              0.478              7.5                           0.225               -2.50             -0.227           downtrend_blocked_streak           False                  False
   CEG           88.24               17            1.35              2.49        263.50                42.97         0.552          pass              0.406             28.2                           0.508               -5.01             -0.504 downtrend_blocked_slope_and_streak           False                  False
  COST           90.91               11            1.44              9.24        914.95                19.80         0.544          pass              0.365              4.3                           0.231               -4.04             -0.400 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915124506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915124506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915124506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915124506)

</details>
