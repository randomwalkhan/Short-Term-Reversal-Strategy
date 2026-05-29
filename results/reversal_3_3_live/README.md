# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-29 14:55:02 EDT`
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

- Cash: `$18,164.25`
- Equity: `$32,444.25`
- Realized PnL: `$22,264.25`
- Unrealized PnL: `$180.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   0      4     14100.0                 14280.0        35.25           35.7      477.34        474.29          bid_ask_mid                       35.7                bid_ask_mid                    True           180.0                   1.28         97.22               36              0.69         45.69           51.73                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-05-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.31               26            1.52              2.39        223.61               139.09         0.740          pass              0.640             43.8                           0.370               18.81              3.719                                 ok            True                  False
  MELI           94.44               36            0.59              6.95       1692.55                61.27         0.622          pass              0.729             36.0                           0.281                4.87              0.800                                 ok            True                  False
  INTC           95.45               22            2.27              1.93        120.06                85.20         0.584          pass              0.635             32.3                           0.537                1.91              0.997                                 ok            True                  False
  INSM           67.74               31            1.52              1.15        107.88               111.11         0.762          pass              0.282             22.0                           0.246               -7.69             -0.398            downtrend_blocked_slope           False                  False
   AEP           69.23               13            0.67              0.59        127.51                25.60         0.595          pass              0.137             19.0                           0.281               -1.31              0.102                                 ok           False                  False
  AMAT           91.43               35            0.11              0.36        449.53                50.48         0.564          pass              0.789             87.2                           0.545                2.08              0.646                                 ok           False                  False
  REGN           80.95               21            1.54              6.69        618.65                44.05         0.554          pass              0.194             13.3                           0.254              -14.03             -1.109 downtrend_blocked_slope_and_streak           False                  False
  GOOG           87.50                8            2.00              5.42        383.80                41.01         0.539          pass              0.310             18.8                           0.230               -4.73             -0.359            downtrend_blocked_slope           False                  False
  KLAC           91.67               36            0.31              4.15       1925.85                52.36         0.537          pass              0.728             63.4                           0.433                1.65              0.906                                 ok           False                  False
 GOOGL           87.50                8            2.14              5.85        387.62                41.30         0.537          pass              0.296             14.3                           0.207               -4.81             -0.350            downtrend_blocked_slope           False                  False
  SBUX           90.00               10            1.45              1.02        100.31                16.60         0.510          pass              0.479             53.7                           0.489               -6.14             -0.734            downtrend_blocked_slope           False                  False
  AMGN           91.18               34            0.23              0.55        336.24                27.03         0.501          pass              0.739             76.9                           0.629                0.59              0.284                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-29T14:55:02.058255-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-29T14:50:03.249987-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T14:50:03.249987-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-29", "training_samples": 5149, "window": 5}
2026-05-29T12:00:03.057178-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:55:04.089378-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:50:02.199680-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:45:01.211344-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:40:05.216205-04:00 early_entry_1140  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:35:06.186769-04:00 early_entry_1135  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-29T11:30:03.208249-04:00 early_entry_1130  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260529145502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260529145502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260529145502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260529145502)

</details>
