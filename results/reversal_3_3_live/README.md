# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-22 11:05:06 EDT`
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

- Cash: `$17,264.25`
- Equity: `$33,956.75`
- Realized PnL: `$24,176.75`
- Unrealized PnL: `$-220.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260821C00055000       2026-07-21                   1     55     16912.5                 16692.5         3.08           3.04       55.67         55.43          bid_ask_mid                       3.04                bid_ask_mid                    True          -220.0                   -1.3          80.0               10              2.03         42.85           48.27                  61.63                6395.0           68.0               0.05                      ok
```

## Today's Closed Trades (2026-07-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.76               29            1.04              0.43         58.67               115.77         0.712          pass              0.513             80.6                           0.649               -6.13             -1.377                                 ok            True                  False
  PYPL           86.67               30            0.75              0.29         55.72                62.33         0.651          pass              0.445             22.9                           0.375               24.48              2.788                                 ok            True                  False
  AAPL           95.83               24            0.90              2.05        326.86                37.60         0.596          pass              0.613             20.0                           0.392                3.64              0.532                                 ok            True                  False
   ADP           96.15               26            0.92              1.59        245.54                36.45         0.560          pass              0.628             21.6                           0.278                1.07              0.335                                 ok            True                  False
  PAYX          100.00               26            1.03              0.81        111.61                33.94         0.544          pass              0.604             14.4                           0.201                3.96              0.655                                 ok            True                  False
  CTSH           87.18               39            0.62              0.19         43.55                49.89         0.514          pass              0.574             46.0                           0.431                2.19              0.304                                 ok            True                  False
  ABNB           95.00               20            1.95              1.97        143.26                31.72         0.512          pass              0.573             18.3                           0.454               -1.16             -0.188                                 ok            True                  False
   TRI           87.88               33            1.05              0.67         90.42                49.06         0.505          pass              0.498             28.0                           0.319                0.97              0.395                                 ok            True                  False
  PANW           91.67               24            2.21              5.29        339.88                60.47         0.503          pass              0.587             44.0                           0.283                4.37              0.572                                 ok            True                  False
  AMAT           89.29               28            0.97              3.84        562.91               100.84         0.722          pass              0.676             78.9                           0.644               -2.00             -0.821 downtrend_blocked_slope_and_streak           False                  False
  LRCX           89.29               28            0.75              1.70        321.27                94.63         0.695          pass              0.688             83.8                           0.620               -4.08             -1.050 downtrend_blocked_slope_and_streak           False                  False
  ASML           94.29               35            0.14              1.76       1800.75                63.30         0.618          pass              0.893             94.7                           0.706                1.72              0.009                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-07-22T11:05:06.654140-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T11:00:03.703283-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:55:01.795388-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                 {"contract_symbol": "ASML260821C01800000", "current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "entry_ask": 123.4, "entry_bid": 119.9, "entry_mode": "early", "entry_option_price": 121.65, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 224.0, "option_spread_pct": 2.88, "option_volume": 138.0, "reason": "shadow_insufficient_cash", "recovery_stability_score": 0.597, "shadow_only": true, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.822, "early_reclaim_pct": 75.6, "matched_signals": 34, "recovery_stability_score": 0.597, "success_rate": 94.12, "ticker": "ASML", "timing_score": 0.591, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T10:50:06.298041-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:45:04.805546-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:40:06.812850-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-22T10:35:07.269157-04:00 early_entry_1035 early_entry_shadow   {"contract_symbol": "PANW260821C00340000", "current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "entry_ask": 24.8, "entry_bid": 23.4, "entry_mode": "early", "entry_option_price": 24.1, "hypothetical_budget": 8632.13, "hypothetical_contracts": 3, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 923.0, "option_spread_pct": 5.81, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.611, "shadow_only": true, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "top_candidates": [{"current_drop_pct": 1.48, "early_entry_score": 0.74, "early_reclaim_pct": 62.5, "matched_signals": 31, "recovery_stability_score": 0.611, "success_rate": 93.55, "ticker": "PANW", "timing_score": 0.508, "trend_health_status": "ok"}, {"current_drop_pct": 0.95, "early_entry_score": 0.712, "early_reclaim_pct": 70.3, "matched_signals": 39, "recovery_stability_score": 0.722, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-22T10:30:05.882610-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                       {"contract_symbol": "CRWD260821C00190000", "current_drop_pct": 1.03, "early_entry_score": 0.704, "early_reclaim_pct": 67.7, "entry_ask": 14.05, "entry_bid": 13.05, "entry_mode": "early", "entry_option_price": 13.55, "hypothetical_budget": 8632.13, "hypothetical_contracts": 6, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1740.0, "option_spread_pct": 7.38, "option_volume": 66.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.712, "shadow_only": true, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.473, "top_candidates": [{"current_drop_pct": 1.03, "early_entry_score": 0.704, "early_reclaim_pct": 67.7, "matched_signals": 39, "recovery_stability_score": 0.712, "success_rate": 89.74, "ticker": "CRWD", "timing_score": 0.473, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-22T10:25:01.797338-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                        {"contract_symbol": "MELI260821C01800000", "current_drop_pct": 0.98, "early_entry_score": 0.749, "early_reclaim_pct": 63.4, "entry_ask": 121.7, "entry_bid": 103.0, "entry_mode": "early", "entry_option_price": 112.35, "hypothetical_budget": 8632.13, "hypothetical_contracts": 0, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 111.0, "option_spread_pct": 16.64, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 93.75, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.749, "early_reclaim_pct": 63.4, "matched_signals": 32, "recovery_stability_score": 0.662, "success_rate": 93.75, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-22T10:20:05.679884-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "FTNT260821C00165000", "current_drop_pct": 0.57, "early_entry_score": 0.86, "early_reclaim_pct": 72.4, "entry_ask": 10.75, "entry_bid": 9.9, "entry_mode": "early", "entry_option_price": 10.325, "hypothetical_budget": 8632.13, "hypothetical_contracts": 8, "matched_signals": 45, "option_liquidity_status": "ok", "option_open_interest": 717.0, "option_spread_pct": 8.23, "option_volume": 44.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.792, "shadow_only": true, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.427, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.86, "early_reclaim_pct": 72.4, "matched_signals": 45, "recovery_stability_score": 0.792, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.427, "trend_health_status": "ok"}, {"current_drop_pct": 0.93, "early_entry_score": 0.766, "early_reclaim_pct": 65.3, "matched_signals": 33, "recovery_stability_score": 0.781, "success_rate": 93.94, "ticker": "MELI", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260722110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260722110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260722110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260722110506)

</details>
