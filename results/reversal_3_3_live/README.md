# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 09:35:04 EDT`
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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           81.82               33            2.34              2.48        150.90               119.42         0.706          pass              0.419             48.8                           0.631               17.98              2.556                                 ok            True                  False
  DRAM           80.65               31            1.10              0.49         63.46                51.34         0.571          pass              0.336             40.7                           0.487                2.26              0.672                                 ok            True                  False
  MPWR           87.10               31            1.13             10.88       1375.96                51.84         0.555          pass              0.491             35.4                           0.326               13.40              1.326                                 ok            True                  False
  INTC           83.33               36            1.61              1.39        123.26                67.82         0.534          pass              0.337              7.0                           0.286               14.71              2.108                                 ok            True                  False
  NXPI           87.10               31            0.68              1.13        237.08                36.32         0.515          pass              0.523             47.4                           0.428                6.13              0.455                                 ok            True                  False
  QCOM           91.18               34            0.60              0.83        197.91                46.97         0.502          pass              0.676             55.9                           0.485               11.72              1.057                                 ok            True                  False
  PYPL           88.89               36            0.44              0.16         52.82                57.12         0.604          pass              0.557             28.8                           0.303                0.93             -0.136                                 ok           False                  False
  NVDA           92.11               38            0.07              0.10        228.83                44.57         0.585          pass              0.840             90.6                           0.794                2.37              0.513                                 ok           False                  False
  ADSK           84.21               38            0.45              0.70        219.32                55.47         0.567          pass              0.467             37.0                           0.309                5.81              0.336                                 ok           False                  False
  CHTR           86.05               43            0.24              0.20        117.18                65.60         0.555          pass              0.644             75.9                           0.500              -12.63             -1.968 downtrend_blocked_slope_and_streak           False                  False
  AMAT           80.49               41            0.03              0.11        472.41                51.05         0.542          pass              0.563             98.6                           0.926                0.74              0.293                                 ok           False                  False
   WBD           92.86               42            0.05              0.01         30.83                38.24         0.536          pass              0.875             92.9                           0.653               10.40              1.015                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                 detail
2026-09-23T09:35:04.357346-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                              {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-09-22T14:50:01.294026-04:00   entry_1500 entry_candidate_skipped {"early_entry_score": 0.621, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 21.01, "option_volume": 6.0, "reason": "no_trade_low_option_liquidity", "ticker": "TEAM", "timing_score": 0.504}
2026-09-22T14:50:01.294026-04:00   entry_1500          timing_overlay                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-22", "training_samples": 5799, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923093504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923093504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923093504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923093504)

</details>
