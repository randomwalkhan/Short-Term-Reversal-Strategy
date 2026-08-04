# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 09:30:01 EDT`
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

- Cash: `$17,739.75`
- Equity: `$34,699.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$-530.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-08-03                   1    106     17490.0                 16960.0         1.65            1.6       49.76         49.59     last_price_stale                        NaN                unavailable                   False          -530.0                  -3.03         100.0               11              1.28         25.54            0.78                  27.78                2866.0          205.0               0.06                      ok
```

## Today's Closed Trades (2026-08-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           91.18               34            0.61              0.25         57.76                60.15         0.665          pass              0.680             51.8                           0.392                2.99              0.428                      ok            True                  False
 CMCSA           81.25               16            0.86              0.15         24.50                43.78         0.634          pass              0.262             41.7                           0.279                2.27              0.680                      ok            True                  False
   KHC           90.00               20            0.61              0.11         26.37                32.72         0.620          pass              0.477             27.3                           0.239                1.82              0.295                      ok            True                  False
  MDLZ           91.30               23            0.53              0.23         61.63                32.17         0.595          pass              0.606             52.8                           0.473                2.57              0.406                      ok            True                  False
   ROP           93.33               30            0.68              1.86        391.77                47.45         0.579          pass              0.754             69.0                           0.407               11.19              1.491                      ok            True                  False
   TRI           85.29               34            1.30              0.92        101.21                64.54         0.578          pass              0.427             22.5                           0.325               10.57              1.621                      ok            True                  False
   EXC          100.00               20            0.70              0.22         45.53                21.77         0.550          pass              0.751             76.5                           0.794               -1.26             -0.306                      ok            True                  False
  WDAY           83.33               36            1.01              1.16        164.55                70.22         0.532          pass              0.538             74.2                           0.510               15.74              2.483                      ok            True                  False
  ABNB           91.43               35            0.58              0.62        151.26                33.33         0.501          pass              0.646             41.3                           0.396                4.54              0.904                      ok            True                  False
  ISRG           85.71               42            0.09              0.25        375.30                72.79         0.656          pass              0.692             91.5                           0.593                7.14              0.908                      ok           False                  False
  GEHC           94.59               37            0.49              0.24         69.63                58.11         0.618          pass              0.825             64.8                           0.424               11.90              1.639                      ok           False                  False
  TMUS           89.19               37            0.34              0.43        176.91                55.96         0.607          pass              0.698             70.8                           0.426               -7.49             -0.639 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-08-04T08:05:01.281633-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T08:00:06.156963-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:55:05.413752-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:50:01.172793-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:45:05.958919-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:40:04.165148-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:35:01.120189-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:30:05.395017-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:25:03.273027-04:00 data_refresh data_refresh {'saved': 93}
2026-08-04T07:20:01.112569-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804093001)

</details>
