# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 09:35:05 EDT`
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

- Cash: `$1,161.80`
- Equity: `$143,751.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$-1,080.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option  EXC261218C00045000       2026-10-23                   1    657     72270.0                 72270.0         1.10           1.10       44.42         44.57     last_price_stale                        NaN                unavailable                   False             0.0                   0.00          80.0               15              0.97         20.09            0.78                  20.91                 278.0           48.0               0.09                      ok
  TEAM     option         option TEAM261120C00230000       2026-10-22                   2     40     71400.0                 70320.0        17.85          17.58      223.97        224.91     last_price_stale                        NaN                unavailable                   False         -1080.0                  -1.51         100.0               38              0.68         80.16            1.56                  49.42                7633.0           62.0               0.11                      ok
```

## Today's Closed Trades (2026-10-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           91.89               37            0.58              1.04        254.70                57.49         0.547            pass              0.595             14.4                           0.383               12.35              1.248                                 ok            True                  False
   CEG           83.33               36            0.57              1.01        253.01                65.46         0.614            pass              0.324              0.0                           0.279              -14.25             -1.580 downtrend_blocked_slope_and_streak           False                  False
  MRVL           90.00               40            0.26              0.42        228.33                64.81         0.554            pass              0.782             86.8                           0.494              -14.27             -1.468            downtrend_blocked_slope           False                  False
  MDLZ           96.15               26            0.31              0.14         63.74                25.23         0.543            pass              0.743             60.8                           0.408                2.93              0.369                                 ok           False                  False
  MPWR           78.57               42            0.17              1.38       1139.53                56.28         0.535            pass              0.485             77.2                           0.443              -13.73             -1.296            downtrend_blocked_slope           False                  False
 CMCSA          100.00                2            2.29              0.36         22.53                23.68         0.525            pass              0.505             17.5                           0.207                7.21              0.886                                 ok           False                  False
  AAPL           89.47               19            1.03              2.51        346.65                16.45         0.497 below_threshold              0.492             43.3                           0.514                0.93              0.152                                 ok           False                  False
  PYPL           85.71               14            1.74              0.69         56.72                19.14         0.495 below_threshold              0.240              3.9                           0.203               -0.04              0.130                                 ok           False                  False
  DASH           78.95               19            2.25              2.83        178.17                51.53         0.494 below_threshold              0.109              0.0                           0.165               -9.73             -0.775            downtrend_blocked_slope           False                  False
  DXCM           86.21               29            1.17              0.64         77.67                37.22         0.493 below_threshold              0.399             19.0                           0.275              -10.35             -1.153 downtrend_blocked_slope_and_streak           False                  False
  NFLX           76.92               26            1.20              0.55         65.61                35.37         0.490 below_threshold              0.193             12.5                           0.124               -7.86             -0.982 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               34            1.19              1.89        226.80                47.89         0.489 below_threshold              0.802             64.5                           0.390                8.26              1.049                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-26T03:00:06.095406-04:00   data_refresh  data_refresh                   {'saved': 91, 'empty': 2}
2026-10-24T02:55:06.111058-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:50:04.428173-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:45:06.637393-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:40:05.798457-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:35:04.182353-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:30:05.264704-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:25:04.373629-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:20:05.341779-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:15:04.235685-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026093505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026093505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026093505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026093505)

</details>
