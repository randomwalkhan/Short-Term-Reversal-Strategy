# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 09:45:05 EDT`
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

- Cash: `$22,561.75`
- Equity: `$33,761.75`
- Realized PnL: `$24,571.75`
- Unrealized PnL: `$-810.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SOXL     option         option SOXL260717C00270000       2026-06-04                   1      2     12010.0                 11200.0        60.05           56.0      270.38         220.5     last_price_stale                        NaN                unavailable                   False          -810.0                  -6.74         94.74               19              3.62        161.75            12.5                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               14            1.95              2.05        148.79                44.88         0.562          pass              0.540             19.1                           0.251                9.57              1.456                                 ok            True                  False
  PANW           89.66               29            1.25              2.43        278.21                60.15         0.557          pass              0.596             52.0                           0.464                9.04              1.326                                 ok            True                  False
  CRWD           81.82               11            3.06             15.40        712.49                64.90         0.535          pass              0.225             38.8                           0.401                7.54              1.212                                 ok            True                  False
  TEAM           95.24               42            0.48              0.34        101.35                86.36         0.632          pass              0.819             52.0                           0.443               18.25              1.952                                 ok           False                  False
  WDAY           90.91               44            0.11              0.11        147.86                69.97         0.599          pass              0.797             82.2                           0.432               15.30              2.013                                 ok           False                  False
  CSCO          100.00                1            3.58              3.26        128.60                55.20         0.583          pass              0.496             12.6                           0.219                4.09              0.801                                 ok           False                  False
  QCOM           80.00                5            5.26              8.92        238.75                97.97         0.555          pass              0.061              1.8                           0.153               -3.15             -0.262            downtrend_blocked_slope           False                  False
   CEG           76.00               25            1.79              3.31        263.17                55.63         0.533          pass              0.238             28.1                           0.276               -9.09             -1.371            downtrend_blocked_slope           False                  False
  SHOP           75.86               29            1.78              1.45        115.42                59.82         0.530          pass              0.180              0.0                           0.197               10.65              0.980                                 ok           False                  False
   ADI          100.00                4            3.46             10.40        424.30                45.54         0.528          pass              0.474              7.0                           0.111                4.53              0.363                                 ok           False                  False
    MU           88.89                9            6.26             43.62        977.31               105.49         0.526          pass              0.290              0.0                           0.183               24.33              1.763                                 ok           False                  False
   TXN          100.00                2            3.80              8.13        301.89                44.40         0.517          pass              0.479              9.2                           0.176               -5.00             -0.744 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605094505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605094505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605094505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605094505)

</details>
