# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 14:55:02 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$17,610.75`
- Equity: `$33,370.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-05                   0     16     15760.0                 15760.0         9.85           9.85       98.17          98.6          bid_ask_mid                       9.85                bid_ask_mid                    True             0.0                    0.0         95.65               23              3.29          79.1           77.55                  86.36                1414.0           56.0               0.11                      ok
```

## Today's Closed Trades (2026-06-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SOXL     option         option SOXL260717C00270000      2          2026-06-04         2026-06-05        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           88.24               34            1.10              1.14        147.42                69.97         0.568          pass              0.625             62.8                           0.725               14.16              1.967                                 ok            True                  False
  PANW           81.25               16            2.25              4.39        277.37                60.15         0.566          pass              0.194             21.3                           0.291                7.93              1.280                                 ok            True                  False
  ROST           92.31               26            1.01              1.64        232.36                43.36         0.537          pass              0.672             61.2                           0.417               -1.75             -0.109                                 ok            True                  False
  TEAM           96.15               26            2.86              2.03        100.63                86.36         0.534          pass              0.676             38.5                           0.320               15.43              1.842                                 ok            True                  False
   APP           85.00               40            0.87              3.41        557.41                74.69         0.502          pass              0.498             38.1                           0.213               14.02              1.766                                 ok            True                  False
    ZS           75.00               12            3.99              3.78        133.64               157.69         0.832          pass              0.121              8.2                           0.193              -28.79             -2.389            downtrend_blocked_slope           False                  False
  MELI           91.67               24            1.64             18.79       1626.73                60.42         0.613          pass              0.470              1.5                           0.169               -3.39             -0.355            downtrend_blocked_slope           False                  False
  CTSH           94.29               35            0.43              0.16         53.33                51.38         0.535          pass              0.845             81.3                           0.640                0.80              0.179                                 ok           False                  False
  ADSK           88.89               27            1.17              1.91        232.82                42.86         0.530          pass              0.454             17.0                           0.161               -4.18             -0.359            downtrend_blocked_slope           False                  False
  TTWO           96.43               28            1.10              1.67        215.94                37.81         0.519          pass              0.661             29.6                           0.358               -5.84             -0.354            downtrend_blocked_slope           False                  False
  AMZN           90.00               10            2.08              3.70        252.20                26.09         0.516          pass              0.360             14.1                           0.237               -6.69             -0.863 downtrend_blocked_slope_and_streak           False                  False
  PCAR           78.95               19            1.21              1.00        117.64                26.01         0.503          pass              0.115              1.7                           0.154                6.66              0.677                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-06-05T14:55:02.045804-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-06-05T14:50:02.059586-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 15760.0, "asset_type": "option", "contract_symbol": "TEAM260717C00100000", "contracts": 16, "early_entry_score": 0.627, "entry_mode": "regular", "entry_option_price": 9.85, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 1414.0, "option_spread_pct": 11.17, "option_volume": 56.0, "success_rate": 95.65, "ticker": "TEAM", "timing_score": 0.524}
2026-06-05T14:50:02.059586-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"early_entry_score": 0.774, "option_liquidity_status": "low_volume", "option_open_interest": 374.0, "option_spread_pct": 9.63, "option_volume": 3.0, "reason": "no_trade_low_option_liquidity", "ticker": "ROST", "timing_score": 0.527}
2026-06-05T14:50:02.059586-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"early_entry_score": 0.624, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 359.0, "option_spread_pct": 16.53, "option_volume": 18.0, "reason": "no_trade_low_option_liquidity", "ticker": "WDAY", "timing_score": 0.567}
2026-06-05T14:50:02.059586-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-05", "training_samples": 5221, "window": 5}
2026-06-05T12:00:02.830136-04:00 early_entry_1200      early_entry_shadow  {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.78, "early_entry_score": 0.748, "early_reclaim_pct": 69.8, "entry_ask": 17.4, "entry_bid": 16.75, "entry_mode": "early", "entry_option_price": 17.075, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 3.81, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.748, "early_reclaim_pct": 69.8, "matched_signals": 36, "recovery_stability_score": 0.673, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:55:06.016628-04:00 early_entry_1155      early_entry_shadow {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 0.86, "early_entry_score": 0.738, "early_reclaim_pct": 66.8, "entry_ask": 17.15, "entry_bid": 16.0, "entry_mode": "early", "entry_option_price": 16.575, "hypothetical_budget": 16685.38, "hypothetical_contracts": 10, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 6.94, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.624, "shadow_only": true, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.537, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.738, "early_reclaim_pct": 66.8, "matched_signals": 36, "recovery_stability_score": 0.624, "success_rate": 91.67, "ticker": "PANW", "timing_score": 0.537, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:50:01.555393-04:00 early_entry_1150      early_entry_shadow    {"contract_symbol": "PANW260717C00280000", "current_drop_pct": 1.0, "early_entry_score": 0.709, "early_reclaim_pct": 61.4, "entry_ask": 17.15, "entry_bid": 16.5, "entry_mode": "early", "entry_option_price": 16.825, "hypothetical_budget": 16685.38, "hypothetical_contracts": 9, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 1840.0, "option_spread_pct": 3.86, "option_volume": 117.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.562, "shadow_only": true, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.535, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.709, "early_reclaim_pct": 61.4, "matched_signals": 35, "recovery_stability_score": 0.562, "success_rate": 91.43, "ticker": "PANW", "timing_score": 0.535, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-05T11:45:02.029445-04:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T11:40:05.991728-04:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605145502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605145502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605145502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605145502)

</details>
