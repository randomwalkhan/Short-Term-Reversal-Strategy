# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 11:45:05 EDT`
Last processed slot: `early_entry_1145`

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

## Today's Closed Trades (2026-09-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           87.18               39            0.89              1.56        248.68                96.94         0.666            pass              0.607             51.9                           0.450               17.66              2.091                                 ok            True                  False
   KHC           94.12               17            0.66              0.11         24.32                22.03         0.538            pass              0.531             17.9                           0.203               -2.77             -0.132                                 ok            True                  False
  MSFT          100.00               17            1.27              4.47        499.69                22.55         0.520            pass              0.539             13.6                           0.260                0.26              0.072                                 ok            True                  False
  WDAY           91.30               23            2.04              2.74        190.75                50.40         0.500            pass              0.459              6.9                           0.231                0.93              0.379                                 ok            True                  False
  PANW           78.38               37            1.22              3.18        370.40                79.39         0.570            pass              0.370             44.4                           0.374                8.97              1.196                                 ok           False                  False
   TRI           93.10               29            1.33              0.89         95.05                58.54         0.558            pass              0.532              0.0                           0.183               -4.71             -0.316 downtrend_blocked_slope_and_streak           False                  False
   WBD           93.33               45            0.02              0.00         30.80                38.22         0.524            pass              0.858             83.3                           0.471                9.51              0.744                                 ok           False                  False
  UPRO           83.33               36            0.30              0.32        153.93                31.53         0.502            pass              0.490             59.3                           0.343                2.89              0.307                                 ok           False                  False
  FTNT           87.88               33            1.54              1.89        174.42                58.27         0.497 below_threshold              0.551             45.9                           0.593                9.56              1.183                                 ok           False                  False
  ADBE           88.89                9            3.69              6.45        246.76                45.94         0.456 below_threshold              0.382             33.3                           0.199               -6.59             -0.436            downtrend_blocked_slope           False                  False
  MELI           87.50               32            0.75              9.51       1816.39                29.69         0.453 below_threshold              0.557             55.1                           0.499               -6.20             -0.676            downtrend_blocked_slope           False                  False
  VRSK           91.67               36            0.57              0.69        171.73                39.65         0.450 below_threshold              0.802             90.7                           0.480               -2.28             -0.235           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-22T11:45:05.185045-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:40:04.072289-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:35:05.251125-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:30:06.235648-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:25:05.068681-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                             {"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.684, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "matched_signals": 31, "recovery_stability_score": 0.684, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:20:05.152954-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                               {"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.652, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "matched_signals": 31, "recovery_stability_score": 0.652, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:14:41.644035-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T10:55:06.218660-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T10:50:09.139180-04:00 early_entry_1050 early_entry_shadow     {"contract_symbol": "ZS261030C00205000", "current_drop_pct": 0.5, "early_entry_score": 0.924, "early_reclaim_pct": 98.0, "entry_ask": 16.1, "entry_bid": 14.3, "entry_mode": "early", "entry_option_price": 15.2, "hypothetical_budget": 35735.4, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 259.0, "option_spread_pct": 11.84, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.76, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.924, "early_reclaim_pct": 98.0, "matched_signals": 38, "recovery_stability_score": 0.76, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T10:45:01.139506-04:00 early_entry_1045 early_entry_shadow {"contract_symbol": "ZS261030C00205000", "current_drop_pct": 0.66, "early_entry_score": 0.921, "early_reclaim_pct": 97.4, "entry_ask": 16.1, "entry_bid": 14.3, "entry_mode": "early", "entry_option_price": 15.2, "hypothetical_budget": 35735.4, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 259.0, "option_spread_pct": 11.84, "option_volume": 12.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.791, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.921, "early_reclaim_pct": 97.4, "matched_signals": 38, "recovery_stability_score": 0.791, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922114505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922114505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922114505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922114505)

</details>
