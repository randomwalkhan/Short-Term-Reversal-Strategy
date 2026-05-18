# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-18 15:50:04 EDT`
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
- Equity: `$29,342.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$150.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   0     10     13550.0                 13700.0        13.55           13.7      241.03        242.32          bid_ask_mid                       13.7                bid_ask_mid                    True           150.0                   1.11         97.62               42              0.58         61.06            59.5                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-18)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CDNS     option         option CDNS260618C00330000      5          2026-05-15         2026-05-18        29.05      26.145 -1452.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               30            1.12              0.85        108.40               115.99         0.696            pass              0.829             75.2                           0.669               12.29              0.754                                 ok            True                   True
   TXN           92.00               25            0.83              1.75        301.98                68.84         0.686            pass              0.685             65.6                           0.796                7.43              0.920                                 ok            True                  False
  SNPS           97.14               35            0.89              3.13        501.08                42.05         0.509            pass              0.817             66.5                           0.760                0.09              0.042                                 ok            True                   True
  AAPL           86.96               23            1.01              2.11        299.32                22.88         0.502            pass              0.452             43.2                           0.635                7.46              0.710                                 ok            True                  False
  INSM           68.75               32            1.55              1.18        108.63               111.34         0.644            pass              0.402             63.6                           0.612              -23.26             -2.224 downtrend_blocked_slope_and_streak           False                  False
  SBUX           96.97               33            0.13              0.09        106.77                32.79         0.531            pass              0.885             92.9                           0.626                2.22              0.228                                 ok           False                  False
  MCHP           80.00               25            1.36              0.90         93.47                53.01         0.525            pass              0.311             52.9                           0.640               -2.86             -0.570 downtrend_blocked_slope_and_streak           False                  False
  AMGN           82.61               23            0.69              1.58        325.63                26.25         0.491 below_threshold              0.372             55.7                           0.635                0.82              0.123                                 ok           False                  False
  META           78.95               38            0.53              2.26        613.26                37.75         0.480 below_threshold              0.472             79.0                           0.649                0.10              0.074                                 ok           False                  False
   ADI           85.00               40            0.02              0.06        417.47                35.99         0.477 below_threshold              0.676             98.3                           0.587                5.14              0.522                                 ok           False                  False
  ASML           80.00               25            1.95             20.55       1493.00                50.55         0.477 below_threshold              0.266             39.4                           0.546                6.22              0.524                                 ok           False                  False
  CDNS           97.37               38            0.29              0.70        346.94                38.71         0.473 below_threshold              0.890             85.5                           0.673               -0.94             -0.149                                 ok           False                  False
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

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260518155004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260518155004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260518155004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260518155004)

</details>
