# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 15:55:05 EST`
Last processed slot: `manage_1600`

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
  ODFL           85.71               28            1.10              1.32        170.71                44.14         0.510          pass              0.546             74.1                           0.730                0.82             -0.007                                 ok            True                  False
  UPRO           80.00               20            1.90              1.60        119.06                94.72         0.651          pass              0.307             58.5                           0.687              -13.87             -2.400 downtrend_blocked_slope_and_streak           False                  False
  NVDA           75.00                4            5.97              6.90        162.09               126.24         0.608          pass              0.158             32.2                           0.678               -8.11             -1.566 downtrend_blocked_slope_and_streak           False                  False
  INTC           50.00                6            8.14              3.40         58.20               154.63         0.578          pass              0.120             20.7                           0.438               -5.72             -1.057 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           76.00               25            1.22              2.40        281.07                61.35         0.575          pass              0.288             43.5                           0.661               -3.03             -0.759            downtrend_blocked_slope           False                  False
  GOOG           75.00               24            1.20              2.35        278.52                58.63         0.572          pass              0.271             40.3                           0.626               -3.07             -0.735            downtrend_blocked_slope           False                  False
   BKR           84.85               33            0.51              0.16         45.97                56.59         0.568          pass              0.565             75.3                           0.644               -4.11             -0.801 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71               14            2.87              5.05        249.55                65.44         0.566          pass              0.290             18.2                           0.344               -8.55             -1.428 downtrend_blocked_slope_and_streak           False                  False
  ABNB           90.00               40            0.44              0.54        173.73                57.35         0.559          pass              0.686             54.6                           0.320               -7.34             -0.832 downtrend_blocked_slope_and_streak           False                  False
  SHOP           76.92               26            1.63              1.54        133.64                71.17         0.555          pass              0.262             33.3                           0.499               -9.89             -1.574 downtrend_blocked_slope_and_streak           False                  False
  ASML           62.50                8            3.74             36.19       1368.27                73.86         0.552          pass              0.140             28.4                           0.402              -11.66             -1.581 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.22               45            0.13              0.33        353.29                70.38         0.546          pass              0.599             95.0                           0.853                8.15              1.002                                 ok           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124155505)

</details>
