# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 11:35:05 EDT`
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
   AEP           80.00               10            0.99              0.85        122.97                16.49         0.530            pass              0.123             23.4                           0.365               -0.16              0.052                                 ok            True                  False
  SNPS           69.23               13            2.57              7.15        394.31                60.55         0.576            pass              0.115             12.6                           0.338              -12.53             -1.251            downtrend_blocked_slope           False                  False
   KHC           90.00               10            1.00              0.17         24.53                26.10         0.567            pass              0.386             21.0                           0.276               -3.72             -0.480            downtrend_blocked_slope           False                  False
  CHTR           90.48               42            0.09              0.09        145.73                68.13         0.562            pass              0.826             96.9                           0.652               -5.19             -0.859            downtrend_blocked_slope           False                  False
   EXC          100.00                6            1.26              0.38         43.00                14.68         0.546            pass              0.455              0.0                           0.190               -2.07             -0.106           downtrend_blocked_streak           False                  False
 CMCSA           96.55               29            0.56              0.10         25.16                34.99         0.528            pass              0.729             50.0                           0.368               -7.39             -0.836 downtrend_blocked_slope_and_streak           False                  False
  NVDA           90.91               11            2.94              4.49        216.37                43.68         0.528            pass              0.445             31.5                           0.672               -2.50             -0.154           downtrend_blocked_streak           False                  False
   CSX           78.57               14            0.92              0.32         48.82                18.07         0.512            pass              0.182             34.8                           0.266               -5.16             -0.346            downtrend_blocked_slope           False                  False
  UPRO           90.48               21            1.40              1.45        147.40                26.03         0.504            pass              0.536             44.2                           0.705               -3.84             -0.333 downtrend_blocked_slope_and_streak           False                  False
  CDNS           70.00               20            2.05              4.16        287.59                43.36         0.486 below_threshold              0.190             24.8                           0.294              -16.73             -1.862 downtrend_blocked_slope_and_streak           False                  False
  ABNB           94.44               36            0.30              0.36        170.04                31.21         0.480 below_threshold              0.806             66.6                           0.462              -10.43             -1.196 downtrend_blocked_slope_and_streak           False                  False
   STX           87.88               33            1.67              9.69        826.02                70.14         0.480 below_threshold              0.645             77.9                           0.917               -1.62              0.361           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-14T11:35:05.164573-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:30:05.695481-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:25:05.217490-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:20:05.740603-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.83, "early_entry_score": 0.779, "early_reclaim_pct": 65.5, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.779, "early_reclaim_pct": 65.5, "matched_signals": 31, "recovery_stability_score": 0.551, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:15:01.136676-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.598, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.803, "early_reclaim_pct": 69.3, "matched_signals": 33, "recovery_stability_score": 0.598, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.712, "early_reclaim_pct": 84.2, "matched_signals": 36, "recovery_stability_score": 0.754, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:10:05.058091-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                   {"contract_symbol": "ALNY261016C00250000", "current_drop_pct": 0.53, "early_entry_score": 0.731, "early_reclaim_pct": 85.9, "entry_ask": 12.3, "entry_bid": 11.1, "entry_mode": "early", "entry_option_price": 11.7, "hypothetical_budget": 38058.05, "hypothetical_contracts": 32, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 838.0, "option_spread_pct": 10.26, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 89.19, "ticker": "ALNY", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.731, "early_reclaim_pct": 85.9, "matched_signals": 37, "recovery_stability_score": 0.736, "success_rate": 89.19, "ticker": "ALNY", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:05:02.179238-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-14T11:00:03.361025-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.72, "early_entry_score": 0.812, "early_reclaim_pct": 70.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.812, "early_reclaim_pct": 70.3, "matched_signals": 34, "recovery_stability_score": 0.663, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:55:03.263135-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.844, "early_reclaim_pct": 76.4, "matched_signals": 36, "recovery_stability_score": 0.722, "success_rate": 97.22, "ticker": "PCAR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T10:50:05.324545-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.724, "shadow_only": true, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.831, "early_reclaim_pct": 74.3, "matched_signals": 35, "recovery_stability_score": 0.724, "success_rate": 97.14, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914113505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914113505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914113505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914113505)

</details>
