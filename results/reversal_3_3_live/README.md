# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 10:00:04 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$22,561.75`
- Equity: `$33,761.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$-810.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260717C00270000       2026-06-04                   1      2     12010.0                 11200.0        60.05           56.0      270.38        214.46     last_price_stale                        NaN                unavailable                   False          -810.0                  -6.74         94.74               19              3.62        161.75            12.5                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           94.59               37            1.21              0.86        101.13                86.36         0.598            pass              0.781             50.6                           0.385               17.38              1.919                                 ok            True                  False
  WDAY           90.00               40            0.61              0.63        147.64                69.97         0.582            pass              0.686             53.7                           0.331               14.73              1.990                                 ok            True                  False
  FTNT          100.00               10            2.27              2.38        148.65                44.88         0.566            pass              0.502             15.2                           0.153                9.21              1.441                                 ok            True                  False
  PANW           86.36               22            1.81              3.54        277.73                60.15         0.563            pass              0.397             30.2                           0.262                8.41              1.300                                 ok            True                  False
    ZS           81.82               33            1.27              1.20        134.74               157.69         0.877            pass              0.362             24.2                           0.232              -26.78             -2.262            downtrend_blocked_slope           False                  False
  MELI           93.33               45            0.03              0.35       1634.63                60.42         0.594            pass              0.906             97.0                           0.528               -1.81             -0.281            downtrend_blocked_slope           False                  False
   ADI          100.00                4            3.30              9.91        424.51                45.54         0.536            pass              0.499             15.1                           0.205                4.70              0.371                                 ok           False                  False
   TXN          100.00                1            3.94              8.43        301.76                44.40         0.515            pass              0.471              6.4                           0.197               -5.14             -0.750 downtrend_blocked_slope_and_streak           False                  False
  SHOP           70.00               20            2.68              2.17        115.11                59.82         0.512            pass              0.130              4.2                           0.121                9.65              0.939                                 ok           False                  False
   BKR           62.50                8            2.24              1.04         65.67                32.54         0.508            pass              0.093             14.0                           0.149               -2.16             -0.081                                 ok           False                  False
   CEG           73.68               19            2.70              5.00        262.45                55.63         0.507            pass              0.111              0.0                           0.150               -9.93             -1.413            downtrend_blocked_slope           False                  False
  AVGO           60.00                5            4.06             11.91        413.80                65.35         0.500 below_threshold              0.080             10.0                           0.171               -2.96             -0.034           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-05T10:00:04.998731-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T09:35:04.249601-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T09:30:04.938889-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T09:25:01.283083-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T09:20:04.897767-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T09:15:01.957387-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T09:10:02.051454-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T09:05:06.659544-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T09:00:02.942935-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-05T08:55:01.992892-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605100004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605100004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605100004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605100004)

</details>
