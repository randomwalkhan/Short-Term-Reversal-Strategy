# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-23 13:21:08 EST`
Last processed slot: `manage_1330`

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
  PAYX           73.91               23            0.56              0.44        112.44                33.87         0.549              pass              0.300             52.8                           0.631               -2.41             -0.356            downtrend_blocked_slope           False                  False
  VRSK           78.26               23            1.45              2.06        201.21                40.90         0.503              pass              0.332             65.1                           0.598               -0.72             -0.188                                 ok           False                  False
  TMUS           84.85               33            0.72              0.83        165.24                34.83         0.490   below_threshold              0.498             55.4                           0.764               -2.55             -0.437            downtrend_blocked_slope           False                  False
   ADP           90.62               32            0.39              0.83        301.36                24.32         0.480   below_threshold              0.703             74.9                           0.733               -0.51             -0.133                                 ok           False                  False
   KHC           88.57               35            0.57              0.10         25.35                28.13         0.466   below_threshold              0.657             71.6                           0.727                3.38              0.462                                 ok           False                  False
  MNST           50.00               12            1.97              0.60         43.43                30.90         0.458   below_threshold              0.182             40.9                           0.461               -6.16             -0.580            downtrend_blocked_slope           False                  False
   PEP           88.37               43            0.02              0.02        140.53                27.59         0.452   below_threshold              0.765             98.7                           0.860               -0.97             -0.245                                 ok           False                  False
   ROP           88.89               45            0.02              0.05        459.81                29.79         0.433   below_threshold              0.777             98.8                           0.866               -2.52             -0.358 downtrend_blocked_slope_and_streak           False                  False
  AAPL             NaN                0            0.00              0.00        349.92                27.98           NaN no_signal_history                NaN              NaN                           0.512               -0.14             -0.138                                 ok           False                  False
  ABNB             NaN                0            0.00              0.00        174.05                56.89           NaN no_signal_history                NaN              NaN                           0.353               -8.53             -0.909 downtrend_blocked_slope_and_streak           False                  False
  ADBE             NaN                0            0.00              0.00        223.35                29.82           NaN no_signal_history                NaN              NaN                           0.566               -5.88             -0.894 downtrend_blocked_slope_and_streak           False                  False
   ADI             NaN                0            0.00              0.00        378.43                71.12           NaN no_signal_history                NaN              NaN                           0.310               -4.11             -1.036            downtrend_blocked_slope           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261123132108)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261123132108)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261123132108)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261123132108)

</details>
