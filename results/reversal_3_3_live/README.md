# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 13:05:03 EDT`
Last processed slot: `manage_1300`

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
   KHC           95.24               21            0.12              0.02         24.42                22.04         0.550            pass              0.782             84.6                           0.645               -1.81             -0.109                                 ok           False                  False
  ADBE           97.37               38            0.44              0.76        248.59                46.23         0.529            pass              0.870             76.8                           0.477               -7.01             -0.442            downtrend_blocked_slope           False                  False
  CHTR           88.57               35            1.54              1.38        127.58                64.18         0.520            pass              0.568             40.1                           0.425              -16.97             -1.425 downtrend_blocked_slope_and_streak           False                  False
  WDAY           95.24               42            0.36              0.48        193.66                50.60         0.515            pass              0.858             69.0                           0.336               -1.33              0.322                                 ok           False                  False
   ADP           96.30               27            0.39              0.73        270.91                22.01         0.507            pass              0.785             73.8                           0.510               -2.06              0.140           downtrend_blocked_streak           False                  False
   XEL          100.00               25            0.16              0.08         72.27                19.27         0.506            pass              0.764             71.2                           0.512               -3.90             -0.528            downtrend_blocked_slope           False                  False
  VRSK           88.24               17            1.94              2.38        174.39                39.25         0.505            pass              0.392             25.1                           0.271               -7.17             -0.259            downtrend_blocked_slope           False                  False
  TMUS           95.83               24            0.76              0.89        167.80                33.56         0.502            pass              0.783             79.9                           0.739               -8.05             -0.854            downtrend_blocked_slope           False                  False
  PAYX           85.71               21            0.98              0.80        115.80                23.92         0.494 below_threshold              0.401             41.8                           0.408               -5.51             -0.197           downtrend_blocked_streak           False                  False
  INTU          100.00               41            0.19              0.41        303.01                42.64         0.491 below_threshold              0.927             92.8                           0.644               -9.05             -0.570 downtrend_blocked_slope_and_streak           False                  False
   ROP           96.55               29            1.00              2.60        371.63                24.70         0.474 below_threshold              0.697             40.8                           0.580               -9.39             -0.848 downtrend_blocked_slope_and_streak           False                  False
  ORLY           94.74               19            1.48              0.88         84.33                19.71         0.474 below_threshold              0.575             24.7                           0.268               -5.04             -0.370            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-21T12:00:03.740450-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:55:03.827589-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:50:05.829625-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:45:05.912968-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "DXCM261023C00089000", "current_drop_pct": 0.53, "early_entry_score": 0.695, "early_reclaim_pct": 61.8, "entry_ask": 4.1, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 95, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 18.67, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 90.0, "ticker": "DXCM", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.695, "early_reclaim_pct": 61.8, "matched_signals": 40, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "DXCM", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-21T11:40:02.996024-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:35:05.882163-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:30:05.864479-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:25:04.810284-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:20:06.298711-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:15:05.659477-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921130503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921130503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921130503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921130503)

</details>
