# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 11:20:04 EDT`
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
  PYPL           92.59               27            0.81              0.30         53.90                58.07         0.638          pass              0.612             33.1                           0.490                2.02              0.011                                 ok            True                  False
    ZS           97.44               39            0.59              0.80        191.39                82.09         0.624          pass              0.882             75.4                           0.715                1.17              0.010                                 ok            True                   True
  PANW           80.95               42            0.65              1.70        373.21                81.04         0.596          pass              0.483             66.1                           0.465               -2.78              0.047                                 ok            True                  False
  MSTR           81.82               22            4.01              3.84        135.29               103.17         0.590          pass              0.292             35.0                           0.752               -1.12              0.168                                 ok            True                  False
  TEAM          100.00               33            1.22              1.65        192.06                63.46         0.571          pass              0.788             59.2                           0.769               -1.93             -0.285                                 ok            True                  False
   PEP           87.50               16            0.59              0.56        136.10                16.22         0.531          pass              0.442             49.7                           0.476               -2.39             -0.247                                 ok            True                  False
   AEP           85.71               14            0.86              0.73        121.92                16.70         0.520          pass              0.280             16.3                           0.263               -1.02             -0.090                                 ok            True                  False
  ISRG           80.95               21            1.50              3.97        376.24                34.61         0.515          pass              0.263             37.7                           0.674               -1.22             -0.072                                 ok            True                  False
  AAPL           87.50               24            0.88              2.05        332.20                23.75         0.507          pass              0.458             38.1                           0.507                4.20              0.313                                 ok            True                  False
  AMGN           93.33               15            1.15              3.07        380.18                45.29         0.623          pass              0.532             27.0                           0.404              -12.28             -1.908 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00                5            2.11             11.74        788.71                29.50         0.560          pass              0.498             14.1                           0.320               -2.77             -0.632 downtrend_blocked_slope_and_streak           False                  False
   EXC          100.00               10            0.75              0.22         42.62                14.63         0.554          pass              0.551             31.9                           0.228               -2.10             -0.209           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-15T11:20:04.224010-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                 {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.59, "early_entry_score": 0.882, "early_reclaim_pct": 75.4, "entry_ask": 13.8, "entry_bid": 12.85, "entry_mode": "early", "entry_option_price": 13.325, "hypothetical_budget": 36158.05, "hypothetical_contracts": 27, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 7.13, "option_volume": 37.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.715, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.624, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.882, "early_reclaim_pct": 75.4, "matched_signals": 39, "recovery_stability_score": 0.715, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.624, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:15:01.103562-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                               {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "entry_ask": 13.2, "entry_bid": 12.4, "entry_mode": "early", "entry_option_price": 12.8, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 6.25, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.805, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "top_candidates": [{"current_drop_pct": 1.0, "early_entry_score": 0.823, "early_reclaim_pct": 66.5, "matched_signals": 35, "recovery_stability_score": 0.805, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.572, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:10:01.228919-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                              {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.02, "early_entry_score": 0.821, "early_reclaim_pct": 65.8, "entry_ask": 13.4, "entry_bid": 12.3, "entry_mode": "early", "entry_option_price": 12.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 8.56, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.775, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.57, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.821, "early_reclaim_pct": 65.8, "matched_signals": 35, "recovery_stability_score": 0.775, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.57, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:05:02.271330-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                             {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 1.16, "early_entry_score": 0.795, "early_reclaim_pct": 61.3, "entry_ask": 13.1, "entry_bid": 12.1, "entry_mode": "early", "entry_option_price": 12.6, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 7403.0, "option_spread_pct": 7.94, "option_volume": 40.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.708, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.574, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.795, "early_reclaim_pct": 61.3, "matched_signals": 33, "recovery_stability_score": 0.708, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.574, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T11:00:05.317059-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                             {"contract_symbol": "GILD261016C00150000", "current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "entry_ask": 3.1, "entry_bid": 2.74, "entry_mode": "early", "entry_option_price": 2.92, "hypothetical_budget": 36158.05, "hypothetical_contracts": 123, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 529.0, "option_spread_pct": 12.33, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.576, "shadow_only": true, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "matched_signals": 37, "recovery_stability_score": 0.576, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:55:01.169845-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CTSH261016C00065000", "current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "entry_ask": 2.55, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.475, "hypothetical_budget": 36158.05, "hypothetical_contracts": 146, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 712.0, "option_spread_pct": 6.06, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.691, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "matched_signals": 35, "recovery_stability_score": 0.691, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.769, "early_reclaim_pct": 71.9, "matched_signals": 38, "recovery_stability_score": 0.65, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:50:06.229690-04:00 early_entry_1050 early_entry_shadow   {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "entry_ask": 3.8, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.6, "hypothetical_budget": 36158.05, "hypothetical_contracts": 100, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 792.0, "option_spread_pct": 11.11, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "matched_signals": 34, "recovery_stability_score": 0.593, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.799, "early_reclaim_pct": 77.7, "matched_signals": 39, "recovery_stability_score": 0.735, "success_rate": 92.31, "ticker": "GILD", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:45:06.502503-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:40:02.128909-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:35:06.132265-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915112004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915112004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915112004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915112004)

</details>
