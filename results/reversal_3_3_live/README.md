# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 14:15:02 EDT`
Last processed slot: `manual`

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

- Cash: `$33,480.75`
- Equity: `$33,480.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-04)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CSX     option         option CSX260918C00050000    106          2026-08-03         2026-08-04         1.65       1.485 -1749.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   ROP           93.33               30            0.75              2.07        391.68                47.45         0.574            pass              0.743             65.6                           0.676               11.10              1.488                                 ok            True                   True
   PEP           83.33               24            0.61              0.60        139.37                26.13         0.549            pass              0.435             66.0                           0.634                2.80              0.393                                 ok            True                  False
  ALNY           88.89               36            0.96              1.48        219.70               126.96         0.801            pass              0.666             58.5                           0.652              -19.59             -2.903            downtrend_blocked_slope           False                  False
  ISRG           69.23               13            2.46              6.45        372.64                72.79         0.647            pass              0.118             11.3                           0.336                4.61              0.799                                 ok           False                  False
  TMUS           89.19               37            0.31              0.38        176.93                55.96         0.604            pass              0.729             81.1                           0.666               -7.46             -0.637            downtrend_blocked_slope           False                  False
  AMZN           76.47               17            2.13              4.23        282.21                60.32         0.594            pass              0.213             35.7                           0.288               12.29              1.484                                 ok           False                  False
   MAR          100.00               31            0.64              1.56        346.16                34.81         0.538            pass              0.783             63.0                           0.595               -6.31             -0.467 downtrend_blocked_slope_and_streak           False                  False
  VRSK           94.74               38            0.47              0.64        192.84                44.31         0.516            pass              0.843             70.7                           0.671               -1.56             -0.013           downtrend_blocked_streak           False                  False
  META           88.64               44            0.21              0.88        589.86                55.17         0.513            pass              0.756             91.6                           0.654               -8.51             -1.050 downtrend_blocked_slope_and_streak           False                  False
  CTSH           87.80               41            0.34              0.13         55.11                60.42         0.511            pass              0.726             88.8                           0.831               26.03              3.098                                 ok           False                  False
  COST           77.78               27            0.70              4.68        952.08                24.00         0.487 below_threshold              0.345             60.9                           0.733                2.12              0.342                                 ok           False                  False
  ABNB           91.18               34            0.82              0.86        150.27                33.33         0.486 below_threshold              0.621             38.2                           0.577                3.68              0.867                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-08-04T12:00:02.363319-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.73, "early_reclaim_pct": 76.3, "matched_signals": 33, "recovery_stability_score": 0.74, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.566, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:55:01.364368-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.747, "early_reclaim_pct": 67.0, "matched_signals": 30, "recovery_stability_score": 0.701, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.576, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:50:01.376014-04:00 early_entry_1150 early_entry_shadow               {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "entry_ask": 36.7, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.35, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 7.64, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.828, "early_reclaim_pct": 87.9, "matched_signals": 39, "recovery_stability_score": 0.646, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.43, "trend_health_status": "ok"}, {"current_drop_pct": 0.6, "early_entry_score": 0.717, "early_reclaim_pct": 72.3, "matched_signals": 33, "recovery_stability_score": 0.747, "success_rate": 90.91, "ticker": "ROP", "timing_score": 0.56, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:45:01.424926-04:00 early_entry_1145 early_entry_shadow              {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "entry_ask": 37.4, "entry_bid": 34.0, "entry_mode": "early", "entry_option_price": 35.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 10.0, "option_spread_pct": 9.52, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.827, "early_reclaim_pct": 87.6, "matched_signals": 39, "recovery_stability_score": 0.69, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.429, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.752, "early_reclaim_pct": 68.4, "matched_signals": 30, "recovery_stability_score": 0.736, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.578, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:40:04.541695-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "REGN260918C00755000", "current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "entry_ask": 40.8, "entry_bid": 34.6, "entry_mode": "early", "entry_option_price": 37.7, "hypothetical_budget": 16740.38, "hypothetical_contracts": 4, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 10.0, "option_spread_pct": 16.45, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.83, "early_reclaim_pct": 88.3, "matched_signals": 39, "recovery_stability_score": 0.715, "success_rate": 92.31, "ticker": "REGN", "timing_score": 0.431, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.741, "early_reclaim_pct": 64.9, "matched_signals": 30, "recovery_stability_score": 0.733, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.573, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:35:05.362040-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "ROP260918C00390000", "current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "entry_ask": 21.4, "entry_bid": 15.9, "entry_mode": "early", "entry_option_price": 18.65, "hypothetical_budget": 16740.38, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.711, "shadow_only": true, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.736, "early_reclaim_pct": 63.5, "matched_signals": 30, "recovery_stability_score": 0.711, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:30:01.403472-04:00 early_entry_1130 early_entry_shadow  {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.585, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.808, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.585, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.499, "trend_health_status": "ok"}, {"current_drop_pct": 0.71, "early_entry_score": 0.749, "early_reclaim_pct": 67.3, "matched_signals": 30, "recovery_stability_score": 0.694, "success_rate": 93.33, "ticker": "ROP", "timing_score": 0.577, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-04T11:25:01.272769-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:20:01.453908-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-04T11:15:06.199893-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "CTAS260911C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "entry_ask": 8.7, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 7.0, "hypothetical_budget": 16740.38, "hypothetical_contracts": 23, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 48.57, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.657, "shadow_only": true, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.813, "early_reclaim_pct": 71.8, "matched_signals": 35, "recovery_stability_score": 0.657, "success_rate": 94.29, "ticker": "CTAS", "timing_score": 0.501, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804141502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804141502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804141502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804141502)

</details>
