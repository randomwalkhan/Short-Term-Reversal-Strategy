# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 09:35:04 EDT`
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
  SOXL     option         option SOXL260717C00270000       2026-06-04                   1      2     12010.0                 11200.0        60.05           56.0      270.38        227.32     last_price_stale                        NaN                unavailable                   False          -810.0                  -6.74         94.74               19              3.62        161.75            12.5                 141.59                 112.0           64.0               0.05                      ok
```

## Today's Closed Trades (2026-06-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               14            1.95              2.04        148.79                44.88         0.563          pass              0.532             16.5                           0.241                9.57              1.456                                 ok            True                  False
  SHOP           83.33               42            0.61              0.49        115.83                59.82         0.532          pass              0.537             65.1                           0.489               11.98              1.034                                 ok            True                  False
  QCOM           80.00                5            4.39              7.46        239.37                97.97         0.619          pass              0.084              7.3                           0.199               -2.26             -0.221                                 ok           False                  False
  CSCO          100.00                3            3.10              2.82        128.79                55.20         0.611          pass              0.461              0.0                           0.177                4.62              0.824                                 ok           False                  False
    MU           78.57               14            4.47             31.18        982.64               105.49         0.602          pass              0.158             23.7                           0.360               26.69              1.848                                 ok           False                  False
   ADI          100.00                4            3.19              9.57        424.66                45.54         0.546          pass              0.498             14.4                           0.185                4.82              0.376                                 ok           False                  False
   CEG           76.92               26            1.66              3.07        263.27                55.63         0.544          pass              0.196             11.7                           0.167               -8.97             -1.365            downtrend_blocked_slope           False                  False
  PANW           92.50               40            0.49              0.95        278.84                60.15         0.537          pass              0.831             81.2                           0.608                9.87              1.361                                 ok           False                  False
  AVGO           60.00                5            3.75             11.01        414.19                65.35         0.530          pass              0.053              0.0                           0.163               -2.65             -0.019           downtrend_blocked_streak           False                  False
   TXN          100.00                2            3.69              7.89        301.99                44.40         0.528          pass              0.471              6.2                           0.214               -4.89             -0.738 downtrend_blocked_slope_and_streak           False                  False
   BKR           69.23               13            1.72              0.79         65.77                32.54         0.523          pass              0.116             14.7                           0.274               -1.64             -0.056                                 ok           False                  False
  SNPS           88.24               17            2.18              7.56        491.24                44.26         0.516          pass              0.356             12.7                           0.221               -7.82             -0.783            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605093504)

</details>
