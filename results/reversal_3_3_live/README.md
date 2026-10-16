# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-16 15:05:04 EDT`
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

- Cash: `$62,756.80`
- Equity: `$122,256.80`
- Realized PnL: `$112,431.80`
- Unrealized PnL: `$-175.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CEG     option         option CEG261120C00270000       2026-10-16                   0     35     59675.0                 59500.0        17.05           17.0      270.43         270.0          bid_ask_mid                       17.0                bid_ask_mid                    True          -175.0                  -0.29         85.71               21              1.66         51.07           50.16                  60.14                 462.0           59.0               0.05                      ok
```

## Today's Closed Trades (2026-10-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   CEG     option         option CEG261120C00270000     33          2026-10-15         2026-10-16         19.1       17.19 -6303.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           85.71               21            1.87              3.60        273.46                60.14         0.551            pass              0.309              9.5                           0.212                4.80              0.120                                 ok            True                  False
  ABNB           90.00               30            0.96              1.18        173.78                41.32         0.526            pass              0.568             38.5                           0.510                6.26              0.663                                 ok            True                  False
  PAYX           79.49               39            0.22              0.17        110.71                41.26         0.539            pass              0.469             73.8                           0.668               11.72              1.160                                 ok           False                  False
  CSCO           66.67                6            2.19              1.69        109.13                35.07         0.526            pass              0.073              6.9                           0.188               -4.24             -0.428 downtrend_blocked_slope_and_streak           False                  False
  QCOM           66.67                9            3.18              3.97        176.70                54.84         0.517            pass              0.081              9.9                           0.283               -6.57             -0.498 downtrend_blocked_slope_and_streak           False                  False
  SNPS           60.00                5            3.77             12.34        462.82                53.97         0.513            pass              0.086             11.5                           0.261               -8.05             -0.697 downtrend_blocked_slope_and_streak           False                  False
  DXCM           75.00                8            2.11              1.30         87.15                29.21         0.505            pass              0.059              2.9                           0.153                0.58              0.095                                 ok           False                  False
  MSFT          100.00                3            2.65             10.01        535.15                21.00         0.499 below_threshold              0.464              4.7                           0.136                1.47              0.264                                 ok           False                  False
  MPWR           73.68               19            2.54             22.17       1239.70                56.34         0.496 below_threshold              0.183             24.6                           0.184              -15.43             -2.017            downtrend_blocked_slope           False                  False
  VRTX           62.50                8            1.95              6.95        505.77                25.61         0.494 below_threshold              0.066              5.6                           0.211               -1.17             -0.105                                 ok           False                  False
  META           75.00                4            4.37             22.55        727.05                55.08         0.490 below_threshold              0.056              2.3                           0.212               -3.24             -0.052           downtrend_blocked_streak           False                  False
  DASH           75.00                8            3.39              4.58        191.09                48.67         0.485 below_threshold              0.060              4.0                           0.160               -1.40             -0.149                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-16T15:05:04.429616-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T15:00:06.363478-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T14:55:05.627788-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-10-16T14:50:06.542626-04:00       entry_1500              entry {"allocated_cash": 59675.0, "asset_type": "option", "contract_symbol": "CEG261120C00270000", "contracts": 35, "early_entry_score": 0.326, "entry_mode": "regular", "entry_option_price": 17.05, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 462.0, "option_spread_pct": 5.28, "option_volume": 59.0, "success_rate": 85.71, "ticker": "CEG", "timing_score": 0.564}
2026-10-16T14:50:06.542626-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-16", "training_samples": 6095, "window": 5}
2026-10-16T12:00:06.321774-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:55:06.475716-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:50:05.492018-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:45:05.286618-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:40:05.599147-04:00      manage_1130               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "CEG261120C00270000", "fill_price": 17.19, "pnl": -6303.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CEG"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261016150504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261016150504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261016150504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261016150504)

</details>
