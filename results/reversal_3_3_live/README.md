# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 12:20:05 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$27,898.25`
- Equity: `$27,898.25`
- Realized PnL: `$17,898.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-17)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  DRAM     option         option DRAM260717C00069000     17          2026-06-16         2026-06-17        7.425        8.55 1912.5   15.151515 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   EXC           90.00               10            1.12              0.36         46.43                19.22         0.575          pass              0.355             10.3                           0.184                3.34              0.396                                 ok            True                  False
  MDLZ           90.00               10            1.58              0.69         61.86                20.23         0.566          pass              0.323              0.0                           0.163                0.16              0.197                                 ok            True                  False
  FTNT           94.44               18            1.86              1.91        146.20                47.06         0.535          pass              0.638             48.8                           0.426               -3.07             -0.267                                 ok            True                  False
  SBUX           84.62               26            0.66              0.47        101.48                25.47         0.522          pass              0.460             59.3                           0.358                5.75              0.900                                 ok            True                  False
  CTAS           94.74               19            1.54              1.91        175.89                29.79         0.517          pass              0.571             22.0                           0.172                0.39              0.027                                 ok            True                  False
    ZS           78.57               42            0.28              0.25        127.12               152.67         0.876          pass              0.552             88.1                           0.703               -5.57             -0.540 downtrend_blocked_slope_and_streak           False                  False
  INTU           79.07               43            0.39              0.77        280.66                99.11         0.705          pass              0.525             84.7                           0.527              -13.12             -1.456 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                1            1.89              0.31         23.67                25.54         0.653          pass              0.465              0.0                           0.158                4.45              0.768                                 ok           False                  False
   XEL          100.00               17            0.47              0.26         78.87                23.22         0.632          pass              0.628             39.3                           0.239                1.71              0.263                                 ok           False                  False
   PEP          100.00                3            1.66              1.69        145.39                20.43         0.631          pass              0.480              5.5                           0.095                2.26              0.370                                 ok           False                  False
   CSX          100.00                4            1.63              0.54         46.67                20.12         0.625          pass              0.486              7.8                           0.244               -0.01              0.173                                 ok           False                  False
  PAYX          100.00               26            0.26              0.18        100.20                31.37         0.587          pass              0.822             85.4                           0.576               -0.76              0.106                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-17T12:20:05.226581-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "DRAM260717C00069000", "fill_price": 8.55, "pnl": 1912.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.15, "ticker": "DRAM"}
2026-06-17T12:00:04.853951-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-17T11:55:03.988623-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.73, "early_entry_score": 0.778, "early_reclaim_pct": 63.1, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.625, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.778, "early_reclaim_pct": 63.1, "matched_signals": 31, "recovery_stability_score": 0.625, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:50:02.970534-04:00 early_entry_1150 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.58, "early_entry_score": 0.82, "early_reclaim_pct": 70.7, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.82, "early_reclaim_pct": 70.7, "matched_signals": 34, "recovery_stability_score": 0.685, "success_rate": 97.06, "ticker": "CTAS", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:45:05.887848-04:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.57, "early_entry_score": 0.828, "early_reclaim_pct": 71.4, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.828, "early_reclaim_pct": 71.4, "matched_signals": 35, "recovery_stability_score": 0.69, "success_rate": 97.14, "ticker": "CTAS", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:40:04.886888-04:00 early_entry_1140 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.65, "early_entry_score": 0.804, "early_reclaim_pct": 67.4, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.667, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.48, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.804, "early_reclaim_pct": 67.4, "matched_signals": 33, "recovery_stability_score": 0.667, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.48, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:35:01.995528-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.63, "early_entry_score": 0.805, "early_reclaim_pct": 68.0, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.805, "early_reclaim_pct": 68.0, "matched_signals": 33, "recovery_stability_score": 0.674, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:30:04.966423-04:00 early_entry_1130 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.7, "early_entry_score": 0.783, "early_reclaim_pct": 64.7, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.783, "early_reclaim_pct": 64.7, "matched_signals": 31, "recovery_stability_score": 0.646, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:25:01.981601-04:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.74, "early_entry_score": 0.777, "early_reclaim_pct": 62.9, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.777, "early_reclaim_pct": 62.9, "matched_signals": 31, "recovery_stability_score": 0.62, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-17T11:20:05.975593-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "CTAS260731C00180000", "current_drop_pct": 0.78, "early_entry_score": 0.765, "early_reclaim_pct": 60.9, "entry_ask": 7.1, "entry_bid": 5.0, "entry_mode": "early", "entry_option_price": 6.05, "hypothetical_budget": 6681.63, "hypothetical_contracts": 11, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 11.0, "option_spread_pct": 34.71, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 96.67, "ticker": "CTAS", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.765, "early_reclaim_pct": 60.9, "matched_signals": 30, "recovery_stability_score": 0.593, "success_rate": 96.67, "ticker": "CTAS", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617122005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617122005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617122005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617122005)

</details>
