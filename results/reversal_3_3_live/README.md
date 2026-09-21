# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 10:10:06 EDT`
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

## Today's Closed Trades (2026-09-21)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  VRSK           89.47               19            1.72              2.11        174.50                39.25         0.511            pass              0.415             17.3                           0.220               -6.96             -0.249                                 ok            True                  False
   PEP          100.00                9            1.08              0.98        129.33                15.76         0.554            pass              0.519             21.2                           0.331               -6.74             -0.651 downtrend_blocked_slope_and_streak           False                  False
   KHC           94.74               19            0.29              0.05         24.41                22.04         0.552            pass              0.685             58.8                           0.371               -1.97             -0.117                                 ok           False                  False
  ADBE           97.37               38            0.27              0.47        248.72                46.23         0.540            pass              0.898             85.8                           0.795               -6.85             -0.434            downtrend_blocked_slope           False                  False
  ADSK           87.80               41            0.19              0.29        216.83                55.58         0.531            pass              0.730             89.6                           0.728               -0.62              0.338                                 ok           False                  False
   ADP           95.00               20            0.72              1.36        270.64                22.01         0.526            pass              0.674             51.5                           0.343               -2.38              0.125           downtrend_blocked_streak           False                  False
  CHTR           88.24               34            1.55              1.39        127.57                64.18         0.525            pass              0.551             39.5                           0.477              -16.98             -1.426 downtrend_blocked_slope_and_streak           False                  False
  ASML           82.05               39            0.10              1.13       1679.43                40.24         0.514            pass              0.428             42.8                           0.203               -2.13             -0.593                                 ok           False                  False
   XEL          100.00               23            0.25              0.13         72.25                19.27         0.513            pass              0.703             55.0                           0.525               -3.99             -0.532            downtrend_blocked_slope           False                  False
  INTU          100.00               31            1.00              2.11        302.28                42.64         0.503            pass              0.778             62.6                           0.730               -9.78             -0.606 downtrend_blocked_slope_and_streak           False                  False
   EXC           96.15               26            0.15              0.05         42.05                15.92         0.497 below_threshold              0.821             88.2                           0.658               -3.75             -0.460 downtrend_blocked_slope_and_streak           False                  False
   CEG           82.35               34            0.47              0.83        254.35                41.10         0.489 below_threshold              0.486             71.5                           0.572              -15.20             -1.897 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-09-21T10:10:06.043789-04:00 early_entry_1010      early_entry_shadow {"contract_symbol": "CTAS261030C00195000", "current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "entry_ask": 10.1, "entry_bid": 7.4, "entry_mode": "early", "entry_option_price": 8.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 40, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 30.86, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.783, "early_reclaim_pct": 64.2, "matched_signals": 32, "recovery_stability_score": 0.632, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.436, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-21T10:05:06.363886-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:00:04.768791-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T09:20:04.809937-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-18T15:10:04.788288-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T15:05:05.954030-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T15:00:03.968650-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T14:55:06.162001-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-09-18T14:50:01.910301-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"early_entry_score": 0.541, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 24.0, "option_spread_pct": 14.53, "option_volume": 21.0, "reason": "no_trade_low_option_liquidity", "ticker": "KHC", "timing_score": 0.534}
2026-09-18T14:50:01.910301-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-18", "training_samples": 5785, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921101006)

</details>
