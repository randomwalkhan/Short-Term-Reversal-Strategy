# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 14:50:05 EDT`
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

- Cash: `$17,739.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-08-03                   0    106     17490.0                 17490.0         1.65           1.65       49.76         49.74          bid_ask_mid                       1.65                bid_ask_mid                    True             0.0                    0.0         100.0               11              1.28         25.54           25.54                  27.78                2866.0          205.0               0.06                      ok
```

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX          100.00               11            1.28              0.45         50.21                27.78         0.614          pass              0.481              4.4                           0.292               -0.71             -0.096                                 ok            True                  False
  MDLZ           93.33               15            1.13              0.49         62.10                33.81         0.596          pass              0.494             15.1                           0.281                2.22              0.516                                 ok            True                  False
   EXC           93.75               16            1.00              0.32         45.68                22.49         0.559          pass              0.487              8.0                           0.145               -1.31             -0.145                                 ok            True                  False
  AMGN          100.00               13            1.56              4.22        383.35                25.80         0.525          pass              0.576             34.5                           0.489                4.11              0.640                                 ok            True                  False
   WDC           84.00               25            2.70             10.30        540.43               105.07         0.520          pass              0.457             66.2                           0.464                8.76             -0.208                                 ok            True                  False
  LRCX           89.19               37            0.28              0.57        292.78                90.68         0.603          pass              0.770             95.0                           0.566               -4.74             -1.298 downtrend_blocked_slope_and_streak           False                  False
  AAPL           94.44               18            1.24              2.69        307.76                37.33         0.590          pass              0.616             39.4                           0.267               -6.59             -0.353 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               11            1.18              0.64         77.92                17.46         0.563          pass              0.469              2.1                           0.200               -1.77             -0.234           downtrend_blocked_streak           False                  False
   KDP           78.95               19            0.87              0.19         31.04                33.11         0.557          pass              0.131              5.3                           0.141                1.35              0.438                                 ok           False                  False
  CTAS           95.00               40            0.10              0.15        204.57                38.81         0.539          pass              0.888             78.1                           0.543                1.30              0.361                                 ok           False                  False
   PEP           87.10               31            0.25              0.24        139.46                26.18         0.536          pass              0.559             58.8                           0.510                2.77              0.487                                 ok           False                  False
  KLAC           86.21               29            1.28              1.64        182.12                69.24         0.529          pass              0.560             71.5                           0.537              -13.06             -2.290 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-08-03T14:50:05.995871-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"allocated_cash": 17490.0, "asset_type": "option", "contract_symbol": "CSX260918C00050000", "contracts": 106, "early_entry_score": 0.481, "entry_mode": "regular", "entry_option_price": 1.65, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 2866.0, "option_spread_pct": 6.06, "option_volume": 205.0, "success_rate": 100.0, "ticker": "CSX", "timing_score": 0.614}
2026-08-03T14:50:05.995871-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-03", "training_samples": 5546, "window": 5}
2026-08-03T12:00:03.854898-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "CDNS260918C00335000", "current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "entry_ask": 25.3, "entry_bid": 22.6, "entry_mode": "early", "entry_option_price": 23.95, "hypothetical_budget": 17614.88, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.27, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "matched_signals": 45, "recovery_stability_score": 0.703, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-03T11:55:02.829313-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:50:02.007481-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:45:01.947551-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:40:02.921785-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:35:06.072757-04:00 early_entry_1135 early_entry_shadow                                       {"contract_symbol": "CSCO260918C00115000", "current_drop_pct": 0.5, "early_entry_score": 0.697, "early_reclaim_pct": 75.4, "entry_ask": 8.45, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.325, "hypothetical_budget": 17614.88, "hypothetical_contracts": 21, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 5712.0, "option_spread_pct": 3.0, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.671, "shadow_only": true, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.697, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.671, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T11:30:04.782483-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:25:05.765544-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803145005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803145005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803145005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803145005)

</details>
