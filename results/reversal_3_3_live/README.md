# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-29 09:35:02 EDT`
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

- Cash: `$18,410.50`
- Equity: `$36,470.50`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$-322.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   CSX     option         option CSX260918C00052500       2026-07-28                   1    129     18382.5                 18060.0         1.42            1.4       51.22         50.62     last_price_stale                        NaN                unavailable                   False          -322.5                  -1.75         92.86               14              1.11         25.66            3.13                  24.65                4433.0          101.0               0.04                      ok
```

## Today's Closed Trades (2026-07-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  BKNG           91.30               23            1.49              2.08        198.42                45.62         0.562          pass              0.563             39.5                           0.435               12.29              0.721                      ok            True                  False
   TRI           87.88               33            1.28              0.93        102.89                68.18         0.557          pass              0.427              2.6                           0.109               11.15              0.421                      ok            True                  False
   HON           84.21               19            1.09              1.89        246.24                39.75         0.540          pass              0.231              1.6                           0.174                9.73              1.172                      ok            True                  False
   MAR          100.00               24            0.98              2.63        382.39                28.18         0.537          pass              0.700             51.0                           0.423                4.57              0.395                      ok            True                  False
  GILD           86.96               23            1.02              0.96        133.91                34.28         0.517          pass              0.338              4.9                           0.048                2.24             -0.040                      ok            True                  False
  DXCM           88.24               34            0.92              0.48         74.64                45.20         0.511          pass              0.583             50.9                           0.460                0.05             -0.306                      ok            True                  False
  ISRG           71.43               14            1.93              4.89        359.70                72.57         0.660          pass              0.137             14.6                           0.205               -8.78             -0.911                      ok           False                  False
   KHC           91.30               23            0.04              0.01         27.30                34.60         0.630          pass              0.740             96.3                           0.620                7.23              0.475                      ok           False                  False
  PYPL           90.00               40            0.36              0.15         58.26                61.52         0.616          pass              0.751             74.4                           0.607                4.66              0.264                      ok           False                  False
  TMUS           92.31               26            0.90              1.15        181.90                56.22         0.597          pass              0.584             29.7                           0.232               -3.66             -0.887 downtrend_blocked_slope           False                  False
  FAST          100.00                8            1.77              0.60         47.84                27.18         0.575          pass              0.477              6.6                           0.082                3.87              0.433                      ok           False                  False
   APP           82.22               45            0.54              1.58        417.54                74.36         0.573          pass              0.547             76.7                           0.544               -8.12             -0.831 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et         slot   event_type        detail
2026-07-29T09:35:02.435322-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:30:03.798822-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:25:01.530149-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:20:02.789351-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:15:01.480372-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:10:04.312418-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:05:01.483120-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T09:00:02.430762-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T08:55:05.405467-04:00 data_refresh data_refresh {'saved': 93}
2026-07-29T08:50:01.443256-04:00 data_refresh data_refresh {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260729093502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260729093502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260729093502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260729093502)

</details>
