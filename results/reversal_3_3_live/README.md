# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-26 13:15:05 EDT`
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

- Cash: `$27,460.60`
- Equity: `$54,505.60`
- Realized PnL: `$44,775.60`
- Unrealized PnL: `$-270.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX261016C00310000       2026-08-24                   2      9     27315.0                 27045.0        30.35          30.05      310.66        313.31          bid_ask_mid                      30.05                bid_ask_mid                    True          -270.0                  -0.99          87.5               32              1.06         63.04           60.36                   88.6                 214.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-26)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KHC     option         option KHC261016C00025000    287          2026-08-25         2026-08-26         1.02       0.918 -2927.4       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MNST           87.50               16            1.21              0.41         48.55               552.32         1.000          pass              0.354              4.7                           0.282                4.70              0.575                                 ok            True                  False
  ABNB           96.30               27            1.10              1.47        189.87                61.60         0.660          pass              0.636             19.0                           0.394                4.61              0.487                                 ok            True                  False
  SHOP           90.62               32            1.52              1.64        153.18                72.08         0.618          pass              0.580             29.3                           0.329                0.75             -0.144                                 ok            True                  False
   TRI           88.89               27            1.55              1.13        103.89                66.28         0.608          pass              0.567             52.1                           0.537                0.80              0.325                                 ok            True                  False
  WDAY           82.14               28            2.38              3.23        193.03                76.21         0.589          pass              0.349             37.7                           0.378                8.28              0.263                                 ok            True                  False
  MELI           93.75               16            1.96             27.36       1985.28                47.50         0.567          pass              0.522             19.6                           0.457                7.09              0.984                                 ok            True                  False
  REGN          100.00               20            1.14              6.65        830.71                29.20         0.562          pass              0.658             45.0                           0.662                3.39              0.448                                 ok            True                  False
  CPRT           85.71               21            1.85              0.43         33.15                43.23         0.522          pass              0.280              0.8                           0.122               12.85              1.340                                 ok            True                  False
  BKNG           93.75               16            2.23              3.34        212.35                35.36         0.521          pass              0.508             16.5                           0.468               -1.53              0.004                                 ok            True                  False
  INSM           89.36               47            0.15              0.13        123.84               110.58         0.695          pass              0.809             96.5                           0.689               -6.48             -0.431            downtrend_blocked_slope           False                  False
  AMAT           88.57               35            0.42              1.42        479.43                76.53         0.658          pass              0.681             73.3                           0.659              -12.70             -1.310 downtrend_blocked_slope_and_streak           False                  False
   APP           70.45               44            0.52              1.12        310.06                88.60         0.644          pass              0.458             64.6                           0.523                1.70             -0.130                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-26T12:00:04.193922-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:55:03.284797-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "PYPL261002C00062000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 2.68, "entry_bid": 2.25, "entry_mode": "early", "entry_option_price": 2.465, "hypothetical_budget": 13730.3, "hypothetical_contracts": 55, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 610.0, "option_spread_pct": 17.44, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.702, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.702, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-26T11:50:01.099073-04:00 early_entry_1150 early_entry_shadow                                   {"contract_symbol": "PYPL261016C00065000", "current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "entry_ask": 1.6, "entry_bid": 1.5, "entry_mode": "early", "entry_option_price": 1.55, "hypothetical_budget": 13730.3, "hypothetical_contracts": 88, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 6048.0, "option_spread_pct": 6.45, "option_volume": 584.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.734, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.788, "early_reclaim_pct": 64.9, "matched_signals": 35, "recovery_stability_score": 0.734, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:45:03.275607-04:00 early_entry_1145 early_entry_shadow                                    {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.785, "early_reclaim_pct": 63.9, "matched_signals": 35, "recovery_stability_score": 0.706, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.46, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:40:01.100306-04:00 early_entry_1140 early_entry_shadow                                  {"contract_symbol": "PYPL260925C00060000", "current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "entry_ask": 3.45, "entry_bid": 3.15, "entry_mode": "early", "entry_option_price": 3.3, "hypothetical_budget": 13730.3, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 240.0, "option_spread_pct": 9.09, "option_volume": 52.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.684, "shadow_only": true, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.776, "early_reclaim_pct": 60.9, "matched_signals": 35, "recovery_stability_score": 0.684, "success_rate": 94.29, "ticker": "PYPL", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-26T11:35:01.234662-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:30:01.097446-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:25:05.264548-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:20:05.287776-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-26T11:15:01.102404-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260826131505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260826131505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260826131505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260826131505)

</details>
