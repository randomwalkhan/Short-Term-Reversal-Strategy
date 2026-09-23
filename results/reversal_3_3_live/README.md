# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 11:10:05 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.75               32            1.28              1.50        166.69               109.59         0.731          pass              0.769             61.0                           0.653               24.48              2.877                                 ok            True                   True
  PYPL           86.96               23            1.12              0.41         52.71                57.12         0.626          pass              0.471             45.3                           0.572                0.25             -0.166                                 ok            True                  False
  NVDA           92.00               25            1.22              1.95        228.03                44.57         0.583          pass              0.561             27.7                           0.390                1.19              0.460                                 ok            True                  False
  DRAM           82.14               28            2.00              0.89         63.24                51.34         0.524          pass              0.337             35.9                           0.568                1.25              0.627                                 ok            True                  False
  UPRO           82.61               23            1.40              1.51        153.09                31.44         0.504          pass              0.296             29.9                           0.460                2.99              0.486                                 ok            True                  False
  MRVL           77.78               36            0.95              1.74        261.61                69.87         0.583          pass              0.403             57.0                           0.608               10.58              1.507                                 ok           False                  False
  SOXL           77.78               27            4.45              4.73        149.92               119.42         0.583          pass              0.308             45.4                           0.821               15.42              2.456                                 ok           False                  False
  AMGN           86.11               36            0.34              0.99        409.82                46.69         0.559          pass              0.575             60.9                           0.283                4.49              0.629                                 ok           False                  False
  ADSK           86.05               43            0.06              0.09        219.58                55.47         0.557          pass              0.706             96.3                           0.912                6.23              0.354                                 ok           False                  False
   XEL          100.00                4            1.44              0.73         71.75                15.29         0.556          pass              0.482              8.8                           0.203               -6.03             -0.571 downtrend_blocked_slope_and_streak           False                  False
   WBD           92.50               40            0.13              0.03         30.82                38.24         0.543          pass              0.834             82.1                           0.552               10.32              1.011                                 ok           False                  False
  AMAT           80.49               41            0.20              0.67        472.17                51.05         0.529          pass              0.541             91.6                           0.938                0.57              0.285                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-23T11:10:05.417180-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.57, "early_entry_score": 0.78, "early_reclaim_pct": 78.6, "entry_ask": 4.9, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 35735.4, "hypothetical_contracts": 78, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 15.38, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.908, "shadow_only": true, "success_rate": 91.89, "ticker": "MCHP", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.78, "early_reclaim_pct": 78.6, "matched_signals": 37, "recovery_stability_score": 0.908, "success_rate": 91.89, "ticker": "MCHP", "timing_score": 0.476, "trend_health_status": "ok"}, {"current_drop_pct": 1.28, "early_entry_score": 0.769, "early_reclaim_pct": 61.0, "matched_signals": 32, "recovery_stability_score": 0.653, "success_rate": 93.75, "ticker": "MSTR", "timing_score": 0.731, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T11:05:04.282212-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.62, "early_entry_score": 0.763, "early_reclaim_pct": 76.8, "entry_ask": 4.7, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 4.35, "hypothetical_budget": 35735.4, "hypothetical_contracts": 82, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 16.09, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.912, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.763, "early_reclaim_pct": 76.8, "matched_signals": 36, "recovery_stability_score": 0.912, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T11:00:02.325719-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.72, "early_entry_score": 0.751, "early_reclaim_pct": 73.2, "entry_ask": 4.7, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.6, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.887, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.751, "early_reclaim_pct": 73.2, "matched_signals": 36, "recovery_stability_score": 0.887, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:55:05.536781-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.67, "early_entry_score": 0.757, "early_reclaim_pct": 74.9, "entry_ask": 4.7, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.6, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.851, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.757, "early_reclaim_pct": 74.9, "matched_signals": 36, "recovery_stability_score": 0.851, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.476, "trend_health_status": "ok"}, {"current_drop_pct": 0.85, "early_entry_score": 0.678, "early_reclaim_pct": 66.5, "matched_signals": 32, "recovery_stability_score": 0.814, "success_rate": 90.62, "ticker": "QCOM", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:50:05.940190-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:45:05.446928-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:40:01.660057-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:35:05.492268-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:30:06.224797-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:25:06.407969-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923111005)

</details>
