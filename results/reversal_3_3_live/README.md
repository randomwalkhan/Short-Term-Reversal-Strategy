# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 12:15:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ABNB           93.55               31            0.80              1.05        187.62                62.05         0.664            pass              0.664             32.1                           0.295                0.78              0.351                  ok            True                  False
  MRVL           80.56               36            0.71              1.21        244.59                86.13         0.593            pass              0.377             43.3                           0.391                9.54              0.951                  ok            True                  False
  MELI           96.97               33            0.74             10.14       1946.10                48.46         0.569            pass              0.657             15.6                           0.241                5.89              0.937                  ok            True                  False
   MAR           96.15               26            0.73              1.83        357.88                33.81         0.565            pass              0.721             52.5                           0.455                1.20              0.107                  ok            True                  False
  PCAR          100.00               11            1.77              1.60        128.54                19.19         0.540            pass              0.473              4.0                           0.310               -2.89             -0.159                  ok            True                  False
  SBUX           94.74               19            0.72              0.55        108.26                22.90         0.537            pass              0.677             56.9                           0.392               -0.20              0.006                  ok            True                  False
   KDP           84.62               26            0.82              0.19         32.13                31.04         0.537            pass              0.419             45.1                           0.278                2.63              0.470                  ok            True                  False
  ALNY           82.35               17            2.45              4.10        237.24               130.65         0.535            pass              0.264             33.7                           0.383                2.65              0.495                  ok            True                  False
  CSCO           87.18               39            0.51              0.40        112.19                41.57         0.531            pass              0.601             54.4                           0.439               -1.48             -0.108                  ok            True                  False
 CMCSA           93.33               15            1.71              0.33         27.06                26.47         0.517            pass              0.512             23.8                           0.222                2.12              0.458                  ok            True                  False
  BKNG           95.24               21            1.79              2.62        207.77                36.49         0.512            pass              0.603             26.1                           0.250               -3.84             -0.086                  ok            True                  False
  NFLX           81.25               16            2.26              1.29         80.91                32.24         0.500 below_threshold              0.169             15.2                           0.258                1.76              0.488                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827121505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827121505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827121505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827121505)

</details>
