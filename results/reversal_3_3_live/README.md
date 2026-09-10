# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 14:50:04 EDT`
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

- Cash: `$35,166.10`
- Equity: `$69,741.10`
- Realized PnL: `$59,741.10`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261016C00130000       2026-09-10                   0     30     34575.0                 34575.0        11.52          11.52      129.47        129.47          bid_ask_mid                      11.52                bid_ask_mid                    True             0.0                    0.0          80.0               30              2.43          70.7            70.7                 104.12               13089.0          181.0               0.03                      ok
```

## Today's Closed Trades (2026-09-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261009C00135000     34          2026-09-09         2026-09-10        10.85       9.765 -3689.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.00               30            2.43              2.26        131.73               104.12         0.627          pass              0.329             44.2                           0.376                5.10              0.555                                 ok            True                  False
   KHC          100.00               11            0.87              0.15         24.55                28.60         0.602          pass              0.593             41.9                           0.311               -0.02             -0.108                                 ok            True                  False
   EXC           92.31               13            0.50              0.15         43.63                15.30         0.565          pass              0.531             42.1                           0.437               -1.23              0.012                                 ok            True                  False
   STX           86.67               30            1.86             11.55        880.97                74.71         0.546          pass              0.534             56.2                           0.749                2.72              0.545                                 ok            True                  False
  CPRT           85.71               21            1.90              0.43         31.85                45.10         0.510          pass              0.348             23.8                           0.228               -3.83             -0.221                                 ok            True                  False
   CEG           86.67               15            1.80              3.70        292.32                32.56         0.503          pass              0.373             37.3                           0.451                3.26              0.671                                 ok            True                  False
  AMGN          100.00                4            1.99              5.46        388.93                44.45         0.640          pass              0.524             20.1                           0.360              -12.92             -1.247 downtrend_blocked_slope_and_streak           False                  False
  WDAY           91.67               36            0.76              0.99        185.63                77.13         0.636          pass              0.704             52.0                           0.420               -3.20             -0.527 downtrend_blocked_slope_and_streak           False                  False
   TRI           96.88               32            0.73              0.50         96.77                52.79         0.548          pass              0.674             24.1                           0.236               -6.03             -0.744 downtrend_blocked_slope_and_streak           False                  False
  MRVL           76.47               34            2.06              3.38        233.56                80.25         0.535          pass              0.371             52.6                           0.483               -6.09             -0.183           downtrend_blocked_streak           False                  False
  INTU           97.06               34            0.65              1.43        313.33                48.73         0.534          pass              0.766             50.7                           0.390               -9.82             -1.302 downtrend_blocked_slope_and_streak           False                  False
    ZS           96.43               28            2.10              2.45        165.05                64.27         0.527          pass              0.613             13.5                           0.357               -4.52             -1.191            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-09-10T14:50:04.321187-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"allocated_cash": 34575.0, "asset_type": "option", "contract_symbol": "MSTR261016C00130000", "contracts": 30, "early_entry_score": 0.329, "entry_mode": "regular", "entry_option_price": 11.525, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 13089.0, "option_spread_pct": 3.04, "option_volume": 181.0, "success_rate": 80.0, "ticker": "MSTR", "timing_score": 0.627}
2026-09-10T14:50:04.321187-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-10", "training_samples": 5765, "window": 5}
2026-09-10T12:00:03.311742-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:55:04.274439-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "entry_ask": 5.8, "entry_bid": 4.7, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 20.95, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.0, "matched_signals": 37, "recovery_stability_score": 0.651, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:50:01.152194-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "entry_ask": 5.7, "entry_bid": 4.8, "entry_mode": "early", "entry_option_price": 5.25, "hypothetical_budget": 34870.55, "hypothetical_contracts": 66, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 17.14, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.674, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.747, "early_reclaim_pct": 77.8, "matched_signals": 41, "recovery_stability_score": 0.674, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.406, "trend_health_status": "ok"}, {"current_drop_pct": 1.12, "early_entry_score": 0.67, "early_reclaim_pct": 66.3, "matched_signals": 32, "recovery_stability_score": 0.576, "success_rate": 90.62, "ticker": "MCHP", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:45:04.259583-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "entry_ask": 5.9, "entry_bid": 4.4, "entry_mode": "early", "entry_option_price": 5.15, "hypothetical_budget": 34870.55, "hypothetical_contracts": 67, "matched_signals": 41, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 29.13, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.748, "early_reclaim_pct": 78.2, "matched_signals": 41, "recovery_stability_score": 0.664, "success_rate": 90.24, "ticker": "INSM", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:40:01.104202-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                       {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "entry_ask": 5.8, "entry_bid": 5.2, "entry_mode": "early", "entry_option_price": 5.5, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 10.91, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.96, "early_entry_score": 0.684, "early_reclaim_pct": 72.5, "matched_signals": 37, "recovery_stability_score": 0.632, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:35:01.128582-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T11:30:05.235557-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "entry_ask": 6.0, "entry_bid": 5.3, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.39, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.653, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.1, "matched_signals": 37, "recovery_stability_score": 0.653, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T11:25:01.128031-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                      {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "entry_ask": 5.8, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.45, "hypothetical_budget": 34870.55, "hypothetical_contracts": 63, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 146.0, "option_spread_pct": 12.84, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.629, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.91, "early_entry_score": 0.689, "early_reclaim_pct": 74.1, "matched_signals": 37, "recovery_stability_score": 0.629, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.421, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910145004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910145004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910145004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910145004)

</details>
