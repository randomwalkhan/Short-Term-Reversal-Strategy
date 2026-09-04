# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 11:05:01 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$81,160.60`
- Equity: `$81,160.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-04)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261016C00110000     99          2026-09-03         2026-09-04        3.725         4.4 6682.5   18.120805 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN          100.00               11            1.41              4.38        442.24                21.54         0.554          pass              0.556             31.4                           0.271               -0.33             -0.033                                 ok            True                  False
   WMT           83.33               30            0.78              0.60        108.16                40.07         0.548          pass              0.306              9.6                           0.171                3.73              0.297                                 ok            True                  False
  PAYX          100.00               11            1.77              1.55        124.42                25.54         0.544          pass              0.568             35.6                           0.321               -1.29             -0.091                                 ok            True                  False
  MELI          100.00               33            0.68              9.50       1986.99                45.76         0.543          pass              0.745             45.9                           0.305                2.85              0.235                                 ok            True                  False
 CMCSA           92.00               25            0.92              0.17         26.58                25.91         0.514          pass              0.499              9.3                           0.283               -1.66             -0.209                                 ok            True                  False
  REGN          100.00               21            1.13              6.68        840.61                28.19         0.513          pass              0.559             11.6                           0.179               -0.01              0.135                                 ok            True                  False
    ZS          100.00               10            4.00              4.98        175.67                62.66         0.511          pass              0.584             44.2                           0.445               -6.08             -0.091                                 ok            True                  False
  WDAY           82.35               17            3.96              5.74        204.46                73.93         0.511          pass              0.237             25.3                           0.268               -0.64              0.288                                 ok            True                  False
  VRTX           96.00               25            1.26              4.93        555.85                32.02         0.510          pass              0.741             63.5                           0.381                0.52              0.107                                 ok            True                  False
  UPRO           88.24               17            1.50              1.62        153.04                24.72         0.509          pass              0.344              9.1                           0.155                1.03              0.105                                 ok            True                  False
  CHTR           90.24               41            0.83              0.88        151.00                61.35         0.507          pass              0.584             20.1                           0.279               -0.03              0.023                                 ok            True                  False
  MNST           86.11               36            0.32              0.10         44.04               424.09         0.998          pass              0.638             67.4                           0.648               -8.06             -1.139 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-04T11:05:01.496232-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T11:00:05.474387-04:00 early_entry_1100 early_entry_shadow                  {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.53, "early_entry_score": 0.682, "early_reclaim_pct": 63.4, "entry_ask": 17.5, "entry_bid": 15.2, "entry_mode": "early", "entry_option_price": 16.35, "hypothetical_budget": 40580.3, "hypothetical_contracts": 24, "matched_signals": 33, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 158.0, "option_spread_pct": 14.07, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.568, "shadow_only": true, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.475, "top_candidates": [{"current_drop_pct": 1.53, "early_entry_score": 0.682, "early_reclaim_pct": 63.4, "matched_signals": 33, "recovery_stability_score": 0.568, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:55:01.387671-04:00 early_entry_1055 early_entry_shadow                    {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.34, "early_entry_score": 0.71, "early_reclaim_pct": 68.1, "entry_ask": 17.5, "entry_bid": 15.2, "entry_mode": "early", "entry_option_price": 16.35, "hypothetical_budget": 40580.3, "hypothetical_contracts": 24, "matched_signals": 34, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 158.0, "option_spread_pct": 14.07, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 91.18, "ticker": "TEAM", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 1.34, "early_entry_score": 0.71, "early_reclaim_pct": 68.1, "matched_signals": 34, "recovery_stability_score": 0.633, "success_rate": 91.18, "ticker": "TEAM", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:50:01.475605-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 1.03, "early_entry_score": 0.759, "early_reclaim_pct": 75.4, "entry_ask": 15.1, "entry_bid": 12.2, "entry_mode": "early", "entry_option_price": 13.65, "hypothetical_budget": 40580.3, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 21.25, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.725, "shadow_only": true, "success_rate": 91.67, "ticker": "TEAM", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 1.03, "early_entry_score": 0.759, "early_reclaim_pct": 75.4, "matched_signals": 36, "recovery_stability_score": 0.725, "success_rate": 91.67, "ticker": "TEAM", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:45:05.638849-04:00 early_entry_1045 early_entry_shadow    {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 1.1, "early_entry_score": 0.741, "early_reclaim_pct": 73.6, "entry_ask": 15.1, "entry_bid": 12.1, "entry_mode": "early", "entry_option_price": 13.6, "hypothetical_budget": 40580.3, "hypothetical_contracts": 29, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 22.06, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 91.43, "ticker": "TEAM", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 1.1, "early_entry_score": 0.741, "early_reclaim_pct": 73.6, "matched_signals": 35, "recovery_stability_score": 0.777, "success_rate": 91.43, "ticker": "TEAM", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:40:01.177649-04:00 early_entry_1040 early_entry_shadow   {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 0.77, "early_entry_score": 0.803, "early_reclaim_pct": 81.6, "entry_ask": 15.3, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 13.6, "hypothetical_budget": 40580.3, "hypothetical_contracts": 29, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 25.0, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.893, "shadow_only": true, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.803, "early_reclaim_pct": 81.6, "matched_signals": 38, "recovery_stability_score": 0.893, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:35:02.277988-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 1.06, "early_entry_score": 0.757, "early_reclaim_pct": 74.6, "entry_ask": 14.4, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.95, "hypothetical_budget": 40580.3, "hypothetical_contracts": 31, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 22.39, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.895, "shadow_only": true, "success_rate": 91.67, "ticker": "TEAM", "timing_score": 0.485, "top_candidates": [{"current_drop_pct": 1.06, "early_entry_score": 0.757, "early_reclaim_pct": 74.6, "matched_signals": 36, "recovery_stability_score": 0.895, "success_rate": 91.67, "ticker": "TEAM", "timing_score": 0.485, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:30:01.189639-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 82.8, "entry_ask": 13.9, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 12.55, "hypothetical_budget": 40580.3, "hypothetical_contracts": 32, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 21.51, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.942, "shadow_only": true, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.494, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 82.8, "matched_signals": 38, "recovery_stability_score": 0.942, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.494, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:25:02.305265-04:00 early_entry_1025 early_entry_shadow   {"contract_symbol": "TEAM261016C00195000", "current_drop_pct": 0.79, "early_entry_score": 0.802, "early_reclaim_pct": 81.2, "entry_ask": 13.7, "entry_bid": 11.2, "entry_mode": "early", "entry_option_price": 12.45, "hypothetical_budget": 40580.3, "hypothetical_contracts": 32, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 76.0, "option_spread_pct": 20.08, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.924, "shadow_only": true, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.802, "early_reclaim_pct": 81.2, "matched_signals": 38, "recovery_stability_score": 0.924, "success_rate": 92.11, "ticker": "TEAM", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T10:20:02.325434-04:00 early_entry_1020 early_entry_shadow                                {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.56, "early_entry_score": 0.68, "early_reclaim_pct": 62.8, "entry_ask": 16.5, "entry_bid": 14.4, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 40580.3, "hypothetical_contracts": 26, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 158.0, "option_spread_pct": 13.59, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.831, "shadow_only": true, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 1.56, "early_entry_score": 0.68, "early_reclaim_pct": 62.8, "matched_signals": 33, "recovery_stability_score": 0.831, "success_rate": 90.91, "ticker": "TEAM", "timing_score": 0.474, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904110501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904110501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904110501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904110501)

</details>
