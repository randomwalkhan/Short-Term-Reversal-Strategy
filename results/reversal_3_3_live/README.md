# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 09:50:05 EDT`
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
  SOXL     option         option SOXL260717C00270000       2026-06-04                   1      2     12010.0                 11200.0        60.05           56.0      270.38        217.98     last_price_stale                        NaN                unavailable                   False          -810.0                  -6.74         94.74               19              3.62        161.75            12.5                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           94.12               34            1.59              1.13        101.02                86.36         0.602          pass              0.597              0.0                           0.252               16.93              1.901                                 ok            True                  False
  PANW           86.36               22            1.81              3.55        277.73                60.15         0.563          pass              0.396             30.1                           0.325                8.41              1.300                                 ok            True                  False
    ZS           82.05               39            0.60              0.57        135.02               157.69         0.880          pass              0.528             64.1                           0.530              -26.28             -2.231            downtrend_blocked_slope           False                  False
  WDAY           90.48               42            0.36              0.37        147.75                69.97         0.593          pass              0.689             50.0                           0.365               15.01              2.001                                 ok           False                  False
  FTNT          100.00                9            2.49              2.61        148.55                44.88         0.560          pass              0.462              2.1                           0.137                8.97              1.431                                 ok           False                  False
  CTSH           94.74               38            0.21              0.08         53.37                51.38         0.531          pass              0.906             91.1                           0.608                1.02              0.189                                 ok           False                  False
  SHOP           76.92               26            2.05              1.67        115.33                59.82         0.530          pass              0.160              0.0                           0.197               10.35              0.968                                 ok           False                  False
  QCOM           75.00                4            5.56              9.44        238.53                97.97         0.527          pass              0.076              7.8                           0.202               -3.45             -0.277            downtrend_blocked_slope           False                  False
   TXN          100.00                2            3.68              7.88        301.99                44.40         0.525          pass              0.489             12.0                           0.207               -4.88             -0.738 downtrend_blocked_slope_and_streak           False                  False
   CEG           78.26               23            2.18              4.04        262.86                55.63         0.523          pass              0.176             12.2                           0.147               -9.45             -1.389            downtrend_blocked_slope           False                  False
   ADI          100.00                3            3.72             11.17        423.97                45.54         0.516          pass              0.465              4.4                           0.191                4.25              0.351                                 ok           False                  False
  NVDA           66.67                9            2.44              3.74        217.06                40.68         0.511          pass              0.075              8.1                           0.216               -0.82              0.089                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605095005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605095005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605095005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605095005)

</details>
