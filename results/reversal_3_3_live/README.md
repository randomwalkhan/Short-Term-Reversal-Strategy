# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-09 09:40:01 EDT`
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

- Cash: `$39,968.10`
- Equity: `$75,172.10`
- Realized PnL: `$67,148.10`
- Unrealized PnL: `$-1,976.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  CRWD     option         option CRWD261016C00210000       2026-09-08                   1     26     37180.0                 35204.0         14.3          13.54      209.63        211.71     last_price_stale                        NaN                unavailable                   False         -1976.0                  -5.31         88.89               36              1.63         52.75             0.0                  91.63                 699.0          116.0               0.04                      ok
```

## Today's Closed Trades (2026-09-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   STX           88.89               36            0.57              3.63        902.82                74.46         0.615            pass              0.682             70.0                           0.666                9.43              0.566                                 ok            True                   True
   KHC          100.00               10            0.88              0.15         24.83                28.58         0.614            pass              0.555             31.3                           0.427               -0.97              0.043                                 ok            True                  False
   PEP           87.50               16            0.58              0.56        138.21                16.46         0.547            pass              0.375             26.9                           0.316               -2.21             -0.185                                 ok            True                  False
   WMT           85.71               35            0.54              0.40        105.88                40.18         0.537            pass              0.481             36.0                           0.426                0.09              0.283                                 ok            True                  False
  CPRT           85.71               21            1.84              0.42         32.42                44.55         0.525            pass              0.314             11.8                           0.149               -3.99             -0.105                                 ok            True                  False
  LRCX           81.58               38            0.74              1.67        319.71                52.73         0.515            pass              0.469             62.9                           0.599                1.07             -0.057                                 ok            True                  False
   KDP           84.00               25            1.11              0.25         32.44                29.05         0.507            pass              0.346             29.4                           0.373                1.10              0.208                                 ok            True                  False
  TMUS           94.12               17            1.31              1.67        180.98                25.45         0.500 below_threshold              0.501              9.2                           0.071               -0.70              0.203                                 ok            True                  False
  PYPL           95.45               22            1.02              0.38         53.02                58.35         0.632            pass              0.742             66.2                           0.417              -15.26             -1.451 downtrend_blocked_slope_and_streak           False                  False
  WDAY           92.86               42            0.32              0.42        186.10                77.37         0.622            pass              0.802             65.8                           0.504               -4.49             -0.229                                 ok           False                  False
  AMGN           96.43               28            0.57              1.56        392.50                44.47         0.590            pass              0.707             42.5                           0.287              -11.60             -0.895 downtrend_blocked_slope_and_streak           False                  False
  PAYX          100.00               17            1.15              0.94        116.53                30.90         0.570            pass              0.532              9.5                           0.151               -7.52             -0.752            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-09T00:00:04.345374-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-09-08T15:10:02.485838-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-08T15:05:04.629730-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-08T15:00:03.621763-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-08T14:55:03.619621-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-09-08T14:50:01.652709-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"allocated_cash": 37180.0, "asset_type": "option", "contract_symbol": "CRWD261016C00210000", "contracts": 26, "early_entry_score": 0.637, "entry_mode": "regular", "entry_option_price": 14.3, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 699.0, "option_spread_pct": 4.2, "option_volume": 116.0, "success_rate": 88.89, "ticker": "CRWD", "timing_score": 0.617}
2026-09-08T14:50:01.652709-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-08", "training_samples": 5748, "window": 5}
2026-09-08T12:00:01.401463-04:00 early_entry_1200 early_entry_shadow  {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.67, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "entry_ask": 10.05, "entry_bid": 9.45, "entry_mode": "early", "entry_option_price": 9.75, "hypothetical_budget": 38574.05, "hypothetical_contracts": 39, "matched_signals": 42, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 6.15, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.62, "shadow_only": true, "success_rate": 92.86, "ticker": "FTNT", "timing_score": 0.472, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.817, "early_reclaim_pct": 75.8, "matched_signals": 42, "recovery_stability_score": 0.62, "success_rate": 92.86, "ticker": "FTNT", "timing_score": 0.472, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.716, "early_reclaim_pct": 77.6, "matched_signals": 38, "recovery_stability_score": 0.691, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:55:05.335939-04:00 early_entry_1155 early_entry_shadow    {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.6, "entry_ask": 10.1, "entry_bid": 9.15, "entry_mode": "early", "entry_option_price": 9.625, "hypothetical_budget": 38574.05, "hypothetical_contracts": 40, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 9.87, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.605, "shadow_only": true, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.783, "early_reclaim_pct": 67.6, "matched_signals": 40, "recovery_stability_score": 0.605, "success_rate": 92.5, "ticker": "FTNT", "timing_score": 0.47, "trend_health_status": "ok"}, {"current_drop_pct": 0.97, "early_entry_score": 0.693, "early_reclaim_pct": 74.9, "matched_signals": 37, "recovery_stability_score": 0.648, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.435, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-08T11:50:01.520765-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "FTNT261016C00155000", "current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 73.9, "entry_ask": 10.15, "entry_bid": 9.15, "entry_mode": "early", "entry_option_price": 9.65, "hypothetical_budget": 38574.05, "hypothetical_contracts": 39, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 253.0, "option_spread_pct": 10.36, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.71, "shadow_only": true, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.474, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.807, "early_reclaim_pct": 73.9, "matched_signals": 41, "recovery_stability_score": 0.71, "success_rate": 92.68, "ticker": "FTNT", "timing_score": 0.474, "trend_health_status": "ok"}, {"current_drop_pct": 0.87, "early_entry_score": 0.716, "early_reclaim_pct": 77.6, "matched_signals": 38, "recovery_stability_score": 0.648, "success_rate": 89.47, "ticker": "INSM", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260909094001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260909094001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260909094001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260909094001)

</details>
