# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 09:30:05 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$40,598.30`
- Equity: `$79,238.30`
- Realized PnL: `$68,758.30`
- Unrealized PnL: `$480.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261120C00155000       2026-09-29                   1     24     38160.0                 38640.0         15.9           16.1      154.43        161.97     last_price_stale                        NaN                unavailable                   False           480.0                   1.26          93.1               29              1.72         68.77             0.0                  99.69                1758.0          230.0               0.02                      ok
```

## Today's Closed Trades (2026-09-30)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  DRAM           82.35               34            0.57              0.25         61.25                54.99         0.590          pass              0.477             65.2                           0.436               10.25              0.629                       ok            True                  False
   CEG           90.32               31            0.79              1.46        263.96                42.03         0.519          pass              0.654             62.3                           0.496                1.14              0.138                       ok            True                  False
  META           76.47               17            1.55              8.02        735.35                54.80         0.596          pass              0.115              2.8                           0.061                8.11              0.920                       ok           False                  False
   TRI           89.74               39            0.18              0.12         96.19                56.37         0.595          pass              0.625             37.6                           0.463               -5.17             -0.168 downtrend_blocked_streak           False                  False
  MRVL           83.78               37            0.13              0.24        263.17                56.16         0.595          pass              0.600             86.4                           0.521               14.46              1.043                       ok           False                  False
  CRWD           89.13               46            0.19              0.35        262.59                69.80         0.579          pass              0.541             13.2                           0.194                8.65              0.913                       ok           False                  False
  SHOP           86.36               44            0.15              0.15        148.20                61.90         0.558          pass              0.655             76.6                           0.467               13.92              1.461                       ok           False                  False
  ASML           83.33               36            0.39              4.95       1832.27                42.72         0.552          pass              0.488             56.9                           0.353               14.05              1.194                       ok           False                  False
  MPWR           89.74               39            0.28              2.63       1352.86                52.13         0.545          pass              0.755             82.5                           0.400               17.66              1.654                       ok           False                  False
  KLAC           79.07               43            0.03              0.04        196.51                49.05         0.541          pass              0.548             97.9                           0.562               17.40              1.493                       ok           False                  False
  TMUS           89.19               37            0.10              0.11        162.93                33.84         0.502          pass              0.714             79.5                           0.496               -7.63             -0.447  downtrend_blocked_slope           False                  False
  PYPL           91.89               37            0.39              0.15         53.83                34.93         0.501          pass              0.547              0.0                           0.250                1.84              0.320                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-30T00:00:05.973499-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 92, 'empty': 1}
2026-09-29T15:10:01.396429-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-29T15:05:05.953732-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-29T15:00:06.204288-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-29T14:55:06.447137-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-29T14:50:06.330440-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 38160.0, "asset_type": "option", "contract_symbol": "MSTR261120C00155000", "contracts": 24, "early_entry_score": 0.675, "entry_mode": "regular", "entry_option_price": 15.9, "execution_mode": "option", "matched_signals": 29, "option_liquidity_status": "ok", "option_open_interest": 1758.0, "option_spread_pct": 1.89, "option_volume": 230.0, "success_rate": 93.1, "ticker": "MSTR", "timing_score": 0.682}
2026-09-29T14:50:06.330440-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-29", "training_samples": 5875, "window": 5}
2026-09-29T12:00:02.521898-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.71, "early_entry_score": 0.849, "early_reclaim_pct": 85.5, "entry_ask": 2.4, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.275, "hypothetical_budget": 39379.15, "hypothetical_contracts": 173, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 10.99, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.386, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.849, "early_reclaim_pct": 85.5, "matched_signals": 33, "recovery_stability_score": 0.603, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.386, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:55:06.341077-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.72, "early_entry_score": 0.848, "early_reclaim_pct": 85.3, "entry_ask": 2.35, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.25, "hypothetical_budget": 39379.15, "hypothetical_contracts": 175, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 8.89, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.577, "shadow_only": true, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.385, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.848, "early_reclaim_pct": 85.3, "matched_signals": 33, "recovery_stability_score": 0.577, "success_rate": 96.97, "ticker": "FAST", "timing_score": 0.385, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-29T11:50:06.042061-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "FAST261120C00050000", "current_drop_pct": 0.82, "early_entry_score": 0.829, "early_reclaim_pct": 83.3, "entry_ask": 2.4, "entry_bid": 2.15, "entry_mode": "early", "entry_option_price": 2.275, "hypothetical_budget": 39379.15, "hypothetical_contracts": 173, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 3440.0, "option_spread_pct": 10.99, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 96.77, "ticker": "FAST", "timing_score": 0.39, "top_candidates": [{"current_drop_pct": 0.82, "early_entry_score": 0.829, "early_reclaim_pct": 83.3, "matched_signals": 31, "recovery_stability_score": 0.556, "success_rate": 96.77, "ticker": "FAST", "timing_score": 0.39, "trend_health_status": "ok"}, {"current_drop_pct": 0.86, "early_entry_score": 0.711, "early_reclaim_pct": 61.4, "matched_signals": 42, "recovery_stability_score": 0.711, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930093005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930093005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930093005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930093005)

</details>
