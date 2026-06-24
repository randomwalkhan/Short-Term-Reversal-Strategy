# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-24 10:40:03 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$30,612.50`
- Equity: `$30,612.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               23            2.54              4.95        276.92               157.48         0.763          pass              0.716             51.1                           0.632                1.91              0.831                                 ok            True                  False
  KLAC           91.67               24            1.32              2.25        243.52                93.06         0.728          pass              0.635             52.6                           0.455               12.78              1.308                                 ok            True                  False
  ASML           96.43               28            1.26             15.73       1771.72                65.60         0.632          pass              0.743             53.4                           0.687               -1.23              0.129                                 ok            True                  False
  MCHP           93.10               29            0.83              0.54         93.03                72.77         0.630          pass              0.703             54.7                           0.668                1.12              0.564                                 ok            True                  False
  PANW           92.50               40            0.86              1.74        290.17                56.69         0.524          pass              0.773             62.5                           0.709               10.71              0.937                                 ok            True                   True
  NXPI           92.00               25            1.53              3.22        298.56                63.85         0.521          pass              0.582             36.5                           0.301               -0.69              0.325                                 ok            True                  False
   STX           96.43               28            0.95              6.87       1035.64                68.20         0.520          pass              0.842             90.0                           0.860               21.60              2.692                                 ok            True                  False
   WDC           91.30               23            2.17             10.19        666.38                96.85         0.514          pass              0.695             85.1                           0.816               26.75              3.696                                 ok            True                  False
  SOXL           93.75               32            0.00              0.00        231.42               242.24         0.965          pass              0.910            100.0                           0.920               14.75              2.507                                 ok           False                  False
  MPWR           94.12               34            0.27              2.68       1422.61                86.34         0.691          pass              0.868             87.5                           0.850               -7.31             -0.695            downtrend_blocked_slope           False                  False
  TEAM           90.91               44            0.06              0.03         81.34                80.88         0.587          pass              0.845             98.4                           0.533              -14.97             -1.662 downtrend_blocked_slope_and_streak           False                  False
   APP           88.10               42            0.42              1.37        466.43                74.04         0.564          pass              0.715             80.8                           0.796              -10.71             -0.942 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-06-24T10:40:03.313621-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "PANW260731C00290000", "current_drop_pct": 0.86, "early_entry_score": 0.773, "early_reclaim_pct": 62.5, "entry_ask": 18.8, "entry_bid": 15.35, "entry_mode": "early", "entry_option_price": 17.075, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 234.0, "option_spread_pct": 20.2, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.709, "shadow_only": true, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.524, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.773, "early_reclaim_pct": 62.5, "matched_signals": 40, "recovery_stability_score": 0.709, "success_rate": 92.5, "ticker": "PANW", "timing_score": 0.524, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:35:01.108253-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PANW260731C00290000", "current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 75.9, "entry_ask": 19.45, "entry_bid": 15.35, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "wide_spread", "option_open_interest": 234.0, "option_spread_pct": 23.56, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 92.86, "ticker": "PANW", "timing_score": 0.531, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.824, "early_reclaim_pct": 75.9, "matched_signals": 42, "recovery_stability_score": 0.68, "success_rate": 92.86, "ticker": "PANW", "timing_score": 0.531, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.811, "early_reclaim_pct": 67.2, "matched_signals": 36, "recovery_stability_score": 0.586, "success_rate": 94.44, "ticker": "CDNS", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:30:01.120180-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:25:01.196604-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                          {"contract_symbol": "LRCX260731C00370000", "current_drop_pct": 0.72, "early_entry_score": 0.874, "early_reclaim_pct": 92.7, "entry_ask": 41.0, "entry_bid": 37.95, "entry_mode": "early", "entry_option_price": 39.475, "hypothetical_budget": 15306.25, "hypothetical_contracts": 3, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 87.0, "option_spread_pct": 7.73, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 96.67, "ticker": "LRCX", "timing_score": 0.629, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.874, "early_reclaim_pct": 92.7, "matched_signals": 30, "recovery_stability_score": 0.562, "success_rate": 96.67, "ticker": "LRCX", "timing_score": 0.629, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:20:01.164945-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                            {"contract_symbol": "AMAT260724C00580000", "current_drop_pct": 0.65, "early_entry_score": 0.888, "early_reclaim_pct": 96.1, "entry_ask": 54.55, "entry_bid": 49.75, "entry_mode": "early", "entry_option_price": 52.15, "hypothetical_budget": 15306.25, "hypothetical_contracts": 2, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 65.0, "option_spread_pct": 9.2, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.599, "shadow_only": true, "success_rate": 96.88, "ticker": "AMAT", "timing_score": 0.53, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.888, "early_reclaim_pct": 96.1, "matched_signals": 32, "recovery_stability_score": 0.599, "success_rate": 96.88, "ticker": "AMAT", "timing_score": 0.53, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:15:01.116504-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:10:01.169006-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "entry_mode": "early", "error": "KLAC: no call expiries found in the 21-40 trading-day window.", "matched_signals": 33, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "matched_signals": 33, "recovery_stability_score": 0.751, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:05:01.111815-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:00:02.286958-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                  {"contract_symbol": "LRCX260724C00370000", "current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "entry_ask": 35.3, "entry_bid": 32.3, "entry_mode": "early", "entry_option_price": 33.8, "hypothetical_budget": 15306.25, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 114.0, "option_spread_pct": 8.88, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "matched_signals": 33, "recovery_stability_score": 0.655, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-24T09:20:01.109273-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260624104003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260624104003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260624104003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260624104003)

</details>
