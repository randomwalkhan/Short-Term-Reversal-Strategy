# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-22 13:35:02 EDT`
Last processed slot: `manage_1330`

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
- Equity: `$27,190.50`
- Realized PnL: `$16,514.50`
- Unrealized PnL: `$676.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   WMT     option         option WMT260724C00120000       2026-06-18                   1     52     13052.0                 13728.0         2.51           2.64      117.33        117.36          bid_ask_mid                       2.64                bid_ask_mid                    True           676.0                   5.18         86.21               29              0.68         25.57           28.59                  34.58                 124.0           47.0               0.14                      ok
```

## Today's Closed Trades (2026-06-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               28            1.13              2.47        309.52               150.94         0.845          pass              0.819             71.6                           0.841               16.54              1.447                      ok            True                  False
  UPRO           91.67               24            0.98              0.98        142.39                49.73         0.615          pass              0.555             29.6                           0.305                2.82              0.505                      ok            True                  False
  MPWR           90.00               20            2.53             27.73       1551.81                82.20         0.592          pass              0.485             30.9                           0.370                2.91              0.054                      ok            True                  False
  CDNS           91.30               23            1.76              4.76        385.35                57.09         0.587          pass              0.525             26.0                           0.491                1.17              0.018                      ok            True                  False
   WDC           92.31               26            1.63              8.50        742.59                88.76         0.579          pass              0.607             38.2                           0.497               43.46              4.565                      ok            True                  False
  PAYX          100.00               23            0.73              0.50         98.02                31.80         0.567          pass              0.743             66.5                           0.536               -2.99             -0.238                      ok            True                  False
  ASML           92.00               25            2.05             27.74       1917.79                57.74         0.557          pass              0.496              6.7                           0.175               15.12              1.201                      ok            True                  False
  NVDA           80.65               31            0.96              1.42        210.08                45.37         0.542          pass              0.260             16.4                           0.188                1.74              0.162                      ok            True                  False
  PANW           92.68               41            0.61              1.23        287.25                57.46         0.523          pass              0.777             62.3                           0.426                5.14              0.854                      ok            True                  False
   ROP           90.91               22            1.49              3.45        328.77                27.66         0.510          pass              0.441              6.4                           0.247               -2.07             -0.161                      ok            True                  False
    ZS           76.67               30            1.87              1.64        124.15               152.43         0.855          pass              0.295             25.2                           0.381               -6.32             -0.388 downtrend_blocked_slope           False                  False
   PEP          100.00               14            0.45              0.45        141.83                22.29         0.647          pass              0.542             16.9                           0.204               -0.38              0.033                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260622133502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260622133502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260622133502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260622133502)

</details>
