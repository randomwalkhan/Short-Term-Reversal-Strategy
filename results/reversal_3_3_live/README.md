# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-22 12:20:05 EDT`
Last processed slot: `manage_1230`

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
  CRWD           86.84               38            1.28              2.24        248.39                96.94         0.650            pass              0.528             31.1                           0.270               17.21              2.073                                 ok            True                  False
   KHC           93.75               16            0.68              0.12         24.32                22.03         0.542            pass              0.507             15.4                           0.299               -2.79             -0.133                                 ok            True                  False
  FTNT           84.62               26            1.88              2.30        174.24                58.27         0.515            pass              0.383             34.1                           0.298                9.19              1.168                                 ok            True                  False
  WDAY           93.55               31            1.11              1.49        191.28                50.40         0.512            pass              0.700             49.3                           0.638                1.88              0.422                                 ok            True                  False
  MSFT          100.00               19            1.24              4.34        499.75                22.55         0.509            pass              0.577             22.1                           0.417                0.30              0.074                                 ok            True                  False
  MSTR           94.74               38            0.34              0.40        168.33               109.37         0.753            pass              0.931             92.1                           0.468               23.01              2.244                                 ok           False                  False
  INTC           83.33               42            0.07              0.06        121.75                69.88         0.582            pass              0.637             96.7                           0.634               16.49              1.542                                 ok           False                  False
  PANW           78.38               37            1.32              3.43        370.29                79.39         0.564            pass              0.357             40.2                           0.362                8.87              1.192                                 ok           False                  False
   TRI           93.33               30            1.12              0.75         95.11                58.54         0.561            pass              0.657             37.4                           0.354               -4.50             -0.306 downtrend_blocked_slope_and_streak           False                  False
   WBD           93.33               45            0.00              0.00         30.80                38.22         0.525            pass              0.908            100.0                           0.602                9.53              0.745                                 ok           False                  False
  UPRO           83.78               37            0.19              0.20        153.98                31.53         0.503            pass              0.554             74.3                           0.524                3.00              0.312                                 ok           False                  False
  ADBE           88.89                9            3.58              6.26        246.84                45.94         0.463 below_threshold              0.389             35.2                           0.285               -6.49             -0.431            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-22T12:00:04.192622-04:00 early_entry_1200 early_entry_shadow      {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.559, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:55:04.534124-04:00 early_entry_1155 early_entry_shadow      {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "entry_ask": 15.15, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 35735.4, "hypothetical_contracts": 24, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.89, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.92, "early_reclaim_pct": 97.3, "matched_signals": 38, "recovery_stability_score": 0.586, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:50:04.129679-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "ZS261023C00205000", "current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "entry_ask": 15.05, "entry_bid": 13.45, "entry_mode": "early", "entry_option_price": 14.25, "hypothetical_budget": 35735.4, "hypothetical_contracts": 25, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 244.0, "option_spread_pct": 11.23, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.747, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.923, "early_reclaim_pct": 97.9, "matched_signals": 38, "recovery_stability_score": 0.747, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:45:05.185045-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:40:04.072289-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:35:05.251125-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:30:06.235648-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-22T11:25:05.068681-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                               {"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.684, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.86, "early_reclaim_pct": 96.1, "matched_signals": 31, "recovery_stability_score": 0.684, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.322, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:20:05.152954-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                 {"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "entry_mode": "early", "error": "CTSH: no call expiries found in the 21-40 trading-day window.", "matched_signals": 31, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.652, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "top_candidates": [{"current_drop_pct": 0.9, "early_entry_score": 0.86, "early_reclaim_pct": 96.0, "matched_signals": 31, "recovery_stability_score": 0.652, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.321, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-22T11:14:41.644035-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260922122005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260922122005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260922122005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260922122005)

</details>
