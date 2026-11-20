# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 14:55:06 EST`
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
- Equity: `$98,049.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$1,920.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   0     32     47200.0                 49120.0        14.75          15.35       344.6        345.24          bid_ask_mid                      15.35                bid_ask_mid                    True          1920.0                   4.07         100.0               14              1.32         27.92            28.5                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           97.06               34            0.87              4.20        687.85                78.44         0.696          pass              0.751             40.4                           0.425                1.13             -0.059                                 ok            True                  False
   MAR           90.00               10            1.38              3.99        412.33                25.25         0.555          pass              0.397             24.9                           0.408               -1.78             -0.143                                 ok            True                  False
  AAPL          100.00               17            1.16              2.84        347.99                27.12         0.548          pass              0.614             37.6                           0.503                0.89              0.037                                 ok            True                  False
  INSM           81.58               38            1.19              1.20        143.94                87.95         0.536          pass              0.373             30.1                           0.238               24.76              1.860                                 ok            True                  False
  SBUX           90.91               22            0.84              0.62        104.21                35.02         0.535          pass              0.489             21.4                           0.266               -1.15             -0.217                                 ok            True                  False
  DXCM           85.71               35            0.72              0.40         80.02                45.06         0.504          pass              0.442             24.3                           0.155                0.26              0.100                                 ok            True                  False
  ALNY           78.95               38            0.89              0.92        147.43               110.46         0.735          pass              0.310             16.6                           0.267               -6.05             -0.555 downtrend_blocked_slope_and_streak           False                  False
  INTC           63.64               11            5.06              1.97         54.87               141.91         0.718          pass              0.132             17.7                           0.372               -6.01             -0.996 downtrend_blocked_slope_and_streak           False                  False
   APP          100.00                2            7.12             18.89        370.92               122.37         0.633          pass              0.481              6.0                           0.290              -10.02             -0.775 downtrend_blocked_slope_and_streak           False                  False
  FTNT           50.00                8            4.65              4.28        129.63                96.17         0.568          pass              0.079              7.5                           0.285                5.48              0.579                                 ok           False                  False
 GOOGL           82.14               28            0.72              1.38        272.07                55.59         0.550          pass              0.364             44.0                           0.415               -4.95             -0.610            downtrend_blocked_slope           False                  False
  ODFL           72.73               11            2.05              2.50        172.76                43.88         0.544          pass              0.101             13.2                           0.225                3.24              0.348                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-20T14:55:06.056762-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T14:50:04.211371-05:00       entry_1500                   entry {"allocated_cash": 47200.0, "asset_type": "option", "contract_symbol": "AAPL270115C00345000", "contracts": 32, "early_entry_score": 0.57, "entry_mode": "regular", "entry_option_price": 14.75, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 12741.0, "option_spread_pct": 3.39, "option_volume": 229.0, "success_rate": 100.0, "ticker": "AAPL", "timing_score": 0.558}
2026-11-20T14:50:04.211371-05:00       entry_1500 entry_candidate_skipped                                                                                                                                                                           {"early_entry_score": 0.665, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 75.0, "option_spread_pct": 14.91, "option_volume": 62.0, "reason": "no_trade_low_option_liquidity", "ticker": "IDXX", "timing_score": 0.708}
2026-11-20T14:50:04.211371-05:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-20", "training_samples": 6240, "window": 5}
2026-11-20T12:00:03.900140-05:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:55:04.983316-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:50:06.003914-05:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:45:06.435631-05:00 early_entry_1145      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:40:06.030121-05:00 early_entry_1140      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:35:06.036427-05:00 early_entry_1135      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120145506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120145506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120145506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120145506)

</details>
