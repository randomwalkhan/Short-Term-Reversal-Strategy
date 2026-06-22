# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-22 13:00:05 EDT`
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

- Cash: `$13,462.50`
- Equity: `$27,840.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$1,326.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT260724C00120000       2026-06-18                   1     52     13052.0                 14378.0         2.51           2.76      117.33        117.43          bid_ask_mid                       2.76                bid_ask_mid                    True          1326.0                  10.16         86.21               29              0.68         25.57           28.82                  34.58                 124.0           47.0               0.14                      ok
```

## Today's Closed Trades (2026-06-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               23            2.08              4.51        308.65               150.94         0.826          pass              0.713             48.0                           0.570               15.43              1.404                      ok            True                  False
  UPRO           93.33               30            0.69              0.69        142.51                49.73         0.595          pass              0.699             50.3                           0.422                3.12              0.518                      ok            True                  False
  MPWR           90.48               21            2.41             26.42       1552.38                82.20         0.594          pass              0.515             34.2                           0.394                3.03              0.060                      ok            True                  False
  CDNS           90.00               20            1.99              5.39        385.08                57.09         0.591          pass              0.441             16.2                           0.355                0.93              0.007                      ok            True                  False
  ASML           93.10               29            1.54             20.75       1920.79                57.74         0.566          pass              0.623             30.2                           0.419               15.73              1.225                      ok            True                  False
  PAYX          100.00               23            0.76              0.52         98.02                31.80         0.565          pass              0.739             65.3                           0.563               -3.02             -0.239                      ok            True                  False
  NVDA           81.82               33            0.67              0.99        210.27                45.37         0.549          pass              0.382             41.9                           0.328                2.04              0.176                      ok            True                  False
   WDC           92.00               25            2.21             11.56        741.28                88.76         0.547          pass              0.491              5.5                           0.086               42.60              4.538                      ok            True                  False
    ZS           76.67               30            1.75              1.53        124.20               152.43         0.860          pass              0.310             30.4                           0.519               -6.20             -0.382 downtrend_blocked_slope           False                  False
   PEP          100.00               15            0.32              0.32        141.88                22.29         0.649          pass              0.621             40.9                           0.260               -0.25              0.039                      ok           False                  False
   KHC          100.00                1            2.17              0.35         22.67                27.88         0.625          pass              0.480              5.7                           0.189               -1.13             -0.190                      ok           False                  False
  AVGO           75.00               12            3.44              9.91        407.10                74.96         0.598          pass              0.144             23.5                           0.440                2.97              0.313                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-06-22T03:00:02.560041-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-06-20T02:55:02.206016-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:50:04.120512-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:45:02.079519-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:40:02.993800-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:35:04.122508-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:30:05.305021-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T01:05:03.587151-04:00 share_ext_0105 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T01:00:02.570714-04:00 share_ext_0100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-20T00:55:02.530724-04:00 share_ext_0055 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260622130005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260622130005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260622130005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260622130005)

</details>
