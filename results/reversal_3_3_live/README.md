# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 10:05:05 EDT`
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
  PYPL           90.48               21            1.30              0.48         52.68                57.12         0.630          pass              0.430              4.9                           0.191                0.06             -0.175                                 ok            True                  False
  ADSK           82.14               28            1.30              2.00        218.76                55.47         0.564          pass              0.234              0.0                           0.170                4.91              0.297                                 ok            True                  False
  DRAM           82.14               28            1.54              0.69         63.33                51.34         0.562          pass              0.308             24.9                           0.285                1.72              0.648                                 ok            True                  False
  INTC           82.35               34            1.71              1.48        123.22                67.82         0.533          pass              0.364             29.3                           0.368               14.59              2.103                                 ok            True                  False
  UPRO           83.33               24            1.26              1.36        153.16                31.44         0.513          pass              0.234              0.0                           0.150                3.13              0.492                                 ok            True                  False
  MRVL           79.49               39            0.31              0.57        262.12                69.87         0.615          pass              0.475             73.4                           0.441               11.29              1.537                                 ok           False                  False
  SOXL           79.31               29            4.28              4.55        150.00               119.42         0.604          pass              0.274             28.9                           0.268               15.63              2.465                                 ok           False                  False
  NVDA           90.91               33            0.35              0.56        228.63                44.57         0.596          pass              0.653             49.7                           0.361                2.08              0.500                                 ok           False                  False
   XEL          100.00                4            1.47              0.74         71.74                15.29         0.555          pass              0.461              1.9                           0.157               -6.06             -0.573 downtrend_blocked_slope_and_streak           False                  False
  ADBE           94.87               39            0.08              0.14        238.19                47.75         0.550          pass              0.705             20.0                           0.132               -6.60             -0.622            downtrend_blocked_slope           False                  False
   PEP          100.00               10            1.02              0.94        130.79                15.28         0.546          pass              0.490             11.8                           0.176               -5.00             -0.627 downtrend_blocked_slope_and_streak           False                  False
   WBD           92.50               40            0.13              0.03         30.82                38.24         0.543          pass              0.834             82.2                           0.530               10.32              1.011                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-23T10:05:05.428675-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:00:05.505875-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "entry_ask": 5.3, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 35735.4, "hypothetical_contracts": 78, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 32.97, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "matched_signals": 33, "recovery_stability_score": 0.713, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T09:35:04.357346-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T15:00:05.737900-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-09-22T14:55:05.306648-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923100505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923100505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923100505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923100505)

</details>
