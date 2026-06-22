# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-22 15:30:02 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$2,962.50`
- Equity: `$26,043.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$-471.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option  WMT260724C00120000       2026-06-18                   1     52     13052.0                 12896.0         2.51           2.48      117.33        117.32          bid_ask_mid                       2.48                bid_ask_mid                    True          -156.0                   -1.2         86.21               29              0.68         25.57           27.23                  34.58                 124.0           47.0               0.14                      ok
  MRVL     option         option MRVL260724C00310000       2026-06-22                   0      3     10500.0                 10185.0        35.00          33.95      305.16        306.17          bid_ask_mid                      33.95                bid_ask_mid                    True          -315.0                   -3.0        100.00               24              1.75        101.16           96.82                 150.94                 195.0           52.0               0.06                      ok
```

## Today's Closed Trades (2026-06-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               26            1.42              3.09        309.25               150.94         0.841          pass              0.784             64.4                           0.584               16.20              1.434                      ok            True                  False
  QCOM           86.36               22            1.75              2.76        224.93                96.20         0.665          pass              0.505             62.8                           0.368                2.88              0.646                      ok            True                  False
  UPRO           95.24               21            1.26              1.26        142.27                49.73         0.621          pass              0.563              9.3                           0.146                2.53              0.492                      ok            True                  False
  MPWR           90.91               22            2.36             25.88       1552.61                82.20         0.591          pass              0.536             35.5                           0.340                3.08              0.062                      ok            True                  False
  CDNS           92.86               28            1.27              3.44        385.92                57.09         0.586          pass              0.661             46.6                           0.423                1.67              0.040                      ok            True                  False
  ASML           92.00               25            1.96             26.43       1918.35                57.74         0.564          pass              0.514             12.6                           0.342               15.24              1.205                      ok            True                  False
  CRWD           85.19               27            1.28              6.14        682.23                61.84         0.563          pass              0.382             24.8                           0.311                0.76              0.420                      ok            True                  False
   WDC           92.00               25            1.99             10.38        741.78                88.76         0.560          pass              0.549             24.5                           0.195               42.93              4.548                      ok            True                  False
  SBUX           83.33               24            0.63              0.44        100.46                26.69         0.525          pass              0.444             69.9                           0.356                4.96              0.551                      ok            True                  False
  PANW           92.68               41            0.66              1.32        287.21                57.46         0.520          pass              0.769             59.5                           0.339                5.09              0.852                      ok            True                  False
   ROP           86.67               15            1.86              4.31        328.41                27.66         0.506          pass              0.380             39.3                           0.507               -2.43             -0.178                      ok            True                  False
    ZS           78.12               32            1.44              1.26        124.31               152.43         0.865          pass              0.361             42.5                           0.499               -5.91             -0.368 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et           slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-22T15:10:01.120080-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:05:02.154937-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:00:02.230019-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T14:55:01.213018-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T14:50:05.502859-04:00     entry_1500          entry {"allocated_cash": 10500.0, "asset_type": "option", "contract_symbol": "MRVL260724C00310000", "contracts": 3, "early_entry_score": 0.746, "entry_mode": "regular", "entry_option_price": 35.0, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 195.0, "option_spread_pct": 5.71, "option_volume": 52.0, "success_rate": 100.0, "ticker": "MRVL", "timing_score": 0.836}
2026-06-22T14:50:05.502859-04:00     entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                        {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-22", "training_samples": 5273, "window": 5}
2026-06-22T03:00:02.560041-04:00   data_refresh   data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-20T02:55:02.206016-04:00 share_ext_0255  market_closed                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:50:04.120512-04:00 share_ext_0250  market_closed                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-06-20T02:45:02.079519-04:00 share_ext_0245  market_closed                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260622153002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260622153002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260622153002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260622153002)

</details>
