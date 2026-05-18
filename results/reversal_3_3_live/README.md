# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 15:55:05 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$29,242.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$50.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13600.0        13.55           13.6      241.03        241.95          bid_ask_mid                       13.6                bid_ask_mid                    True            50.0                   0.37         97.62               42              0.58         61.06           59.67                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           93.10               29            0.60              1.27        302.19                68.84         0.678            pass              0.769             75.1                           0.862                7.68              0.931                                 ok            True                  False
  SNPS           97.14               35            0.88              3.09        501.10                42.05         0.509            pass              0.818             66.9                           0.789                0.10              0.043                                 ok            True                   True
  INTC          100.00               35            0.36              0.27        108.65               115.99         0.711            pass              0.914             92.1                           0.806               13.16              0.789                                 ok           False                  False
  INSM           68.75               32            1.61              1.23        108.61               111.34         0.640            pass              0.397             62.2                           0.660              -23.30             -2.227 downtrend_blocked_slope_and_streak           False                  False
  MCHP           80.77               26            1.25              0.82         93.50                53.01         0.527            pass              0.351             57.0                           0.699               -2.75             -0.564 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.97               33            0.22              0.17        106.74                32.79         0.524            pass              0.868             87.3                           0.635                2.12              0.224                                 ok           False                  False
  AAPL           88.46               26            0.86              1.80        299.46                22.88         0.495 below_threshold              0.537             51.7                           0.690                7.62              0.717                                 ok           False                  False
  META           76.47               34            0.66              2.85        613.01                37.75         0.493 below_threshold              0.430             73.5                           0.595               -0.04              0.068                                 ok           False                  False
  AMGN           83.33               24            0.60              1.37        325.72                26.25         0.492 below_threshold              0.417             61.8                           0.680                0.91              0.127                                 ok           False                  False
  ASML           81.48               27            1.63             17.15       1494.46                50.55         0.488 below_threshold              0.350             49.5                           0.639                6.57              0.539                                 ok           False                  False
 GOOGL           90.48               42            0.12              0.34        396.64                41.12         0.486 below_threshold              0.810             94.1                           0.506                3.41              0.240                                 ok           False                  False
  GOOG           88.37               43            0.20              0.54        393.09                41.06         0.478 below_threshold              0.736             88.2                           0.480                3.40              0.237                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-18T15:10:01.689138-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T15:05:01.585453-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T15:00:05.590805-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:55:05.590920-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:50:01.599355-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T14:50:01.599355-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-18", "training_samples": 5028, "window": 5}
2026-05-18T12:00:03.667934-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:55:01.697815-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:50:04.542688-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:45:01.537610-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518155505)

</details>
