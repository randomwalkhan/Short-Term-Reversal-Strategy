# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-22 15:05:09 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$2,402.75`
- Equity: `$28,482.75`
- Realized PnL: `$18,317.75`
- Unrealized PnL: `$165.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   0     38     13775.0                 14440.0         3.62            3.8      103.16        103.41          bid_ask_mid                        3.8                bid_ask_mid                    True           665.0                   4.83         94.74               19              0.93         28.13           28.55                  32.97                2147.0           78.0               0.07                      ok
  AVGO     option         option AVGO260717C00420000       2026-05-21                   1      4     12140.0                 11640.0        30.35           29.1      415.18        412.39          bid_ask_mid                       29.1                bid_ask_mid                    True          -500.0                  -4.12         91.67               36              0.62         50.17           50.30                  40.33                2101.0          296.0               0.03                      ok
```

## Today's Closed Trades (2026-05-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SBUX           95.45               22            0.69              0.50        103.91                32.97         0.580          pass              0.714             58.6                           0.718               -0.87             -0.035                                 ok            True                  False
  MELI           94.59               37            0.71              8.33       1674.33                61.16         0.574          pass              0.798             57.1                           0.460                2.05              0.511                                 ok            True                  False
  NVDA           85.71               21            1.60              2.46        218.46                44.83         0.526          pass              0.336             19.3                           0.302                0.37             -0.045                                 ok            True                  False
  INSM           70.83               24            2.40              1.84        108.74               111.27         0.725          pass              0.214             16.0                           0.229                5.48             -0.003                                 ok           False                  False
  GEHC           75.00               40            0.26              0.12         64.28                59.89         0.575          pass              0.436             59.5                           0.385                1.09              0.260                                 ok           False                  False
   WMT           93.75               16            1.10              0.93        120.94                34.61         0.573          pass              0.600             45.3                           0.476               -7.99             -0.507            downtrend_blocked_slope           False                  False
  REGN           93.33               30            0.89              4.01        640.87                49.06         0.549          pass              0.779             78.5                           0.697              -10.78             -1.533 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           86.67               30            0.85              2.31        386.67                41.05         0.544          pass              0.396             10.3                           0.232               -4.10             -0.267            downtrend_blocked_slope           False                  False
    EA           83.33               12            0.43              0.61        201.61                 2.73         0.543          pass              0.294             46.0                           0.298                0.28              0.076                                 ok           False                  False
   WDC           95.12               41            0.27              0.92        486.06                59.01         0.538          pass              0.904             83.3                           0.637                1.07             -0.537                                 ok           False                  False
  GOOG           87.88               33            0.75              2.00        382.61                40.91         0.534          pass              0.444              9.1                           0.227               -4.14             -0.291 downtrend_blocked_slope_and_streak           False                  False
  COST           75.00                4            2.22             16.35       1043.44                22.19         0.515          pass              0.073              7.2                           0.161                1.82              0.533                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-05-22T15:05:09.997978-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T15:00:10.044120-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T14:55:09.944950-04:00       entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-05-22T14:50:09.909553-04:00       entry_1500          entry {"allocated_cash": 13775.0, "asset_type": "option", "contract_symbol": "SBUX260717C00105000", "contracts": 38, "early_entry_score": 0.644, "entry_mode": "regular", "entry_option_price": 3.625, "execution_mode": "option", "matched_signals": 19, "option_liquidity_status": "ok", "option_open_interest": 2147.0, "option_spread_pct": 6.9, "option_volume": 78.0, "success_rate": 94.74, "ticker": "SBUX", "timing_score": 0.584}
2026-05-22T14:50:09.909553-04:00       entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-22", "training_samples": 5081, "window": 5}
2026-05-22T12:00:04.237005-04:00 early_entry_1200  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:55:01.324366-04:00 early_entry_1155  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:50:01.298135-04:00 early_entry_1150  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:45:04.354154-04:00 early_entry_1145  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
2026-05-22T11:40:06.366318-04:00 early_entry_1140  entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260522150509)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260522150509)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260522150509)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260522150509)

</details>
