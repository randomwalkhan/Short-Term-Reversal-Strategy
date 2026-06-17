# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-17 12:30:02 EDT`
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
   XEL          100.00               17            0.53              0.29         78.85                23.22         0.628          pass              0.603             31.1                           0.233                1.65              0.260                                 ok            True                  False
  GOOG           80.00               10            1.98              5.14        368.90                27.92         0.534          pass              0.140             28.8                           0.477                2.33              0.072                                 ok            True                  False
  FTNT           94.44               18            1.94              2.00        146.16                47.06         0.529          pass              0.631             46.4                           0.489               -3.15             -0.271                                 ok            True                  False
  SBUX           83.33               24            0.81              0.57        101.43                25.47         0.525          pass              0.387             50.6                           0.282                5.60              0.894                                 ok            True                  False
  CTAS           94.44               18            1.57              1.94        175.88                29.79         0.522          pass              0.553             20.9                           0.140                0.36              0.026                                 ok            True                  False
    ZS           76.74               43            0.14              0.13        127.18               152.67         0.876          pass              0.569             93.9                           0.795               -5.45             -0.534 downtrend_blocked_slope_and_streak           False                  False
  INTU           79.07               43            0.40              0.78        280.66                99.11         0.704          pass              0.524             84.6                           0.563              -13.12             -1.456 downtrend_blocked_slope_and_streak           False                  False
   KHC          100.00                1            2.04              0.34         23.65                25.54         0.642          pass              0.467              1.0                           0.155                4.30              0.761                                 ok           False                  False
   CSX          100.00                4            1.56              0.51         46.68                20.12         0.629          pass              0.499             12.0                           0.321                0.07              0.176                                 ok           False                  False
   PEP          100.00                2            1.95              1.99        145.27                20.43         0.618          pass              0.469              2.4                           0.138                1.96              0.356                                 ok           False                  False
  PAYX          100.00               23            0.49              0.34        100.13                31.37         0.594          pass              0.763             72.4                           0.378               -0.99              0.096                                 ok           False                  False
   TXN           94.12               34            0.32              0.69        305.42                52.85         0.581          pass              0.843             82.8                           0.570               -1.10              0.040                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260617123002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260617123002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260617123002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260617123002)

</details>
