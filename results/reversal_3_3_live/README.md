# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-20 15:45:01 EST`
Last processed slot: `manual`

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
- Equity: `$97,089.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$960.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   0     32     47200.0                 48160.0        14.75          15.05       344.6         344.1          bid_ask_mid                      15.05                bid_ask_mid                    True           960.0                   2.03         100.0               14              1.32         27.92           29.08                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00380000     13          2026-11-19         2026-11-20        37.05      33.345 -4816.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           94.74               19            1.87              9.01        685.79                78.44         0.718          pass              0.556             10.3                           0.182                0.11             -0.105                                 ok            True                  False
  AAPL          100.00               10            1.87              4.56        347.26                27.12         0.547          pass              0.489             11.4                           0.176                0.17              0.005                                 ok            True                  False
  SBUX           89.47               19            0.95              0.70        104.17                35.02         0.543          pass              0.460             30.9                           0.339               -1.26             -0.222                                 ok            True                  False
  DXCM           80.77               26            1.37              0.77         79.86                45.06         0.507          pass              0.250             24.0                           0.276               -0.40              0.070                                 ok            True                  False
   CSX           83.33               18            1.24              0.43         49.79                27.80         0.506          pass              0.225             10.8                           0.217                0.49             -0.034                                 ok            True                  False
  ALNY           71.43               28            1.99              2.06        146.94               110.46         0.710          pass              0.263             24.1                           0.240               -7.10             -0.606 downtrend_blocked_slope_and_streak           False                  False
  INTC           42.86                7            6.83              2.66         54.58               141.91         0.607          pass              0.074              4.4                           0.178               -7.76             -1.081 downtrend_blocked_slope_and_streak           False                  False
   HON          100.00                4            2.19              3.34        216.41                33.63         0.571          pass              0.481              7.8                           0.176               -2.87             -0.446 downtrend_blocked_slope_and_streak           False                  False
  ABNB           85.71               28            1.22              1.48        172.16                57.19         0.557          pass              0.342              4.5                           0.066              -10.16             -0.914 downtrend_blocked_slope_and_streak           False                  False
   MAR           88.89                9            1.49              4.30        412.20                25.25         0.554          pass              0.349             19.0                           0.230               -1.89             -0.148                                 ok           False                  False
   APP          100.00                1            8.44             22.39        369.42               122.37         0.553          pass              0.456              0.4                           0.076              -11.30             -0.840 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           70.00               10            2.25              4.29        270.82                55.59         0.542          pass              0.092             12.6                           0.205               -6.41             -0.680            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-20T15:10:05.376851-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T15:05:06.103074-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T15:00:05.079544-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T14:55:06.056762-05:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-11-20T14:50:04.211371-05:00       entry_1500                   entry {"allocated_cash": 47200.0, "asset_type": "option", "contract_symbol": "AAPL270115C00345000", "contracts": 32, "early_entry_score": 0.57, "entry_mode": "regular", "entry_option_price": 14.75, "execution_mode": "option", "matched_signals": 14, "option_liquidity_status": "ok", "option_open_interest": 12741.0, "option_spread_pct": 3.39, "option_volume": 229.0, "success_rate": 100.0, "ticker": "AAPL", "timing_score": 0.558}
2026-11-20T14:50:04.211371-05:00       entry_1500 entry_candidate_skipped                                                                                                                                                                           {"early_entry_score": 0.665, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 75.0, "option_spread_pct": 14.91, "option_volume": 62.0, "reason": "no_trade_low_option_liquidity", "ticker": "IDXX", "timing_score": 0.708}
2026-11-20T14:50:04.211371-05:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                            {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-20", "training_samples": 6240, "window": 5}
2026-11-20T12:00:03.900140-05:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:55:04.983316-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-20T11:50:06.003914-05:00 early_entry_1150      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261120154501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261120154501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261120154501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261120154501)

</details>
