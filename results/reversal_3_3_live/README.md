# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 09:40:02 EDT`
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

- Cash: `$41,269.30`
- Equity: `$79,609.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$-1,755.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode        instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
    ZS     option         option ZS261120C00200000       2026-10-02                   1     27     40095.0                 38340.0        14.85           14.2      196.86        202.24     last_price_stale                        NaN                unavailable                   False         -1755.0                  -4.38         94.59               37              0.97         55.98             0.0                   77.3                 818.0          103.0               0.04                      ok
```

## Today's Closed Trades (2026-10-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           84.85               33            1.45              1.66        162.96               114.85         0.737          pass              0.497             46.7                           0.587               13.72              0.983                      ok            True                  False
  AMGN           84.62               26            0.71              2.00        402.18                47.11         0.580          pass              0.445             52.4                           0.331                1.79              0.112                      ok            True                  False
  MRVL           83.78               37            0.55              1.04        271.84                54.74         0.525          pass              0.479             48.6                           0.436                5.21              0.481                      ok            True                  False
   XEL           85.00               20            0.55              0.27         71.28                18.48         0.518          pass              0.369             39.1                           0.322               -1.17             -0.056                      ok            True                  False
    MU           90.32               31            1.20              9.04       1071.02                50.82         0.511          pass              0.481              4.9                           0.145                1.73              0.030                      ok            True                  False
  NXPI           86.21               29            1.05              1.80        242.89                37.68         0.507          pass              0.485             47.2                           0.411                3.73              0.353                      ok            True                  False
  DRAM           81.08               37            0.02              0.01         61.74                54.09         0.587          pass              0.559             97.1                           0.685                0.24             -0.110                      ok           False                  False
   TRI           89.47               38            0.29              0.20         97.54                53.36         0.558          pass              0.720             75.0                           0.774                2.00              0.108                      ok           False                  False
  INTC           84.85               33            1.76              1.47        118.70                74.20         0.552          pass              0.527             63.2                           0.829               -3.74             -0.526 downtrend_blocked_slope           False                  False
  CRWD           89.13               46            0.20              0.38        269.88                56.43         0.546          pass              0.742             81.2                           0.465                8.08              0.743                      ok           False                  False
  ASML           82.86               35            0.44              5.80       1864.83                42.39         0.545          pass              0.518             73.5                           0.736                8.63              0.852                      ok           False                  False
  CSCO           89.19               37            0.12              0.10        112.16                31.23         0.518          pass              0.731             84.6                           0.739                0.93              0.320                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-05T03:00:05.114767-04:00   data_refresh  data_refresh                   {'saved': 92, 'empty': 1}
2026-10-03T02:55:05.889514-04:00 share_ext_0255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:50:05.063422-04:00 share_ext_0250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:45:04.071042-04:00 share_ext_0245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:40:05.983879-04:00 share_ext_0240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:35:05.098506-04:00 share_ext_0235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:30:06.414009-04:00 share_ext_0230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:25:01.959731-04:00 share_ext_0225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:20:06.968956-04:00 share_ext_0220 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:15:04.972202-04:00 share_ext_0215 market_closed {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005094002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005094002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005094002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005094002)

</details>
