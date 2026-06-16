# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-16 10:14:03 EDT`
Last processed slot: `early_entry_1010`

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

- Cash: `$14,083.25`
- Equity: `$26,618.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$-690.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  ROST     option         option ROST260717C00240000       2026-06-15                   1     23     13225.0                 12535.0         5.75           5.45      236.66        234.95          bid_ask_mid                       5.45                bid_ask_mid                    True          -690.0                  -5.22         91.67               12              1.45         26.78           31.81                  38.75                 169.0           31.0               0.12                      ok
```

## Today's Closed Trades (2026-06-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           89.66               29            0.65              1.24        271.97               205.25         0.922          pass              0.710             77.8                           0.597                1.65             -0.125                  ok            True                  False
  ROST           96.15               26            0.77              1.28        236.22                39.26         0.591          pass              0.634             22.7                           0.214                5.18              0.481                  ok            True                  False
  KLAC           88.00               25            1.41              2.52        255.34                74.49         0.585          pass              0.530             52.7                           0.636               18.97              2.639                  ok            True                  False
  INTC           92.31               26            2.02              1.81        127.08                82.35         0.545          pass              0.652             54.2                           0.374               16.07              1.649                  ok            True                  False
   MAR           93.33               15            1.27              3.55        399.11                27.71         0.544          pass              0.627             61.4                           0.786                4.99              0.366                  ok            True                  False
  ASML           92.86               28            1.68             22.27       1883.12                56.35         0.542          pass              0.611             31.3                           0.331                7.79              1.131                  ok            True                  False
  ODFL           90.00               20            1.57              2.60        236.30                37.63         0.530          pass              0.422             12.1                           0.228                2.15              0.124                  ok            True                  False
  NVDA           80.77               26            1.37              2.03        211.58                42.14         0.527          pass              0.251             23.6                           0.302               -5.85             -0.577                  ok            True                  False
   LIN           95.24               21            0.90              3.29        520.07                19.32         0.525          pass              0.621             31.9                           0.372                4.54              0.436                  ok            True                  False
  FTNT           94.44               18            1.90              1.99        148.64                47.06         0.519          pass              0.625             44.9                           0.565               -1.48             -0.193                  ok            True                  False
  PANW           85.19               27            1.84              3.66        282.97                59.82         0.518          pass              0.435             43.9                           0.504               -0.40              0.234                  ok            True                  False
  MSTR           85.37               41            0.92              0.84        130.78                75.43         0.509          pass              0.552             52.8                           0.425               -4.51             -0.322                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-06-16T10:14:03.006542-04:00 early_entry_1010 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T09:17:33.022205-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T09:07:53.036386-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T08:52:12.067336-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T08:35:06.869974-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T08:34:05.066207-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T08:16:33.030188-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T08:07:34.001869-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T07:49:39.046752-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-06-16T07:33:34.031589-04:00     data_refresh       data_refresh                                                         {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260616101403)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260616101403)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260616101403)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260616101403)

</details>
