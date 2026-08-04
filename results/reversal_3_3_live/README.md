# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 09:35:04 EDT`
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
   CSX     option         option CSX260918C00050000       2026-08-03                   1    106     17490.0                 16960.0         1.65            1.6       49.76         49.51     last_price_stale                        NaN                unavailable                   False          -530.0                  -3.03         100.0               11              1.28         25.54            0.78                  27.78                2866.0          205.0               0.06                      ok
```

## Today's Closed Trades (2026-08-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           91.18               34            0.57              0.23         57.77                60.15         0.667          pass              0.689             54.8                           0.490                3.03              0.429                  ok            True                  False
  GEHC           92.86               28            0.98              0.48         69.53                58.11         0.643          pass              0.619             30.6                           0.255               11.36              1.617                  ok            True                  False
   KHC           90.91               22            0.53              0.10         26.38                32.72         0.614          pass              0.541             36.4                           0.310                1.90              0.299                  ok            True                  False
  MDLZ           92.86               14            1.18              0.51         61.51                32.17         0.614          pass              0.431              0.0                           0.254                1.90              0.376                  ok            True                  False
  FAST          100.00               10            1.38              0.47         47.91                27.92         0.592          pass              0.486              8.9                           0.232                5.99              0.610                  ok            True                  False
   CSX           91.30               23            0.66              0.23         49.73                28.13         0.585          pass              0.447              0.0                           0.219               -0.78             -0.296                  ok            True                  False
   ROP           93.33               30            0.69              1.90        391.76                47.45         0.578          pass              0.752             68.3                           0.446               11.17              1.491                  ok            True                  False
  DXCM           88.89               36            0.78              0.48         87.10                57.42         0.549          pass              0.566             33.6                           0.354               15.89              1.957                  ok            True                  False
  CTAS           90.91               22            1.14              1.62        203.31                37.98         0.545          pass              0.552             42.1                           0.296                0.64              0.126                  ok            True                  False
  PAYX          100.00               12            1.34              1.11        117.20                35.86         0.527          pass              0.711             81.8                           0.666                4.77              0.770                  ok            True                  False
  GILD           85.71               28            0.88              0.81        130.80                32.36         0.509          pass              0.349              8.6                           0.138               -0.22              0.042                  ok            True                  False
  ISRG           79.31               29            0.92              2.42        374.37                72.79         0.670          pass              0.325             43.8                           0.369                6.25              0.870                  ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804093504)

</details>
