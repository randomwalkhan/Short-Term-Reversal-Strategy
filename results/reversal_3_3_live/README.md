# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 11:25:06 EST`
Last processed slot: `manage_1130`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
 CMCSA           90.48               21            0.56              0.10         24.81                35.54         0.581          pass              0.477             22.2                           0.259                8.19              1.110                                 ok            True                  False
   MAR           84.62               13            1.24              3.70        423.29                23.45         0.534          pass              0.247             17.0                           0.247                5.74              0.833                                 ok            True                  False
  REGN           80.65               31            0.99              6.45        927.91                52.52         0.528          pass              0.214              1.2                           0.058               12.50              1.989                                 ok            True                  False
   KHC           88.00               25            1.06              0.19         25.36                36.26         0.520          pass              0.400             11.5                           0.185                0.32              0.167                                 ok            True                  False
  GILD           92.31               26            1.00              1.22        173.96                33.00         0.509          pass              0.486              0.0                           0.197                9.89              1.169                                 ok            True                  False
  FTNT           60.00               10            3.24              2.93        128.13                91.87         0.658          pass              0.161             31.9                           0.640              -27.62             -4.566 downtrend_blocked_slope_and_streak           False                  False
  INTC           54.55               11            4.97              2.03         57.40               128.90         0.645          pass              0.225             51.2                           0.794              -35.23             -5.677            downtrend_blocked_slope           False                  False
 GOOGL           78.95               19            1.30              2.63        287.80                52.55         0.582          pass              0.323             68.3                           0.732              -12.04             -1.682            downtrend_blocked_slope           False                  False
  GOOG           84.62               26            1.08              2.17        286.37                51.02         0.551          pass              0.501             72.1                           0.850              -11.40             -1.612            downtrend_blocked_slope           False                  False
  MSFT          100.00                8            2.04              7.93        552.40                33.48         0.548          pass              0.608             51.0                           0.755                4.49              0.250                                 ok           False                  False
  ISRG           75.00                4            2.77              9.36        478.09                40.52         0.543          pass              0.058              1.1                           0.053                5.61              0.351                                 ok           False                  False
  GEHC           71.43               14            1.68              1.01         85.38                36.41         0.528          pass              0.124             14.8                           0.241               18.20              1.949                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-05T11:25:06.091579-05:00 early_entry_1125 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:20:06.476287-05:00 early_entry_1120 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:15:05.542359-05:00 early_entry_1115 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:10:04.336352-05:00 early_entry_1110 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:05:06.800397-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:00:05.994941-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:55:06.152127-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:50:05.415668-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:45:06.084583-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:40:06.595810-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105112506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105112506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105112506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105112506)

</details>
