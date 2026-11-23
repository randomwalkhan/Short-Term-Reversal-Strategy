# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-23 13:15:05 EST`
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

- Cash: `$48,929.80`
- Equity: `$101,489.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$5,360.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   1     32     47200.0                 52560.0        14.75          16.42       344.6        349.37          bid_ask_mid                      16.42                bid_ask_mid                    True          5360.0                  11.36         100.0               14              1.32         27.92           27.08                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           92.00               25            0.72              0.13         24.85                33.22         0.526            pass              0.685             70.7                           0.802                0.86              0.081                                 ok            True                  False
  PAYX           76.19               21            0.64              0.51        112.41                33.87         0.560            pass              0.268             46.1                           0.544               -2.49             -0.360            downtrend_blocked_slope           False                  False
  VRSK           78.26               23            1.46              2.07        201.20                40.90         0.503            pass              0.332             65.0                           0.549               -0.73             -0.188                                 ok           False                  False
  TMUS           83.87               31            0.79              0.91        165.21                34.83         0.498 below_threshold              0.447             51.3                           0.715               -2.61             -0.440            downtrend_blocked_slope           False                  False
   ADP           89.66               29            0.57              1.21        301.19                24.32         0.486 below_threshold              0.623             63.3                           0.638               -0.69             -0.141                                 ok           False                  False
  COST           90.62               32            0.33              2.57       1101.05                21.93         0.485 below_threshold              0.714             78.6                           0.786                3.03              0.283                                 ok           False                  False
  CHTR           72.97               37            1.02              0.92        128.34                65.33         0.480 below_threshold              0.426             66.1                           0.758                5.13              0.105                                 ok           False                  False
  MNST           60.00               15            1.73              0.53         43.46                30.90         0.466 below_threshold              0.224             48.1                           0.663               -5.93             -0.569            downtrend_blocked_slope           False                  False
   KHC           88.57               35            0.61              0.11         25.34                28.13         0.464 below_threshold              0.650             69.6                           0.688                3.34              0.460                                 ok           False                  False
   PEP           88.37               43            0.01              0.01        140.53                27.59         0.453 below_threshold              0.766             99.2                           0.873               -0.96             -0.244                                 ok           False                  False
   ROP           88.10               42            0.13              0.42        459.65                29.79         0.443 below_threshold              0.731             90.1                           0.806               -2.63             -0.363 downtrend_blocked_slope_and_streak           False                  False
  CRWD          100.00                1           10.44             16.77        222.25                61.68         0.156 below_threshold              0.467             17.1                           0.394              -10.11             -0.232                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261123131505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261123131505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261123131505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261123131505)

</details>
