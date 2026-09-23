# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 11:05:04 EDT`
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
  MSTR           93.75               32            1.42              1.67        166.62               109.59         0.724          pass              0.756             56.7                           0.618               24.30              2.871                                 ok            True                  False
  PYPL           89.29               28            0.89              0.33         52.75                57.12         0.614          pass              0.598             56.5                           0.708                0.48             -0.156                                 ok            True                  False
  NVDA           91.67               24            1.25              2.00        228.01                44.57         0.586          pass              0.540             25.7                           0.392                1.16              0.459                                 ok            True                  False
  AMAT           82.50               40            0.52              1.73        471.72                51.05         0.517          pass              0.554             78.4                           0.882                0.24              0.271                                 ok            True                  False
  DRAM           82.14               28            2.20              0.98         63.20                51.34         0.511          pass              0.316             29.3                           0.507                1.04              0.618                                 ok            True                  False
  UPRO           82.61               23            1.44              1.55        153.07                31.44         0.501          pass              0.289             27.6                           0.444                2.94              0.484                                 ok            True                  False
  MRVL           77.14               35            1.13              2.08        261.47                69.87         0.577          pass              0.370             48.6                           0.560               10.37              1.499                                 ok           False                  False
  AMGN           85.71               35            0.37              1.05        409.79                46.69         0.563          pass              0.551             58.4                           0.267                4.46              0.628                                 ok           False                  False
   XEL          100.00                4            1.47              0.74         71.74                15.29         0.555          pass              0.469              4.5                           0.125               -6.06             -0.573 downtrend_blocked_slope_and_streak           False                  False
  ADSK           85.00               40            0.35              0.54        219.39                55.47         0.554          pass              0.623             78.1                           0.837                5.92              0.341                                 ok           False                  False
  SOXL           77.78               27            5.14              5.46        149.61               119.42         0.541          pass              0.278             36.9                           0.654               14.59              2.424                                 ok           False                  False
   WBD           92.68               41            0.08              0.02         30.82                38.24         0.540          pass              0.859             88.8                           0.689               10.37              1.013                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-23T11:05:04.282212-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.62, "early_entry_score": 0.763, "early_reclaim_pct": 76.8, "entry_ask": 4.7, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 4.35, "hypothetical_budget": 35735.4, "hypothetical_contracts": 82, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 16.09, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.912, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.763, "early_reclaim_pct": 76.8, "matched_signals": 36, "recovery_stability_score": 0.912, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T11:00:02.325719-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.72, "early_entry_score": 0.751, "early_reclaim_pct": 73.2, "entry_ask": 4.7, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.6, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.887, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.751, "early_reclaim_pct": 73.2, "matched_signals": 36, "recovery_stability_score": 0.887, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:55:05.536781-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "MCHP261030C00075000", "current_drop_pct": 0.67, "early_entry_score": 0.757, "early_reclaim_pct": 74.9, "entry_ask": 4.7, "entry_bid": 3.9, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 18.6, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.851, "shadow_only": true, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.476, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.757, "early_reclaim_pct": 74.9, "matched_signals": 36, "recovery_stability_score": 0.851, "success_rate": 91.67, "ticker": "MCHP", "timing_score": 0.476, "trend_health_status": "ok"}, {"current_drop_pct": 0.85, "early_entry_score": 0.678, "early_reclaim_pct": 66.5, "matched_signals": 32, "recovery_stability_score": 0.814, "success_rate": 90.62, "ticker": "QCOM", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:50:05.940190-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:45:05.446928-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:40:01.660057-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:35:05.492268-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:30:06.224797-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:25:06.407969-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:20:05.981567-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923110504)

</details>
