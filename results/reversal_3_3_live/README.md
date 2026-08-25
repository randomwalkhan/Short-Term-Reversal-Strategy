# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-25 13:20:01 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$30,388.00`
- Equity: `$58,378.00`
- Realized PnL: `$47,703.00`
- Unrealized PnL: `$675.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   1      9     27315.0                 27990.0        30.35           31.1      310.66        311.96          bid_ask_mid                       31.1                bid_ask_mid                    True           675.0                   2.47          87.5               32              1.06         63.04           63.83                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MNST           92.00               25            0.76              0.26         48.81               552.55         1.000          pass              0.556             11.9                           0.203                6.63              0.645                      ok            True                  False
  TEAM           81.82               33            1.97              2.37        170.32               115.46         0.743          pass              0.372             32.1                           0.270                9.00              1.068                      ok            True                  False
  DXCM           88.57               35            0.55              0.35         90.91                50.36         0.583          pass              0.628             58.3                           0.593                1.15              0.109                      ok            True                  False
  WDAY           80.00               30            2.08              2.90        197.91                78.88         0.567          pass              0.288             32.7                           0.216                7.58              0.731                      ok            True                  False
  PAYX          100.00               18            1.03              0.91        125.62                34.31         0.563          pass              0.612             34.0                           0.231                2.81              0.316                      ok            True                  False
  FAST          100.00               12            1.48              0.53         51.05                22.00         0.562          pass              0.471              0.7                           0.160               -3.55             -0.244                      ok            True                  False
   KHC           84.21               19            1.46              0.26         25.56                37.91         0.554          pass              0.272             14.8                           0.197                2.62              0.342                      ok            True                  False
  MDLZ           90.91               11            1.87              0.85         64.34                26.88         0.542          pass              0.385             11.0                           0.363                2.77              0.351                      ok            True                  False
   KDP           82.35               17            1.71              0.39         32.34                31.66         0.515          pass              0.209             15.9                           0.240                9.51              0.874                      ok            True                  False
  COST           95.24               21            0.97              6.59        968.57                19.15         0.511          pass              0.556             10.4                           0.219                1.87              0.077                      ok            True                  False
   LIN           82.14               28            0.77              2.65        488.89                26.61         0.501          pass              0.342             38.2                           0.359               -0.87              0.100                      ok            True                  False
  AMAT           90.00               30            1.32              4.47        482.27                81.86         0.644          pass              0.497             10.8                           0.204               -9.00             -1.204 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-08-25T12:00:02.529828-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T11:55:01.683706-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 0.99, "early_entry_score": 0.807, "early_reclaim_pct": 75.6, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.99, "early_entry_score": 0.807, "early_reclaim_pct": 75.6, "matched_signals": 30, "recovery_stability_score": 0.61, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:50:05.938320-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "GEHC261002C00074000", "current_drop_pct": 0.55, "early_entry_score": 0.818, "early_reclaim_pct": 60.2, "entry_ask": 3.0, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 15194.0, "hypothetical_contracts": 56, "matched_signals": 37, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 26.0, "option_spread_pct": 22.22, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.599, "shadow_only": true, "success_rate": 97.3, "ticker": "GEHC", "timing_score": 0.577, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.818, "early_reclaim_pct": 60.2, "matched_signals": 37, "recovery_stability_score": 0.599, "success_rate": 97.3, "ticker": "GEHC", "timing_score": 0.577, "trend_health_status": "ok"}, {"current_drop_pct": 1.01, "early_entry_score": 0.805, "early_reclaim_pct": 75.0, "matched_signals": 30, "recovery_stability_score": 0.632, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:45:01.861392-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 0.96, "early_entry_score": 0.81, "early_reclaim_pct": 76.4, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.475, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.81, "early_reclaim_pct": 76.4, "matched_signals": 30, "recovery_stability_score": 0.655, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:40:01.910397-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 77.5, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 77.5, "matched_signals": 31, "recovery_stability_score": 0.693, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:35:01.805788-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 77.6, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.82, "early_reclaim_pct": 77.6, "matched_signals": 31, "recovery_stability_score": 0.694, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:30:01.809806-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-25T11:25:06.462358-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 1.01, "early_entry_score": 0.806, "early_reclaim_pct": 75.1, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.806, "early_reclaim_pct": 75.1, "matched_signals": 30, "recovery_stability_score": 0.713, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:20:01.845673-04:00 early_entry_1120 early_entry_shadow {"contract_symbol": "GEHC261002C00074000", "current_drop_pct": 0.54, "early_entry_score": 0.827, "early_reclaim_pct": 61.2, "entry_ask": 3.5, "entry_bid": 2.3, "entry_mode": "early", "entry_option_price": 2.9, "hypothetical_budget": 15194.0, "hypothetical_contracts": 52, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 26.0, "option_spread_pct": 41.38, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.572, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.827, "early_reclaim_pct": 61.2, "matched_signals": 38, "recovery_stability_score": 0.673, "success_rate": 97.37, "ticker": "GEHC", "timing_score": 0.572, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.81, "early_reclaim_pct": 76.5, "matched_signals": 30, "recovery_stability_score": 0.73, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.475, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-25T11:15:01.710634-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ROP261016C00410000", "current_drop_pct": 0.98, "early_entry_score": 0.808, "early_reclaim_pct": 75.8, "entry_ask": 22.5, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 20.05, "hypothetical_budget": 15194.0, "hypothetical_contracts": 7, "matched_signals": 30, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 24.44, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.697, "shadow_only": true, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.808, "early_reclaim_pct": 75.8, "matched_signals": 30, "recovery_stability_score": 0.697, "success_rate": 100.0, "ticker": "ROP", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260825132001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260825132001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260825132001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260825132001)

</details>
