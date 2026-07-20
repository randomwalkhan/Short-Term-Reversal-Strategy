# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 09:45:05 EDT`
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

- Cash: `$15,119.25`
- Equity: `$30,414.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$1,190.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260821C00290000       2026-07-17                   1      7     14105.0                 15295.0        20.15          21.85      284.95        290.52          bid_ask_mid                      21.85                bid_ask_mid                    True          1190.0                   8.44          90.0               20              2.15         62.88           62.11                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.00               10            1.94              0.77         56.23                61.55         0.671          pass              0.109             14.1                           0.264               23.00              2.770                  ok            True                  False
   KHC           90.91               11            0.89              0.16         25.81                35.69         0.634          pass              0.361              0.0                           0.223                3.34              0.436                  ok            True                  False
  AAPL           95.65               23            0.94              2.19        332.80                36.42         0.585          pass              0.593             16.0                           0.265                5.74              0.744                  ok            True                  False
  TMUS           88.24               17            1.44              1.94        191.60                36.04         0.550          pass              0.427             35.1                           0.231                4.33              0.585                  ok            True                  False
  PAYX          100.00               21            1.32              1.06        113.94                33.31         0.545          pass              0.552              7.9                           0.115                7.11              0.797                  ok            True                  False
   ROP           89.47               19            1.48              3.75        361.53                31.85         0.531          pass              0.467             33.9                           0.259               -1.53             -0.059                  ok            True                  False
  ORLY           82.14               28            1.20              0.72         85.74                41.23         0.522          pass              0.251              7.2                           0.195                0.93             -0.000                  ok            True                  False
  BKNG           87.50               32            0.74              0.94        181.28                41.44         0.519          pass              0.540             47.3                           0.270               -0.39              0.190                  ok            True                  False
   ADP           96.30               27            0.85              1.52        254.61                34.14         0.506          pass              0.667             34.3                           0.366                5.68              0.621                  ok            True                  False
  PCAR           87.88               33            0.58              0.51        125.98                30.30         0.501          pass              0.541             42.5                           0.268               -0.35              0.119                  ok            True                  False
  MDLZ          100.00                7            1.41              0.60         60.74                32.63         0.604          pass              0.500             13.1                           0.216                1.64              0.221                  ok           False                  False
   KDP           92.59               27            0.29              0.06         30.88                36.31         0.586          pass              0.628             40.0                           0.313               -2.93             -0.234                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-07-20T03:00:02.156318-04:00   data_refresh  data_refresh                               {'saved': 93}
2026-07-18T02:55:03.939140-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:50:01.103428-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:45:05.126153-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:40:02.148173-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:35:01.094896-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:30:05.538230-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:25:04.133294-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:20:01.118741-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:15:01.103129-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720094505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720094505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720094505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720094505)

</details>
