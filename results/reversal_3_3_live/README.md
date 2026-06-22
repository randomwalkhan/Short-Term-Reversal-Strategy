# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-22 13:50:01 EDT`
Last processed slot: `manage_1400`

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
- Equity: `$27,346.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$832.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT260724C00120000       2026-06-18                   1     52     13052.0                 13884.0         2.51           2.67      117.33        117.39          bid_ask_mid                       2.67                bid_ask_mid                    True           832.0                   6.37         86.21               29              0.68         25.57           28.43                  34.58                 124.0           47.0               0.14                      ok
```

## Today's Closed Trades (2026-06-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               26            1.35              2.93        309.33               150.94         0.844          pass              0.790             66.3                           0.674               16.29              1.438                      ok            True                  False
   PEP          100.00               13            0.51              0.51        141.80                22.29         0.650          pass              0.503              5.8                           0.098               -0.44              0.030                      ok            True                  False
  UPRO           92.31               26            0.74              0.74        142.49                49.73         0.619          pass              0.638             47.2                           0.351                3.08              0.516                      ok            True                  False
  MPWR           91.30               23            2.05             22.41       1554.10                82.20         0.607          pass              0.581             44.2                           0.483                3.42              0.077                      ok            True                  False
  CDNS           91.67               24            1.72              4.67        385.39                57.09         0.583          pass              0.545             27.5                           0.520                1.21              0.020                      ok            True                  False
   WDC           92.86               28            1.48              7.74        742.91                88.76         0.576          pass              0.652             43.7                           0.528               43.67              4.572                      ok            True                  False
  ASML           92.00               25            1.98             26.80       1918.19                57.74         0.562          pass              0.506              9.9                           0.203               15.21              1.204                      ok            True                  False
  NVDA           80.65               31            0.85              1.26        210.15                45.37         0.549          pass              0.290             25.9                           0.209                1.85              0.167                      ok            True                  False
  CRWD           89.47               38            0.66              3.14        683.51                61.84         0.538          pass              0.639             48.7                           0.388                1.39              0.449                      ok            True                  False
  PANW           92.86               42            0.52              1.04        287.33                57.46         0.523          pass              0.799             68.1                           0.518                5.23              0.859                      ok            True                  False
   ROP           86.67               15            1.95              4.50        328.32                27.66         0.516          pass              0.289              8.7                           0.140               -2.52             -0.182                      ok            True                  False
    ZS           76.67               30            1.80              1.58        124.17               152.43         0.858          pass              0.303             28.1                           0.428               -6.25             -0.385 downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260622135001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260622135001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260622135001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260622135001)

</details>
