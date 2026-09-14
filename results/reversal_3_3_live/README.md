# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 11:05:02 EDT`
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
   AEP           84.62               13            0.89              0.77        123.00                16.49         0.523            pass              0.288             30.9                           0.310               -0.06              0.056                                 ok            True                  False
   KHC           94.74               19            0.12              0.02         24.59                26.10         0.578            pass              0.763             84.2                           0.514               -2.87             -0.440            downtrend_blocked_slope           False                  False
  SNPS           69.23               13            2.56              7.13        394.33                60.55         0.577            pass              0.116             12.9                           0.225              -12.52             -1.251            downtrend_blocked_slope           False                  False
  CHTR           90.48               42            0.20              0.21        145.68                68.13         0.555            pass              0.814             93.0                           0.682               -5.30             -0.864            downtrend_blocked_slope           False                  False
   EXC          100.00               10            0.78              0.23         43.06                14.68         0.552            pass              0.534             26.4                           0.307               -1.59             -0.084           downtrend_blocked_streak           False                  False
 CMCSA           96.55               29            0.58              0.10         25.16                34.99         0.527            pass              0.724             48.2                           0.361               -7.41             -0.837 downtrend_blocked_slope_and_streak           False                  False
  NVDA           83.33                6            3.40              5.20        216.06                43.68         0.523            pass              0.203             20.7                           0.420               -2.96             -0.176           downtrend_blocked_streak           False                  False
  UPRO           92.86               14            1.98              2.05        147.14                26.03         0.515            pass              0.484             21.0                           0.410               -4.41             -0.360 downtrend_blocked_slope_and_streak           False                  False
   CSX           81.25               16            0.84              0.29         48.83                18.07         0.508            pass              0.246             40.6                           0.279               -5.08             -0.343            downtrend_blocked_slope           False                  False
  ABNB           93.75               32            0.61              0.72        169.88                31.21         0.485 below_threshold              0.661             33.1                           0.259              -10.70             -1.209 downtrend_blocked_slope_and_streak           False                  False
  CDNS           73.68               19            2.27              4.59        287.40                43.36         0.483 below_threshold              0.159             17.0                           0.385              -16.92             -1.872 downtrend_blocked_slope_and_streak           False                  False
   LIN           75.00               20            0.71              2.33        465.22                15.11         0.478 below_threshold              0.209             31.6                           0.392               -5.13             -0.640 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-14T11:05:02.179238-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:00:03.361025-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.72, "early_entry_score": 0.812, "early_reclaim_pct": 70.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.812, "early_reclaim_pct": 70.3, "matched_signals": 34, "recovery_stability_score": 0.663, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:55:03.263135-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.722, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:50:05.324545-04:00 early_entry_1050 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.724, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "matched_signals": 35, "recovery_stability_score": 0.724, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:45:01.220656-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T10:40:02.381036-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.65, "early_entry_score": 0.828, "early_reclaim_pct": 73.1, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.828, "early_reclaim_pct": 73.1, "matched_signals": 35, "recovery_stability_score": 0.748, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:35:03.129508-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.786, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.845, "early_reclaim_pct": 76.9, "matched_signals": 36, "recovery_stability_score": 0.786, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.414, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:30:01.152638-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.771, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.818, "early_reclaim_pct": 72.0, "matched_signals": 34, "recovery_stability_score": 0.771, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:25:02.232009-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "matched_signals": 35, "recovery_stability_score": 0.789, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:20:02.245642-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.54, "early_entry_score": 0.848, "early_reclaim_pct": 77.7, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.792, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.848, "early_reclaim_pct": 77.7, "matched_signals": 36, "recovery_stability_score": 0.792, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914110502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914110502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914110502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914110502)

</details>
