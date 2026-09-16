# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-16 11:30:01 EDT`
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
  PYPL           93.55               31            0.67              0.25         53.70                57.87         0.631          pass              0.726             53.8                           0.510                2.26             -0.117                                 ok            True                  False
  MSTR           82.14               28            2.90              2.63        128.47               105.80         0.612          pass              0.238              0.0                           0.253                0.77             -0.145                                 ok            True                  False
  CTSH          100.00               29            1.23              0.55         63.05                43.25         0.532          pass              0.710             43.5                           0.448               -1.40             -0.187                                 ok            True                  False
   TRI           94.12               34            0.50              0.36        102.46                58.06         0.602          pass              0.804             69.0                           0.629               -3.99             -0.626 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               40            0.14              0.19        189.73                62.94         0.594          pass              0.942             94.3                           0.838                1.34              0.018                                 ok           False                  False
  AMGN           91.18               34            0.13              0.34        375.51                45.15         0.576          pass              0.695             59.7                           0.450              -14.37             -2.011 downtrend_blocked_slope_and_streak           False                  False
  CHTR           88.89               27            1.99              1.97        140.36                64.00         0.534          pass              0.423              6.3                           0.156               -5.34             -0.938            downtrend_blocked_slope           False                  False
   PEP           89.47               19            0.27              0.26        135.39                15.04         0.533          pass              0.498             43.9                           0.420               -2.30             -0.272            downtrend_blocked_slope           False                  False
  ADSK           84.00               25            1.98              3.14        225.16                56.46         0.525          pass              0.332             24.3                           0.483              -10.36             -0.883 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           95.83               24            1.09              0.19         24.34                34.84         0.523          pass              0.597             17.2                           0.344               -8.16             -1.045 downtrend_blocked_slope_and_streak           False                  False
  WDAY           93.55               31            1.26              1.68        189.95                46.67         0.518          pass              0.688             44.9                           0.657               -5.09             -0.702 downtrend_blocked_slope_and_streak           False                  False
   CEG           92.59               27            0.87              1.59        259.21                43.08         0.514          pass              0.669             56.2                           0.417               -8.09             -1.115 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-16T11:30:01.814450-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:25:01.704586-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "entry_ask": 15.05, "entry_bid": 14.5, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 3.72, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.849, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "matched_signals": 31, "recovery_stability_score": 0.849, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:20:01.844256-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "entry_ask": 14.55, "entry_bid": 14.1, "entry_mode": "early", "entry_option_price": 14.325, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 3.14, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "matched_signals": 31, "recovery_stability_score": 0.827, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:15:01.730377-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:10:01.521161-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "entry_ask": 14.2, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.05, "hypothetical_budget": 34373.05, "hypothetical_contracts": 24, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 2.14, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.782, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "matched_signals": 31, "recovery_stability_score": 0.782, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 60.9, "matched_signals": 34, "recovery_stability_score": 0.592, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.621, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:05:04.610676-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:00:02.599495-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                               {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.72, "early_entry_score": 0.885, "early_reclaim_pct": 78.4, "entry_ask": 15.1, "entry_bid": 13.65, "entry_mode": "early", "entry_option_price": 14.375, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 540.0, "option_spread_pct": 10.09, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.627, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.885, "early_reclaim_pct": 78.4, "matched_signals": 38, "recovery_stability_score": 0.634, "success_rate": 97.37, "ticker": "ZS", "timing_score": 0.627, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T10:55:04.710670-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                {"contract_symbol": "ZS261016C00190000", "current_drop_pct": 0.71, "early_entry_score": 0.891, "early_reclaim_pct": 78.7, "entry_ask": 14.55, "entry_bid": 13.6, "entry_mode": "early", "entry_option_price": 14.075, "hypothetical_budget": 34373.05, "hypothetical_contracts": 24, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 540.0, "option_spread_pct": 6.75, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.622, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.891, "early_reclaim_pct": 78.7, "matched_signals": 39, "recovery_stability_score": 0.661, "success_rate": 97.44, "ticker": "ZS", "timing_score": 0.622, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T10:50:06.428854-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T10:46:30.761311-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                             {"contract_symbol": "TEAM261016C00190000", "current_drop_pct": 0.51, "early_entry_score": 0.878, "early_reclaim_pct": 79.8, "entry_ask": 13.1, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.5, "hypothetical_budget": 34373.05, "hypothetical_contracts": 27, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 7403.0, "option_spread_pct": 9.6, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.586, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.59, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.878, "early_reclaim_pct": 79.8, "matched_signals": 37, "recovery_stability_score": 0.586, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.59, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260916113001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260916113001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260916113001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260916113001)

</details>
