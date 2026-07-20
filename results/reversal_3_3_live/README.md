# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 10:00:05 EDT`
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
- Equity: `$30,764.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$1,540.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260821C00290000       2026-07-17                   1      7     14105.0                 15645.0        20.15          22.35      284.95        290.27          bid_ask_mid                      22.35                bid_ask_mid                    True          1540.0                  10.92          90.0               20              2.15         62.88            63.6                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.00               10            2.02              0.80         56.22                61.55         0.667          pass              0.098             10.5                           0.136               22.90              2.766                  ok            True                  False
  AAPL           90.91               11            1.47              3.44        332.27                36.42         0.618          pass              0.384              8.1                           0.161                5.17              0.720                  ok            True                  False
  META           82.61               23            1.37              6.20        643.35                53.08         0.593          pass              0.250             11.5                           0.171                6.14              0.838                  ok            True                  False
   WBD           86.67               15            0.87              0.16         26.80                20.40         0.572          pass              0.302             11.3                           0.133                1.97              0.381                  ok            True                  False
  PAYX          100.00               19            1.53              1.22        113.87                33.31         0.544          pass              0.523              2.8                           0.047                6.88              0.787                  ok            True                  False
  TMUS           91.67               24            1.08              1.46        191.81                36.04         0.530          pass              0.611             51.3                           0.325                4.71              0.602                  ok            True                  False
  BKNG           82.61               23            1.47              1.87        180.88                41.44         0.524          pass              0.209              0.0                           0.177               -1.12              0.156                  ok            True                  False
  ORLY           80.00               25            1.43              0.86         85.68                41.23         0.523          pass              0.154              0.4                           0.151                0.69             -0.011                  ok            True                  False
   ADP           94.74               19            1.38              2.47        254.21                34.14         0.522          pass              0.505              0.0                           0.171                5.11              0.596                  ok            True                  False
   ROP           88.24               17            1.83              4.65        361.15                31.85         0.521          pass              0.373             18.1                           0.223               -1.88             -0.075                  ok            True                  False
  ABNB           97.06               34            0.60              0.62        145.72                32.96         0.504          pass              0.742             43.9                           0.281               -1.73             -0.052                  ok            True                  False
   KHC           88.24               17            0.33              0.06         25.85                35.69         0.628          pass              0.521             63.8                           0.593                3.93              0.462                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-07-20T10:00:05.019489-04:00 early_entry_1000 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-20T03:00:02.156318-04:00     data_refresh       data_refresh                                                         {'saved': 93}
2026-07-18T02:55:03.939140-04:00   share_ext_0255      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:50:01.103428-04:00   share_ext_0250      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:45:05.126153-04:00   share_ext_0245      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:40:02.148173-04:00   share_ext_0240      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:35:01.094896-04:00   share_ext_0235      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:30:05.538230-04:00   share_ext_0230      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:25:04.133294-04:00   share_ext_0225      market_closed                           {"holiday_name": null, "reason": "weekend"}
2026-07-18T02:20:01.118741-04:00   share_ext_0220      market_closed                           {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720100005)

</details>
