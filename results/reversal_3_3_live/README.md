# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-23 14:41:25 EST`
Last processed slot: `manage_1430`

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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL270115C00345000     32          2026-11-20         2026-11-23        14.75        17.2 7840.0   16.610169 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           97.14               35            0.00              0.00         66.28                24.95         0.508              pass              0.917            100.0                           0.702               -0.24             -0.077                                 ok           False                  False
  VRSK           80.77               26            1.28              1.81        201.31                40.90         0.498   below_threshold              0.385             69.2                           0.703               -0.55             -0.180                                 ok           False                  False
  TMUS           86.49               37            0.43              0.50        165.38                34.83         0.484   below_threshold              0.621             73.0                           0.662               -2.27             -0.424            downtrend_blocked_slope           False                  False
  MNST           50.00                6            2.25              0.69         43.39                30.90         0.479   below_threshold              0.145             32.3                           0.383               -6.43             -0.593            downtrend_blocked_slope           False                  False
   KHC           88.89               36            0.53              0.09         25.35                28.13         0.463   below_threshold              0.677             73.5                           0.674                3.42              0.463                                 ok           False                   True
   ADP           92.31               39            0.07              0.15        301.65                24.32         0.458   below_threshold              0.854             95.5                           0.822               -0.19             -0.118                                 ok           False                  False
   PEP           88.10               42            0.06              0.06        140.51                27.59         0.456   below_threshold              0.751             96.4                           0.780               -1.00             -0.246                                 ok           False                  False
   ROP           89.74               39            0.30              0.96        459.42                29.79         0.454   below_threshold              0.731             77.6                           0.657               -2.79             -0.371 downtrend_blocked_slope_and_streak           False                  False
  TTWO           90.91               44            0.10              0.15        209.93                60.05         0.438   below_threshold              0.826             97.0                           0.606                1.15             -0.660                                 ok           False                  False
  CRWD          100.00                1           10.52             16.90        222.20                61.68         0.154   below_threshold              0.465             16.5                           0.406              -10.18             -0.236                                 ok           False                  False
  AAPL             NaN                0            0.00              0.00        349.77                27.98           NaN no_signal_history                NaN              NaN                           0.451               -0.19             -0.140                                 ok           False                  False
  ABNB             NaN                0            0.00              0.00        174.34                56.89           NaN no_signal_history                NaN              NaN                           0.398               -8.38             -0.902 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                 detail
2026-11-23T13:21:08.156830-05:00      manage_1330               exit {"asset_type": "option", "contract_symbol": "AAPL270115C00345000", "fill_price": 17.2, "pnl": 7840.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.61, "ticker": "AAPL"}
2026-11-23T11:30:26.190239-05:00 early_entry_1130 early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-23T03:00:06.095274-05:00     data_refresh       data_refresh                                                                                                                                                              {'saved': 91, 'empty': 2}
2026-11-21T02:55:05.433853-05:00   share_ext_0255      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:50:06.291709-05:00   share_ext_0250      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:45:05.697713-05:00   share_ext_0245      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:40:04.140323-05:00   share_ext_0240      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:35:05.478218-05:00   share_ext_0235      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:30:05.376683-05:00   share_ext_0230      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-11-21T02:25:04.330669-05:00   share_ext_0225      market_closed                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261123144125)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261123144125)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261123144125)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261123144125)

</details>
