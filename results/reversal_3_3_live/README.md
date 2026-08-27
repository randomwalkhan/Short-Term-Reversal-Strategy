# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-27 12:20:02 EDT`
Last processed slot: `manage_1230`

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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  ABNB           96.55               29            0.90              1.18        187.56                62.05         0.674          pass              0.665             23.5                           0.234                0.68              0.347                  ok            True                  False
  MRVL           80.00               35            0.80              1.37        244.52                86.13         0.593          pass              0.334             36.1                           0.302                9.44              0.947                  ok            True                  False
   MAR           95.45               22            0.92              2.31        357.68                33.81         0.578          pass              0.659             40.3                           0.344                1.01              0.099                  ok            True                  False
  MELI           96.88               32            0.89             12.21       1945.21                48.46         0.566          pass              0.603              0.0                           0.221                5.73              0.930                  ok            True                  False
  SBUX           93.75               16            0.90              0.69        108.20                22.90         0.543          pass              0.599             45.9                           0.318               -0.39             -0.003                  ok            True                  False
  PCAR          100.00               11            1.80              1.63        128.53                19.19         0.538          pass              0.469              2.9                           0.274               -2.92             -0.160                  ok            True                  False
  ALNY           82.35               17            2.53              4.23        237.19               130.65         0.531          pass              0.257             31.6                           0.357                2.57              0.492                  ok            True                  False
   KDP           85.71               28            0.79              0.18         32.13                31.04         0.528          pass              0.467             47.2                           0.291                2.67              0.472                  ok            True                  False
 CMCSA           93.75               16            1.67              0.32         27.06                26.47         0.513          pass              0.534             25.4                           0.219                2.16              0.459                  ok            True                  False
  BKNG           95.24               21            1.85              2.70        207.73                36.49         0.509          pass              0.596             23.9                           0.222               -3.90             -0.088                  ok            True                  False
  IDXX           88.00               25            1.31              5.07        551.27                28.64         0.505          pass              0.406             14.1                           0.224               -3.66             -0.122                  ok            True                  False
  NFLX           81.25               16            2.24              1.28         80.91                32.24         0.501          pass              0.171             15.9                           0.252                1.78              0.489                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260827122002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260827122002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260827122002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260827122002)

</details>
