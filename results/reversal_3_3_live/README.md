# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 09:45:01 EDT`
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

- Cash: `$13,976.50`
- Equity: `$28,280.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$384.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   KDP     option         option KDP260821C00033000       2026-07-02                   1     96     13920.0                 14304.0         1.45           1.49       33.12         32.69     last_price_stale                        NaN                unavailable                   False           384.0                   2.76         100.0               15              0.76         30.37            0.78                  28.32                2956.0          194.0               0.14                      ok
```

## Today's Closed Trades (2026-07-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   XEL          100.00               20            0.52              0.30         81.83                20.81         0.573          pass              0.661             45.6                           0.373                5.32              0.333                  ok            True                  False
  GILD           88.24               17            1.14              1.04        130.82                30.05         0.552          pass              0.321              0.0                           0.223                4.86              0.453                  ok            True                  False
  CTAS           85.00               20            1.22              1.55        180.70                35.27         0.552          pass              0.301             15.3                           0.265                4.86              0.540                  ok            True                  False
  PYPL           84.62               13            1.61              0.51         45.25                34.53         0.544          pass              0.368             56.8                           0.581                5.25              0.714                  ok            True                  False
   ADP           91.30               23            0.99              1.67        241.55                30.79         0.527          pass              0.532             30.3                           0.278                9.83              1.119                  ok            True                  False
  CTSH           81.08               37            0.76              0.22         41.89                56.76         0.520          pass              0.473             70.6                           0.512               -4.65             -0.327                  ok            True                  False
  FAST           95.24               21            1.11              0.38         48.44                20.75         0.510          pass              0.530              1.8                           0.257                4.73              0.604                  ok            True                  False
  MNST          100.00               26            0.65              0.44         97.41                16.38         0.505          pass              0.602             14.9                           0.276                6.16              0.595                  ok            True                  False
  MDLZ          100.00                5            1.34              0.57         60.67                28.43         0.636          pass              0.513             16.5                           0.235                0.80             -0.023                  ok           False                  False
   KDP          100.00                6            1.49              0.35         33.15                28.43         0.625          pass              0.515             17.5                           0.272                7.41              0.980                  ok           False                  False
   KHC           85.71                7            1.73              0.31         25.24                36.79         0.609          pass              0.305             30.7                           0.320                9.25              1.288                  ok           False                  False
   PEP           80.00                5            1.48              1.49        143.58                27.18         0.602          pass              0.060              0.0                           0.210                0.05             -0.021                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-07-06T03:00:03.074522-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-07-04T02:55:10.939731-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:50:08.940118-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:45:08.118438-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:40:02.422082-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:35:05.961779-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:30:09.469505-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:25:09.745804-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:20:09.451939-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-04T02:15:07.359670-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706094501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706094501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706094501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706094501)

</details>
