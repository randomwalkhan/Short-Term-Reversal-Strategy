# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 09:35:01 EDT`
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

- Cash: `$13,976.50`
- Equity: `$28,280.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$384.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   KDP     option         option KDP260821C00033000       2026-07-02                   1     96     13920.0                 14304.0         1.45           1.49       33.12         32.87     last_price_stale                        NaN                unavailable                   False           384.0                   2.76         100.0               15              0.76         30.37            0.39                  28.32                2956.0          194.0               0.14                      ok
```

## Today's Closed Trades (2026-07-06)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AMGN           92.31               13            1.27              3.33        372.72                27.58         0.588          pass              0.411              1.3                           0.187                9.42              0.891                                 ok            True                  False
   LIN           94.44               18            1.06              4.07        544.90                21.57         0.538          pass              0.492              0.0                           0.199                5.60              0.555                                 ok            True                  False
  CTAS           90.00               30            0.71              0.90        180.98                35.27         0.533          pass              0.474              6.9                           0.239                5.41              0.564                                 ok            True                  False
   ADP           92.31               26            0.82              1.39        241.67                30.79         0.524          pass              0.536             16.2                           0.185               10.02              1.126                                 ok            True                  False
  BKNG           88.57               35            0.60              0.78        184.23                41.33         0.520          pass              0.447              0.0                           0.289                6.79              0.855                                 ok            True                  False
  MDLZ          100.00                7            1.12              0.48         60.71                28.43         0.643          pass              0.464              0.0                           0.226                1.02             -0.013                                 ok           False                  False
   KHC           85.71                7            1.58              0.28         25.25                36.79         0.630          pass              0.215              0.0                           0.285                9.42              1.295                                 ok           False                  False
   PEP           83.33                6            1.18              1.19        143.71                27.18         0.623          pass              0.151              0.0                           0.270                0.36             -0.007                                 ok           False                  False
   KDP          100.00                9            1.38              0.32         33.16                28.43         0.616          pass              0.462              0.0                           0.145                7.52              0.985                                 ok           False                  False
   EXC           78.57               14            0.77              0.26         47.77                22.14         0.583          pass              0.127             14.0                           0.107                3.71              0.292                                 ok           False                  False
  CTSH           72.00               25            1.54              0.45         41.80                56.76         0.548          pass              0.174              6.5                           0.245               -5.39             -0.362                                 ok           False                  False
  ROST           83.33               18            1.14              1.70        212.70                31.68         0.547          pass              0.334             45.6                           0.343               -9.36             -1.196 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706093501)

</details>
