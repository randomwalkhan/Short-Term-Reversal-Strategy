# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 14:55:04 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$33,333.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$-270.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13140.0         44.7           43.8      510.62        507.16          -270.0                  -2.01         97.14               35               0.5         52.16           54.57                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           88.89               18            4.40              2.62         83.88               115.69         0.606          pass              0.417             22.1                           0.359               15.28              1.347                                 ok            True                  False
   ADP           92.31               13            2.00              3.00        212.53                33.54         0.530          pass              0.562             53.7                           0.770               -2.57             -0.090                                 ok            True                  False
  SNPS           96.97               33            1.18              4.23        511.40                43.23         0.526          pass              0.740             44.6                           0.633                5.39              0.683                                 ok            True                  False
  CDNS           96.67               30            1.36              3.42        356.57                38.69         0.514          pass              0.702             39.2                           0.345                7.03              0.866                                 ok            True                  False
  MCHP           80.77               26            1.26              0.86         97.33                50.72         0.513          pass              0.308             43.1                           0.212                6.99              0.732                                 ok            True                  False
  MSTR           90.32               31            2.27              2.93        183.16                75.69         0.503          pass              0.624             52.7                           0.564               13.94              1.264                                 ok            True                  False
  CHTR           63.64               11            3.47              3.60        146.38               118.13         0.751          pass              0.128             15.3                           0.333              -10.00             -1.397            downtrend_blocked_slope           False                  False
  GEHC           73.68               38            0.53              0.23         62.19                57.10         0.566          pass              0.466             74.2                           0.502                4.16              0.377                                 ok           False                  False
  ORLY           80.00               10            1.95              1.25         91.30                35.45         0.554          pass              0.178             40.7                           0.498               -1.79             -0.548 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.00               10            1.61              1.71        151.12                21.96         0.530          pass              0.366             15.6                           0.421               -3.79             -0.466            downtrend_blocked_slope           False                  False
  MELI           88.46               26            1.64             18.15       1571.00                57.67         0.526          pass              0.592             69.0                           0.623              -12.12             -1.684            downtrend_blocked_slope           False                  False
  TMUS           83.33               24            1.28              1.74        192.56                36.44         0.523          pass              0.301             22.3                           0.405               -3.71             -0.294            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-13T14:55:04.771508-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-13T14:50:04.762391-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T14:50:04.762391-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-13", "training_samples": 5035, "window": 5}
2026-05-13T12:00:04.870227-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:55:04.850117-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:50:06.013562-04:00 early_entry_1150  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:45:03.915734-04:00 early_entry_1145  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:23:31.678775-04:00 early_entry_1120  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:05:05.896760-04:00 early_entry_1105  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-13T11:00:06.549783-04:00 early_entry_1100  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513145504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513145504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513145504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513145504)

</details>
