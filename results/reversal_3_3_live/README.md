# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-05 11:05:06 EST`
Last processed slot: `manage_1100`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   MAR           84.62               13            1.26              3.76        423.26                23.45         0.534            pass              0.216              6.6                           0.135                5.72              0.832                                 ok            True                  False
  GEHC           82.61               23            1.28              0.77         85.48                36.41         0.506            pass              0.312             34.9                           0.404               18.67              1.968                                 ok            True                  False
  FTNT           60.00                5            4.58              4.14        127.61                91.87         0.608            pass              0.072              3.7                           0.123              -28.62             -4.630 downtrend_blocked_slope_and_streak           False                  False
  ISRG           87.50                8            2.17              7.32        478.96                40.52         0.568            pass              0.297             13.5                           0.166                6.26              0.379                                 ok           False                  False
  DXCM           75.00                4            2.80              1.74         87.74                45.01         0.550            pass              0.057              0.8                           0.068                9.81              1.215                                 ok           False                  False
 GOOGL           50.00                2            3.23              6.53        286.13                52.55         0.538            pass              0.118             21.3                           0.201              -13.76             -1.772            downtrend_blocked_slope           False                  False
  GOOG           33.33                3            3.00              6.03        284.71                51.02         0.525            pass              0.119             22.3                           0.210              -13.12             -1.701            downtrend_blocked_slope           False                  False
  INTC          100.00                1            8.66              3.53         56.76               128.90         0.519            pass              0.496             14.9                           0.265              -37.75             -5.857            downtrend_blocked_slope           False                  False
  INTU           87.50               40            0.06              0.15        356.57                43.29         0.507            pass              0.732             93.7                           0.599                0.43              0.357                                 ok           False                  False
  ROST          100.00                2            3.26              5.60        243.34                31.27         0.497 below_threshold              0.465              5.2                           0.169                0.45              0.248                                 ok           False                  False
  AAPL           96.43               28            0.55              1.35        348.93                25.40         0.492 below_threshold              0.725             52.0                           0.343               -0.18             -0.131                                 ok           False                  False
  INSM           61.90               21            2.55              1.96        109.16                61.82         0.488 below_threshold              0.158             12.1                           0.106               12.77              1.840                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                detail
2026-11-05T11:05:06.800397-05:00 early_entry_1105 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T11:00:05.994941-05:00 early_entry_1100 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:55:06.152127-05:00 early_entry_1055 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:50:05.415668-05:00 early_entry_1050 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:45:06.084583-05:00 early_entry_1045 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:40:06.595810-05:00 early_entry_1040 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:35:05.725069-05:00 early_entry_1035 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:30:04.290480-05:00 early_entry_1030 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:25:05.601697-05:00 early_entry_1025 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-05T10:20:04.519114-05:00 early_entry_1020 early_entry_shadow {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261105110506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261105110506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261105110506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261105110506)

</details>
