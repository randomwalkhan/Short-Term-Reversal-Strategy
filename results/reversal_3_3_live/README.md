# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 09:35:04 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$29,294.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$70.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   TXN     option         option TXN260821C00290000       2026-07-17                   1      7     14105.0                 14175.0        20.15          20.25      284.95        289.23     last_price_stale                        NaN                unavailable                   False            70.0                    0.5          90.0               20              2.15         62.88             0.1                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PYPL           80.95               21            1.16              0.46         56.36                61.55         0.662          pass              0.233             22.6                           0.348               23.99              2.806                  ok            True                  False
   KHC           90.91               11            0.73              0.13         25.82                35.69         0.645          pass              0.362              0.0                           0.263                3.51              0.443                  ok            True                  False
  META           82.76               29            0.93              4.19        644.21                53.08         0.587          pass              0.323             21.2                           0.287                6.62              0.858                  ok            True                  False
  AAPL           96.30               27            0.63              1.46        333.11                36.42         0.583          pass              0.631             19.9                           0.240                6.07              0.759                  ok            True                  False
   WBD           84.62               13            0.89              0.17         26.80                20.40         0.583          pass              0.201              0.0                           0.237                1.95              0.380                  ok            True                  False
  PAYX          100.00               22            1.21              0.97        113.97                33.31         0.547          pass              0.565             10.1                           0.165                7.23              0.802                  ok            True                  False
   ROP           83.33               12            2.04              5.19        360.92                31.85         0.537          pass              0.156              0.0                           0.179               -2.09             -0.085                  ok            True                  False
  TMUS           92.00               25            0.94              1.26        191.89                36.04         0.533          pass              0.647             57.7                           0.325                4.86              0.608                  ok            True                  False
  CTAS           86.96               23            1.08              1.54        203.79                36.07         0.524          pass              0.469             48.0                           0.396               13.47              1.537                  ok            True                  False
   ADP           95.65               23            1.06              1.89        254.45                34.14         0.520          pass              0.569             10.0                           0.068                5.46              0.611                  ok            True                  False
  BKNG           88.24               34            0.65              0.83        181.32                41.44         0.512          pass              0.591             53.5                           0.300               -0.30              0.194                  ok            True                  False
  PCAR           87.88               33            0.64              0.56        125.96                30.30         0.501          pass              0.436              7.5                           0.111               -0.41              0.117                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720093504)

</details>
