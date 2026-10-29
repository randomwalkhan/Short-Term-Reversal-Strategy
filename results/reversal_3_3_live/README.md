# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-29 10:05:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$64,409.30`
- Equity: `$126,284.30`
- Realized PnL: `$119,884.30`
- Unrealized PnL: `$-3,600.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CSCO     option         option CSCO261218C00110000       2026-10-28                   1     90     65475.0                 61875.0         7.28           6.88      110.47        109.92          bid_ask_mid                       6.88                bid_ask_mid                    True         -3600.0                   -5.5         80.77               26              0.82         42.92           43.56                  35.12                4095.0         1198.0               0.02                      ok
```

## Today's Closed Trades (2026-10-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           85.71               21            2.90              2.95        143.90                71.12         0.561          pass              0.381             33.0                           0.601               -6.83             -0.084                                 ok            True                  False
  UPRO           83.33               24            1.18              1.25        150.60                30.20         0.514          pass              0.357             41.0                           0.580               -1.43             -0.007                                 ok            True                  False
  SOXL           68.18               22            5.59              4.20        105.55               137.18         0.582          pass              0.261             40.9                           0.582               -5.59             -0.028                                 ok           False                  False
   WDC           75.56               45            0.16              0.46        396.22                80.12         0.581          pass              0.546             96.1                           0.885               11.03              1.205                                 ok           False                  False
  MPWR           60.00               20            2.29             19.43       1202.89                59.53         0.547          pass              0.246             41.4                           0.485               -5.26             -0.567            downtrend_blocked_slope           False                  False
  NVDA           75.00               20            1.09              1.65        214.67                30.56         0.544          pass              0.207             28.8                           0.293               -1.93             -0.107                                 ok           False                  False
   STX           72.22               36            1.07              5.21        695.74                77.70         0.533          pass              0.452             75.1                           0.743               -0.04              0.172                                 ok           False                  False
  AVGO           50.00               10            2.66              6.54        349.01                43.15         0.521          pass              0.137             28.2                           0.473               -0.54              0.211                                 ok           False                  False
  CSCO           86.49               37            0.20              0.16        110.22                35.33         0.510          pass              0.649             81.8                           0.630                0.20              0.281                                 ok           False                  False
  MELI           72.22               36            0.98             11.45       1668.18                48.85         0.509          pass              0.418             64.5                           0.774              -10.78             -1.338 downtrend_blocked_slope_and_streak           False                  False
  DRAM           62.50               16            3.56              1.35         53.54                63.50         0.507          pass              0.173             27.4                           0.462                5.81              0.917                                 ok           False                  False
    MU           72.22               18            3.22             22.17        973.73                57.32         0.500          pass              0.178             24.8                           0.263                2.18              0.556                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-29T10:05:06.192375-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ADBE261218C00250000", "current_drop_pct": 0.64, "early_entry_score": 0.777, "early_reclaim_pct": 81.8, "entry_ask": 17.25, "entry_bid": 15.55, "entry_mode": "early", "entry_option_price": 16.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 19, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 5906.0, "option_spread_pct": 10.37, "option_volume": 156.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.915, "shadow_only": true, "success_rate": 90.7, "ticker": "ADBE", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.777, "early_reclaim_pct": 81.8, "matched_signals": 43, "recovery_stability_score": 0.915, "success_rate": 90.7, "ticker": "ADBE", "timing_score": 0.464, "trend_health_status": "ok"}, {"current_drop_pct": 1.41, "early_entry_score": 0.758, "early_reclaim_pct": 84.8, "matched_signals": 34, "recovery_stability_score": 0.949, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T10:00:05.728324-04:00 early_entry_1000 early_entry_shadow      {"contract_symbol": "MCHP261218C00077500", "current_drop_pct": 0.67, "early_entry_score": 0.753, "early_reclaim_pct": 84.2, "entry_ask": 7.9, "entry_bid": 6.9, "entry_mode": "early", "entry_option_price": 7.4, "hypothetical_budget": 32204.65, "hypothetical_contracts": 43, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 827.0, "option_spread_pct": 13.51, "option_volume": 22.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.753, "early_reclaim_pct": 84.2, "matched_signals": 39, "recovery_stability_score": 0.707, "success_rate": 89.74, "ticker": "MCHP", "timing_score": 0.469, "trend_health_status": "ok"}, {"current_drop_pct": 0.83, "early_entry_score": 0.742, "early_reclaim_pct": 76.3, "matched_signals": 40, "recovery_stability_score": 0.898, "success_rate": 90.0, "ticker": "ADBE", "timing_score": 0.47, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T00:00:06.637519-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-10-28T15:50:06.462666-04:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TEAM261218C00230000", "fill_price": 19.1, "pnl": -2880.0, "reason": "time_exit_at_4pm_scan", "return_pct": -4.5, "ticker": "TEAM"}
2026-10-28T15:10:04.409011-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-28T15:05:05.708724-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-28T15:00:05.530535-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-28T14:55:06.400966-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-28T14:50:01.756543-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-28", "training_samples": 6213, "window": 5}
2026-10-28T14:50:01.756543-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"allocated_cash": 65475.0, "asset_type": "option", "contract_symbol": "CSCO261218C00110000", "contracts": 90, "early_entry_score": 0.34, "entry_mode": "regular", "entry_option_price": 7.275, "execution_mode": "option", "matched_signals": 26, "option_liquidity_status": "ok", "option_open_interest": 4095.0, "option_spread_pct": 2.06, "option_volume": 1198.0, "success_rate": 80.77, "ticker": "CSCO", "timing_score": 0.533}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261029100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261029100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261029100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261029100506)

</details>
