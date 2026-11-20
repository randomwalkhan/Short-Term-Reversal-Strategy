# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 14:50:04 EST`
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

- Cash: `$48,929.80`
- Equity: `$96,129.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   0     32     47200.0                 47200.0        14.75          14.75       344.6        344.63          bid_ask_mid                      14.75                bid_ask_mid                    True             0.0                    0.0         100.0               14              1.32         27.92           27.92                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           96.55               29            1.13              5.47        687.31                78.44         0.708          pass              0.665             22.4                           0.265                0.86             -0.071                                 ok            True                  False
  AAPL          100.00               14            1.32              3.23        347.83                27.12         0.558          pass              0.570             29.2                           0.400                0.73              0.030                                 ok            True                  False
  SBUX           89.47               19            0.97              0.71        104.17                35.02         0.544          pass              0.397              9.8                           0.133               -1.27             -0.222                                 ok            True                  False
  INSM           80.56               36            1.35              1.36        143.88                87.95         0.538          pass              0.305             20.9                           0.168               24.57              1.853                                 ok            True                  False
  ALNY           80.49               41            0.75              0.78        147.49               110.46         0.730          pass              0.309              7.5                           0.148               -5.92             -0.549 downtrend_blocked_slope_and_streak           False                  False
  INTC           63.64               11            5.64              2.20         54.78               141.91         0.686          pass              0.100              8.2                           0.234               -6.58             -1.024 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                1            7.32             19.42        370.70               122.37         0.627          pass              0.473              3.4                           0.250              -10.21             -0.785 downtrend_blocked_slope_and_streak           False                  False
  FTNT           50.00                8            4.81              4.42        129.56                96.17         0.558          pass              0.069              4.3                           0.167                5.30              0.572                                 ok           False                  False
 GOOGL           82.14               28            0.64              1.22        272.14                55.59         0.556          pass              0.384             50.3                           0.420               -4.87             -0.606            downtrend_blocked_slope           False                  False
   MAR           87.50                8            1.56              4.52        412.10                25.25         0.554          pass              0.300             14.9                           0.279               -1.97             -0.152                                 ok           False                  False
  GOOG           82.14               28            0.84              1.60        270.34                53.33         0.537          pass              0.357             42.0                           0.389               -5.35             -0.629            downtrend_blocked_slope           False                  False
  MSFT           85.71                7            2.22              7.73        494.99                37.07         0.535          pass              0.288             27.3                           0.251               -7.99             -0.890            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-20T14:50:04.211371-05:00       entry_1500                   entry {"allocated_cash": 47200.0, "asset_type": "option", "contract_symbol": "AAPL270115C00345000", "contracts": 32, "early_entry_score": 0.57, "entry_mode": "regular", "entry_option_price": 14.75, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 12741.0, "option_spread_pct": 3.39, "option_volume": 229.0, "success_rate": 100.0, "ticker": "AAPL", "timing_score": 0.558}
2026-11-20T14:50:04.211371-05:00       entry_1500 entry_candidate_skipped                                                                                                                                                                           {"early_entry_score": 0.665, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 75.0, "option_spread_pct": 14.91, "option_volume": 62.0, "reason": "no_trade_low_option_liquidity", "ticker": "IDXX", "timing_score": 0.708}
2026-11-20T14:50:04.211371-05:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-20", "training_samples": 6240, "window": 5}
2026-11-20T12:00:03.900140-05:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:55:04.983316-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:50:06.003914-05:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:45:06.435631-05:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:40:06.030121-05:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:35:06.036427-05:00 early_entry_1135      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:30:06.242321-05:00 early_entry_1130      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120145004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120145004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120145004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120145004)

</details>
