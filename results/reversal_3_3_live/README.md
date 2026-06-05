# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 09:40:04 EDT`
Last processed slot: `manage_0930`

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
  SOXL     option         option SOXL260717C00270000       2026-06-04                   1      2     12010.0                 11200.0        60.05           56.0      270.38        224.55     last_price_stale                        NaN                unavailable                   False          -810.0                  -6.74         94.74               19              3.62        161.75            12.5                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
    MU           81.82               11            5.37             37.47        979.94               105.49         0.567            pass              0.137              8.3                           0.140               25.50              1.805                       ok            True                  False
  PANW           91.89               37            0.61              1.20        278.74                60.15         0.548            pass              0.781             76.3                           0.672                9.73              1.355                       ok            True                   True
  FTNT          100.00               23            1.62              1.69        148.94                44.88         0.524            pass              0.631             30.8                           0.245                9.95              1.471                       ok            True                  False
  SHOP           82.05               39            1.04              0.85        115.68                59.82         0.520            pass              0.420             40.1                           0.278               11.49              1.014                       ok            True                  False
  QCOM           80.00                5            4.55              7.73        239.26                97.97         0.604            pass              0.092             10.4                           0.172               -2.42             -0.229                       ok           False                  False
   ADI          100.00                4            3.16              9.48        424.70                45.54         0.548            pass              0.500             15.2                           0.177                4.86              0.378                       ok           False                  False
  CRWD           75.00               12            2.65             13.36        713.36                64.90         0.544            pass              0.208             46.9                           0.451                7.99              1.231                       ok           False                  False
   BKR           69.23               13            1.74              0.81         65.76                32.54         0.520            pass              0.132             20.1                           0.280               -1.67             -0.057                       ok           False                  False
   CEG           76.19               21            2.44              4.52        262.65                55.63         0.516            pass              0.128              0.9                           0.188               -9.69             -1.401  downtrend_blocked_slope           False                  False
  AVGO           75.00                4            4.20             12.32        413.63                65.35         0.515            pass              0.072              6.9                           0.141               -3.10             -0.041 downtrend_blocked_streak           False                  False
  NVDA           70.00               10            2.42              3.70        217.07                40.68         0.510            pass              0.077              8.8                           0.144               -0.79              0.090                       ok           False                  False
  NXPI          100.00                4            4.12              9.30        318.23                49.12         0.491 below_threshold              0.484             11.6                           0.208               -2.38             -0.474  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-06-05T09:35:04.249601-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:30:04.938889-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:25:01.283083-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:20:04.897767-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:15:01.957387-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:10:02.051454-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:05:06.659544-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:00:02.942935-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T08:55:01.992892-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T08:50:03.852379-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605094004)

</details>
