# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 12:50:01 EDT`
Last processed slot: `manage_1300`

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
- Equity: `$34,726.75`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$550.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 17462.5         3.08           3.18       55.67         55.63          bid_ask_mid                       3.18                bid_ask_mid                    True           550.0                   3.25          80.0               10              2.03         42.85           46.97                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            1.21              0.50         58.64               115.77         0.701          pass              0.502             77.3                           0.561               -6.29             -1.385                                 ok            True                  False
  AAPL           95.00               20            1.05              2.41        326.71                37.60         0.610          pass              0.564             12.2                           0.273                3.48              0.525                                 ok            True                  False
  INTC           86.11               36            0.86              0.64        105.18                79.77         0.570          pass              0.637             81.2                           0.410               -5.17             -1.059                                 ok            True                  False
   ADP           95.65               23            1.03              1.77        245.46                36.45         0.568          pass              0.630             29.0                           0.432                0.96              0.330                                 ok            True                  False
  PAYX          100.00               26            1.01              0.79        111.62                33.94         0.544          pass              0.632             23.6                           0.409                3.99              0.656                                 ok            True                  False
  CTSH           85.29               34            1.17              0.36         43.48                49.89         0.508          pass              0.363              3.8                           0.188                1.63              0.279                                 ok            True                  False
  ORLY           84.85               33            0.97              0.59         87.72                43.42         0.505          pass              0.473             46.5                           0.422                2.52              0.156                                 ok            True                  False
  ABNB           95.83               24            1.67              1.69        143.38                31.72         0.503          pass              0.635             30.5                           0.619               -0.88             -0.175                                 ok            True                  False
  AMAT           88.89               27            1.15              4.54        562.61               100.84         0.717          pass              0.647             75.0                           0.539               -2.18             -0.829 downtrend_blocked_slope_and_streak           False                  False
  KLAC           87.50               32            0.97              1.47        216.93               102.77         0.709          pass              0.655             79.1                           0.492               -2.59             -0.735 downtrend_blocked_slope_and_streak           False                  False
  LRCX           88.89               27            0.91              2.05        321.12                94.63         0.691          pass              0.661             80.5                           0.645               -4.22             -1.057 downtrend_blocked_slope_and_streak           False                  False
  PYPL           89.19               37            0.39              0.15         55.78                62.33         0.631          pass              0.667             59.6                           0.452               24.93              2.804                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722125001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722125001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722125001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722125001)

</details>
