# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 12:25:04 EDT`
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

- Cash: `$17,264.25`
- Equity: `$34,424.25`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$247.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 17160.0         3.08           3.12       55.67         55.72          bid_ask_mid                       3.12                bid_ask_mid                    True           247.5                   1.46          80.0               10              2.03         42.85           46.19                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            0.82              0.34         58.71               115.77         0.725          pass              0.527             84.8                           0.774               -5.92             -1.367                                 ok            True                  False
  AAPL           95.83               24            0.90              2.07        326.85                37.60         0.595          pass              0.611             19.3                           0.266                3.63              0.532                                 ok            True                  False
   ADP           95.65               23            1.04              1.80        245.45                36.45         0.567          pass              0.627             28.0                           0.299                0.94              0.330                                 ok            True                  False
  PAYX          100.00               26            1.00              0.78        111.62                33.94         0.544          pass              0.633             24.1                           0.319                4.00              0.657                                 ok            True                  False
  CTSH           85.71               35            1.03              0.31         43.50                49.89         0.512          pass              0.400             10.0                           0.224                1.77              0.285                                 ok            True                  False
  ORLY           84.85               33            0.93              0.57         87.73                43.42         0.507          pass              0.480             48.7                           0.317                2.56              0.158                                 ok            True                  False
  PANW           92.31               26            2.02              4.84        340.08                60.47         0.504          pass              0.632             48.9                           0.489                4.57              0.581                                 ok            True                  False
  AMAT           89.29               28            1.07              4.24        562.73               100.84         0.716          pass              0.669             76.6                           0.603               -2.11             -0.826 downtrend_blocked_slope_and_streak           False                  False
  KLAC           87.50               32            0.91              1.38        216.97               102.77         0.712          pass              0.659             80.4                           0.614               -2.53             -0.732 downtrend_blocked_slope_and_streak           False                  False
  LRCX           89.66               29            0.67              1.51        321.35                94.63         0.694          pass              0.710             85.6                           0.755               -4.00             -1.046 downtrend_blocked_slope_and_streak           False                  False
  ISRG           66.67               12            2.32              5.69        347.62                68.15         0.625          pass              0.084              2.8                           0.093              -17.63             -2.101            downtrend_blocked_slope           False                  False
  PYPL           90.00               40            0.22              0.09         55.81                62.33         0.624          pass              0.760             77.1                           0.582               25.14              2.812                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-22T12:00:05.697705-04:00 early_entry_1200 early_entry_shadow      {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.82, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "matched_signals": 35, "recovery_stability_score": 0.584, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:55:06.689792-04:00 early_entry_1155 early_entry_shadow  {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.91, "early_entry_score": 0.769, "early_reclaim_pct": 66.0, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.584, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.455, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.769, "early_reclaim_pct": 66.0, "matched_signals": 33, "recovery_stability_score": 0.584, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.455, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:50:01.765013-04:00 early_entry_1150 early_entry_shadow      {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.83, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "top_candidates": [{"current_drop_pct": 0.83, "early_entry_score": 0.8, "early_reclaim_pct": 69.3, "matched_signals": 35, "recovery_stability_score": 0.646, "success_rate": 94.29, "ticker": "MELI", "timing_score": 0.448, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:45:06.236742-04:00 early_entry_1145 early_entry_shadow  {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.92, "early_entry_score": 0.767, "early_reclaim_pct": 65.6, "entry_ask": 112.8, "entry_bid": 94.2, "entry_mode": "early", "entry_option_price": 103.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 17.97, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.677, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.92, "early_entry_score": 0.767, "early_reclaim_pct": 65.6, "matched_signals": 33, "recovery_stability_score": 0.677, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:40:06.764688-04:00 early_entry_1140 early_entry_shadow   {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.0, "entry_ask": 112.8, "entry_bid": 94.1, "entry_mode": "early", "entry_option_price": 103.45, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 18.08, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.722, "shadow_only": true, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.45, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.0, "matched_signals": 34, "recovery_stability_score": 0.722, "success_rate": 94.12, "ticker": "MELI", "timing_score": 0.45, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:35:05.764580-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.72, "early_entry_score": 0.833, "early_reclaim_pct": 73.4, "entry_ask": 112.8, "entry_bid": 94.1, "entry_mode": "early", "entry_option_price": 103.45, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 18.08, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.833, "early_reclaim_pct": 73.4, "matched_signals": 37, "recovery_stability_score": 0.753, "success_rate": 94.59, "ticker": "MELI", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:30:01.756167-04:00 early_entry_1130 early_entry_shadow   {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.6, "early_entry_score": 0.857, "early_reclaim_pct": 77.6, "entry_ask": 112.8, "entry_bid": 94.1, "entry_mode": "early", "entry_option_price": 103.45, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 18.08, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 94.74, "ticker": "MELI", "timing_score": 0.443, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.857, "early_reclaim_pct": 77.6, "matched_signals": 38, "recovery_stability_score": 0.753, "success_rate": 94.74, "ticker": "MELI", "timing_score": 0.443, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:25:05.729794-04:00 early_entry_1125 early_entry_shadow     {"contract_symbol": "MELI260821C01810000", "current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 72.4, "entry_ask": 112.8, "entry_bid": 94.1, "entry_mode": "early", "entry_option_price": 103.45, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 37.0, "option_spread_pct": 18.08, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.69, "shadow_only": true, "success_rate": 94.44, "ticker": "MELI", "timing_score": 0.447, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.82, "early_reclaim_pct": 72.4, "matched_signals": 36, "recovery_stability_score": 0.69, "success_rate": 94.44, "ticker": "MELI", "timing_score": 0.447, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:20:03.697647-04:00 early_entry_1120 early_entry_shadow                              {"contract_symbol": "MELI260821C01800000", "current_drop_pct": 0.97, "early_entry_score": 0.762, "early_reclaim_pct": 63.9, "entry_ask": 111.6, "entry_bid": 99.4, "entry_mode": "early", "entry_option_price": 105.5, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 111.0, "option_spread_pct": 11.56, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.614, "shadow_only": true, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.97, "early_entry_score": 0.762, "early_reclaim_pct": 63.9, "matched_signals": 33, "recovery_stability_score": 0.614, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T11:15:05.770543-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722122504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722122504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722122504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722122504)

</details>
