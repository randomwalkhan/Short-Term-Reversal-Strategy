# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 11:20:06 EST`
Last processed slot: `manage_1130`

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

- Cash: `$136,446.55`
- Equity: `$136,446.55`
- Realized PnL: `$126,446.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     34          2026-11-02         2026-11-03        18.25       21.05 9520.0   15.342466 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           92.86               14            0.92              0.43         66.20                28.20         0.594          pass              0.595             55.5                           0.557                2.78              0.267                                 ok            True                  False
   PEP           81.82               11            1.38              1.36        139.84                26.86         0.571          pass              0.200             29.2                           0.352                3.33              0.225                                 ok            True                  False
   KHC           81.25               16            1.62              0.28         24.81                33.68         0.547          pass              0.235             35.7                           0.496                2.92              0.163                                 ok            True                  False
   ROP           89.29               28            1.01              3.40        478.08                37.35         0.521          pass              0.595             58.4                           0.617               19.20              1.709                                 ok            True                  False
   ADP           89.29               28            0.53              1.10        298.31                27.85         0.518          pass              0.647             75.8                           0.715                1.52             -0.167                                 ok            True                  False
   EXC           87.50               24            0.66              0.21         46.36                22.18         0.510          pass              0.501             52.3                           0.585                7.24              0.737                                 ok            True                  False
  TMUS           69.23               13            1.63              1.82        159.37                68.40         0.674          pass              0.209             40.7                           0.600               -0.13              0.118                                 ok           False                  False
  PAYX           72.22               18            0.54              0.44        115.30                35.36         0.581          pass              0.359             82.5                           0.774                3.03             -0.044                                 ok           False                  False
  MRVL           88.89               36            1.06              1.27        170.87                97.23         0.570          pass              0.534             22.1                           0.177              -29.46             -3.249 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           92.31               26            0.17              0.03         23.86                32.70         0.568          pass              0.762             90.1                           0.703                6.57              0.564                                 ok           False                  False
   CSX           71.43               14            0.94              0.34         51.47                27.65         0.556          pass              0.211             43.0                           0.612                6.35              0.594                                 ok           False                  False
  GOOG           87.80               41            0.22              0.43        277.86                49.16         0.553          pass              0.718             84.9                           0.542              -17.53             -2.088 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-03T11:20:06.072141-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:15:01.990433-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:10:06.114764-05:00 early_entry_1110 early_entry_shadow  {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "entry_ask": 7.5, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 68223.28, "hypothetical_contracts": 99, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 18.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.633, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T11:05:06.948885-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:00:05.972600-05:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "entry_ask": 7.5, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 6.8, "hypothetical_budget": 68223.28, "hypothetical_contracts": 100, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 20.59, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "matched_signals": 31, "recovery_stability_score": 0.675, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:55:05.970636-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:50:06.376487-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:45:05.029360-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T10:40:06.271998-05:00 early_entry_1040 early_entry_shadow   {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "entry_ask": 7.5, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 68223.28, "hypothetical_contracts": 101, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 22.22, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.76, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.76, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:35:07.004174-05:00 early_entry_1035 early_entry_shadow {"contract_symbol": "CTAS261204C00225000", "current_drop_pct": 0.52, "early_entry_score": 0.803, "early_reclaim_pct": 68.9, "entry_ask": 6.4, "entry_bid": 5.1, "entry_mode": "early", "entry_option_price": 5.75, "hypothetical_budget": 68223.28, "hypothetical_contracts": 118, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 22.61, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.762, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.495, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.803, "early_reclaim_pct": 68.9, "matched_signals": 32, "recovery_stability_score": 0.762, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.495, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103112006)

</details>
