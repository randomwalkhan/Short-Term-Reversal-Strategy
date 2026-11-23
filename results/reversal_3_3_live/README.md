# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-23 12:10:57 EST`
Last processed slot: `manage_1200`

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

- Cash: `$48,929.80`
- Equity: `$100,929.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$4,800.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   1     32     47200.0                 52000.0        14.75          16.25       344.6        348.03          bid_ask_mid                      16.25                bid_ask_mid                    True          4800.0                  10.17         100.0               14              1.32         27.92           27.37                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           93.75               16            1.35              0.23         24.80                33.22         0.568              pass              0.463              0.0                             NaN                0.22              0.052                                 ok            True                  False
  COST           89.47               19            0.76              5.83       1099.65                21.93         0.541              pass              0.521             51.3                           0.494                2.59              0.263                                 ok            True                  False
  PAYX           73.91               23            0.58              0.46        112.43                33.87         0.548              pass              0.295             51.3                           0.584               -2.43             -0.357            downtrend_blocked_slope           False                  False
  TMUS           77.78               18            1.49              1.72        164.86                34.83         0.531              pass              0.123              5.4                           0.177               -3.30             -0.472            downtrend_blocked_slope           False                  False
  MDLZ          100.00               30            0.26              0.12         66.23                24.95         0.528              pass              0.838             84.0                           0.691               -0.50             -0.089                                 ok           False                  False
  VRSK           79.17               24            1.44              2.03        201.22                40.90         0.499   below_threshold              0.340             65.6                           0.634               -0.70             -0.187                                 ok           False                  False
   PEP           87.10               31            0.57              0.56        140.30                27.59         0.493   below_threshold              0.579             66.7                           0.496               -1.50             -0.269            downtrend_blocked_slope           False                  False
   ADP           89.29               28            0.64              1.35        301.13                24.32         0.487   below_threshold              0.593             58.9                           0.465               -0.76             -0.144                                 ok           False                  False
   ROP           87.88               33            0.58              1.86        459.03                29.79         0.472   below_threshold              0.580             56.5                           0.594               -3.07             -0.383 downtrend_blocked_slope_and_streak           False                  False
   KHC           87.88               33            0.77              0.14         25.33                28.13         0.466   below_threshold              0.595             61.8                           0.516                3.17              0.453                                 ok           False                  False
  CRWD          100.00                1            9.82             15.78        222.68                61.68         0.176   below_threshold              0.484             22.0                           0.520               -9.48             -0.201                                 ok           False                  False
  AAPL             NaN                0            0.00              0.00        348.03                27.98           NaN no_signal_history                NaN              NaN                           0.242               -0.68             -0.162                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-23T11:30:26.190239-05:00 early_entry_1130 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-23T03:00:06.095274-05:00     data_refresh       data_refresh                                             {'saved': 91, 'empty': 2}
2026-11-21T02:55:05.433853-05:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:50:06.291709-05:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:45:05.697713-05:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:40:04.140323-05:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:35:05.478218-05:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:30:05.376683-05:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:25:04.330669-05:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:20:06.220258-05:00   share_ext_0220      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261123121057)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261123121057)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261123121057)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261123121057)

</details>
