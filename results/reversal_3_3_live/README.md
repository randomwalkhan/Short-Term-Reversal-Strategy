# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 11:00:05 EDT`
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
  PYPL           92.00               25            0.87              0.33         53.89                58.07         0.645          pass              0.567             27.3                           0.306                1.95              0.008                                 ok            True                  False
    ZS           97.22               36            0.95              1.28        191.18                82.09         0.620          pass              0.817             60.5                           0.409                0.80             -0.006                                 ok            True                  False
  TEAM          100.00               29            1.65              2.23        191.82                63.46         0.569          pass              0.718             44.8                           0.566               -2.36             -0.305                                 ok            True                  False
   PEP           87.50               16            0.51              0.49        136.13                16.22         0.536          pass              0.462             56.0                           0.666               -2.32             -0.244                                 ok            True                  False
   AEP           87.50               16            0.75              0.64        121.96                16.70         0.518          pass              0.344             17.6                           0.257               -0.91             -0.085                                 ok            True                  False
  AAPL           86.96               23            1.00              2.32        332.09                23.75         0.506          pass              0.412             29.9                           0.394                4.08              0.308                                 ok            True                  False
  MSFT          100.00               22            1.11              3.92        503.73                22.76         0.500          pass              0.600             23.4                           0.353               -1.47             -0.121                                 ok            True                  False
  AMGN           92.86               14            1.29              3.45        380.02                45.29         0.620          pass              0.486             18.1                           0.347              -12.40             -1.914 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.98               47            0.07              0.19        373.86                81.04         0.603          pass              0.628             96.2                           0.702               -2.21              0.074                                 ok           False                  False
  REGN          100.00                2            2.38             13.22        788.07                29.50         0.562          pass              0.466              3.3                           0.227               -3.03             -0.645 downtrend_blocked_slope_and_streak           False                  False
   WMT           86.49               37            0.20              0.15        109.01                40.03         0.561          pass              0.634             75.0                           0.618                3.80              0.247                                 ok           False                  False
   EXC          100.00               11            0.59              0.17         42.65                14.63         0.558          pass              0.603             46.8                           0.368               -1.93             -0.201           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-15T11:00:05.317059-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                             {"contract_symbol": "GILD261016C00150000", "current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "entry_ask": 3.1, "entry_bid": 2.74, "entry_mode": "early", "entry_option_price": 2.92, "hypothetical_budget": 36158.05, "hypothetical_contracts": 123, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 529.0, "option_spread_pct": 12.33, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.576, "shadow_only": true, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.748, "early_reclaim_pct": 68.8, "matched_signals": 37, "recovery_stability_score": 0.576, "success_rate": 91.89, "ticker": "GILD", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:55:01.169845-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CTSH261016C00065000", "current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "entry_ask": 2.55, "entry_bid": 2.4, "entry_mode": "early", "entry_option_price": 2.475, "hypothetical_budget": 36158.05, "hypothetical_contracts": 146, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 712.0, "option_spread_pct": 6.06, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.691, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.871, "early_reclaim_pct": 84.0, "matched_signals": 35, "recovery_stability_score": 0.691, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.521, "trend_health_status": "ok"}, {"current_drop_pct": 0.69, "early_entry_score": 0.769, "early_reclaim_pct": 71.9, "matched_signals": 38, "recovery_stability_score": 0.65, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:50:06.229690-04:00 early_entry_1050 early_entry_shadow   {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "entry_ask": 3.8, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.6, "hypothetical_budget": 36158.05, "hypothetical_contracts": 100, "matched_signals": 34, "option_liquidity_status": "low_volume", "option_open_interest": 792.0, "option_spread_pct": 11.11, "option_volume": 7.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.849, "early_reclaim_pct": 79.0, "matched_signals": 34, "recovery_stability_score": 0.593, "success_rate": 97.06, "ticker": "CTSH", "timing_score": 0.516, "trend_health_status": "ok"}, {"current_drop_pct": 0.55, "early_entry_score": 0.799, "early_reclaim_pct": 77.7, "matched_signals": 39, "recovery_stability_score": 0.735, "success_rate": 92.31, "ticker": "GILD", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:45:06.502503-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:40:02.128909-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:35:06.132265-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-15T10:30:04.241835-04:00 early_entry_1030 early_entry_shadow                   {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "entry_ask": 9.9, "entry_bid": 9.25, "entry_mode": "early", "entry_option_price": 9.575, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 602.0, "option_spread_pct": 6.79, "option_volume": 100.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.581, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.781, "early_reclaim_pct": 83.2, "matched_signals": 42, "recovery_stability_score": 0.581, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.526, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.778, "early_reclaim_pct": 74.8, "matched_signals": 38, "recovery_stability_score": 0.752, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.446, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:25:01.133088-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                              {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "entry_ask": 4.8, "entry_bid": 4.3, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 36158.05, "hypothetical_contracts": 79, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 10.99, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.739, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "matched_signals": 38, "recovery_stability_score": 0.739, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:20:02.316834-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                             {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "entry_ask": 4.8, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.5, "hypothetical_budget": 36158.05, "hypothetical_contracts": 80, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 13.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "matched_signals": 38, "recovery_stability_score": 0.753, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:15:01.098518-04:00 early_entry_1015 early_entry_shadow                         {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "entry_ask": 13.8, "entry_bid": 12.0, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 13.95, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "matched_signals": 38, "recovery_stability_score": 0.618, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 67.1, "matched_signals": 34, "recovery_stability_score": 0.698, "success_rate": 91.18, "ticker": "GILD", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915110005)

</details>
