# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 10:50:06 EDT`
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
  MSTR           93.10               29            1.82              2.02        157.74               104.19         0.702            pass              0.670             41.3                           0.226               13.72              2.441                                 ok            True                  False
   CEG           83.33               18            1.38              2.55        262.18                41.90         0.558            pass              0.297             33.1                           0.421               -1.87              0.021                                 ok            True                  False
  PYPL           88.24               17            1.63              0.63         54.77                60.08         0.508            pass              0.489             57.4                           0.452                0.21              0.080                                 ok            True                  False
   ADI           86.96               23            1.20              3.32        392.18                35.26         0.502            pass              0.493             56.7                           0.359                7.71              0.944                                 ok            True                  False
  CRWD           89.13               46            0.09              0.16        252.06                73.82         0.589            pass              0.793             97.0                           0.479                7.02              0.816                                 ok           False                  False
   TRI           87.50               32            1.07              0.74         98.67                56.74         0.580            pass              0.577             57.3                           0.611               -7.46             -0.516 downtrend_blocked_slope_and_streak           False                  False
  ASML           84.21               38            0.22              2.71       1742.78                41.71         0.523            pass              0.621             90.0                           0.448               10.47              1.143                                 ok           False                  False
  UPRO          100.00                7            2.58              2.75        151.02                32.02         0.518            pass              0.484             10.9                           0.214                1.74              0.525                                 ok           False                  False
  SHOP           76.47               17            2.86              2.85        141.03                62.03         0.512            pass              0.185             29.2                           0.426                3.20              1.088                                 ok           False                  False
  MSFT          100.00               12            1.95              7.03        513.16                25.07         0.497 below_threshold              0.547             28.0                           0.246                0.14              0.203                                 ok           False                  False
  LRCX           72.00               25            2.61              5.76        312.74                61.39         0.495 below_threshold              0.255             35.3                           0.232               12.37              1.759                                 ok           False                  False
  CDNS           81.25               48            0.13              0.30        326.00                46.95         0.491 below_threshold              0.568             95.0                           0.654               16.72              1.956                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-28T10:50:06.030235-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:45:06.952611-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:40:05.912979-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.673, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:35:06.564944-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.688, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.688, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:30:06.050551-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "matched_signals": 33, "recovery_stability_score": 0.706, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:25:04.005737-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "matched_signals": 33, "recovery_stability_score": 0.777, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:20:06.719133-04:00 early_entry_1020 early_entry_shadow      {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.893, "shadow_only": true, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "matched_signals": 34, "recovery_stability_score": 0.893, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:15:02.047493-04:00 early_entry_1015 early_entry_shadow   {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "entry_ask": 13.9, "entry_bid": 9.8, "entry_mode": "early", "entry_option_price": 11.85, "hypothetical_budget": 34999.15, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 34.6, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.949, "shadow_only": true, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "matched_signals": 36, "recovery_stability_score": 0.949, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:10:05.010808-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:05:05.986578-04:00 early_entry_1005 early_entry_shadow   {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "entry_ask": 11.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 9.95, "hypothetical_budget": 34999.15, "hypothetical_contracts": 35, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 35.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.871, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "matched_signals": 33, "recovery_stability_score": 0.871, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928105006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928105006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928105006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928105006)

</details>
