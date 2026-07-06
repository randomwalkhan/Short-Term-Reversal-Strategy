# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 11:30:02 EDT`
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

- Cash: `$26,504.50`
- Equity: `$26,504.50`
- Realized PnL: `$16,504.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-06)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KDP     option         option KDP260821C00033000     96          2026-07-02         2026-07-06         1.45       1.305 -1392.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  AMAT           96.67               30            0.66              2.78        601.85               110.01         0.680          pass              0.789             62.7                           0.368               -2.92              0.343                      ok            True                  False
   WBD           94.74               19            0.62              0.12         26.43                22.17         0.563          pass              0.691             60.7                           0.557                0.44             -0.083                      ok            True                  False
  MNST          100.00               17            0.91              0.62         97.33                16.38         0.541          pass              0.617             38.6                           0.468                5.88              0.583                      ok            True                  False
  GILD           90.00               10            1.88              1.73        130.53                30.05         0.535          pass              0.401             26.9                           0.425                4.07              0.418                      ok            True                  False
   ADP           91.30               23            0.96              1.62        241.58                30.79         0.522          pass              0.597             52.3                           0.716                9.86              1.120                      ok            True                  False
  FAST           90.91               11            1.77              0.60         48.34                20.75         0.510          pass              0.458             36.3                           0.651                4.03              0.573                      ok            True                  False
  BKNG           87.88               33            0.77              1.00        184.13                41.33         0.507          pass              0.582             55.9                           0.680                6.61              0.847                      ok            True                  False
   XEL          100.00                3            1.81              1.04         81.52                20.81         0.593          pass              0.489              9.8                           0.241                3.97              0.274                      ok           False                  False
   EXC           85.71                7            1.55              0.52         47.66                22.14         0.581          pass              0.220              3.3                           0.146                2.90              0.256                      ok           False                  False
   PEP           80.00                5            1.74              1.75        143.47                27.18         0.580          pass              0.094             11.9                           0.280               -0.21             -0.033                      ok           False                  False
   KHC          100.00                2            3.20              0.57         25.13                36.79         0.557          pass              0.482              8.8                           0.311                7.62              1.220                      ok           False                  False
  CPRT          100.00                6            2.57              0.54         29.78                43.39         0.552          pass              0.558             34.4                           0.588               -3.28             -0.361 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-07-06T11:30:02.309296-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "VRTX260807C00525000", "current_drop_pct": 0.59, "early_entry_score": 0.842, "early_reclaim_pct": 80.1, "entry_ask": 23.8, "entry_bid": 16.1, "entry_mode": "early", "entry_option_price": 19.95, "hypothetical_budget": 13252.25, "hypothetical_contracts": 6, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 38.6, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.848, "shadow_only": true, "success_rate": 94.44, "ticker": "VRTX", "timing_score": 0.427, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.842, "early_reclaim_pct": 80.1, "matched_signals": 36, "recovery_stability_score": 0.848, "success_rate": 94.44, "ticker": "VRTX", "timing_score": 0.427, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:25:01.367825-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "VRTX260807C00525000", "current_drop_pct": 0.73, "early_entry_score": 0.795, "early_reclaim_pct": 75.5, "entry_ask": 23.8, "entry_bid": 16.1, "entry_mode": "early", "entry_option_price": 19.95, "hypothetical_budget": 13252.25, "hypothetical_contracts": 6, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 38.6, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.824, "shadow_only": true, "success_rate": 93.94, "ticker": "VRTX", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.795, "early_reclaim_pct": 75.5, "matched_signals": 33, "recovery_stability_score": 0.824, "success_rate": 93.94, "ticker": "VRTX", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:20:05.831796-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.62, "early_entry_score": 0.784, "early_reclaim_pct": 78.0, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.784, "early_reclaim_pct": 78.0, "matched_signals": 38, "recovery_stability_score": 0.827, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:15:04.342098-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.58, "early_entry_score": 0.788, "early_reclaim_pct": 79.4, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.806, "shadow_only": true, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.408, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.788, "early_reclaim_pct": 79.4, "matched_signals": 38, "recovery_stability_score": 0.806, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.408, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:10:04.321314-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "IDXX260821C00550000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 70.5, "entry_ask": 39.6, "entry_bid": 32.3, "entry_mode": "early", "entry_option_price": 35.95, "hypothetical_budget": 13252.25, "hypothetical_contracts": 3, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 15.0, "option_spread_pct": 20.31, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 92.86, "ticker": "IDXX", "timing_score": 0.358, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 70.5, "matched_signals": 42, "recovery_stability_score": 0.747, "success_rate": 92.86, "ticker": "IDXX", "timing_score": 0.358, "trend_health_status": "ok"}, {"current_drop_pct": 0.64, "early_entry_score": 0.782, "early_reclaim_pct": 77.3, "matched_signals": 38, "recovery_stability_score": 0.758, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.404, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:05:05.715043-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.64, "shadow_only": true, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "matched_signals": 33, "recovery_stability_score": 0.64, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:00:02.142551-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "matched_signals": 32, "recovery_stability_score": 0.602, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T10:55:01.329795-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:50:01.323991-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:45:01.326292-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706113002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706113002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706113002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706113002)

</details>
