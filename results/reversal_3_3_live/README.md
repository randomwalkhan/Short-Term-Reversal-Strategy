# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 15:55:04 EDT`
Last processed slot: `manage_1600`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$33,483.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-120.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13290.0         44.7           44.3      510.62        507.93          -120.0                  -0.89         97.14               35               0.5         52.16           54.48                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           85.71               14            4.86              2.89         83.76               115.69         0.600          pass              0.281             14.0                           0.227               14.73              1.325                                 ok            True                  False
   ADP          100.00               10            2.35              3.52        212.30                33.54         0.542          pass              0.591             45.7                           0.502               -2.92             -0.106                                 ok            True                  False
  SNPS           97.06               34            1.03              3.69        511.63                43.23         0.528          pass              0.768             51.7                           0.497                5.55              0.690                                 ok            True                  False
  CDNS           96.77               31            1.17              2.93        356.78                38.69         0.518          pass              0.736             47.9                           0.407                7.25              0.875                                 ok            True                  False
  CHTR           75.00               16            2.91              3.01        146.63               118.13         0.765          pass              0.207             30.1                           0.577               -9.48             -1.371            downtrend_blocked_slope           False                  False
  INTC          100.00               36            0.35              0.29        120.48               109.00         0.670          pass              0.910             90.0                           0.430               26.85              3.178                                 ok           False                  False
  ORLY           83.33                6            2.39              1.54         91.18                35.45         0.560          pass              0.227             27.3                           0.294               -2.23             -0.568 downtrend_blocked_slope_and_streak           False                  False
  GEHC           75.00               40            0.48              0.21         62.20                57.10         0.559          pass              0.486             76.6                           0.671                4.21              0.380                                 ok           False                  False
  MELI           88.46               26            1.62             17.92       1571.10                57.67         0.527          pass              0.593             69.4                           0.706              -12.10             -1.683            downtrend_blocked_slope           False                  False
   PEP           88.89                9            1.76              1.87        151.05                21.96         0.527          pass              0.313              7.6                           0.189               -3.93             -0.473            downtrend_blocked_slope           False                  False
  TMUS           80.95               21            1.62              2.20        192.36                36.44         0.519          pass              0.160              3.1                           0.249               -4.04             -0.310            downtrend_blocked_slope           False                  False
  MCHP           79.17               24            1.36              0.93         97.30                50.72         0.517          pass              0.261             38.7                           0.242                6.88              0.728                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T15:10:06.837461-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T15:05:03.914074-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T15:00:02.608671-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:55:04.771508-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T12:00:04.870227-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513155504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513155504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513155504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513155504)

</details>
