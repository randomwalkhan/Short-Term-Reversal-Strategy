# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 09:55:05 EDT`
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

- Cash: `$167.25`
- Equity: `$35,367.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$2,145.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-07-31                   1     66     16500.0                 18645.0         2.50           2.82       57.10         57.88          bid_ask_mid                       2.82                bid_ask_mid                    True          2145.0                   13.0         86.21               29              0.95         31.54           36.77                  60.55                6425.0          263.0               0.05                      ok
   CSX     option         option  CSX260918C00050000       2026-07-30                   2     86     16555.0                 16555.0         1.92           1.92       50.11         49.97          bid_ask_mid                       1.92                bid_ask_mid                    True             0.0                    0.0         92.31               13              1.24         25.34           28.27                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-08-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           94.74               19            0.83              0.29         50.27                27.78         0.586            pass              0.560             16.0                           0.170               -0.26             -0.075                                 ok            True                  False
  MNST           88.89               18            1.06              0.72         96.07                24.15         0.565            pass              0.347              0.0                           0.157               -0.10              0.235                                 ok            True                  False
  AMGN          100.00               25            0.80              2.17        384.23                25.80         0.511            pass              0.551              0.0                           0.150                4.91              0.675                                 ok            True                  False
  AMAT           87.50               24            2.57              9.14        503.75                87.25         0.561            pass              0.428             26.1                           0.268               -5.91             -1.503 downtrend_blocked_slope_and_streak           False                  False
  GILD           86.67               30            0.58              0.53        129.98                32.59         0.534            pass              0.439             24.8                           0.174               -2.82             -0.052           downtrend_blocked_streak           False                  False
   EXC           96.77               31            0.09              0.03         45.81                22.49         0.523            pass              0.868             92.0                           0.658               -0.39             -0.103                                 ok           False                  False
  AAPL           97.50               40            0.31              0.67        308.62                37.33         0.519            pass              0.875             74.3                           0.435               -5.71             -0.310 downtrend_blocked_slope_and_streak           False                  False
   XEL          100.00               30            0.15              0.08         78.16                17.46         0.505            pass              0.833             83.1                           0.562               -0.75             -0.187                                 ok           False                  False
  CSCO           81.82               22            1.33              1.08        115.53                33.42         0.496 below_threshold              0.282             34.7                           0.290                3.39              0.312                                 ok           False                  False
  ASML           90.62               32            1.00             11.45       1624.09                49.80         0.494 below_threshold              0.675             65.2                           0.695               -7.15             -1.298 downtrend_blocked_slope_and_streak           False                  False
   BKR           61.54               13            2.14              0.91         60.10                35.32         0.493 below_threshold              0.094              8.2                           0.125                7.33              0.834                                 ok           False                  False
  DRAM           73.91               23            3.79              1.34         49.80               111.30         0.490 below_threshold              0.223             29.0                           0.401               -8.67             -1.822 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-03T03:00:01.318857-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-08-01T02:55:05.543757-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:50:03.559727-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:45:01.711119-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:40:01.558683-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:35:03.491522-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:30:02.590104-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:25:05.555029-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:20:01.118394-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-01T02:15:04.473515-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803095505)

</details>
