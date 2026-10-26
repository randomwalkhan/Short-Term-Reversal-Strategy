# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 10:00:02 EDT`
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

- Cash: `$1,161.80`
- Equity: `$145,674.30`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$842.50`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   1    657     72270.0                 73912.5         1.10           1.12       44.42         44.73          bid_ask_mid                       1.12                bid_ask_mid                    True          1642.5                   2.27          80.0               15              0.97         20.09           23.63                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261120C00230000       2026-10-22                   2     40     71400.0                 70600.0        17.85          17.65      223.97        221.24          bid_ask_mid                      17.65                bid_ask_mid                    True          -800.0                  -1.12         100.0               38              0.68         80.16           90.77                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.31               13            0.74              0.33         63.66                25.23         0.587            pass              0.535             42.7                           0.336                2.49              0.350                                 ok            True                  False
    ZS           91.89               37            0.60              1.08        254.69                57.49         0.542            pass              0.684             44.2                           0.329               12.33              1.247                                 ok            True                  False
  TEAM          100.00               15            2.80              4.46        225.70                47.89         0.512            pass              0.536             17.3                           0.152                6.49              0.974                                 ok            True                  False
   CEG           85.71               35            0.75              1.34        252.88                65.46         0.606            pass              0.486             35.4                           0.279              -14.41             -1.589 downtrend_blocked_slope_and_streak           False                  False
   STX           76.19               42            0.08              0.37        630.33                71.81         0.585            pass              0.535             92.1                           0.497              -16.37             -1.652 downtrend_blocked_slope_and_streak           False                  False
  MRVL           89.74               39            0.52              0.83        228.15                64.81         0.544            pass              0.729             73.7                           0.419              -14.49             -1.480            downtrend_blocked_slope           False                  False
 CMCSA           88.89                9            1.06              0.17         22.62                23.68         0.541            pass              0.479             62.5                           0.640                8.56              0.943                                 ok           False                  False
  MPWR           77.27               44            0.07              0.55       1139.89                56.28         0.528            pass              0.526             91.0                           0.524              -13.64             -1.291            downtrend_blocked_slope           False                  False
  CTSH           95.00               40            0.43              0.21         70.45                46.28         0.509            pass              0.842             63.7                           0.411               17.69              1.831                                 ok           False                  False
  AAPL           87.50               16            1.30              3.17        346.37                16.45         0.497 below_threshold              0.387             32.4                           0.351                0.65              0.139                                 ok           False                  False
  DXCM           84.62               26            1.39              0.76         77.62                37.22         0.493 below_threshold              0.351             23.9                           0.224              -10.54             -1.163 downtrend_blocked_slope_and_streak           False                  False
  CRWD           84.21               38            1.06              1.91        256.75                57.83         0.492 below_threshold              0.380             10.6                           0.230               -3.11             -0.361           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-10-26T10:00:02.755892-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T03:00:06.095406-04:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-10-24T02:55:06.111058-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:50:04.428173-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:45:06.637393-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:40:05.798457-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:35:04.182353-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:30:05.264704-04:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:25:04.373629-04:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:20:05.341779-04:00   share_ext_0220      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026100002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026100002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026100002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026100002)

</details>
