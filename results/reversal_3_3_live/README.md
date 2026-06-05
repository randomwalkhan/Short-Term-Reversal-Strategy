# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-05 10:05:02 EDT`
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

- Cash: `$33,370.75`
- Equity: `$33,370.75`
- Realized PnL: `$23,370.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-05)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SOXL     option         option SOXL260717C00270000      2          2026-06-04         2026-06-05        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  WDAY           88.57               35            1.04              1.08        147.45                69.97         0.584          pass              0.515             20.6                           0.149               14.22              1.970                                 ok            True                  False
  TEAM           93.55               31            2.19              1.55        100.83                86.36         0.570          pass              0.591             10.8                           0.123               16.23              1.873                                 ok            True                  False
  PANW           88.00               25            1.46              2.86        278.02                60.15         0.567          pass              0.501             43.6                           0.294                8.79              1.316                                 ok            True                  False
  FTNT          100.00               10            2.41              2.53        148.59                44.88         0.557          pass              0.486             10.0                           0.123                9.06              1.434                                 ok            True                  False
    ZS           80.56               36            0.74              0.70        134.96               157.69         0.884          pass              0.445             56.0                           0.330              -26.38             -2.238            downtrend_blocked_slope           False                  False
  MELI           93.33               45            0.08              0.92       1634.39                60.42         0.590          pass              0.891             92.1                           0.478               -1.86             -0.284            downtrend_blocked_slope           False                  False
  CSCO          100.00                2            3.47              3.16        128.65                55.20         0.583          pass              0.504             15.4                           0.272                4.22              0.807                                 ok           False                  False
   ADI          100.00                5            3.04              9.11        424.85                45.54         0.547          pass              0.520             21.9                           0.466                4.99              0.384                                 ok           False                  False
   TXN          100.00                2            3.70              7.90        301.98                44.40         0.524          pass              0.489             12.2                           0.252               -4.89             -0.739 downtrend_blocked_slope_and_streak           False                  False
   CEG           76.19               21            2.38              4.41        262.70                55.63         0.516          pass              0.173             16.1                           0.205               -9.63             -1.398            downtrend_blocked_slope           False                  False
  AVGO           60.00                5            3.95             11.59        413.94                65.35         0.507          pass              0.088             12.5                           0.287               -2.84             -0.029           downtrend_blocked_streak           False                  False
   BKR           62.50                8            2.26              1.05         65.66                32.54         0.506          pass              0.094             14.6                           0.189               -2.19             -0.082                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                             detail
2026-06-05T10:05:02.004075-04:00 early_entry_1005 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T10:05:02.004075-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "SOXL260717C00270000", "fill_price": 54.045, "pnl": -1201.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SOXL"}
2026-06-05T10:00:04.998731-04:00 early_entry_1000 early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-05T09:35:04.249601-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-06-05T09:30:04.938889-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-06-05T09:25:01.283083-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-06-05T09:20:04.897767-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-06-05T09:15:01.957387-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-06-05T09:10:02.051454-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
2026-06-05T09:05:06.659544-04:00     data_refresh       data_refresh                                                                                                                                                                      {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260605100502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260605100502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260605100502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260605100502)

</details>
