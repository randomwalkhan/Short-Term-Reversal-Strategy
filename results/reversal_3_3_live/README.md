# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-15 10:25:01 EDT`
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
  PYPL           92.59               27            0.80              0.30         53.90                58.07         0.641          pass              0.565             17.2                           0.142                2.03              0.012                                 ok            True                  False
    ZS           97.37               38            0.84              1.12        191.25                82.09         0.616          pass              0.844             65.3                           0.487                0.92             -0.001                                 ok            True                  False
  TEAM          100.00               26            2.21              2.99        191.49                63.46         0.554          pass              0.640             26.0                           0.206               -2.92             -0.331                                 ok            True                  False
  CTSH           97.06               34            0.84              0.38         63.94                45.53         0.509          pass              0.837             75.3                           0.440               -1.58             -0.431                                 ok            True                  False
   AEP           89.47               19            0.67              0.57        121.98                16.70         0.507          pass              0.442             26.1                           0.342               -0.83             -0.082                                 ok            True                  False
  AAPL           86.36               22            1.11              2.58        331.97                23.75         0.505          pass              0.366             22.0                           0.213                3.96              0.303                                 ok            True                  False
  MSFT          100.00               20            1.27              4.49        503.49                22.76         0.503          pass              0.554             12.3                           0.105               -1.63             -0.129                                 ok            True                  False
  AMGN           91.67               12            1.42              3.79        379.88                45.29         0.623          pass              0.417             10.0                           0.225              -12.51             -1.920 downtrend_blocked_slope_and_streak           False                  False
  PANW           82.98               47            0.02              0.06        373.91                81.04         0.606          pass              0.636             98.8                           0.803               -2.17              0.076                                 ok           False                  False
  MSTR           81.25               16            4.70              4.51        135.01               103.17         0.592          pass              0.169             12.3                           0.242               -1.84              0.135           downtrend_blocked_streak           False                  False
   KHC           90.91               11            0.93              0.16         24.20                26.10         0.573          pass              0.525             56.7                           0.644               -4.94             -0.539            downtrend_blocked_slope           False                  False
  ADSK           85.29               34            0.67              1.08        228.47                57.97         0.562          pass              0.598             80.2                           0.653              -12.05             -1.481           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-09-15T10:25:01.133088-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                      {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "entry_ask": 4.8, "entry_bid": 4.3, "entry_mode": "early", "entry_option_price": 4.55, "hypothetical_budget": 36158.05, "hypothetical_contracts": 79, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 10.99, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.739, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.767, "early_reclaim_pct": 71.0, "matched_signals": 38, "recovery_stability_score": 0.739, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.44, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:20:02.316834-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                     {"contract_symbol": "GILD261016C00145000", "current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "entry_ask": 4.8, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 4.5, "hypothetical_budget": 36158.05, "hypothetical_contracts": 80, "matched_signals": 38, "option_liquidity_status": "low_volume", "option_open_interest": 1112.0, "option_spread_pct": 13.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.753, "shadow_only": true, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.777, "early_reclaim_pct": 74.4, "matched_signals": 38, "recovery_stability_score": 0.753, "success_rate": 92.11, "ticker": "GILD", "timing_score": 0.445, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:15:01.098518-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "entry_ask": 13.8, "entry_bid": 12.0, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 36158.05, "hypothetical_contracts": 28, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 13.95, "option_volume": 26.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.858, "early_reclaim_pct": 69.9, "matched_signals": 38, "recovery_stability_score": 0.618, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}, {"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 67.1, "matched_signals": 34, "recovery_stability_score": 0.698, "success_rate": 91.18, "ticker": "GILD", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:10:06.048953-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "entry_ask": 4.4, "entry_bid": 3.3, "entry_mode": "early", "entry_option_price": 3.85, "hypothetical_budget": 36158.05, "hypothetical_contracts": 93, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 792.0, "option_spread_pct": 28.57, "option_volume": 16.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.682, "shadow_only": true, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.86, "early_reclaim_pct": 80.6, "matched_signals": 35, "recovery_stability_score": 0.682, "success_rate": 97.14, "ticker": "CTSH", "timing_score": 0.514, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:05:04.072258-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "entry_ask": 14.15, "entry_bid": 12.65, "entry_mode": "early", "entry_option_price": 13.4, "hypothetical_budget": 36158.05, "hypothetical_contracts": 26, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 523.0, "option_spread_pct": 11.19, "option_volume": 24.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.593, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.859, "early_reclaim_pct": 70.2, "matched_signals": 38, "recovery_stability_score": 0.593, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-15T10:00:04.052597-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                  {"contract_symbol": "FTNT261016C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "entry_ask": 10.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.525, "hypothetical_budget": 36158.05, "hypothetical_contracts": 37, "matched_signals": 42, "option_liquidity_status": "wide_spread", "option_open_interest": 602.0, "option_spread_pct": 21.52, "option_volume": 98.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.701, "shadow_only": true, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.79, "early_reclaim_pct": 85.8, "matched_signals": 42, "recovery_stability_score": 0.701, "success_rate": 90.48, "ticker": "FTNT", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-15T10:00:04.052597-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "EXC261016C00043000", "fill_price": 0.855, "pnl": -3800.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "EXC"}
2026-09-15T00:00:03.212916-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {'saved': 93}
2026-09-14T15:10:01.099454-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
2026-09-14T15:05:01.081991-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260915102501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260915102501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260915102501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260915102501)

</details>
