# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 11:10:06 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           93.94               33            1.25              1.39        158.02               104.19         0.713          pass              0.775             59.7                           0.458               14.38              2.467                                 ok            True                  False
   CEG           84.21               19            1.30              2.39        262.25                41.90         0.559          pass              0.340             37.4                           0.457               -1.78              0.025                                 ok            True                  False
  SHOP           82.61               23            1.94              1.93        141.42                62.03         0.540          pass              0.366             52.0                           0.707                4.18              1.131                                 ok            True                  False
  PYPL           88.89               18            1.53              0.59         54.79                60.08         0.509          pass              0.521             60.0                           0.516                0.31              0.084                                 ok            True                  False
  MSFT          100.00               15            1.51              5.46        513.83                25.07         0.507          pass              0.616             44.1                           0.571                0.59              0.223                                 ok            True                  False
   ADI           88.00               25            0.99              2.73        392.43                35.26         0.506          pass              0.557             64.4                           0.445                7.94              0.954                                 ok            True                  False
  UPRO           90.91               11            2.27              2.41        151.16                32.02         0.506          pass              0.419             23.5                           0.306                2.07              0.540                                 ok            True                  False
   TRI           87.88               33            0.86              0.60         98.73                56.74         0.588          pass              0.620             65.9                           0.575               -7.26             -0.507 downtrend_blocked_slope_and_streak           False                  False
   WBD           95.65               46            0.03              0.01         30.86                38.15         0.544          pass              0.916             87.3                           0.579                9.79              1.280                                 ok           False                  False
  LRCX           73.08               26            2.39              5.26        312.95                61.39         0.505          pass              0.280             40.8                           0.342               12.62              1.769                                 ok           False                  False
  CHTR           79.07               43            0.49              0.38        112.75                64.54         0.503          pass              0.486             78.5                           0.384              -21.62             -2.623 downtrend_blocked_slope_and_streak           False                  False
   KHC           95.83               24            0.18              0.03         23.62                20.56         0.502          pass              0.772             76.2                           0.428               -2.81             -0.479 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-09-28T11:10:06.397628-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:05:04.918839-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:00:06.419831-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:55:05.016465-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:50:06.030235-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:45:06.952611-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:40:05.912979-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.673, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.673, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:35:06.564944-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.688, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "top_candidates": [{"current_drop_pct": 0.78, "early_entry_score": 0.739, "early_reclaim_pct": 81.5, "matched_signals": 33, "recovery_stability_score": 0.688, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.504, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:30:06.050551-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "entry_ask": 13.8, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.25, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 25.31, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.706, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.86, "early_entry_score": 0.733, "early_reclaim_pct": 79.5, "matched_signals": 33, "recovery_stability_score": 0.706, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:25:04.005737-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.94, "early_entry_score": 0.726, "early_reclaim_pct": 77.6, "matched_signals": 33, "recovery_stability_score": 0.777, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928111006)

</details>
