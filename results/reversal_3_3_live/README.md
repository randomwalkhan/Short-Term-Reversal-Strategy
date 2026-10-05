# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 09:50:04 EDT`
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

- Cash: `$41,269.30`
- Equity: `$84,266.80`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$2,902.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode        instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
    ZS     option         option ZS261120C00200000       2026-10-02                   1     27     40095.0                 42997.5        14.85          15.92      196.86        202.02          bid_ask_mid                      15.92                bid_ask_mid                    True          2902.5                   7.24         94.59               37              0.97         55.98           51.51                   77.3                 818.0          103.0               0.04                      ok
```

## Today's Closed Trades (2026-10-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           83.87               31            2.39              2.74        162.54               114.85         0.695          pass              0.402             29.6                           0.384               12.66              0.940                      ok            True                  False
  ASML           80.65               31            0.89             11.64       1862.32                42.39         0.538          pass              0.351             46.8                           0.437                8.14              0.832                      ok            True                  False
   TRI           86.67               30            1.33              0.91         97.23                53.36         0.536          pass              0.365              0.0                           0.325                0.93              0.060                      ok            True                  False
   ADI           86.36               22            1.39              4.05        415.42                32.86         0.517          pass              0.346             15.0                           0.250                7.41              0.776                      ok            True                  False
    MU           89.66               29            1.36             10.21       1070.52                50.82         0.508          pass              0.509             24.6                           0.257                1.57              0.023                      ok            True                  False
  DRAM           80.56               36            0.29              0.13         61.73                54.09         0.575          pass              0.411             55.0                           0.477                0.03             -0.119                      ok           False                  False
  MPWR           92.31               39            0.27              2.74       1438.55                53.21         0.563          pass              0.818             80.1                           0.565               12.54              0.721                      ok           False                  False
  AMGN           85.29               34            0.42              1.18        402.54                47.11         0.551          pass              0.572             72.0                           0.556                2.09              0.125                      ok           False                  False
  INTC           84.38               32            1.94              1.62        118.64                74.20         0.548          pass              0.497             59.6                           0.808               -3.91             -0.534 downtrend_blocked_slope           False                  False
  AMAT           84.62               39            0.45              1.71        539.31                49.71         0.545          pass              0.555             61.4                           0.454               15.80              1.638                      ok           False                  False
  CSCO           87.10               31            0.38              0.30        112.07                31.23         0.535          pass              0.541             52.7                           0.434                0.67              0.308                      ok           False                  False
  LRCX           79.49               39            0.75              1.83        346.70                57.64         0.528          pass              0.385             46.3                           0.407               14.21              1.435                      ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005095004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005095004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005095004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005095004)

</details>
