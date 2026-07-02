# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-02 13:40:04 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$27,896.50`
- Equity: `$27,896.50`
- Realized PnL: `$17,896.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP          100.00               10            1.12              0.26         33.26                28.32         0.621            pass              0.477              5.1                           0.084                7.58              1.057                                 ok            True                  False
  UPRO           93.33               15            2.09              2.07        140.50                55.10         0.603            pass              0.469              6.6                           0.170               -0.00              0.016                                 ok            True                  False
  PCAR           90.91               11            2.05              1.74        120.49                34.47         0.539            pass              0.352              0.0                           0.165                1.20              0.195                                 ok            True                  False
  AVGO           69.23               13            2.69              6.96        366.36                71.90         0.637            pass              0.125             13.6                           0.369               -8.38             -0.964            downtrend_blocked_slope           False                  False
   WBD           66.67                3            1.38              0.26         26.70                21.87         0.599            pass              0.167             35.7                           0.494                0.76              0.090                                 ok           False                  False
   TXN           80.00               10            2.96              6.18        295.76                67.74         0.581            pass              0.070              3.9                           0.195               -4.08             -0.943            downtrend_blocked_slope           False                  False
    MU           87.50                8            6.63             47.91       1011.75               134.25         0.548            pass              0.258              1.2                           0.123               -7.61             -0.608            downtrend_blocked_slope           False                  False
  GOOG           80.95               21            1.46              3.67        356.32                36.19         0.522            pass              0.289             46.0                           0.503               -2.61             -0.181           downtrend_blocked_streak           False                  False
   ADI           80.00                5            3.93             10.70        384.40                61.24         0.520            pass              0.056              1.2                           0.170               -9.83             -1.316            downtrend_blocked_slope           False                  False
 GOOGL           77.78               18            1.49              3.77        359.59                35.15         0.514            pass              0.286             60.5                           0.568               -2.19             -0.091           downtrend_blocked_streak           False                  False
  ODFL           86.84               38            0.46              0.71        217.66                43.21         0.498 below_threshold              0.478             19.8                           0.293               -0.65             -0.100                                 ok           False                  False
  NVDA           60.00               10            2.57              3.55        196.06                42.46         0.498 below_threshold              0.058              2.9                           0.199               -5.93             -0.703 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-07-02T12:00:01.950437-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:55:04.784699-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:50:04.781471-04:00 early_entry_1150 early_entry_shadow    {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "entry_ask": 14.2, "entry_bid": 13.8, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 2.86, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.835, "early_reclaim_pct": 64.4, "matched_signals": 44, "recovery_stability_score": 0.693, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:45:01.785204-04:00 early_entry_1145 early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "entry_ask": 14.9, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.475, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.87, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.678, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.9, "matched_signals": 44, "recovery_stability_score": 0.678, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:40:01.586831-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.65, "early_entry_score": 0.824, "early_reclaim_pct": 60.8, "entry_ask": 14.5, "entry_bid": 13.75, "entry_mode": "early", "entry_option_price": 14.125, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.31, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.641, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.419, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.824, "early_reclaim_pct": 60.8, "matched_signals": 43, "recovery_stability_score": 0.641, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:35:01.638961-04:00 early_entry_1135 early_entry_shadow     {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.7, "entry_ask": 14.55, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.3, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 3.5, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.691, "shadow_only": true, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.833, "early_reclaim_pct": 63.7, "matched_signals": 44, "recovery_stability_score": 0.691, "success_rate": 97.73, "ticker": "FTNT", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:30:01.731929-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.66, "early_entry_score": 0.822, "early_reclaim_pct": 60.1, "entry_ask": 15.0, "entry_bid": 13.95, "entry_mode": "early", "entry_option_price": 14.475, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 7.25, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.648, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.418, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.822, "early_reclaim_pct": 60.1, "matched_signals": 43, "recovery_stability_score": 0.648, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.418, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:25:01.740560-04:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.62, "early_entry_score": 0.829, "early_reclaim_pct": 62.4, "entry_ask": 14.35, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.125, "hypothetical_budget": 13948.25, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 3.19, "option_volume": 33.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.65, "shadow_only": true, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.421, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.829, "early_reclaim_pct": 62.4, "matched_signals": 43, "recovery_stability_score": 0.65, "success_rate": 97.67, "ticker": "FTNT", "timing_score": 0.421, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-02T11:20:05.689456-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-02T11:15:06.544213-04:00 early_entry_1115 early_entry_shadow  {"contract_symbol": "FTNT260821C00160000", "current_drop_pct": 0.5, "early_entry_score": 0.851, "early_reclaim_pct": 69.8, "entry_ask": 14.1, "entry_bid": 13.35, "entry_mode": "early", "entry_option_price": 13.725, "hypothetical_budget": 13948.25, "hypothetical_contracts": 10, "matched_signals": 45, "option_liquidity_status": "ok", "option_open_interest": 784.0, "option_spread_pct": 5.46, "option_volume": 32.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.416, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.851, "early_reclaim_pct": 69.8, "matched_signals": 45, "recovery_stability_score": 0.685, "success_rate": 97.78, "ticker": "FTNT", "timing_score": 0.416, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260702134004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260702134004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260702134004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260702134004)

</details>
