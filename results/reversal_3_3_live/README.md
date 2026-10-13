# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 15:35:04 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$71,454.30`
- Equity: `$141,174.30`
- Realized PnL: `$132,574.30`
- Unrealized PnL: `$-1,400.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS261120C00500000       2026-10-13                   0     28     71120.0                 69720.0         25.4           24.9      497.42        496.84          bid_ask_mid                       24.9                bid_ask_mid                    True         -1400.0                  -1.97         85.71               28              1.01         41.83           41.67                  52.43                 422.0           34.0               0.06                      ok
```

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0   27.397260 take_profit_day2_hit_at_scan
   CEG     option         option  CEG261120C00290000     31          2026-10-12         2026-10-13        18.65       21.65  9300.0   16.085791 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           85.19               27            1.13              3.97        500.81                52.43         0.567            pass              0.481             57.5                           0.406               19.69              1.503                                 ok            True                  False
  SHOP           85.19               27            1.46              1.84        178.43                48.43         0.532            pass              0.459             51.5                           0.284               19.11              2.040                                 ok            True                  False
  MSTR           91.43               35            0.64              0.68        152.39                78.93         0.640            pass              0.599             21.1                           0.294               -1.91             -0.367            downtrend_blocked_slope           False                  False
  SOXL           87.10               31            1.65              1.48        127.76                96.52         0.581            pass              0.637             83.1                           0.909              -14.10             -1.745 downtrend_blocked_slope_and_streak           False                  False
   STX           82.76               29            1.99             10.50        748.75                70.16         0.522            pass              0.483             77.0                           0.695              -19.18             -2.470            downtrend_blocked_slope           False                  False
  CSCO           94.29               35            0.16              0.13        115.28                34.19         0.507            pass              0.876             92.6                           0.793                8.09              0.941                                 ok           False                  False
  MDLZ           93.75               32            0.02              0.01         61.79                19.83         0.497 below_threshold              0.855             97.4                           0.799                5.06              0.678                                 ok           False                  False
  GILD           84.62               13            1.37              1.44        149.81                19.66         0.496 below_threshold              0.298             35.0                           0.624               -1.92              0.056           downtrend_blocked_streak           False                  False
  AMGN           79.17               24            0.95              2.79        416.38                27.37         0.493 below_threshold              0.260             39.1                           0.499               -2.37             -0.051           downtrend_blocked_streak           False                  False
  MELI           81.40               43            0.40              5.28       1890.18                42.28         0.489 below_threshold              0.475             63.1                           0.407                9.28              1.215                                 ok           False                  False
  INTU           89.47               38            0.20              0.43        305.81                36.45         0.484 below_threshold              0.687             66.5                           0.322               14.47              1.398                                 ok           False                  False
   WDC           72.00               25            2.61              7.08        383.91                63.46         0.481 below_threshold              0.356             69.3                           0.676              -16.90             -2.018            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-13T15:10:06.535380-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-13T15:05:06.894886-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-13T15:00:04.732732-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-13T14:55:06.347378-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-10-13T14:50:04.759460-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"allocated_cash": 71120.0, "asset_type": "option", "contract_symbol": "SNPS261120C00500000", "contracts": 28, "early_entry_score": 0.515, "entry_mode": "regular", "entry_option_price": 25.4, "execution_mode": "option", "matched_signals": 28, "option_liquidity_status": "ok", "option_open_interest": 422.0, "option_spread_pct": 5.51, "option_volume": 34.0, "success_rate": 85.71, "ticker": "SNPS", "timing_score": 0.568}
2026-10-13T14:50:04.759460-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-13", "training_samples": 6038, "window": 5}
2026-10-13T12:00:04.609468-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "MRVL261120C00260000", "current_drop_pct": 0.68, "early_entry_score": 0.706, "early_reclaim_pct": 89.7, "entry_ask": 20.5, "entry_bid": 20.05, "entry_mode": "early", "entry_option_price": 20.275, "hypothetical_budget": 71287.15, "hypothetical_contracts": 35, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 3428.0, "option_spread_pct": 2.22, "option_volume": 501.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.919, "shadow_only": true, "success_rate": 88.57, "ticker": "MRVL", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.706, "early_reclaim_pct": 89.7, "matched_signals": 35, "recovery_stability_score": 0.919, "success_rate": 88.57, "ticker": "MRVL", "timing_score": 0.415, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.698, "early_reclaim_pct": 61.7, "matched_signals": 41, "recovery_stability_score": 0.623, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.398, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-13T11:55:06.360057-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.67, "early_entry_score": 0.694, "early_reclaim_pct": 60.5, "entry_ask": 29.6, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 20.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.631, "shadow_only": true, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.694, "early_reclaim_pct": 60.5, "matched_signals": 41, "recovery_stability_score": 0.631, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:50:05.756508-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:45:05.731226-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013153504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013153504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013153504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013153504)

</details>
