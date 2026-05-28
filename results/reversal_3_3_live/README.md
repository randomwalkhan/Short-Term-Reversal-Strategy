# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 10:00:04 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$19,575.25`
- Equity: `$31,075.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$-510.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   1      2     12010.0                 11500.0        60.05           57.5       531.8        499.25     last_price_stale                        NaN                unavailable                   False          -510.0                  -4.25         97.22               36              0.52         54.56             0.2                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               26            0.75              0.63        119.40                51.65         0.630          pass              0.560             20.7                           0.270               16.59              0.874                      ok            True                  False
    MU           82.76               29            2.07             13.46        922.64               100.84         0.620          pass              0.443             60.3                           0.321               13.13              2.047                      ok            True                  False
  FTNT          100.00               42            0.57              0.51        127.71                70.83         0.600          pass              0.741             27.0                           0.264                8.08              0.884                      ok            True                  False
  ASML           94.12               34            0.62              6.88       1594.92                53.18         0.577          pass              0.729             45.0                           0.222                0.41              0.543                      ok            True                  False
  SOXL           90.91               22            3.71              5.66        215.55               139.87         0.575          pass              0.637             69.4                           0.367               13.92              2.595                      ok            True                  False
  INTC           95.24               21            3.16              2.70        120.61                92.16         0.554          pass              0.619             30.0                           0.226               -1.97              0.682                      ok            True                  False
  MNST           88.00               25            0.90              0.56         89.00                49.17         0.554          pass              0.474             35.1                           0.292                2.92              0.246                      ok            True                  False
  AMAT           81.82               22            1.97              6.17        445.61                50.47         0.527          pass              0.217             11.9                           0.132                0.77              0.346                      ok            True                  False
  FAST           94.12               17            1.25              0.39         44.65                20.06         0.511          pass              0.508             11.1                           0.213                1.12              0.190                      ok            True                  False
   TXN           95.45               22            1.21              2.69        316.30                35.35         0.507          pass              0.624             31.2                           0.192                2.37              0.447                      ok            True                  False
   XEL           90.32               31            0.59              0.34         80.86                25.49         0.506          pass              0.586             40.0                           0.366                0.76              0.250                      ok            True                  False
    ZS           85.19               27            1.75              1.55        125.75               152.21         0.827          pass              0.471             45.4                           0.488              -18.52             -1.214 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-28T10:00:04.925583-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-28T00:00:03.757313-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-27T15:10:02.000661-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:05:04.292282-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T15:00:06.354268-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:55:06.489057-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T14:50:01.720844-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-27", "training_samples": 5097, "window": 5}
2026-05-27T12:00:02.710964-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-27T11:55:06.026706-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528100004)

</details>
