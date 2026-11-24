# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-24 14:50:04 EST`
Last processed slot: `entry_1500`

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
  ODFL           84.62               26            1.23              1.48        170.64                44.14         0.512          pass              0.494             70.9                           0.538                0.68             -0.013                                 ok            True                  False
  UPRO           78.95               19            2.10              1.76        118.98                94.72         0.644          pass              0.287             54.2                           0.493              -14.04             -2.409 downtrend_blocked_slope_and_streak           False                  False
  INTC           50.00                8            6.94              2.90         58.42               154.63         0.640          pass              0.161             32.4                           0.491               -4.49             -0.998 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           70.59               17            1.56              3.08        280.78                61.35         0.596          pass              0.189             27.4                           0.265               -3.37             -0.775            downtrend_blocked_slope           False                  False
  ASML           70.00               10            3.21             31.09       1370.46                73.86         0.582          pass              0.174             38.5                           0.472              -11.17             -1.556 downtrend_blocked_slope_and_streak           False                  False
  GOOG           75.00               20            1.47              2.87        278.30                58.63         0.580          pass              0.206             27.0                           0.255               -3.33             -0.747            downtrend_blocked_slope           False                  False
   BKR           84.38               32            0.59              0.19         45.96                56.59         0.569          pass              0.534             71.4                           0.606               -4.19             -0.805 downtrend_blocked_slope_and_streak           False                  False
   CEG           83.33               12            3.13              5.52        249.36                65.44         0.560          pass              0.190             10.8                           0.157               -8.79             -1.441 downtrend_blocked_slope_and_streak           False                  False
   AEP          100.00               24            0.18              0.16        127.12                17.59         0.547          pass              0.788             79.8                           0.423               -0.69             -0.250                                 ok           False                  False
  AVGO           58.33               12            3.36              7.36        310.39                86.52         0.536          pass              0.167             33.2                           0.397               -8.72             -1.202            downtrend_blocked_slope           False                  False
  SHOP           72.73               22            2.26              2.13        133.39                71.17         0.535          pass              0.152              6.2                           0.167              -10.47             -1.603 downtrend_blocked_slope_and_streak           False                  False
  SBUX           87.10               31            0.34              0.25        106.25                36.16         0.532          pass              0.601             72.9                           0.422               -3.02             -0.359            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                    detail
2026-11-24T14:50:04.541007-05:00       entry_1500           entry_skipped                                                                                                                                                                                    {"reason": "no_trade_after_option_and_timing_filters"}
2026-11-24T14:50:04.541007-05:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.494, "option_liquidity_status": "low_volume", "option_open_interest": 122.0, "option_spread_pct": 8.89, "option_volume": 4.0, "reason": "no_trade_low_option_liquidity", "ticker": "ODFL", "timing_score": 0.512}
2026-11-24T14:50:04.541007-05:00       entry_1500          timing_overlay                                                                                                                              {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-11-24", "training_samples": 6215, "window": 5}
2026-11-24T12:00:06.462519-05:00 early_entry_1200      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:55:05.635523-05:00 early_entry_1155      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:50:06.028676-05:00 early_entry_1150      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:45:06.576648-05:00 early_entry_1145      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:40:05.757709-05:00 early_entry_1140      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:35:05.562629-05:00 early_entry_1135      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-24T11:30:04.516511-05:00 early_entry_1130      early_entry_shadow                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261124145004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261124145004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261124145004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261124145004)

</details>
