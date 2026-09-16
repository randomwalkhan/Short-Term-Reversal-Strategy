# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-16 14:10:05 EDT`
Last processed slot: `manage_1400`

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
  PYPL           90.48               21            1.12              0.42         53.63                57.87         0.656          pass              0.524             35.1                           0.320                1.80             -0.138                                 ok            True                  False
  MSTR           83.87               31            2.05              1.86        128.80               105.80         0.638          pass              0.446             46.5                           0.546                1.65             -0.105                                 ok            True                  False
  CTSH          100.00               32            0.93              0.41         63.10                43.25         0.531          pass              0.772             57.2                           0.513               -1.10             -0.174                                 ok            True                  False
   ADP           96.00               25            0.56              1.09        276.06                24.27         0.531          pass              0.751             65.9                           0.381               -2.38             -0.250                                 ok            True                  False
  CRWD           88.89               45            0.36              0.62        242.23               100.47         0.679          pass              0.770             88.2                           0.660               12.34              1.355                                 ok           False                  False
   TRI           93.94               33            0.69              0.50        102.40                58.06         0.596          pass              0.755             56.7                           0.330               -4.18             -0.635 downtrend_blocked_slope_and_streak           False                  False
  WDAY           94.12               34            0.63              0.84        190.31                46.67         0.539          pass              0.808             72.4                           0.529               -4.49             -0.673 downtrend_blocked_slope_and_streak           False                  False
  ADSK           85.19               27            1.60              2.53        225.41                56.46         0.537          pass              0.422             38.9                           0.527              -10.02             -0.866 downtrend_blocked_slope_and_streak           False                  False
   PEP           89.47               19            0.30              0.28        135.38                15.04         0.531          pass              0.484             39.4                           0.352               -2.32             -0.273            downtrend_blocked_slope           False                  False
 CMCSA           94.44               18            1.64              0.28         24.30                34.84         0.521          pass              0.530             13.0                           0.231               -8.67             -1.071 downtrend_blocked_slope_and_streak           False                  False
  CHTR           85.00               20            2.69              2.66        140.06                64.00         0.520          pass              0.306             17.9                           0.212               -6.01             -0.970            downtrend_blocked_slope           False                  False
  FTNT           92.00               50            0.08              0.10        172.33                59.28         0.516          pass              0.861             96.4                           0.586                6.41              0.916                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-16T11:50:05.471536-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "entry_ask": 14.9, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.675, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 3.07, "option_volume": 90.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.719, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "matched_signals": 31, "recovery_stability_score": 0.719, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:45:04.644986-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:40:01.643996-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:35:01.673280-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:30:01.814450-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:25:01.704586-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "entry_ask": 15.05, "entry_bid": 14.5, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 3.72, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.849, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "matched_signals": 31, "recovery_stability_score": 0.849, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:20:01.844256-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                         {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "entry_ask": 14.55, "entry_bid": 14.1, "entry_mode": "early", "entry_option_price": 14.325, "hypothetical_budget": 34373.05, "hypothetical_contracts": 23, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 3.14, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.862, "early_reclaim_pct": 97.8, "matched_signals": 31, "recovery_stability_score": 0.827, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.288, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:15:01.730377-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-16T11:10:01.521161-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "MSFT261016C00495000", "current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "entry_ask": 14.2, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.05, "hypothetical_budget": 34373.05, "hypothetical_contracts": 24, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 5144.0, "option_spread_pct": 2.14, "option_volume": 80.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.782, "shadow_only": true, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.863, "early_reclaim_pct": 97.9, "matched_signals": 31, "recovery_stability_score": 0.782, "success_rate": 96.77, "ticker": "MSFT", "timing_score": 0.289, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 60.9, "matched_signals": 34, "recovery_stability_score": 0.592, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.621, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-16T11:05:04.610676-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260916141005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260916141005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260916141005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260916141005)

</details>
