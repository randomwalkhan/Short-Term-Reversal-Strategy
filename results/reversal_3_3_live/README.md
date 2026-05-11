# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 13:24:21 EDT`
Last processed slot: `manage_1330`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG260618C00290000      7          2026-05-11         2026-05-11         23.2        26.8 2520.0   15.517241 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  GOOG           80.00               10            1.93              5.36        394.75                37.66         0.597          pass              0.060              0.0                             NaN               11.73              1.406                                 ok            True                  False
  TMUS           84.62               26            1.12              1.52        192.98                36.59         0.538          pass              0.344             20.2                           0.270                4.77              0.259                                 ok            True                  False
    ZS           82.61               23            2.13              2.27        151.16                58.64         0.537          pass              0.292             27.4                           0.230               11.02              1.344                                 ok            True                  False
   ADP           91.67               24            0.99              1.47        212.36                34.95         0.529          pass              0.608             50.1                           0.350                6.93              0.480                                 ok            True                  False
  ASML           89.47               19            2.51             27.94       1580.05                48.89         0.510          pass              0.493             43.1                           0.626                8.35              1.241                                 ok            True                  False
  INTU           89.29               28            1.33              3.69        394.73                49.37         0.508          pass              0.578             53.4                           0.424                0.29              0.054                                 ok            True                  False
  CHTR           70.00               10            3.23              3.50        153.36               119.48         0.760          pass              0.172             32.1                           0.544              -14.17             -1.245            downtrend_blocked_slope           False                  False
 CMCSA           90.00               10            1.46              0.26         25.28                62.19         0.708          pass              0.413             25.3                           0.448               -9.03             -0.857 downtrend_blocked_slope_and_streak           False                  False
  GEHC           65.52               29            1.12              0.50         63.26                57.03         0.568          pass              0.313             43.2                           0.445              -10.95             -0.694                                 ok           False                  False
  ORLY           80.00                5            2.39              1.55         92.29                35.12         0.557          pass              0.092             12.3                           0.340               -1.34             -0.024                                 ok           False                  False
  META           79.17               24            1.41              6.03        607.04                41.33         0.551          pass              0.185             12.3                           0.138              -11.44             -1.127 downtrend_blocked_slope_and_streak           False                  False
  TEAM           80.00                5            6.67              4.28         89.77               114.36         0.544          pass              0.073              6.1                           0.278               23.50              3.194                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                          detail
2026-05-11T12:00:16.292660-04:00 early_entry_1200 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:53:58.426024-04:00 early_entry_1150 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:47:42.065930-04:00 early_entry_1145 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:41:24.132378-04:00 early_entry_1140 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:35:07.512033-04:00 early_entry_1135 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:28:46.452605-04:00 early_entry_1125 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:22:14.545933-04:00 early_entry_1120 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:15:52.009097-04:00 early_entry_1115 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:09:25.222860-04:00 early_entry_1105 entry_skipped {"reason": "daily_entry_limit"}
2026-05-11T11:02:58.554215-04:00 early_entry_1100 entry_skipped {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511132421)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511132421)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511132421)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511132421)

</details>
