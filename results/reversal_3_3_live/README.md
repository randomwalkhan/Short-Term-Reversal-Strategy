# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 09:55:01 EDT`
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
  ADSK           84.21               38            0.53              0.82        219.27                55.47         0.559          pass              0.501             48.7                           0.297                5.73              0.332                                 ok            True                  False
  DRAM           82.14               28            1.71              0.76         63.34                51.34         0.551          pass              0.291             19.7                           0.281                1.63              0.644                                 ok            True                  False
  INTC           80.65               31            2.30              1.99        123.01                67.82         0.514          pass              0.224              5.1                           0.110               13.91              2.076                                 ok            True                  False
  UPRO           85.19               27            1.10              1.19        153.21                31.44         0.508          pass              0.305              0.9                           0.173                3.28              0.499                                 ok            True                  False
  MSTR           94.74               38            0.44              0.51        167.11               109.59         0.754          pass              0.874             73.1                           0.487               25.55              2.916                                 ok           False                  False
  MRVL           79.49               39            0.24              0.45        262.17                69.87         0.619          pass              0.492             79.1                           0.484               11.37              1.540                                 ok           False                  False
  PYPL           90.00               40            0.21              0.08         52.86                57.12         0.598          pass              0.726             66.7                           0.356                1.17             -0.125                                 ok           False                  False
  NVDA           90.91               33            0.47              0.76        228.54                44.57         0.588          pass              0.598             31.8                           0.346                1.95              0.494                                 ok           False                  False
  AMGN           86.11               36            0.20              0.56        410.00                46.69         0.572          pass              0.627             77.8                           0.417                4.64              0.636                                 ok           False                  False
  SOXL           77.78               27            5.00              5.32        149.68               119.42         0.570          pass              0.221             16.9                           0.271               14.76              2.430                                 ok           False                  False
   XEL          100.00                6            1.32              0.66         71.78                15.29         0.552          pass              0.472              5.5                           0.148               -5.92             -0.566 downtrend_blocked_slope_and_streak           False                  False
   PEP          100.00               10            0.97              0.89        130.81                15.28         0.551          pass              0.465              3.4                           0.102               -4.95             -0.624 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923095501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923095501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923095501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923095501)

</details>
