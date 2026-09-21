# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-21 14:25:05 EDT`
Last processed slot: `manage_1430`

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
  WDAY           94.29               35            0.58              0.79        193.53                50.60         0.542            pass              0.750             49.4                           0.263               -1.56              0.311                                 ok            True                  False
  CTSH          100.00               33            0.77              0.32         59.73                41.33         0.502            pass              0.604              0.0                           0.181               -4.65              0.103                                 ok            True                  False
   KHC           95.00               20            0.23              0.04         24.41                22.04         0.549            pass              0.737             71.8                           0.646               -1.91             -0.114                                 ok           False                  False
  ADBE           97.44               39            0.18              0.31        248.79                46.23         0.539            pass              0.919             90.6                           0.706               -6.77             -0.430            downtrend_blocked_slope           False                  False
   XEL          100.00               17            0.47              0.24         72.20                19.27         0.534            pass              0.592             30.6                           0.350               -4.20             -0.542            downtrend_blocked_slope           False                  False
  CHTR           85.00               20            2.74              2.46        127.12                64.18         0.533            pass              0.258              1.7                           0.142              -17.98             -1.481 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.67               30            0.16              0.31        271.09                22.01         0.503            pass              0.850             88.9                           0.615               -1.84              0.150           downtrend_blocked_streak           False                  False
  VRSK           89.47               19            1.81              2.23        174.46                39.25         0.502            pass              0.452             29.8                           0.481               -7.05             -0.253            downtrend_blocked_slope           False                  False
   EXC           96.15               26            0.12              0.03         42.06                15.92         0.499 below_threshold              0.829             90.9                           0.506               -3.71             -0.459 downtrend_blocked_slope_and_streak           False                  False
  TMUS           95.83               24            0.85              1.00        167.75                33.56         0.496 below_threshold              0.775             77.4                           0.608               -8.14             -0.858            downtrend_blocked_slope           False                  False
   PEP           92.59               27            0.12              0.10        129.71                15.76         0.492 below_threshold              0.773             91.5                           0.641               -5.83             -0.607 downtrend_blocked_slope_and_streak           False                  False
  PAYX           86.36               22            0.92              0.75        115.82                23.92         0.492 below_threshold              0.436             45.7                           0.507               -5.45             -0.194           downtrend_blocked_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260921142505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260921142505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260921142505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260921142505)

</details>
