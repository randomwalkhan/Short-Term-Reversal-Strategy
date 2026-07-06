# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 11:25:01 EDT`
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
  AMAT           96.55               29            0.86              3.63        601.49               110.01         0.673          pass              0.748             51.4                           0.306               -3.12              0.334                      ok            True                  False
   WBD           95.65               23            0.51              0.09         26.44                22.17         0.544          pass              0.745             67.9                           0.650                0.55             -0.077                      ok            True                  False
  MNST          100.00               17            1.00              0.69         97.31                16.38         0.535          pass              0.597             32.4                           0.415                5.78              0.579                      ok            True                  False
  GILD           90.00               10            1.87              1.72        130.53                30.05         0.535          pass              0.402             27.2                           0.461                4.08              0.419                      ok            True                  False
   ADP           92.31               26            0.86              1.46        241.64                30.79         0.508          pass              0.656             56.9                           0.769                9.97              1.124                      ok            True                  False
   PEP           80.00                5            1.64              1.66        143.51                27.18         0.586          pass              0.108             16.5                           0.363               -0.12             -0.028                      ok           False                  False
   XEL          100.00                3            1.95              1.12         81.48                20.81         0.584          pass              0.466              2.4                           0.215                3.81              0.267                      ok           False                  False
   EXC           85.71                7            1.50              0.50         47.66                22.14         0.584          pass              0.228              5.9                           0.221                2.95              0.258                      ok           False                  False
   KHC          100.00                2            2.94              0.52         25.15                36.79         0.574          pass              0.503             15.3                           0.393                7.91              1.232                      ok           False                  False
  CPRT          100.00                4            2.72              0.57         29.77                43.39         0.556          pass              0.548             30.6                           0.564               -3.42             -0.367 downtrend_blocked_slope           False                  False
  CTAS           66.67                9            1.82              2.31        180.38                35.27         0.554          pass              0.113             19.3                           0.321                4.23              0.513                      ok           False                  False
   AEP           71.43                7            1.64              1.59        137.83                19.65         0.542          pass              0.084              9.8                           0.123                6.70              0.575                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-07-06T11:25:01.367825-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "VRTX260807C00525000", "current_drop_pct": 0.73, "early_entry_score": 0.795, "early_reclaim_pct": 75.5, "entry_ask": 23.8, "entry_bid": 16.1, "entry_mode": "early", "entry_option_price": 19.95, "hypothetical_budget": 13252.25, "hypothetical_contracts": 6, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 38.6, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.824, "shadow_only": true, "success_rate": 93.94, "ticker": "VRTX", "timing_score": 0.437, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.795, "early_reclaim_pct": 75.5, "matched_signals": 33, "recovery_stability_score": 0.824, "success_rate": 93.94, "ticker": "VRTX", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:20:05.831796-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.62, "early_entry_score": 0.784, "early_reclaim_pct": 78.0, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.784, "early_reclaim_pct": 78.0, "matched_signals": 38, "recovery_stability_score": 0.827, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.405, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:15:04.342098-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.58, "early_entry_score": 0.788, "early_reclaim_pct": 79.4, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.806, "shadow_only": true, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.408, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.788, "early_reclaim_pct": 79.4, "matched_signals": 38, "recovery_stability_score": 0.806, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.408, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:10:04.321314-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "IDXX260821C00550000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 70.5, "entry_ask": 39.6, "entry_bid": 32.3, "entry_mode": "early", "entry_option_price": 35.95, "hypothetical_budget": 13252.25, "hypothetical_contracts": 3, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 15.0, "option_spread_pct": 20.31, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 92.86, "ticker": "IDXX", "timing_score": 0.358, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 70.5, "matched_signals": 42, "recovery_stability_score": 0.747, "success_rate": 92.86, "ticker": "IDXX", "timing_score": 0.358, "trend_health_status": "ok"}, {"current_drop_pct": 0.64, "early_entry_score": 0.782, "early_reclaim_pct": 77.3, "matched_signals": 38, "recovery_stability_score": 0.758, "success_rate": 92.11, "ticker": "ROP", "timing_score": 0.404, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:05:05.715043-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.64, "shadow_only": true, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "matched_signals": 33, "recovery_stability_score": 0.64, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:00:02.142551-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "matched_signals": 32, "recovery_stability_score": 0.602, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T10:55:01.329795-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:50:01.323991-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:45:01.326292-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:40:05.174623-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706112501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706112501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706112501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706112501)

</details>
