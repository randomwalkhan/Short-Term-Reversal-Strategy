# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-28 09:30:03 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$36,793.00`
- Equity: `$36,793.00`
- Realized PnL: `$26,793.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-28)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   MAR          100.00               27            0.91              2.44        382.01                28.21         0.532            pass              0.706             46.4                           0.322                4.60              0.363                                 ok            True                  False
  KLAC           84.62               13            4.84              6.89        200.41                94.03         0.589            pass              0.263             20.4                           0.458              -12.93             -1.034 downtrend_blocked_slope_and_streak           False                  False
  UPRO           87.18               39            0.04              0.04        136.34                35.93         0.537            pass              0.728             96.4                           0.561               -4.51             -0.530            downtrend_blocked_slope           False                  False
  MCHP           88.89               36            0.81              0.44         77.71                53.73         0.523            pass              0.697             78.3                           0.779               -8.26             -0.765 downtrend_blocked_slope_and_streak           False                  False
  CSCO           89.74               39            0.29              0.23        114.47                39.56         0.522            pass              0.719             71.3                           0.555               -4.20             -0.200                                 ok           False                  False
   AEP           76.92               13            1.44              1.36        134.95                20.37         0.516            pass              0.113             13.7                           0.268               -1.50             -0.030                                 ok           False                  False
  AMAT           88.24               17            3.41             12.78        530.77                84.50         0.505            pass              0.488             57.1                           0.547               -9.98             -0.882 downtrend_blocked_slope_and_streak           False                  False
  ASML           88.89                9            4.52             52.32       1632.84                55.90         0.505            pass              0.330             14.2                           0.448               -8.43             -0.478            downtrend_blocked_slope           False                  False
  MSTR           68.75               32            2.48              1.72         97.91                77.85         0.504            pass              0.342             48.4                           0.485                4.45              0.203                                 ok           False                  False
   TXN           87.10               31            1.14              2.24        278.45                50.69         0.493 below_threshold              0.577             66.0                           0.733               -7.49             -0.744            downtrend_blocked_slope           False                  False
  PCAR           85.71               21            1.37              1.28        132.89                29.37         0.493 below_threshold              0.376             33.6                           0.414                5.91              0.760                                 ok           False                  False
  AVGO           83.33               24            2.06              5.52        380.85                43.69         0.488 below_threshold              0.348             39.1                           0.387               -2.27             -0.000                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                detail
2026-07-27T15:10:06.692175-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T15:05:03.663832-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T15:00:02.669579-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T14:55:05.984850-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-27T14:50:01.830454-04:00       entry_1500           entry_skipped                                                                                                                                                                                                {"reason": "no_trade_after_option_and_timing_filters"}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.242, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 375.0, "option_spread_pct": 15.38, "option_volume": 9.0, "reason": "no_trade_low_option_liquidity", "ticker": "AEP", "timing_score": 0.504}
2026-07-27T14:50:01.830454-04:00       entry_1500 entry_candidate_skipped {"early_entry_score": 0.544, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 216.0, "option_spread_pct": 14.49, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "XEL", "timing_score": 0.558}
2026-07-27T14:50:01.830454-04:00       entry_1500          timing_overlay                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-27", "training_samples": 5518, "window": 5}
2026-07-27T12:00:02.583905-04:00 early_entry_1200      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-27T11:55:01.558921-04:00 early_entry_1155      early_entry_shadow                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260728093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260728093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260728093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260728093003)

</details>
