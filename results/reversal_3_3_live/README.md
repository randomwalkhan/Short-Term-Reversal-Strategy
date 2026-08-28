# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-28 15:55:04 EDT`
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

- Cash: `$26,688.10`
- Equity: `$53,223.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$435.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SHOP     option         option SHOP261016C00155000       2026-08-28                   0     29     26100.0                 26535.0          9.0           9.15      153.02        152.76          bid_ask_mid                       9.15                bid_ask_mid                    True           435.0                   1.67         94.59               37              0.85         45.17           45.65                  69.26                 763.0          153.0               0.07                      ok
```

## Today's Closed Trades (2026-08-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SHOP           94.29               35            1.02              1.10        153.86                69.26         0.618          pass              0.658             16.2                           0.214               -1.01              0.263                                 ok            True                  False
  AMGN          100.00               14            1.08              3.31        435.57                27.65         0.594          pass              0.560             24.6                           0.421                4.72              0.527                                 ok            True                  False
   MAR           96.15               26            0.78              1.92        353.05                33.75         0.568          pass              0.594             10.3                           0.163               -1.37             -0.065                                 ok            True                  False
  REGN          100.00               10            1.68              9.52        803.63                24.94         0.534          pass              0.600             48.9                           0.441               -1.05             -0.034                                 ok            True                  False
  GILD          100.00               11            2.09              2.18        147.93                26.47         0.530          pass              0.525             21.7                           0.472                5.34              0.610                                 ok            True                  False
  VRTX           96.55               29            1.11              4.25        545.73                32.96         0.518          pass              0.681             34.1                           0.369                7.06              0.641                                 ok            True                  False
  INSM           73.33               15            2.44              2.07        120.50               110.68         0.782          pass              0.202             30.2                           0.316               -4.29             -0.594            downtrend_blocked_slope           False                  False
   WDC           77.14               35            0.44              1.42        461.39                85.14         0.629          pass              0.479             83.0                           0.532               -9.60             -1.266            downtrend_blocked_slope           False                  False
  DRAM           78.12               32            1.64              0.65         56.55                68.22         0.555          pass              0.367             55.1                           0.480               -2.48             -0.290            downtrend_blocked_slope           False                  False
  CSCO           66.67               15            2.06              1.61        111.46                41.41         0.548          pass              0.105              5.5                           0.248               -1.64             -0.067                                 ok           False                  False
   STX           81.48               27            2.12             12.60        841.80                71.05         0.547          pass              0.259             17.1                           0.261              -14.82             -1.577            downtrend_blocked_slope           False                  False
   AEP           95.45               22            0.44              0.38        122.55                17.88         0.544          pass              0.639             34.9                           0.428               -2.73             -0.381 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-08-28T15:10:06.157177-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T15:05:06.122448-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T15:00:05.692919-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T14:55:06.265436-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "already_processed"}
2026-08-28T14:50:05.181555-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"allocated_cash": 26100.0, "asset_type": "option", "contract_symbol": "SHOP261016C00155000", "contracts": 29, "early_entry_score": 0.689, "entry_mode": "regular", "entry_option_price": 9.0, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 763.0, "option_spread_pct": 6.67, "option_volume": 153.0, "success_rate": 94.59, "ticker": "SHOP", "timing_score": 0.617}
2026-08-28T14:50:05.181555-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-28", "training_samples": 5729, "window": 5}
2026-08-28T12:00:05.127019-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:55:02.090702-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-28T11:50:05.095730-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "entry_ask": 19.8, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.7, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 11.76, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "matched_signals": 42, "recovery_stability_score": 0.663, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "trend_health_status": "ok"}, {"current_drop_pct": 0.54, "early_entry_score": 0.821, "early_reclaim_pct": 67.7, "matched_signals": 35, "recovery_stability_score": 0.659, "success_rate": 97.14, "ticker": "VRTX", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-28T11:45:05.139618-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "ZS261016C00185000", "current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "entry_ask": 19.6, "entry_bid": 17.6, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 26394.05, "hypothetical_contracts": 14, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 31.0, "option_spread_pct": 10.75, "option_volume": 6.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.887, "early_reclaim_pct": 79.0, "matched_signals": 42, "recovery_stability_score": 0.749, "success_rate": 95.24, "ticker": "ZS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260828155504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260828155504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260828155504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260828155504)

</details>
