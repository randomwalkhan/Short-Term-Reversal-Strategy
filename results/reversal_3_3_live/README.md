# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-04 14:40:04 EDT`
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

- Cash: `$81,160.60`
- Equity: `$81,160.60`
- Realized PnL: `$71,160.60`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-04)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261016C00110000     99          2026-09-03         2026-09-04        3.725         4.4 6682.5   18.120805 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CRWD           89.74               39            1.13              1.70        214.24                92.33         0.628          pass              0.616             33.4                           0.368               10.73              1.398                                 ok            True                  False
  MSTR           82.86               35            1.49              1.51        144.17               101.55         0.627          pass              0.537             77.3                           0.733               19.63              1.335                                 ok            True                  False
   WMT           84.21               19            1.19              0.90        108.03                40.07         0.587          pass              0.235              1.2                           0.090                3.31              0.279                                 ok            True                  False
  VRTX           92.31               13            1.97              7.68        554.67                32.02         0.539          pass              0.532             43.2                           0.255               -0.19              0.075                                 ok            True                  False
  SBUX           95.45               22            0.68              0.50        105.60                21.61         0.530          pass              0.613             26.5                           0.346               -1.85             -0.165                                 ok            True                  False
  REGN          100.00               16            1.35              7.95        840.06                28.19         0.529          pass              0.509              5.2                           0.194               -0.23              0.125                                 ok            True                  False
   KDP           86.67               30            0.67              0.15         32.81                30.98         0.513          pass              0.449             29.0                           0.303                1.94              0.173                                 ok            True                  False
  WDAY           84.62               13            4.40              6.38        204.19                73.93         0.513          pass              0.245             17.0                           0.214               -1.10              0.267                                 ok            True                  False
   XEL           94.74               19            1.00              0.53         76.11                17.75         0.510          pass              0.599             31.5                           0.382               -0.94             -0.210                                 ok            True                  False
   KHC           88.89               27            0.88              0.15         24.95                29.47         0.503          pass              0.465             21.4                           0.333               -3.05              0.020                                 ok            True                  False
  MNST           86.21               29            0.63              0.20         44.00               424.09         0.998          pass              0.497             35.1                           0.418               -8.35             -1.153 downtrend_blocked_slope_and_streak           False                  False
  PYPL          100.00                4            3.61              1.43         56.21                56.63         0.575          pass              0.491             11.3                           0.354              -11.01             -1.625 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-09-04T12:00:02.433039-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T11:55:02.514482-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 0.99, "early_entry_score": 0.803, "early_reclaim_pct": 71.5, "entry_ask": 24.0, "entry_bid": 21.7, "entry_mode": "early", "entry_option_price": 22.85, "hypothetical_budget": 40580.3, "hypothetical_contracts": 17, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 220.0, "option_spread_pct": 10.07, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 0.99, "early_entry_score": 0.803, "early_reclaim_pct": 71.5, "matched_signals": 31, "recovery_stability_score": 0.731, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T11:50:01.382488-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "VRTX261016C00550000", "current_drop_pct": 1.0, "early_entry_score": 0.802, "early_reclaim_pct": 71.0, "entry_ask": 24.5, "entry_bid": 21.6, "entry_mode": "early", "entry_option_price": 23.05, "hypothetical_budget": 40580.3, "hypothetical_contracts": 17, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 220.0, "option_spread_pct": 12.58, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.707, "shadow_only": true, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.802, "early_reclaim_pct": 71.0, "matched_signals": 31, "recovery_stability_score": 0.707, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-04T11:45:06.187028-04:00 early_entry_1145 early_entry_shadow                       {"contract_symbol": "VRTX261016C00560000", "current_drop_pct": 1.02, "early_entry_score": 0.8, "early_reclaim_pct": 70.4, "entry_ask": 18.5, "entry_bid": 16.9, "entry_mode": "early", "entry_option_price": 17.7, "hypothetical_budget": 40580.3, "hypothetical_contracts": 22, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 286.0, "option_spread_pct": 9.04, "option_volume": 55.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.488, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.8, "early_reclaim_pct": 70.4, "matched_signals": 31, "recovery_stability_score": 0.676, "success_rate": 96.77, "ticker": "VRTX", "timing_score": 0.488, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-04T11:40:05.184091-04:00 early_entry_1140 early_entry_shadow                   {"contract_symbol": "VRTX261016C00560000", "current_drop_pct": 1.06, "early_entry_score": 0.791, "early_reclaim_pct": 69.5, "entry_ask": 18.5, "entry_bid": 16.9, "entry_mode": "early", "entry_option_price": 17.7, "hypothetical_budget": 40580.3, "hypothetical_contracts": 22, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 286.0, "option_spread_pct": 9.04, "option_volume": 55.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.551, "shadow_only": true, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.492, "top_candidates": [{"current_drop_pct": 1.06, "early_entry_score": 0.791, "early_reclaim_pct": 69.5, "matched_signals": 30, "recovery_stability_score": 0.551, "success_rate": 96.67, "ticker": "VRTX", "timing_score": 0.492, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-04T11:35:01.374380-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T11:30:01.357870-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T11:25:04.310412-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T11:20:01.293932-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-04T11:15:01.361292-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260904144004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260904144004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260904144004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260904144004)

</details>
