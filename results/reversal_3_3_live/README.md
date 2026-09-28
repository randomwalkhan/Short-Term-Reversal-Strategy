# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 10:55:05 EDT`
Last processed slot: `manage_1100`

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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.10               29            1.74              1.93        157.78               104.19         0.706            pass              0.678             43.9                           0.237               13.81              2.445                                 ok            True                  False
   CEG           82.35               17            1.61              2.96        262.00                41.90         0.547            pass              0.231             22.4                           0.332               -2.09              0.011                                 ok            True                  False
  PYPL           86.67               15            1.68              0.65         54.76                60.08         0.514            pass              0.430             56.0                           0.444                0.16              0.077                                 ok            True                  False
  MSFT          100.00               10            2.01              7.28        513.05                25.07         0.504            pass              0.527             25.5                           0.204                0.07              0.200                                 ok            True                  False
   ADI           86.96               23            1.21              3.33        392.17                35.26         0.502            pass              0.492             56.5                           0.325                7.71              0.944                                 ok            True                  False
  CRWD           89.13               46            0.04              0.06        252.10                73.82         0.592            pass              0.799             98.8                           0.453                7.08              0.818                                 ok           False                  False
   TRI           87.10               31            1.29              0.90         98.61                56.74         0.571            pass              0.532             48.6                           0.546               -7.66             -0.527 downtrend_blocked_slope_and_streak           False                  False
  ASML           84.21               38            0.17              2.07       1743.05                41.71         0.527            pass              0.629             92.4                           0.437               10.53              1.145                                 ok           False                  False
  UPRO          100.00                4            2.94              3.13        150.86                32.02         0.513            pass              0.451              0.0                           0.157                1.37              0.509                                 ok           False                  False
  SHOP           76.47               17            2.85              2.84        141.03                62.03         0.512            pass              0.186             29.4                           0.440                3.21              1.088                                 ok           False                  False
  LRCX           72.00               25            2.64              5.83        312.71                61.39         0.493 below_threshold              0.253             34.5                           0.215               12.33              1.757                                 ok           False                  False
  PAYX           83.33               24            1.03              0.73        101.06                37.87         0.492 below_threshold              0.405             57.7                           0.487              -15.34             -1.908 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-28T10:55:05.016465-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:50:06.030235-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:45:06.952611-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:40:05.912979-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.673, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:35:06.564944-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.688, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.688, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:30:06.050551-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "matched_signals": 33, "recovery_stability_score": 0.706, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:25:04.005737-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "matched_signals": 33, "recovery_stability_score": 0.777, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:20:06.719133-04:00 early_entry_1020 early_entry_shadow      {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.893, "shadow_only": true, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "matched_signals": 34, "recovery_stability_score": 0.893, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:15:02.047493-04:00 early_entry_1015 early_entry_shadow   {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "entry_ask": 13.9, "entry_bid": 9.8, "entry_mode": "early", "entry_option_price": 11.85, "hypothetical_budget": 34999.15, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 34.6, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.949, "shadow_only": true, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "matched_signals": 36, "recovery_stability_score": 0.949, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:10:05.010808-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928105505)

</details>
