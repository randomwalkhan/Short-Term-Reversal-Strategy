# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 15:40:04 EST`
Last processed slot: `manage_1530`

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
  PANW           80.00               40            0.84              2.07        352.54                70.38         0.530          pass              0.459             68.6                           0.588                7.39              0.970                                 ok            True                  False
  ODFL           85.71               28            1.13              1.35        170.69                44.14         0.508          pass              0.543             73.4                           0.664                0.79             -0.009                                 ok            True                  False
  UPRO           76.92               13            2.59              2.17        118.81                94.72         0.648          pass              0.215             43.5                           0.440              -14.47             -2.432 downtrend_blocked_slope_and_streak           False                  False
  QCOM           86.67               45            0.20              0.23        165.28                82.33         0.611          pass              0.721             94.1                           0.620               -4.89             -1.083 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           70.59               17            1.62              3.20        280.73                61.35         0.593          pass              0.180             24.7                           0.352               -3.43             -0.777            downtrend_blocked_slope           False                  False
  GOOG           72.22               18            1.54              3.01        278.24                58.63         0.584          pass              0.182             23.5                           0.328               -3.40             -0.750            downtrend_blocked_slope           False                  False
  INTC           50.00                4            8.45              3.53         58.15               154.63         0.571          pass              0.110             17.7                           0.208               -6.04             -1.072 downtrend_blocked_slope_and_streak           False                  False
   CEG           83.33               12            3.03              5.34        249.43                65.44         0.566          pass              0.200             13.6                           0.247               -8.70             -1.436 downtrend_blocked_slope_and_streak           False                  False
  ABNB           90.00               40            0.36              0.44        173.77                57.35         0.564          pass              0.712             62.8                           0.334               -7.26             -0.828 downtrend_blocked_slope_and_streak           False                  False
   BKR           86.11               36            0.35              0.11         45.99                56.59         0.562          pass              0.642             83.2                           0.740               -3.96             -0.793 downtrend_blocked_slope_and_streak           False                  False
  SHOP           73.91               23            1.94              1.82        133.52                71.17         0.551          pass              0.205             21.0                           0.411              -10.17             -1.588 downtrend_blocked_slope_and_streak           False                  False
  ASML           57.14                7            3.83             37.07       1367.89                73.86         0.546          pass              0.135             26.7                           0.268              -11.74             -1.585 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124154004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124154004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124154004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124154004)

</details>
