# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-02 10:10:02 EDT`
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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           91.67               36            0.70              5.39       1095.08                49.88         0.527            pass              0.683             48.8                           0.290                7.27              0.388                                 ok            True                  False
   WBD           95.65               46            0.02              0.00         30.95                37.65         0.551            pass              0.805             50.0                           0.365               11.31              0.523                                 ok           False                  False
  AMGN           85.29               34            0.37              1.05        406.82                47.14         0.510            pass              0.498             48.6                           0.392                5.22              0.537                                 ok           False                  False
  PAYX           79.41               34            0.51              0.36        100.69                39.54         0.508            pass              0.375             54.9                           0.546              -13.61             -1.668 downtrend_blocked_slope_and_streak           False                  False
  ADBE           90.24               41            0.39              0.65        241.00                44.30         0.500            pass              0.692             56.1                           0.382               -3.44             -0.350                                 ok           False                  False
  VRSK           85.37               41            0.25              0.29        168.25                37.65         0.493 below_threshold              0.634             80.6                           0.693               -4.25             -0.409 downtrend_blocked_slope_and_streak           False                  False
  CTSH           93.10               29            1.23              0.52         60.66                46.07         0.488 below_threshold              0.659             44.9                           0.557                0.43             -0.027                                 ok           False                  False
  ISRG           92.31               26            1.07              3.01        399.95                28.38         0.468 below_threshold              0.585             34.4                           0.297                0.92              0.165                                 ok           False                  False
   ADP           90.48               21            1.06              1.96        263.12                23.86         0.463 below_threshold              0.485             28.6                           0.269               -3.71             -0.391 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71                7            3.03              5.48        256.57                41.85         0.458 below_threshold              0.260             20.5                           0.171               -1.42             -0.209                                 ok           False                  False
  GILD           92.86               28            0.70              0.72        147.19                19.81         0.450 below_threshold              0.624             38.7                           0.335               -2.42             -0.238           downtrend_blocked_streak           False                  False
  NFLX           83.72               43            0.43              0.21         67.76                35.87         0.446 below_threshold              0.514             56.6                           0.516               -5.90             -0.719            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                       detail
2026-10-02T10:10:02.761986-04:00 early_entry_1010 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:05:05.705073-04:00 early_entry_1005 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T10:00:06.267323-04:00 early_entry_1000 early_entry_shadow                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-02T09:20:04.739617-04:00     data_refresh       data_refresh                                                                                    {'saved': 92, 'empty': 1}
2026-10-01T15:10:06.086305-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T15:05:04.536150-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T15:00:06.279684-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T14:55:05.658187-04:00       entry_1500       slot_skipped                                                                              {"reason": "already_processed"}
2026-10-01T14:50:05.514279-04:00       entry_1500     timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-01", "training_samples": 5895, "window": 5}
2026-10-01T14:50:05.514279-04:00       entry_1500      entry_skipped                                                                                   {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261002101002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261002101002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261002101002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261002101002)

</details>
