# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 15:45:04 EST`
Last processed slot: `manual`

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

## Today's Closed Trades (2026-11-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PANW           80.00               40            0.70              1.73        352.69                70.38         0.539          pass              0.475             73.8                           0.625                7.54              0.976                                 ok            True                  False
  ODFL           85.71               28            1.10              1.32        170.70                44.14         0.509          pass              0.545             74.0                           0.675                0.81             -0.007                                 ok            True                  False
  UPRO           80.00               15            2.33              1.95        118.90                94.72         0.655          pass              0.247             49.3                           0.482              -14.24             -2.420 downtrend_blocked_slope_and_streak           False                  False
  QCOM           86.36               44            0.27              0.31        165.25                82.33         0.613          pass              0.708             92.3                           0.589               -4.95             -1.085 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           73.68               19            1.44              2.84        280.88                61.35         0.596          pass              0.219             33.1                           0.513               -3.25             -0.769            downtrend_blocked_slope           False                  False
  INTC           50.00                6            8.12              3.39         58.21               154.63         0.579          pass              0.120             20.9                           0.254               -5.70             -1.056 downtrend_blocked_slope_and_streak           False                  False
  GOOG           71.43               21            1.38              2.70        278.37                58.63         0.574          pass              0.225             31.3                           0.387               -3.25             -0.743            downtrend_blocked_slope           False                  False
   CEG           85.71               14            2.96              5.21        249.49                65.44         0.561          pass              0.282             15.7                           0.274               -8.63             -1.433 downtrend_blocked_slope_and_streak           False                  False
   BKR           86.84               38            0.20              0.06         46.01                56.59         0.560          pass              0.697             90.5                           0.753               -3.81             -0.786 downtrend_blocked_slope_and_streak           False                  False
  ABNB           89.74               39            0.52              0.64        173.69                57.35         0.560          pass              0.648             46.3                           0.243               -7.41             -0.835 downtrend_blocked_slope_and_streak           False                  False
  SHOP           75.00               24            1.80              1.69        133.57                71.17         0.554          pass              0.228             26.4                           0.459              -10.05             -1.582 downtrend_blocked_slope_and_streak           False                  False
  ASML           62.50                8            3.72             36.07       1368.32                73.86         0.553          pass              0.141             28.7                           0.300              -11.65             -1.580 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                    detail
2026-11-24T15:10:06.406477-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:05:05.745009-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T15:00:04.642854-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:55:06.326922-05:00       entry_1500            slot_skipped                                                                                                                                                                                                           {"reason": "already_processed"}
2026-11-24T14:50:04.541007-05:00       entry_1500           entry_skipped                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-11-24T14:50:04.541007-05:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.494, "option_liquidity_status": "low_volume", "option_open_interest": 122.0, "option_spread_pct": 8.89, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "ODFL", "timing_score": 0.512}
2026-11-24T14:50:04.541007-05:00       entry_1500          timing_overlay                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-24", "training_samples": 6215, "window": 5}
2026-11-24T12:00:06.462519-05:00 early_entry_1200      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:55:05.635523-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:50:06.028676-05:00 early_entry_1150      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124154504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124154504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124154504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124154504)

</details>
