# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-09 09:45:02 EDT`
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

- Cash: `$16,069.75`
- Equity: `$31,029.75`
- Realized PnL: `$21,794.75`
- Unrealized PnL: `$-765.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260717C00100000       2026-06-08                   1     17     15725.0                 14960.0         9.25            8.8       97.75         98.47     last_price_stale                        NaN                unavailable                   False          -765.0                  -4.86         93.94               33              1.73         79.38            1.56                  86.36                1396.0           69.0               0.05                      ok
```

## Today's Closed Trades (2026-06-09)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  PANW           91.43               35            0.69              1.29        265.78                58.75         0.582          pass              0.753             74.5                           0.525                3.01              0.456                       ok            True                  False
  WDAY           81.82               22            2.45              2.47        142.70                70.13         0.546          pass              0.299             38.7                           0.411               13.07              1.325                       ok            True                  False
  FTNT          100.00               23            1.57              1.57        142.37                44.62         0.522          pass              0.654             38.5                           0.330                5.10              1.074                       ok            True                  False
  QCOM           91.67               12            2.32              3.53        216.26               102.17         0.703          pass              0.492             32.4                           0.302              -14.19             -1.225  downtrend_blocked_slope           False                  False
  CSCO           96.67               30            0.48              0.41        123.97                58.94         0.646          pass              0.817             73.1                           0.551                4.42              0.575                       ok           False                  False
  PAYX          100.00               23            0.33              0.23         98.82                34.09         0.624          pass              0.789             80.1                           0.528                4.00              0.497                       ok           False                  False
  CRWD           88.00               25            1.26              5.81        656.30                61.55         0.591          pass              0.524             50.5                           0.358               -3.14             -0.141 downtrend_blocked_streak           False                  False
   EXC           86.96               23            0.20              0.06         44.77                22.32         0.567          pass              0.588             86.4                           0.637               -1.95             -0.147                       ok           False                  False
  AAPL          100.00               11            1.49              3.14        300.19                19.03         0.557          pass              0.462              0.0                           0.217               -3.66             -0.319  downtrend_blocked_slope           False                  False
   APP           86.05               43            0.50              1.97        562.85                67.73         0.552          pass              0.643             75.6                           0.512                9.07             -0.068                       ok           False                  False
  MSFT           88.24               34            0.41              1.18        411.24                36.13         0.546          pass              0.623             62.9                           0.538               -1.43             -0.301                       ok           False                  False
  ADBE           83.33               42            0.27              0.47        244.79                49.77         0.520          pass              0.595             84.8                           0.696                1.59              0.218                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-09T00:00:03.806421-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-08T15:10:01.789141-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T15:05:04.798011-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T15:00:02.588621-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:55:02.835387-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-08T14:50:04.804691-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-08", "training_samples": 5231, "window": 5}
2026-06-08T14:50:04.804691-04:00       entry_1500              entry {"allocated_cash": 15725.0, "asset_type": "option", "contract_symbol": "TEAM260717C00100000", "contracts": 17, "early_entry_score": 0.733, "entry_mode": "regular", "entry_option_price": 9.25, "execution_mode": "option", "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1396.0, "option_spread_pct": 5.41, "option_volume": 69.0, "success_rate": 93.94, "ticker": "TEAM", "timing_score": 0.623}
2026-06-08T12:35:06.508215-04:00      manage_1230               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "TEAM260717C00100000", "fill_price": 8.865, "pnl": -1576.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-06-08T12:00:05.977560-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-08T11:55:06.347594-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260609094502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260609094502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260609094502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260609094502)

</details>
