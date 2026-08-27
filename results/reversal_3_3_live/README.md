# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 13:00:04 EDT`
Last processed slot: `manage_1300`

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
  ABNB           96.55               29            0.93              1.22        187.55                62.05         0.672          pass              0.674             26.6                           0.355                0.65              0.345                      ok            True                  False
   MAR           96.15               26            0.73              1.84        357.88                33.81         0.565          pass              0.720             52.4                           0.481                1.20              0.107                      ok            True                  False
  MELI           96.77               31            1.08             14.78       1944.11                48.46         0.557          pass              0.638             14.1                           0.298                5.53              0.921                      ok            True                  False
  SBUX           93.75               16            0.88              0.66        108.21                22.90         0.545          pass              0.604             47.5                           0.452               -0.36             -0.001                      ok            True                  False
  PCAR          100.00               11            1.75              1.58        128.55                19.19         0.539          pass              0.497             12.2                           0.325               -2.87             -0.158                      ok            True                  False
   KDP           84.00               25            0.99              0.22         32.11                31.04         0.533          pass              0.361             33.7                           0.299                2.46              0.462                      ok            True                  False
  IDXX           86.67               15            2.00              7.74        550.12                28.64         0.520          pass              0.269              2.0                           0.158               -4.33             -0.154                      ok            True                  False
  BKNG           92.86               14            2.36              3.45        207.41                36.49         0.513          pass              0.478             18.9                           0.270               -4.40             -0.112                      ok            True                  False
 CMCSA           92.31               13            2.08              0.40         27.03                26.47         0.509          pass              0.421              7.4                           0.159                1.74              0.441                      ok            True                  False
  NFLX           83.33               18            2.07              1.18         80.95                32.24         0.500          pass              0.259             22.1                           0.381                1.96              0.497                      ok            True                  False
  MNST           71.43                7            2.31              0.77         47.48               551.93         1.000          pass              0.158             19.3                           0.381                0.05              0.329                      ok           False                  False
  INSM           88.57               35            1.25              1.09        123.92               110.38         0.773          pass              0.601             42.8                           0.643               -2.77             -0.304 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-27T12:00:04.808984-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:55:06.264052-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:50:05.715223-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:45:05.725743-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:40:06.618041-04:00 early_entry_1140 early_entry_shadow                                 {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.52, "early_entry_score": 0.753, "early_reclaim_pct": 65.9, "entry_ask": 12.8, "entry_bid": 11.8, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 26394.05, "hypothetical_contracts": 21, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 214.0, "option_spread_pct": 8.13, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.681, "shadow_only": true, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.753, "early_reclaim_pct": 65.9, "matched_signals": 31, "recovery_stability_score": 0.681, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T11:35:03.825065-04:00 early_entry_1135 early_entry_shadow                                {"contract_symbol": "MAR261016C00360000", "current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 66.0, "entry_ask": 12.9, "entry_bid": 11.8, "entry_mode": "early", "entry_option_price": 12.35, "hypothetical_budget": 26394.05, "hypothetical_contracts": 21, "matched_signals": 31, "option_liquidity_status": "low_volume", "option_open_interest": 214.0, "option_spread_pct": 8.91, "option_volume": 8.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.662, "shadow_only": true, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.754, "early_reclaim_pct": 66.0, "matched_signals": 31, "recovery_stability_score": 0.662, "success_rate": 93.55, "ticker": "MAR", "timing_score": 0.543, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-27T11:30:03.621859-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:25:01.920993-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:20:04.659575-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-27T11:15:05.953915-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "IDXX261016C00550000", "current_drop_pct": 0.51, "early_entry_score": 0.686, "early_reclaim_pct": 66.4, "entry_ask": 26.7, "entry_bid": 22.7, "entry_mode": "early", "entry_option_price": 24.7, "hypothetical_budget": 26394.05, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 16.19, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.471, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.686, "early_reclaim_pct": 66.4, "matched_signals": 38, "recovery_stability_score": 0.721, "success_rate": 89.47, "ticker": "IDXX", "timing_score": 0.471, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827130004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827130004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827130004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827130004)

</details>
