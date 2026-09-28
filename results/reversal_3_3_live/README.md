# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 10:40:05 EDT`
Last processed slot: `manage_1030`

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
  MSTR           93.75               32            1.28              1.43        158.00               104.19         0.716            pass              0.760             58.5                           0.299               14.34              2.466                                 ok            True                  False
   CEG           84.21               19            1.31              2.41        262.24                41.90         0.558            pass              0.339             36.9                           0.497               -1.79              0.025                                 ok            True                  False
  UPRO           92.86               14            1.91              2.04        151.33                32.02         0.523            pass              0.429              2.4                           0.114                2.44              0.557                                 ok            True                  False
  PYPL           88.89               18            1.51              0.58         54.79                60.08         0.510            pass              0.523             60.5                           0.516                0.33              0.085                                 ok            True                  False
  WDAY           90.91               33            0.78              1.03        189.01                50.22         0.504            pass              0.739             81.5                           0.673               -3.21             -0.216                                 ok            True                   True
  NXPI           86.21               29            1.02              1.71        237.35                39.27         0.503            pass              0.546             68.0                           0.500                5.56              0.678                                 ok            True                  False
  MPWR           83.33               24            2.16             20.66       1358.57                54.48         0.503            pass              0.364             43.7                           0.320               17.03              2.164                                 ok            True                  False
   TRI           87.50               32            1.07              0.74         98.67                56.74         0.580            pass              0.577             57.4                           0.683               -7.46             -0.516 downtrend_blocked_slope_and_streak           False                  False
   WBD           95.65               46            0.02              0.00         30.86                38.15         0.546            pass              0.936             93.7                           0.673                9.80              1.281                                 ok           False                  False
  LRCX           75.00               32            1.68              3.70        313.62                61.39         0.518            pass              0.374             58.4                           0.381               13.44              1.802                                 ok           False                  False
  SHOP           76.47               17            2.83              2.81        141.04                62.03         0.514            pass              0.188             30.1                           0.503                3.24              1.089                                 ok           False                  False
  MSFT          100.00               13            1.82              6.59        513.34                25.07         0.499 below_threshold              0.567             32.5                           0.439                0.27              0.209                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-28T10:40:05.912979-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.673, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:35:06.564944-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.688, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.688, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:30:06.050551-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "matched_signals": 33, "recovery_stability_score": 0.706, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:25:04.005737-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "matched_signals": 33, "recovery_stability_score": 0.777, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:20:06.719133-04:00 early_entry_1020 early_entry_shadow      {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.893, "shadow_only": true, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "matched_signals": 34, "recovery_stability_score": 0.893, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:15:02.047493-04:00 early_entry_1015 early_entry_shadow   {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "entry_ask": 13.9, "entry_bid": 9.8, "entry_mode": "early", "entry_option_price": 11.85, "hypothetical_budget": 34999.15, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 34.6, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.949, "shadow_only": true, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "matched_signals": 36, "recovery_stability_score": 0.949, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:10:05.010808-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:05:05.986578-04:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "entry_ask": 11.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 9.95, "hypothetical_budget": 34999.15, "hypothetical_contracts": 35, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 35.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.871, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "matched_signals": 33, "recovery_stability_score": 0.871, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:00:06.220548-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T09:50:05.886543-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MSTR261120C00160000", "fill_price": 15.9975, "pnl": -3555.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928104005)

</details>
