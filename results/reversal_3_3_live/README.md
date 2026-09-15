# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 10:55:01 EDT`
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

- Cash: `$72,316.10`
- Equity: `$72,316.10`
- Realized PnL: `$62,316.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-15)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   EXC     option         option EXC261016C00043000    400          2026-09-14         2026-09-15         0.95       0.855 -3800.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           90.00               20            1.15              0.43         53.84                58.07         0.655          pass              0.413              4.6                           0.199                1.67             -0.004                                 ok            True                  False
    ZS           97.14               35            1.11              1.49        191.09                82.09         0.617          pass              0.790             54.0                           0.403                0.65             -0.013                                 ok            True                  False
  TEAM          100.00               28            1.93              2.60        191.66                63.46         0.559          pass              0.682             35.5                           0.365               -2.63             -0.317                                 ok            True                  False
  CTSH           97.14               35            0.55              0.24         63.99                45.53         0.521          pass              0.871             84.0                           0.691               -1.29             -0.418                                 ok            True                   True
  AAPL           86.96               23            1.02              2.38        332.06                23.75         0.504          pass              0.407             28.2                           0.336                4.05              0.307                                 ok            True                  False
  AMGN           93.33               15            1.15              3.07        380.18                45.29         0.623          pass              0.532             27.0                           0.468              -12.28             -1.908 downtrend_blocked_slope_and_streak           False                  False
  MSTR           90.00               10            5.68              5.45        134.60               103.17         0.574          pass              0.347              7.8                           0.196               -2.85              0.088           downtrend_blocked_streak           False                  False
  REGN          100.00                2            2.36             13.10        788.13                29.50         0.563          pass              0.469              4.2                           0.250               -3.01             -0.644 downtrend_blocked_slope_and_streak           False                  False
  ADSK           86.49               37            0.53              0.85        228.56                57.97         0.554          pass              0.661             84.3                           0.615              -11.92             -1.475           downtrend_blocked_streak           False                  False
   CEG           88.24               17            1.42              2.63        263.44                42.97         0.550          pass              0.336              4.8                           0.102               -5.08             -0.507 downtrend_blocked_slope_and_streak           False                  False
   EXC           92.31               13            0.46              0.14         42.66                14.63         0.546          pass              0.578             58.5                           0.557               -1.81             -0.195           downtrend_blocked_streak           False                  False
   PEP           87.50               16            0.40              0.39        136.17                16.22         0.543          pass              0.491             65.4                           0.760               -2.21             -0.239                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-15T10:55:01.169845-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CTSH261016C00065000", "current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "entry_ask": 2.55, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.475, "hypothetical_budget": 36158.05, "hypothetical_contracts": 146, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 712.0, "option_spread_pct": 6.06, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.691, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "matched_signals": 35, "recovery_stability_score": 0.691, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.769, "early_reclaim_pct": 71.9, "matched_signals": 38, "recovery_stability_score": 0.65, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:50:06.229690-04:00 early_entry_1050 early_entry_shadow   {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "entry_ask": 3.8, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.6, "hypothetical_budget": 36158.05, "hypothetical_contracts": 100, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 792.0, "option_spread_pct": 11.11, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "matched_signals": 34, "recovery_stability_score": 0.593, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.799, "early_reclaim_pct": 77.7, "matched_signals": 39, "recovery_stability_score": 0.735, "success_rate": 92.31, "ticker": "GILD", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:45:06.502503-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:40:02.128909-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:35:06.132265-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:30:04.241835-04:00 early_entry_1030 early_entry_shadow                   {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "entry_ask": 9.9, "entry_bid": 9.25, "entry_mode": "early", "entry_option_price": 9.575, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 602.0, "option_spread_pct": 6.79, "option_volume": 100.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.581, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "matched_signals": 42, "recovery_stability_score": 0.581, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.778, "early_reclaim_pct": 74.8, "matched_signals": 38, "recovery_stability_score": 0.752, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:25:01.133088-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "entry_ask": 4.8, "entry_bid": 4.3, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 36158.05, "hypothetical_contracts": 79, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 10.99, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.739, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "matched_signals": 38, "recovery_stability_score": 0.739, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:20:02.316834-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "entry_ask": 4.8, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.5, "hypothetical_budget": 36158.05, "hypothetical_contracts": 80, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 13.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "matched_signals": 38, "recovery_stability_score": 0.753, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:15:01.098518-04:00 early_entry_1015 early_entry_shadow                         {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "entry_ask": 13.8, "entry_bid": 12.0, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 13.95, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "matched_signals": 38, "recovery_stability_score": 0.618, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 67.1, "matched_signals": 34, "recovery_stability_score": 0.698, "success_rate": 91.18, "ticker": "GILD", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:10:06.048953-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                  {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "entry_ask": 4.4, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 3.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 93, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 792.0, "option_spread_pct": 28.57, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "matched_signals": 35, "recovery_stability_score": 0.682, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915105501)

</details>
