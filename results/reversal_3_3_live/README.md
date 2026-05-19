# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-19 09:45:04 EDT`
Last processed slot: `manual`

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
- Equity: `$28,942.50`
- Realized PnL: `$19,192.50`
- Unrealized PnL: `$-250.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260618C00250000       2026-05-18                   1     10     13550.0                 13300.0        13.55           13.3      241.03         240.4     last_price_stale                        NaN                unavailable                   False          -250.0                  -1.85         97.62               42              0.58         61.06            3.13                  33.53                3069.0           22.0               0.11                      ok
```

## Today's Closed Trades (2026-05-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC          100.00               30            1.11              0.84        107.81               114.00         0.743          pass              0.778             56.7                           0.619               -1.09             -0.433                                 ok            True                  False
   TXN           89.47               19            1.44              3.03        299.30                69.24         0.675          pass              0.557             59.0                           0.634                5.44              0.691                                 ok            True                  False
  FTNT          100.00               33            0.96              0.85        126.14                70.72         0.637          pass              0.784             55.7                           0.372               39.33              3.236                                 ok            True                  False
  CSCO           88.24               17            1.52              1.27        118.34                49.96         0.614          pass              0.436             36.3                           0.420               24.15              2.963                                 ok            True                  False
 GOOGL           80.00               10            2.01              5.57        394.55                40.53         0.573          pass              0.057              0.0                           0.150                0.14              0.021                                 ok            True                  False
  GOOG           80.00               10            1.99              5.47        390.77                40.55         0.570          pass              0.057              0.0                           0.150                0.27              0.009                                 ok            True                  False
   HON           83.33               18            0.84              1.28        216.68                27.06         0.543          pass              0.283             29.0                           0.227                3.60              0.200                                 ok            True                  False
  FAST           92.86               14            1.57              0.48         43.79                22.17         0.534          pass              0.471             16.0                           0.184               -2.30             -0.230                                 ok            True                  False
  KLAC           80.77               26            1.51             18.52       1748.52                51.34         0.513          pass              0.333             51.3                           0.621               -0.17             -0.041                                 ok            True                  False
  AVGO           88.89               18            2.32              6.83        417.78                42.85         0.512          pass              0.409             22.5                           0.217               -3.84             -0.120                                 ok            True                  False
   CSX           87.88               33            0.63              0.20         46.11                31.65         0.509          pass              0.525             37.0                           0.471                1.95              0.245                                 ok            True                  False
  INSM           77.78               45            0.13              0.10        107.11               111.34         0.727          pass              0.553             93.3                           0.691              -23.26             -1.639 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-19T00:00:06.432342-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-18T15:10:01.689138-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T15:05:01.585453-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T15:00:05.590805-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:55:05.590920-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-18T14:50:01.599355-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T14:50:01.599355-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-18", "training_samples": 5028, "window": 5}
2026-05-18T12:00:03.667934-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:55:01.697815-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-18T11:50:04.542688-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260519094504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260519094504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260519094504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260519094504)

</details>
