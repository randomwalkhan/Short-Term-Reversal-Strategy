# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 10:55:03 EDT`
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

- Cash: `$76,116.10`
- Equity: `$76,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           92.31               13            0.61              0.10         24.56                26.10         0.580            pass              0.469             21.1                           0.229               -3.34             -0.463            downtrend_blocked_slope           False                  False
  SNPS           62.50                8            2.93              8.16        393.88                60.55         0.577            pass              0.058              0.3                           0.157              -12.85             -1.268            downtrend_blocked_slope           False                  False
   EXC          100.00               10            0.87              0.26         43.05                14.68         0.547            pass              0.502             15.7                           0.254               -1.68             -0.088           downtrend_blocked_streak           False                  False
  CHTR           90.48               42            0.40              0.41        145.59                68.13         0.544            pass              0.792             86.2                           0.651               -5.49             -0.873            downtrend_blocked_slope           False                  False
 CMCSA           96.00               25            0.97              0.17         25.13                34.99         0.528            pass              0.553              0.0                           0.208               -7.78             -0.855 downtrend_blocked_slope_and_streak           False                  False
   AEP           66.67                6            1.24              1.07        122.87                16.49         0.522            pass              0.062              3.2                           0.117               -0.42              0.040                                 ok           False                  False
  NVDA           80.00                5            3.58              5.47        215.95                43.68         0.515            pass              0.101             16.6                           0.320               -3.14             -0.185           downtrend_blocked_streak           False                  False
  UPRO           91.67               12            2.45              2.53        146.93                26.03         0.499 below_threshold              0.382              2.4                           0.199               -4.86             -0.381 downtrend_blocked_slope_and_streak           False                  False
   CSX           78.95               19            0.73              0.25         48.84                18.07         0.494 below_threshold              0.255             48.6                           0.353               -4.98             -0.337            downtrend_blocked_slope           False                  False
  CDNS           75.00               24            1.65              3.35        287.94                43.36         0.492 below_threshold              0.261             39.5                           0.701              -16.39             -1.843 downtrend_blocked_slope_and_streak           False                  False
  MELI           97.44               39            0.30              4.01       1895.65                37.25         0.488 below_threshold              0.862             73.2                           0.742               -3.79             -0.482 downtrend_blocked_slope_and_streak           False                  False
  ABNB           94.12               34            0.45              0.54        169.96                31.21         0.482 below_threshold              0.735             50.0                           0.433              -10.56             -1.203 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-14T10:55:03.263135-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.722, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:50:05.324545-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.724, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "matched_signals": 35, "recovery_stability_score": 0.724, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:45:01.220656-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T10:40:02.381036-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.65, "early_entry_score": 0.828, "early_reclaim_pct": 73.1, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.828, "early_reclaim_pct": 73.1, "matched_signals": 35, "recovery_stability_score": 0.748, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:35:03.129508-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:30:01.152638-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.771, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "matched_signals": 34, "recovery_stability_score": 0.771, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:25:02.232009-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "matched_signals": 35, "recovery_stability_score": 0.789, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:20:02.245642-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.54, "early_entry_score": 0.848, "early_reclaim_pct": 77.7, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.792, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.848, "early_reclaim_pct": 77.7, "matched_signals": 36, "recovery_stability_score": 0.792, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:15:01.117814-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.67, "early_entry_score": 0.825, "early_reclaim_pct": 72.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.743, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.825, "early_reclaim_pct": 72.3, "matched_signals": 35, "recovery_stability_score": 0.743, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:10:06.027535-04:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.87, "early_entry_score": 0.774, "early_reclaim_pct": 64.0, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.68, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.424, "top_candidates": [{"current_drop_pct": 0.87, "early_entry_score": 0.774, "early_reclaim_pct": 64.0, "matched_signals": 31, "recovery_stability_score": 0.68, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.424, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914105503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914105503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914105503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914105503)

</details>
