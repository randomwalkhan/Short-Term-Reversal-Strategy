# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-23 10:15:04 EDT`
Last processed slot: `early_entry_1015`

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
  MSTR           93.75               32            1.37              1.61        166.64               109.59         0.735          pass              0.695             35.9                           0.273               24.37              2.873                                 ok            True                  False
  PYPL           90.00               20            1.36              0.50         52.67                57.12         0.631          pass              0.496             33.3                           0.272                0.00             -0.178                                 ok            True                  False
  NVDA           92.00               25            1.14              1.82        228.09                44.57         0.592          pass              0.503              7.8                           0.195                1.28              0.464                                 ok            True                  False
  ADSK           81.82               33            0.98              1.51        218.97                55.47         0.552          pass              0.366             36.5                           0.290                5.25              0.312                                 ok            True                  False
  DRAM           82.14               28            2.22              0.99         63.20                51.34         0.517          pass              0.248              6.3                           0.229                1.02              0.617                                 ok            True                  False
  UPRO           82.61               23            1.42              1.53        153.08                31.44         0.505          pass              0.246             13.1                           0.193                2.96              0.485                                 ok            True                  False
   STX           84.62               39            0.53              3.39        918.39                53.68         0.502          pass              0.625             86.1                           0.915                3.28              0.614                                 ok            True                  False
  MRVL           76.47               34            1.41              2.59        261.25                69.87         0.572          pass              0.244              8.9                           0.134               10.06              1.486                                 ok           False                  False
   XEL          100.00                6            1.19              0.60         71.80                15.29         0.560          pass              0.517             20.4                           0.307               -5.80             -0.560 downtrend_blocked_slope_and_streak           False                  False
   WBD           92.50               40            0.11              0.02         30.82                38.24         0.544          pass              0.841             84.4                           0.529               10.34              1.012                                 ok           False                  False
   CEG           76.19               21            1.25              2.31        262.47                42.63         0.524          pass              0.241             38.3                           0.454              -11.48             -1.171 downtrend_blocked_slope_and_streak           False                  False
   PEP           88.24               17            0.51              0.47        130.99                15.28         0.523          pass              0.485             55.6                           0.540               -4.52             -0.604 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-23T10:15:04.258896-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:10:06.450659-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "entry_ask": 5.2, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 4.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 83, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 41.86, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.742, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.842, "early_reclaim_pct": 83.8, "matched_signals": 33, "recovery_stability_score": 0.742, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.378, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T10:05:05.428675-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-23T10:00:05.505875-04:00 early_entry_1000 early_entry_shadow  {"contract_symbol": "CTAS261023C00200000", "current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "entry_ask": 5.3, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 35735.4, "hypothetical_contracts": 78, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 32.97, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.713, "shadow_only": true, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.845, "early_reclaim_pct": 84.6, "matched_signals": 33, "recovery_stability_score": 0.713, "success_rate": 96.97, "ticker": "CTAS", "timing_score": 0.38, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-23T09:35:04.357346-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:30:01.473090-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:25:05.427577-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-23T09:20:04.649319-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-22T15:10:06.051324-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-22T15:05:04.283152-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260923101504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260923101504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260923101504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260923101504)

</details>
