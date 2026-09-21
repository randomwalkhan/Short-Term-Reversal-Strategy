# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 11:50:05 EDT`
Last processed slot: `manage_1200`

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
   KHC           93.75               16            0.65              0.11         24.38                22.04         0.546            pass              0.515             17.9                           0.220               -2.33             -0.133                                 ok            True                  False
   PEP          100.00               11            0.82              0.75        129.43                15.76         0.557            pass              0.582             39.8                           0.514               -6.50             -0.639 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.37               38            0.39              0.68        248.63                46.23         0.532            pass              0.878             79.3                           0.650               -6.96             -0.440            downtrend_blocked_slope           False                  False
  CHTR           89.47               38            1.14              1.03        127.73                64.18         0.527            pass              0.658             55.5                           0.592              -16.64             -1.407 downtrend_blocked_slope_and_streak           False                  False
  WDAY           95.45               44            0.07              0.10        193.83                50.60         0.520            pass              0.933             93.7                           0.676               -1.05              0.335                                 ok           False                  False
   ADP           96.00               25            0.52              0.99        270.80                22.01         0.510            pass              0.745             64.7                           0.638               -2.19              0.134           downtrend_blocked_streak           False                  False
  VRSK           85.71               14            2.25              2.76        174.23                39.25         0.501            pass              0.268             13.0                           0.244               -7.46             -0.273            downtrend_blocked_slope           False                  False
  TMUS           95.83               24            0.91              1.07        167.72                33.56         0.493 below_threshold              0.770             75.8                           0.760               -8.19             -0.861            downtrend_blocked_slope           False                  False
  PAYX           86.36               22            0.90              0.74        115.82                23.92         0.493 below_threshold              0.438             46.4                           0.690               -5.44             -0.194           downtrend_blocked_streak           False                  False
  SBUX           81.82               11            1.57              1.05         95.38                22.99         0.490 below_threshold              0.200             32.0                           0.344               -9.71             -0.840 downtrend_blocked_slope_and_streak           False                  False
  INTU          100.00               41            0.31              0.65        302.91                42.64         0.484 below_threshold              0.914             88.5                           0.744               -9.15             -0.575 downtrend_blocked_slope_and_streak           False                  False
   ROP           95.83               24            1.36              3.55        371.22                24.70         0.481 below_threshold              0.599             19.1                           0.262               -9.73             -0.865 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-09-21T11:50:05.829625-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:45:05.912968-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "DXCM261023C00089000", "current_drop_pct": 0.53, "early_entry_score": 0.695, "early_reclaim_pct": 61.8, "entry_ask": 4.1, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.75, "hypothetical_budget": 35735.4, "hypothetical_contracts": 95, "matched_signals": 40, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 18.67, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 90.0, "ticker": "DXCM", "timing_score": 0.428, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.695, "early_reclaim_pct": 61.8, "matched_signals": 40, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "DXCM", "timing_score": 0.428, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-21T11:40:02.996024-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:35:05.882163-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:30:05.864479-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:25:04.810284-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:20:06.298711-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:15:05.659477-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:10:04.948141-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T11:05:05.847856-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921115005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921115005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921115005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921115005)

</details>
