# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-05 10:00:05 EDT`
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

- Cash: `$88,586.80`
- Equity: `$88,586.80`
- Realized PnL: `$78,586.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-05)

```text
ticker asset_type execution_mode        instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
    ZS     option         option ZS261120C00200000     27          2026-10-02         2026-10-05        14.85      17.525 7222.5   18.013468 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           82.14               28            3.32              3.81        162.08               114.85         0.662            pass              0.250              2.1                           0.120               11.59              0.896                                 ok            True                  False
  ASML           80.65               31            0.75              9.75       1863.13                42.39         0.547            pass              0.378             55.4                           0.453                8.30              0.839                                 ok            True                  False
  AMAT           84.62               39            0.51              1.92        539.22                49.71         0.542            pass              0.541             56.9                           0.365               15.74              1.636                                 ok            True                  False
   TRI           86.21               29            1.37              0.94         97.22                53.36         0.534            pass              0.423             26.0                           0.340                0.89              0.059                                 ok            True                  False
  LRCX           80.56               36            1.08              2.62        346.37                57.64         0.528            pass              0.311             23.2                           0.207               13.84              1.420                                 ok            True                  False
   ADI           87.50               24            1.23              3.59        415.61                32.86         0.515            pass              0.419             24.6                           0.257                7.58              0.784                                 ok            True                  False
  NXPI           84.00               25            1.53              2.62        242.54                37.68         0.500 below_threshold              0.326             23.2                           0.211                3.23              0.331                                 ok            True                  False
  DRAM           80.00               35            0.44              0.19         61.70                54.09         0.571            pass              0.321             32.5                           0.281               -0.11             -0.126                                 ok           False                  False
  AMGN           86.49               37            0.21              0.59        402.79                47.11         0.548            pass              0.666             86.0                           0.668                2.30              0.134                                 ok           False                  False
  INTC           80.00               25            2.84              2.37        118.31                74.20         0.532            pass              0.276             40.8                           0.440               -4.79             -0.576            downtrend_blocked_slope           False                  False
   PEP           90.00               10            1.18              1.04        125.45                14.60         0.525            pass              0.354             11.6                           0.187               -4.00             -0.453            downtrend_blocked_slope           False                  False
  QCOM           88.00               25            2.00              2.59        183.76                56.36         0.512            pass              0.391              8.9                           0.112               -6.72             -0.971 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                               detail
2026-10-05T10:00:05.004899-04:00 early_entry_1000 early_entry_shadow                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-05T09:55:04.847980-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "ZS261120C00200000", "fill_price": 17.525, "pnl": 7222.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.01, "ticker": "ZS"}
2026-10-05T03:00:05.114767-04:00     data_refresh       data_refresh                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-10-03T02:55:05.889514-04:00   share_ext_0255      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:50:05.063422-04:00   share_ext_0250      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:45:04.071042-04:00   share_ext_0245      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:40:05.983879-04:00   share_ext_0240      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:35:05.098506-04:00   share_ext_0235      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:30:06.414009-04:00   share_ext_0230      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-03T02:25:01.959731-04:00   share_ext_0225      market_closed                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261005100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261005100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261005100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261005100005)

</details>
