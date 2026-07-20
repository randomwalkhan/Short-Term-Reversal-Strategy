# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-20 09:30:01 EDT`
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
   TXN     option         option TXN260821C00290000       2026-07-17                   1      7     14105.0                 14175.0        20.15          20.25      284.95        288.77     last_price_stale                        NaN                unavailable                   False            70.0                    0.5          90.0               20              2.15         62.88            0.39                  64.46                 207.0          231.0               0.09                      ok
```

## Today's Closed Trades (2026-07-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  PYPL           86.67               30            0.72              0.29         56.44                61.55         0.640          pass              0.530             51.6                           0.598               24.53              2.826                      ok            True                  False
  PAYX          100.00               29            0.74              0.60        114.13                33.31         0.531          pass              0.714             44.8                           0.340                7.73              0.823                      ok            True                  False
   ROP           92.31               26            1.05              2.68        361.99                31.85         0.525          pass              0.541             17.8                           0.170               -1.11             -0.039                      ok            True                  False
  ABNB           96.30               27            1.23              1.27        147.25                32.96         0.514          pass              0.661             32.2                           0.312               -1.13             -0.025                      ok            True                  False
   ADP           96.67               30            0.50              0.91        256.17                34.14         0.506          pass              0.808             74.7                           0.601                6.59              0.660                      ok            True                   True
   KHC           88.24               17            0.30              0.05         25.86                35.69         0.633          pass              0.485             51.7                           0.408                3.96              0.463                      ok           False                  False
  MDLZ           94.44               18            0.34              0.15         60.94                32.63         0.606          pass              0.663             54.7                           0.359                2.74              0.270                      ok           False                  False
   PEP           90.00               30            0.04              0.03        137.11                30.73         0.569          pass              0.726             89.6                           0.580               -4.34             -0.510 downtrend_blocked_slope           False                  False
  NFLX           72.22               18            1.61              0.78         68.62                47.14         0.560          pass              0.162             17.5                           0.240              -10.76             -0.967 downtrend_blocked_slope           False                  False
   AEP           71.43               21            0.71              0.66        132.85                22.59         0.519          pass              0.216             30.4                           0.336               -2.79             -0.352 downtrend_blocked_slope           False                  False
  AAPL           97.62               42            0.22              0.50        333.52                36.42         0.513          pass              0.864             70.9                           0.521                6.51              0.777                      ok           False                  False
  TMUS           91.18               34            0.38              0.52        192.21                36.04         0.509          pass              0.757             82.7                           0.556                5.45              0.634                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260720093001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260720093001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260720093001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260720093001)

</details>
