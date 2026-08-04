# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-04 09:45:01 EDT`
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

- Cash: `$17,739.75`
- Equity: `$34,699.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$-530.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00050000       2026-08-03                   1    106     17490.0                 16960.0         1.65            1.6       49.76          49.6     last_price_stale                        NaN                unavailable                   False          -530.0                  -3.03         100.0               11              1.28         25.54            0.78                  27.78                2866.0          205.0               0.06                      ok
```

## Today's Closed Trades (2026-08-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           90.00               20            0.66              0.12         26.37                32.72         0.617          pass              0.456             20.5                           0.260                1.76              0.292                      ok            True                  False
  MDLZ          100.00               12            1.47              0.64         61.46                32.17         0.611          pass              0.522             15.7                           0.227                1.60              0.363                      ok            True                  False
  FAST          100.00               10            1.50              0.50         47.89                27.92         0.575          pass              0.566             36.1                           0.402                5.87              0.605                      ok            True                  False
   PEP           80.00               15            1.16              1.13        139.14                26.13         0.569          pass              0.196             35.1                           0.392                2.23              0.368                      ok            True                  False
   ROP           93.10               29            0.96              2.63        391.44                47.45         0.567          pass              0.701             56.2                           0.489               10.87              1.479                      ok            True                  False
   WBD           90.48               21            0.67              0.12         26.04                24.14         0.562          pass              0.459             16.7                           0.225                0.33              0.077                      ok            True                  False
  CTAS           90.00               20            1.34              1.92        203.19                37.98         0.544          pass              0.483             31.7                           0.214                0.43              0.117                      ok            True                  False
  MNST           90.48               21            0.81              0.53         93.32                26.29         0.538          pass              0.437             10.1                           0.158               -1.76              0.016                      ok            True                  False
  PAYX          100.00               13            1.13              0.93        117.27                35.86         0.535          pass              0.727             84.7                           0.589                4.99              0.779                      ok            True                  False
  ROST           89.29               28            0.78              1.39        252.31                22.38         0.504          pass              0.418              0.0                           0.189                6.41              0.844                      ok            True                  False
  ALNY           90.91               44            0.01              0.02        220.32               126.96         0.820          pass              0.870             99.1                           0.651              -18.82             -2.859 downtrend_blocked_slope           False                  False
  ISRG           75.00               20            1.50              3.95        373.72                72.79         0.682          pass              0.161              8.7                           0.231                5.63              0.843                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260804094501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260804094501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260804094501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260804094501)

</details>
