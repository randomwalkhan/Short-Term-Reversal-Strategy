# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-30 09:35:06 EDT`
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
  MSTR     option         option MSTR261120C00155000       2026-09-29                   1     24     38160.0                 38640.0         15.9           16.1      154.43        156.76     last_price_stale                        NaN                unavailable                   False           480.0                   1.26          93.1               29              1.72         68.77             0.0                  99.69                1758.0          230.0               0.02                      ok
```

## Today's Closed Trades (2026-09-30)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           83.33               30            0.98              0.42         61.17                54.99         0.589            pass              0.403             40.5                           0.288                9.80              0.611                                 ok            True                  False
  MRVL           82.86               35            0.92              1.70        262.54                56.16         0.556            pass              0.314              5.3                           0.176               13.55              1.007                                 ok            True                  False
  META           69.23               13            2.12             10.97        734.09                54.80         0.572            pass              0.091              4.7                           0.133                7.48              0.894                                 ok           False                  False
  AMAT           82.93               41            0.00              0.01        512.01                51.71         0.567            pass              0.634             99.8                           0.612               23.26              2.024                                 ok           False                  False
   STX           86.49               37            0.10              0.61        913.19                53.64         0.557            pass              0.658             83.1                           0.487               16.62              1.432                                 ok           False                  False
  ASML           83.33               36            0.40              5.12       1832.20                42.72         0.551            pass              0.484             55.4                           0.475               14.03              1.193                                 ok           False                  False
   WBD           95.56               45            0.02              0.00         30.85                37.86         0.545            pass              0.904             83.3                           0.467                9.89              1.042                                 ok           False                  False
  KLAC           78.05               41            0.19              0.27        196.42                49.05         0.541            pass              0.509             85.0                           0.480               17.20              1.485                                 ok           False                  False
  ADBE           90.48               42            0.20              0.32        233.03                42.28         0.513            pass              0.718             62.3                           0.317               -7.10             -0.933            downtrend_blocked_slope           False                  False
  ALNY           84.44               45            0.23              0.42        253.89                45.82         0.503            pass              0.607             79.3                           0.598                5.90              0.636                                 ok           False                  False
  PYPL           94.44               36            0.55              0.21         53.80                34.93         0.498 below_threshold              0.608              0.0                           0.082                1.68              0.313                                 ok           False                  False
  ADSK           80.56               36            0.82              1.17        202.68                48.05         0.496 below_threshold              0.385             49.1                           0.400               -8.53             -0.913 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260930093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260930093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260930093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260930093506)

</details>
