# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 09:30:04 EDT`
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
  SOXL     option         option SOXL260717C00270000       2026-06-04                   1      2     12010.0                 11200.0        60.05           56.0      270.38        227.64     last_price_stale                        NaN                unavailable                   False          -810.0                  -6.74         94.74               19              3.62        161.75            12.5                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           93.33               15            1.36              1.24        129.47                52.29         0.645          pass              0.550             32.1                           0.208                8.49              0.974                                 ok            True                  False
    MU           83.33               12            5.02             35.03        980.99               104.26         0.585          pass              0.203             14.2                           0.213               24.12              2.870                                 ok            True                  False
  AVGO           83.33               18            2.37              6.94        415.94                64.99         0.574          pass              0.247             15.9                           0.201               -1.34              0.636                                 ok            True                  False
   ADI          100.00               10            2.44              7.32        425.62                44.46         0.563          pass              0.510             18.1                           0.284                9.17              0.805                                 ok            True                  False
  PANW           88.46               26            1.57              3.08        277.93                59.60         0.554          pass              0.506             39.4                           0.248               11.43              1.626                                 ok            True                  False
  SHOP           83.72               43            0.64              0.52        115.82                62.96         0.531          pass              0.528             58.4                           0.365                9.80              1.446                                 ok            True                  False
  CDNS           92.31               26            1.65              4.75        409.64                45.01         0.512          pass              0.562             25.4                           0.187               12.95              1.376                                 ok            True                  False
  QCOM           83.33                6            4.06              6.90        239.61                96.58         0.638          pass              0.190             12.3                           0.141               -1.93             -0.113                                 ok           False                  False
  MELI           94.44               36            0.75              8.59       1631.10                60.87         0.614          pass              0.652             10.8                           0.144               -3.30             -0.240           downtrend_blocked_streak           False                  False
  CRWD           76.92               13            2.62             13.17        713.45                54.47         0.565          pass              0.120             14.5                           0.250                7.72              1.650                                 ok           False                  False
 GOOGL           90.00               10            1.80              4.69        370.18                30.59         0.562          pass              0.323              0.0                           0.183               -5.72             -0.753 downtrend_blocked_slope_and_streak           False                  False
   CEG           75.00               28            1.55              2.87        263.36                55.72         0.540          pass              0.174              0.0                           0.232               -7.38             -1.033            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-06-05T09:30:04.938889-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:25:01.283083-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:20:04.897767-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:15:01.957387-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:10:02.051454-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:05:06.659544-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T09:00:02.942935-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T08:55:01.992892-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T08:50:03.852379-04:00 data_refresh data_refresh {'saved': 93}
2026-06-05T08:45:04.982527-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605093004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605093004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605093004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605093004)

</details>
