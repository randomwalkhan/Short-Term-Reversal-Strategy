# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-08 11:15:01 EDT`
Last processed slot: `early_entry_1115`

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

- Cash: `$77,148.10`
- Equity: `$77,148.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261016C00145000     30          2026-09-04         2026-09-08       13.375     12.0375 -4012.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC          100.00               13            0.52              0.09         24.81                29.15         0.621          pass              0.709             75.5                           0.673               -2.16              0.045                                 ok            True                  False
  CRWD           88.89               36            1.56              2.32        212.10                91.63         0.621          pass              0.643             56.8                           0.723               10.02              1.068                                 ok            True                  False
   WMT           85.00               20            1.11              0.83        106.78                40.24         0.592          pass              0.316             18.8                           0.363               -0.50              0.227                                 ok            True                  False
  MELI          100.00               15            2.09             28.90       1965.98                45.80         0.589          pass              0.536             14.6                           0.206               -0.56              0.066                                 ok            True                  False
  NVDA           88.89               27            1.39              2.24        229.40                44.80         0.526          pass              0.436             10.9                           0.241                8.96              0.879                                 ok            True                  False
  PYPL           83.33                6            2.93              1.13         54.48                57.43         0.601          pass              0.176              9.0                           0.274              -13.29             -1.558 downtrend_blocked_slope_and_streak           False                  False
  MSTR           76.92               26            3.09              3.09        141.48               102.15         0.600          pass              0.288             40.6                           0.570               12.85              1.206                                 ok           False                  False
  SBUX           88.89                9            1.49              1.09        104.00                22.08         0.553          pass              0.325             10.7                           0.137               -4.26             -0.334            downtrend_blocked_slope           False                  False
  CPRT           83.33                6            3.05              0.72         33.41                42.28         0.539          pass              0.157              4.6                           0.214               -1.71             -0.009                                 ok           False                  False
  REGN          100.00                8            1.88             10.92        823.04                29.02         0.530          pass              0.588             44.9                           0.343               -1.98              0.108                                 ok           False                  False
   ADP          100.00                3            2.79              5.42        275.30                22.14         0.528          pass              0.465              4.0                           0.136               -4.64             -0.298            downtrend_blocked_slope           False                  False
 CMCSA           90.91               22            1.08              0.20         26.40                26.03         0.521          pass              0.562             46.2                           0.486               -3.02             -0.276            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-08T11:15:01.537130-04:00 early_entry_1115 early_entry_shadow                              {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.82, "early_entry_score": 0.791, "early_reclaim_pct": 70.2, "entry_ask": 9.45, "entry_bid": 8.75, "entry_mode": "early", "entry_option_price": 9.1, "hypothetical_budget": 38574.05, "hypothetical_contracts": 42, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 7.69, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.791, "early_reclaim_pct": 70.2, "matched_signals": 40, "recovery_stability_score": 0.753, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.474, "trend_health_status": "ok"}, {"current_drop_pct": 1.03, "early_entry_score": 0.675, "early_reclaim_pct": 73.5, "matched_signals": 36, "recovery_stability_score": 0.569, "success_rate": 88.89, "ticker": "INSM", "timing_score": 0.437, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:10:05.032926-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                     {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 1.08, "early_entry_score": 0.738, "early_reclaim_pct": 60.6, "entry_ask": 9.2, "entry_bid": 8.35, "entry_mode": "early", "entry_option_price": 8.775, "hypothetical_budget": 38574.05, "hypothetical_contracts": 43, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 9.69, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.689, "shadow_only": true, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 1.08, "early_entry_score": 0.738, "early_reclaim_pct": 60.6, "matched_signals": 38, "recovery_stability_score": 0.689, "success_rate": 92.11, "ticker": "FTNT", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:05:02.503396-04:00 early_entry_1105 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.79, "early_entry_score": 0.748, "early_reclaim_pct": 79.6, "entry_ask": 8.3, "entry_bid": 5.8, "entry_mode": "early", "entry_option_price": 7.05, "hypothetical_budget": 38574.05, "hypothetical_contracts": 54, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 70.0, "option_spread_pct": 35.46, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.594, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.429, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.748, "early_reclaim_pct": 79.6, "matched_signals": 40, "recovery_stability_score": 0.594, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.429, "trend_health_status": "ok"}, {"current_drop_pct": 0.76, "early_entry_score": 0.712, "early_reclaim_pct": 86.2, "matched_signals": 36, "recovery_stability_score": 0.577, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:00:03.391042-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                   {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.77, "early_entry_score": 0.712, "early_reclaim_pct": 86.1, "entry_ask": 20.4, "entry_bid": 19.5, "entry_mode": "early", "entry_option_price": 19.95, "hypothetical_budget": 38574.05, "hypothetical_contracts": 19, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 4.51, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.434, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.712, "early_reclaim_pct": 86.1, "matched_signals": 36, "recovery_stability_score": 0.597, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.434, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:55:04.328012-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.83, "early_entry_score": 0.709, "early_reclaim_pct": 85.0, "entry_ask": 20.0, "entry_bid": 18.1, "entry_mode": "early", "entry_option_price": 19.05, "hypothetical_budget": 38574.05, "hypothetical_contracts": 20, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 9.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.578, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.709, "early_reclaim_pct": 85.0, "matched_signals": 36, "recovery_stability_score": 0.578, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:50:03.448452-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                     {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.81, "early_entry_score": 0.71, "early_reclaim_pct": 85.4, "entry_ask": 19.8, "entry_bid": 18.5, "entry_mode": "early", "entry_option_price": 19.15, "hypothetical_budget": 38574.05, "hypothetical_contracts": 20, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 6.79, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.71, "early_reclaim_pct": 85.4, "matched_signals": 36, "recovery_stability_score": 0.586, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T10:45:04.455818-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T10:40:01.518522-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T10:35:01.536075-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-08T10:30:03.470274-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                   {"contract_symbol": "ALNY261016C00260000", "current_drop_pct": 0.61, "early_entry_score": 0.722, "early_reclaim_pct": 89.0, "entry_ask": 20.8, "entry_bid": 18.9, "entry_mode": "early", "entry_option_price": 19.85, "hypothetical_budget": 38574.05, "hypothetical_contracts": 19, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 37.0, "option_spread_pct": 9.57, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.722, "early_reclaim_pct": 89.0, "matched_signals": 36, "recovery_stability_score": 0.567, "success_rate": 88.89, "ticker": "ALNY", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260908111501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260908111501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260908111501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260908111501)

</details>
