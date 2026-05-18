# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 15:05:01 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$15,642.50`
- Equity: `$29,692.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$500.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 14050.0        13.55          14.05      241.03         243.1          bid_ask_mid                      14.05                bid_ask_mid                    True           500.0                   3.69         97.62               42              0.58         61.06           59.41                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               30            1.18              0.90        108.39               115.99         0.693            pass              0.825             74.0                           0.712               12.23              0.752                                 ok            True                   True
   TXN           86.67               15            1.60              3.38        301.28                68.84         0.693            pass              0.381             33.5                           0.404                6.59              0.885                                 ok            True                  False
  AMGN           91.67               12            1.10              2.51        325.24                26.25         0.551            pass              0.469             29.8                           0.261                0.41              0.104                                 ok            True                  False
  SNPS           95.83               24            1.73              6.08        499.82                42.05         0.524            pass              0.650             34.9                           0.367               -0.76              0.004                                 ok            True                  False
  AAPL           86.36               22            1.07              2.25        299.26                22.88         0.503            pass              0.418             39.5                           0.448                7.39              0.707                                 ok            True                  False
  AVGO           92.00               25            1.42              4.22        423.38                43.18         0.501            pass              0.603             44.2                           0.482                0.64              0.096                                 ok            True                  False
  NXPI           83.33               36            0.35              0.71        291.19                90.58         0.719            pass              0.560             75.4                           0.580               -0.10             -0.052                                 ok           False                  False
  INSM           66.67               27            1.83              1.40        108.54               111.34         0.654            pass              0.349             56.9                           0.719              -23.48             -2.237 downtrend_blocked_slope_and_streak           False                  False
  CSCO           94.44               36            0.06              0.05        118.19                49.84         0.591            pass              0.908             96.8                           0.798               27.54              2.767                                 ok           False                  False
  SBUX           96.55               29            0.31              0.23        106.71                32.79         0.544            pass              0.828             82.3                           0.502                2.03              0.220                                 ok           False                  False
  MCHP           77.27               22            1.99              1.31         93.29                53.01         0.499 below_threshold              0.224             31.2                           0.449               -3.48             -0.599 downtrend_blocked_slope_and_streak           False                  False
  META           78.95               38            0.45              1.95        613.39                37.75         0.485 below_threshold              0.481             81.8                           0.580                0.17              0.077                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-18T15:05:01.585453-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T15:00:05.590805-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:55:05.590920-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:50:01.599355-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T14:50:01.599355-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-18", "training_samples": 5028, "window": 5}
2026-05-18T12:00:03.667934-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:55:01.697815-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:50:04.542688-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:45:01.537610-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:40:04.531844-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518150501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518150501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518150501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518150501)

</details>
