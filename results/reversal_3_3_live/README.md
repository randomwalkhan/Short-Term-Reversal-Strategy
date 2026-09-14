# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-14 15:55:01 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$38,116.10`
- Equity: `$77,116.10`
- Realized PnL: `$66,116.10`
- Unrealized PnL: `$1,000.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261016C00043000       2026-09-14                   0    400     38000.0                 39000.0         0.95           0.98       42.87         42.76          bid_ask_mid                       0.98                bid_ask_mid                    True          1000.0                   2.63         100.0               11              0.67         20.46            23.1                  14.68                 123.0           93.0               0.11                      ok
```

## Today's Closed Trades (2026-09-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   AEP           87.50               16            0.80              0.69        123.03                16.49         0.514            pass              0.404             37.4                           0.309                0.02              0.060                                 ok            True                  False
   KHC           91.67               12            0.75              0.13         24.54                26.10         0.572            pass              0.513             43.9                           0.450               -3.48             -0.469            downtrend_blocked_slope           False                  False
   EXC          100.00                8            1.00              0.30         43.03                14.68         0.549            pass              0.525             23.2                           0.243               -1.81             -0.094           downtrend_blocked_streak           False                  False
 CMCSA           94.44               18            1.45              0.26         25.09                34.99         0.535            pass              0.508              5.2                           0.084               -8.22             -0.877 downtrend_blocked_slope_and_streak           False                  False
  NVDA           87.50                8            3.27              5.00        216.15                43.68         0.523            pass              0.323             23.7                           0.305               -2.83             -0.170           downtrend_blocked_streak           False                  False
  CHTR           91.18               34            1.59              1.62        145.07                68.13         0.519            pass              0.645             45.2                           0.228               -6.62             -0.928            downtrend_blocked_slope           False                  False
  UPRO           90.91               22            1.30              1.34        147.44                26.03         0.505            pass              0.566             48.2                           0.427               -3.74             -0.328 downtrend_blocked_slope_and_streak           False                  False
   XEL           83.33                6            1.86              0.98         75.08                16.49         0.504            pass              0.153              4.4                           0.175               -3.08             -0.146                                 ok           False                  False
  AMZN           73.08               26            1.11              2.00        255.92                26.09         0.469 below_threshold              0.312             52.7                           0.570               -4.69             -0.318 downtrend_blocked_slope_and_streak           False                  False
  SNPS           25.00                4            4.25             11.82        392.31                60.55         0.469 below_threshold              0.061              4.8                           0.173              -14.03             -1.330            downtrend_blocked_slope           False                  False
   LIN           77.78               27            0.40              1.32        465.65                15.11         0.459 below_threshold              0.343             61.3                           0.558               -4.83             -0.626 downtrend_blocked_slope_and_streak           False                  False
  CSCO           70.59               17            1.84              1.44        111.51                22.50         0.452 below_threshold              0.171             26.4                           0.176                0.13              0.006                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-09-14T15:10:01.099454-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-09-14T15:05:01.081991-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-09-14T15:00:05.039225-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-09-14T14:55:02.132179-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-09-14T14:50:04.030674-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"allocated_cash": 38000.0, "asset_type": "option", "contract_symbol": "EXC261016C00043000", "contracts": 400, "early_entry_score": 0.606, "entry_mode": "regular", "entry_option_price": 0.95, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 123.0, "option_spread_pct": 10.53, "option_volume": 93.0, "success_rate": 100.0, "ticker": "EXC", "timing_score": 0.551}
2026-09-14T14:50:04.030674-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-14", "training_samples": 5764, "window": 5}
2026-09-14T12:00:04.262790-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.804, "early_reclaim_pct": 69.6, "matched_signals": 33, "recovery_stability_score": 0.663, "success_rate": 96.97, "ticker": "PCAR", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:55:01.111232-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.8, "early_entry_score": 0.783, "early_reclaim_pct": 66.7, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.8, "early_entry_score": 0.783, "early_reclaim_pct": 66.7, "matched_signals": 31, "recovery_stability_score": 0.61, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:50:01.134863-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.777, "early_reclaim_pct": 64.9, "matched_signals": 31, "recovery_stability_score": 0.577, "success_rate": 96.77, "ticker": "PCAR", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-14T11:45:04.190429-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "PCAR261016C00120000", "current_drop_pct": 0.71, "early_entry_score": 0.813, "early_reclaim_pct": 70.4, "entry_ask": 6.2, "entry_bid": 4.0, "entry_mode": "early", "entry_option_price": 5.1, "hypothetical_budget": 38058.05, "hypothetical_contracts": 74, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 21.0, "option_spread_pct": 43.14, "option_volume": 19.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.572, "shadow_only": true, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.813, "early_reclaim_pct": 70.4, "matched_signals": 34, "recovery_stability_score": 0.572, "success_rate": 97.06, "ticker": "PCAR", "timing_score": 0.416, "trend_health_status": "ok"}, {"current_drop_pct": 1.43, "early_entry_score": 0.671, "early_reclaim_pct": 81.0, "matched_signals": 34, "recovery_stability_score": 0.937, "success_rate": 88.24, "ticker": "STX", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260914155501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260914155501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260914155501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260914155501)

</details>
