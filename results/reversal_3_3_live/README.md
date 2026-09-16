# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-16 12:15:01 EDT`
Last processed slot: `manual`

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
  PYPL           92.31               26            0.94              0.35         53.66                57.87         0.642          pass              0.605             35.3                           0.292                1.98             -0.129                                 ok            True                  False
  MSTR           82.14               28            2.82              2.56        128.50               105.80         0.613          pass              0.286             15.9                           0.270                0.86             -0.141                                 ok            True                  False
  FTNT           90.48               42            0.60              0.72        172.06                59.28         0.532          pass              0.752             73.2                           0.342                5.86              0.892                                 ok            True                  False
  CTSH          100.00               28            1.34              0.59         63.03                43.25         0.531          pass              0.688             38.4                           0.385               -1.51             -0.192                                 ok            True                  False
   TRI           94.44               36            0.25              0.18        102.53                58.06         0.605          pass              0.871             84.1                           0.708               -3.76             -0.615           downtrend_blocked_streak           False                  False
  TEAM          100.00               37            0.46              0.61        189.55                62.94         0.593          pass              0.885             81.8                           0.618                1.02              0.003                                 ok           False                  False
   ADP           96.43               28            0.35              0.68        276.24                24.27         0.527          pass              0.809             78.9                           0.414               -2.17             -0.240                                 ok           False                  False
   PEP           90.48               21            0.20              0.19        135.42                15.04         0.527          pass              0.583             59.1                           0.505               -2.23             -0.269            downtrend_blocked_slope           False                  False
  TMUS           94.12               17            1.21              1.53        179.82                25.85         0.526          pass              0.489              4.4                           0.213               -2.12             -0.323            downtrend_blocked_slope           False                  False
  ADSK           81.82               22            2.25              3.56        224.97                56.46         0.524          pass              0.223             14.0                           0.238              -10.61             -0.896 downtrend_blocked_slope_and_streak           False                  False
  WDAY           93.75               32            1.07              1.42        190.06                46.67         0.523          pass              0.725             53.2                           0.658               -4.91             -0.693 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           95.65               23            1.18              0.20         24.33                34.84         0.523          pass              0.570             10.2                           0.202               -8.24             -1.050 downtrend_blocked_slope_and_streak           False                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260916121501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260916121501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260916121501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260916121501)

</details>
