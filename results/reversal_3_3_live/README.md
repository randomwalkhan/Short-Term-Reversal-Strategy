# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-23 13:11:15 EST`
Last processed slot: `manage_1300`

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
- Equity: `$101,409.80`
- Realized PnL: `$86,129.80`
- Unrealized PnL: `$5,280.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AAPL     option         option AAPL270115C00345000       2026-11-20                   1     32     47200.0                 52480.0        14.75           16.4       344.6         348.6          bid_ask_mid                       16.4                bid_ask_mid                    True          5280.0                  11.19         100.0               14              1.32         27.92            27.6                  27.12               12741.0          229.0               0.03                      ok
```

## Today's Closed Trades (2026-11-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           92.00               25            0.76              0.13         24.84                33.22         0.524            pass              0.680             69.1                           0.760                0.82              0.079                                 ok            True                  False
  PAYX           70.59               17            0.73              0.57        112.38                33.87         0.573            pass              0.221             39.0                           0.367               -2.57             -0.364            downtrend_blocked_slope           False                  False
  MDLZ           97.06               34            0.07              0.03         66.27                24.95         0.510            pass              0.898             95.8                           0.785               -0.31             -0.080                                 ok           False                  False
  VRSK           78.26               23            1.49              2.11        201.19                40.90         0.501            pass              0.330             64.3                           0.540               -0.76             -0.189                                 ok           False                  False
  COST           89.66               29            0.41              3.14       1100.81                21.93         0.499 below_threshold              0.655             73.8                           0.740                2.95              0.279                                 ok           False                  False
  TMUS           84.38               32            0.78              0.91        165.21                34.83         0.492 below_threshold              0.467             51.5                           0.707               -2.61             -0.440            downtrend_blocked_slope           False                  False
   ADP           89.66               29            0.61              1.30        301.15                24.32         0.483 below_threshold              0.615             60.7                           0.501               -0.73             -0.143                                 ok           False                  False
  CHTR           73.68               38            0.95              0.86        128.36                65.33         0.478 below_threshold              0.440             68.4                           0.717                5.20              0.108                                 ok           False                  False
  MNST           60.00               15            1.72              0.53         43.46                30.90         0.467 below_threshold              0.225             48.5                           0.651               -5.92             -0.568            downtrend_blocked_slope           False                  False
   PEP           87.80               41            0.10              0.09        140.50                27.59         0.460 below_threshold              0.737             94.4                           0.854               -1.04             -0.248                                 ok           False                  False
   KHC           88.57               35            0.71              0.13         25.34                28.13         0.457 below_threshold              0.635             64.7                           0.630                3.24              0.455                                 ok           False                  False
   ROP           87.50               40            0.21              0.66        459.55                29.79         0.451 below_threshold              0.698             84.4                           0.759               -2.71             -0.366 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261123131115)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261123131115)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261123131115)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261123131115)

</details>
