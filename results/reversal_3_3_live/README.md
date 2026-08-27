# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 11:40:06 EDT`
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

- Cash: `$52,788.10`
- Equity: `$52,788.10`
- Realized PnL: `$42,788.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-27)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MNST     option         option MNST261016C00048000    140          2026-08-26         2026-08-27         1.95       1.755 -2730.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  ABNB           93.75               32            0.66              0.86        187.70                62.05         0.666          pass              0.712             44.1                           0.467                0.92              0.358                      ok            True                  False
  MRVL           80.00               35            0.97              1.66        244.40                86.13         0.582          pass              0.291             22.1                           0.193                9.25              0.939                      ok            True                  False
  MELI           97.22               36            0.65              8.84       1946.65                48.46         0.557          pass              0.708             26.4                           0.297                5.99              0.941                      ok            True                  False
   MAR           93.55               31            0.52              1.32        358.11                33.81         0.543          pass              0.753             65.9                           0.681                1.41              0.117                      ok            True                   True
  PCAR          100.00               13            1.62              1.46        128.60                19.19         0.537          pass              0.504             10.3                           0.362               -2.74             -0.152                      ok            True                  False
  ALNY           82.35               17            2.56              4.28        237.17               130.65         0.529          pass              0.255             30.8                           0.235                2.54              0.490                      ok            True                  False
   LIN           81.82               22            1.04              3.56        488.80                26.56         0.523          pass              0.317             45.5                           0.600                1.47              0.251                      ok            True                  False
  BKNG           95.83               24            1.56              2.28        207.91                36.49         0.508          pass              0.651             35.7                           0.366               -3.61             -0.075                      ok            True                  False
 CMCSA           89.47               19            1.38              0.26         27.09                26.47         0.504          pass              0.479             38.5                           0.663                2.46              0.473                      ok            True                  False
  NFLX           83.33               18            2.04              1.16         80.96                32.24         0.503          pass              0.263             23.5                           0.387                1.99              0.499                      ok            True                  False
  MNST           75.00                8            2.03              0.68         47.52               551.93         1.000          pass              0.188             29.2                           0.557                0.34              0.343                      ok           False                  False
  INSM           88.89               27            1.57              1.36        123.81               110.38         0.795          pass              0.515             28.3                           0.303               -3.08             -0.318 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-27T11:40:06.618041-04:00 early_entry_1140 early_entry_shadow                                  {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.52, "early_entry_score": 0.753, "early_reclaim_pct": 65.9, "entry_ask": 12.8, "entry_bid": 11.8, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 26394.05, "hypothetical_contracts": 21, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 214.0, "option_spread_pct": 8.13, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.681, "shadow_only": true, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.753, "early_reclaim_pct": 65.9, "matched_signals": 31, "recovery_stability_score": 0.681, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T11:35:03.825065-04:00 early_entry_1135 early_entry_shadow                                 {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 66.0, "entry_ask": 12.9, "entry_bid": 11.8, "entry_mode": "early", "entry_option_price": 12.35, "hypothetical_budget": 26394.05, "hypothetical_contracts": 21, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 214.0, "option_spread_pct": 8.91, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 66.0, "matched_signals": 31, "recovery_stability_score": 0.662, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T11:30:03.621859-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:25:01.920993-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:20:04.659575-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:15:05.953915-04:00 early_entry_1115 early_entry_shadow  {"contract_symbol": "IDXX261016C00550000", "current_drop_pct": 0.51, "early_entry_score": 0.686, "early_reclaim_pct": 66.4, "entry_ask": 26.7, "entry_bid": 22.7, "entry_mode": "early", "entry_option_price": 24.7, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 16.19, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.686, "early_reclaim_pct": 66.4, "matched_signals": 38, "recovery_stability_score": 0.721, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T11:10:04.793952-04:00 early_entry_1110 early_entry_shadow                                                 {"contract_symbol": "INTU261016C00350000", "current_drop_pct": 0.64, "early_entry_score": 0.695, "early_reclaim_pct": 79.8, "entry_ask": 21.5, "entry_bid": 20.7, "entry_mode": "early", "entry_option_price": 21.1, "hypothetical_budget": 26394.05, "hypothetical_contracts": 12, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 792.0, "option_spread_pct": 3.79, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.575, "shadow_only": true, "success_rate": 88.89, "ticker": "INTU", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.695, "early_reclaim_pct": 79.8, "matched_signals": 36, "recovery_stability_score": 0.575, "success_rate": 88.89, "ticker": "INTU", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-27T11:05:01.915991-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:00:05.720063-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T10:55:01.790895-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "IDXX261016C00550000", "current_drop_pct": 0.56, "early_entry_score": 0.675, "early_reclaim_pct": 63.0, "entry_ask": 26.8, "entry_bid": 22.7, "entry_mode": "early", "entry_option_price": 24.75, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 16.57, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.468, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.675, "early_reclaim_pct": 63.0, "matched_signals": 38, "recovery_stability_score": 0.632, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.468, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827114006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827114006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827114006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827114006)

</details>
