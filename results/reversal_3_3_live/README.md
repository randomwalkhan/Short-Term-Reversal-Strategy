# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-16 10:20:02 EDT`
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

- Cash: `$68,746.10`
- Equity: `$68,746.10`
- Realized PnL: `$58,746.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-16)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TMUS     option         option TMUS261016C00185000     70          2026-09-15         2026-09-16          5.1        4.59 -3570.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           83.33               30            2.41              2.18        128.66               105.80         0.632          pass              0.313              9.0                           0.093                1.28             -0.122                                 ok            True                  False
  PYPL           94.12               34            0.52              0.20         53.73                57.87         0.623          pass              0.791             64.1                           0.625                2.41             -0.110                                 ok            True                   True
  CTSH          100.00               33            0.85              0.38         63.12                43.25         0.530          pass              0.789             60.9                           0.570               -1.03             -0.170                                 ok            True                   True
  CRWD           88.89               45            0.39              0.67        242.20               100.47         0.686          pass              0.767             87.2                           0.814               12.31              1.354                                 ok           False                  False
    ZS           97.62               42            0.28              0.39        193.72                82.15         0.629          pass              0.937             91.5                           0.737                8.39              0.944                                 ok           False                  False
  AMGN           91.18               34            0.14              0.36        375.50                45.15         0.575          pass              0.686             56.7                           0.329              -14.38             -2.011 downtrend_blocked_slope_and_streak           False                  False
  ADBE           96.15               26            1.30              2.34        256.76                48.65         0.548          pass              0.700             46.0                           0.641              -11.07             -1.161 downtrend_blocked_slope_and_streak           False                  False
  ADSK           85.71               28            1.44              2.29        225.52                56.46         0.546          pass              0.415             29.2                           0.234               -9.88             -0.859           downtrend_blocked_streak           False                  False
   CEG           90.48               21            1.19              2.16        258.97                43.08         0.535          pass              0.412              1.9                           0.136               -8.38             -1.130 downtrend_blocked_slope_and_streak           False                  False
   PEP           89.47               19            0.30              0.29        135.38                15.04         0.531          pass              0.479             37.9                           0.273               -2.33             -0.274            downtrend_blocked_slope           False                  False
   WMT           85.71               42            0.11              0.08        108.05                40.04         0.528          pass              0.636             76.9                           0.628                1.94              0.169                                 ok           False                  False
  WDAY           93.75               32            1.05              1.41        190.07                46.67         0.524          pass              0.727             53.8                           0.508               -4.90             -0.693 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-09-16T10:20:02.652094-04:00 early_entry_1020 early_entry_shadow                     {"contract_symbol": "PYPL261016C00055000", "current_drop_pct": 0.52, "early_entry_score": 0.791, "early_reclaim_pct": 64.1, "entry_ask": 1.6, "entry_bid": 1.51, "entry_mode": "early", "entry_option_price": 1.555, "hypothetical_budget": 34373.05, "hypothetical_contracts": 221, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 7856.0, "option_spread_pct": 5.79, "option_volume": 222.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.625, "shadow_only": true, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.623, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.791, "early_reclaim_pct": 64.1, "matched_signals": 34, "recovery_stability_score": 0.625, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.623, "trend_health_status": "ok"}, {"current_drop_pct": 0.85, "early_entry_score": 0.789, "early_reclaim_pct": 60.9, "matched_signals": 33, "recovery_stability_score": 0.57, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.53, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T10:15:04.680208-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 0.55, "early_entry_score": 0.873, "early_reclaim_pct": 78.2, "entry_ask": 14.1, "entry_bid": 11.8, "entry_mode": "early", "entry_option_price": 12.95, "hypothetical_budget": 34373.05, "hypothetical_contracts": 26, "matched_signals": 37, "option_liquidity_status": "wide_spread", "option_open_interest": 7403.0, "option_spread_pct": 17.76, "option_volume": 100.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.618, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.589, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.873, "early_reclaim_pct": 78.2, "matched_signals": 37, "recovery_stability_score": 0.618, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.589, "trend_health_status": "ok"}, {"current_drop_pct": 0.84, "early_entry_score": 0.873, "early_reclaim_pct": 74.8, "matched_signals": 38, "recovery_stability_score": 0.627, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-16T10:10:01.638899-04:00 early_entry_1010 early_entry_shadow                        {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 1.06, "early_entry_score": 0.833, "early_reclaim_pct": 68.0, "entry_ask": 15.2, "entry_bid": 13.25, "entry_mode": "early", "entry_option_price": 14.225, "hypothetical_budget": 34373.05, "hypothetical_contracts": 24, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 540.0, "option_spread_pct": 13.71, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.616, "shadow_only": true, "success_rate": 97.14, "ticker": "ZS", "timing_score": 0.625, "top_candidates": [{"current_drop_pct": 1.06, "early_entry_score": 0.833, "early_reclaim_pct": 68.0, "matched_signals": 35, "recovery_stability_score": 0.616, "success_rate": 97.14, "ticker": "ZS", "timing_score": 0.625, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.736, "early_reclaim_pct": 81.4, "matched_signals": 43, "recovery_stability_score": 0.772, "success_rate": 88.37, "ticker": "CRWD", "timing_score": 0.687, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T10:05:01.503854-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T10:00:05.613145-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                 {"contract_symbol": "CTSH261016C00062500", "current_drop_pct": 0.64, "early_entry_score": 0.832, "early_reclaim_pct": 70.7, "entry_ask": 3.5, "entry_bid": 2.75, "entry_mode": "early", "entry_option_price": 3.125, "hypothetical_budget": 34373.05, "hypothetical_contracts": 109, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 792.0, "option_spread_pct": 24.0, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.729, "shadow_only": true, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.531, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.832, "early_reclaim_pct": 70.7, "matched_signals": 35, "recovery_stability_score": 0.729, "success_rate": 100.0, "ticker": "CTSH", "timing_score": 0.531, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-16T09:50:01.541163-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"asset_type": "option", "contract_symbol": "TMUS261016C00185000", "fill_price": 4.59, "pnl": -3570.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TMUS"}
2026-09-16T00:00:06.550315-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 92, 'empty': 1}
2026-09-15T15:10:04.348747-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T15:05:02.260320-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-09-15T15:00:05.246314-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260916102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260916102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260916102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260916102002)

</details>
