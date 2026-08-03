# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 09:50:04 EDT`
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
- Equity: `$34,507.25`
- Realized PnL: `$23,222.25`
- Unrealized PnL: `$1,285.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00057500       2026-07-31                   1     66     16500.0                 18645.0         2.50           2.82       57.10         57.78          bid_ask_mid                       2.82                bid_ask_mid                    True          2145.0                  13.00         86.21               29              0.95         31.54           38.16                  60.55                6425.0          263.0               0.05                      ok
   CSX     option         option  CSX260918C00050000       2026-07-30                   2     86     16555.0                 15695.0         1.92           1.82       50.11         49.95          bid_ask_mid                       1.82                bid_ask_mid                    True          -860.0                  -5.19         92.31               13              1.24         25.34           28.59                  28.82                2759.0          136.0               0.03                      ok
```

## Today's Closed Trades (2026-08-03)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CSX           94.44               18            0.89              0.31         50.27                27.78         0.588            pass              0.516              6.3                           0.125               -0.32             -0.078                                 ok            True                  False
  MNST           88.89               18            0.91              0.62         96.12                24.15         0.577            pass              0.355              2.2                           0.071                0.05              0.242                                 ok            True                  False
  AAPL           96.43               28            0.64              1.39        308.31                37.33         0.576            pass              0.718             46.8                           0.261               -6.02             -0.325 downtrend_blocked_slope_and_streak           False                  False
  AMAT           86.36               22            2.67              9.48        503.61                87.25         0.566            pass              0.376             23.4                           0.273               -6.01             -1.507 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.88               32            0.04              0.01         45.81                22.49         0.519            pass              0.887             96.0                           0.632               -0.35             -0.101                                 ok           False                  False
   XEL          100.00               31            0.08              0.04         78.18                17.46         0.504            pass              0.865             91.5                           0.598               -0.67             -0.183                                 ok           False                  False
  CDNS           81.25               16            2.33              5.55        337.64                48.77         0.499 below_threshold              0.132              3.0                           0.187                0.65              0.009                                 ok           False                  False
  ASML           90.32               31            1.06             12.04       1623.84                49.80         0.497 below_threshold              0.655             63.4                           0.622               -7.20             -1.300 downtrend_blocked_slope_and_streak           False                  False
  CSCO           84.00               25            1.07              0.87        115.62                33.42         0.496 below_threshold              0.398             47.2                           0.443                3.65              0.324                                 ok           False                  False
   BKR           61.54               13            2.23              0.95         60.08                35.32         0.488 below_threshold              0.069              0.0                           0.183                7.23              0.830                                 ok           False                  False
  NVDA           83.33               36            0.62              0.88        200.38                42.43         0.487 below_threshold              0.517             68.8                           0.689               -1.86             -0.645            downtrend_blocked_slope           False                  False
  DRAM           73.91               23            3.85              1.36         49.79               111.30         0.486 below_threshold              0.219             27.9                           0.383               -8.73             -1.825 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803095004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803095004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803095004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803095004)

</details>
