# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-24 12:15:02 EDT`
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

- Cash: `$34,043.00`
- Equity: `$34,043.00`
- Realized PnL: `$24,043.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00320000     13          2026-07-23         2026-07-24       11.225      13.675 3185.0   21.826281 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           85.71               21            2.75             17.60        905.82               102.76         0.655            pass              0.443             50.5                           0.760               -2.43              0.397                                 ok            True                  False
   WDC           90.00               20            4.32             16.87        551.07               114.14         0.594            pass              0.495             34.2                           0.632               -8.31             -0.251                                 ok            True                  False
  ASML           94.12               34            0.78              9.88       1798.77                56.08         0.574            pass              0.808             71.3                           0.753               -0.47              0.140                                 ok            True                   True
  GILD           91.67               24            0.64              0.59        130.61                35.55         0.574            pass              0.584             40.8                           0.288                0.15             -0.043                                 ok            True                  False
  KLAC           87.10               31            1.23              1.88        217.92                98.03         0.705            pass              0.603             67.8                           0.775               -6.69             -0.672 downtrend_blocked_slope_and_streak           False                  False
  LRCX           85.19               27            1.32              2.96        318.51                88.87         0.662            pass              0.525             69.1                           0.765               -9.93             -0.924 downtrend_blocked_slope_and_streak           False                  False
  AMAT           92.31               26            1.77              6.96        559.82                96.41         0.631            pass              0.690             63.9                           0.792               -8.24             -0.776 downtrend_blocked_slope_and_streak           False                  False
  META           85.00               40            0.50              2.14        605.18                54.86         0.555            pass              0.567             59.4                           0.288               -9.89             -1.037 downtrend_blocked_slope_and_streak           False                  False
  MSTR           78.26               46            0.22              0.14         93.57                85.75         0.551            pass              0.539             94.7                           0.868               -1.28              0.186                                 ok           False                  False
   APP           78.95               38            1.80              5.03        396.71                79.31         0.527            pass              0.358             39.5                           0.518              -22.74             -1.905            downtrend_blocked_slope           False                  False
   HON           78.57               14            2.01              3.46        244.79                40.09         0.520            pass              0.105              8.8                           0.158                6.58              0.842                                 ok           False                  False
  GEHC           91.30               23            1.39              0.60         61.73                33.38         0.500 below_threshold              0.589             50.3                           0.360               -5.52             -0.533 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-24T12:00:04.447749-04:00 early_entry_1200 early_entry_shadow        {"contract_symbol": "ASML260918C01790000", "current_drop_pct": 0.6, "early_entry_score": 0.84, "early_reclaim_pct": 78.1, "entry_ask": 155.4, "entry_bid": 151.0, "entry_mode": "early", "entry_option_price": 153.2, "hypothetical_budget": 17021.5, "hypothetical_contracts": 1, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 3.0, "option_spread_pct": 2.87, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.83, "shadow_only": true, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.58, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.84, "early_reclaim_pct": 78.1, "matched_signals": 35, "recovery_stability_score": 0.83, "success_rate": 94.29, "ticker": "ASML", "timing_score": 0.58, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-24T11:55:05.489069-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ASML260828C01785000", "current_drop_pct": 0.92, "early_entry_score": 0.781, "early_reclaim_pct": 66.4, "entry_ask": 129.0, "entry_bid": 115.0, "entry_mode": "early", "entry_option_price": 122.0, "hypothetical_budget": 17021.5, "hypothetical_contracts": 1, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 1.0, "option_spread_pct": 11.48, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.77, "shadow_only": true, "success_rate": 93.94, "ticker": "ASML", "timing_score": 0.571, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.781, "early_reclaim_pct": 66.4, "matched_signals": 33, "recovery_stability_score": 0.77, "success_rate": 93.94, "ticker": "ASML", "timing_score": 0.571, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-24T11:50:02.496150-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:45:02.490359-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:40:02.395425-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:35:03.478911-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:30:02.536091-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:25:02.429701-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:20:02.438945-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-24T11:15:02.420314-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260724121502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260724121502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260724121502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260724121502)

</details>
