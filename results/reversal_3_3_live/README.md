# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 09:55:01 EDT`
Last processed slot: `manage_1000`

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
- Equity: `$30,606.75`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$1,382.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260821C00290000       2026-07-17                   1      7     14105.0                 15487.5        20.15          22.12      284.95        290.86          bid_ask_mid                      22.12                bid_ask_mid                    True          1382.5                    9.8          90.0               20              2.15         62.88           62.93                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.00               10            2.22              0.88         56.18                61.55         0.655          pass              0.071              2.0                           0.079               22.65              2.757                  ok            True                  False
  AAPL           90.91               11            1.51              3.53        332.23                36.42         0.617          pass              0.362              1.0                           0.186                5.13              0.718                  ok            True                  False
  META           82.76               29            0.92              4.17        644.22                53.08         0.588          pass              0.324             21.7                           0.218                6.63              0.858                  ok            True                  False
  TMUS           88.24               17            1.42              1.91        191.61                36.04         0.551          pass              0.430             36.1                           0.239                4.35              0.586                  ok            True                  False
   WBD           90.91               22            0.58              0.11         26.82                20.40         0.549          pass              0.550             41.5                           0.270                2.28              0.395                  ok            True                  False
  PAYX          100.00               19            1.46              1.17        113.89                33.31         0.548          pass              0.537              7.2                           0.192                6.96              0.791                  ok            True                  False
   ROP           88.89               18            1.64              4.16        361.36                31.85         0.527          pass              0.423             26.7                           0.211               -1.69             -0.066                  ok            True                  False
   ADP           95.24               21            1.23              2.20        254.32                34.14         0.520          pass              0.540              4.8                           0.078                5.27              0.603                  ok            True                  False
  ORLY           82.76               29            1.16              0.70         85.75                41.23         0.519          pass              0.282              9.9                           0.098                0.96              0.001                  ok            True                  False
  BKNG           86.21               29            1.03              1.32        181.12                41.44         0.518          pass              0.424             26.6                           0.200               -0.68              0.176                  ok            True                  False
  PCAR           87.10               31            0.78              0.69        125.90                30.30         0.500          pass              0.445             22.0                           0.177               -0.56              0.110                  ok            True                  False
   KHC           87.50               16            0.37              0.07         25.85                35.69         0.631          pass              0.482             59.6                           0.534                3.89              0.460                  ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720095501)

</details>
