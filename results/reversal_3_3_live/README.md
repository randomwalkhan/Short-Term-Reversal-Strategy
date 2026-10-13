# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-13 12:30:05 EDT`
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

- Cash: `$142,574.30`
- Equity: `$142,574.30`
- Realized PnL: `$132,574.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CTSH     option         option CTSH261120C00060000    160          2026-10-09         2026-10-13         3.65        4.65 16000.0   27.397260 take_profit_day2_hit_at_scan
   CEG     option         option  CEG261120C00290000     31          2026-10-12         2026-10-13        18.65       21.65  9300.0   16.085791 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.75               16            0.66              0.28         61.67                19.83         0.555            pass              0.551             29.6                           0.413                4.40              0.649                                 ok            True                  False
  SHOP           84.62               39            0.65              0.82        178.87                48.43         0.505            pass              0.602             78.4                           0.680               20.09              2.077                                 ok            True                  False
  SNPS           76.47               17            1.77              6.24        499.84                52.43         0.581            pass              0.205             33.3                           0.359               18.91              1.474                                 ok           False                  False
  SOXL           86.21               29            2.07              1.86        127.60                96.52         0.569            pass              0.586             78.8                           0.936              -14.46             -1.765 downtrend_blocked_slope_and_streak           False                  False
  MPWR           91.43               35            0.43              3.93       1317.54                51.39         0.549            pass              0.779             84.1                           0.855               -2.98             -0.288            downtrend_blocked_slope           False                  False
  CSCO           92.31               26            0.42              0.34        115.19                34.19         0.543            pass              0.732             81.0                           0.719                7.81              0.929                                 ok           False                  False
   STX           84.38               32            1.34              7.09        750.21                70.16         0.543            pass              0.571             84.5                           0.912              -18.65             -2.441            downtrend_blocked_slope           False                  False
  UPRO           86.11               36            0.22              0.24        155.36                28.94         0.511            pass              0.609             73.7                           0.773                4.84              0.597                                 ok           False                  False
  ABNB           92.50               40            0.18              0.21        163.41                38.50         0.506            pass              0.769             61.5                           0.418                3.98              0.321                                 ok           False                  False
   WDC           79.41               34            1.36              3.67        385.37                63.46         0.506            pass              0.463             84.0                           0.892              -15.83             -1.960            downtrend_blocked_slope           False                  False
  GILD           87.50                8            1.85              1.95        149.59                19.66         0.503            pass              0.265              4.9                           0.124               -2.40              0.033           downtrend_blocked_streak           False                  False
  MELI           82.22               45            0.14              1.87       1891.64                42.28         0.493 below_threshold              0.569             86.9                           0.563                9.56              1.227                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-13T12:00:04.609468-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "MRVL261120C00260000", "current_drop_pct": 0.68, "early_entry_score": 0.706, "early_reclaim_pct": 89.7, "entry_ask": 20.5, "entry_bid": 20.05, "entry_mode": "early", "entry_option_price": 20.275, "hypothetical_budget": 71287.15, "hypothetical_contracts": 35, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 3428.0, "option_spread_pct": 2.22, "option_volume": 501.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.919, "shadow_only": true, "success_rate": 88.57, "ticker": "MRVL", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.706, "early_reclaim_pct": 89.7, "matched_signals": 35, "recovery_stability_score": 0.919, "success_rate": 88.57, "ticker": "MRVL", "timing_score": 0.415, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.698, "early_reclaim_pct": 61.7, "matched_signals": 41, "recovery_stability_score": 0.623, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.398, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-13T11:55:06.360057-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.67, "early_entry_score": 0.694, "early_reclaim_pct": 60.5, "entry_ask": 29.6, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 20.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.631, "shadow_only": true, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.396, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.694, "early_reclaim_pct": 60.5, "matched_signals": 41, "recovery_stability_score": 0.631, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.396, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:50:05.756508-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:45:05.731226-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:40:02.593298-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                   {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 65.0, "entry_ask": 29.6, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 20.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.738, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 65.0, "matched_signals": 42, "recovery_stability_score": 0.738, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:35:06.355807-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-13T11:30:05.585101-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.64, "early_entry_score": 0.706, "early_reclaim_pct": 62.5, "entry_ask": 29.6, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.9, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 20.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.706, "early_reclaim_pct": 62.5, "matched_signals": 42, "recovery_stability_score": 0.736, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:25:04.515865-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                  {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.65, "early_entry_score": 0.698, "early_reclaim_pct": 61.7, "entry_ask": 29.3, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.75, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.07, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.74, "shadow_only": true, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.398, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.698, "early_reclaim_pct": 61.7, "matched_signals": 41, "recovery_stability_score": 0.74, "success_rate": 90.24, "ticker": "IDXX", "timing_score": 0.398, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:20:02.638996-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                    {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 64.9, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.752, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.714, "early_reclaim_pct": 64.9, "matched_signals": 42, "recovery_stability_score": 0.752, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.395, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-13T11:15:05.483725-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                  {"contract_symbol": "IDXX261120C00520000", "current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 62.8, "entry_ask": 29.4, "entry_bid": 24.2, "entry_mode": "early", "entry_option_price": 26.8, "hypothetical_budget": 71287.15, "hypothetical_contracts": 26, "matched_signals": 42, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 19.4, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.736, "shadow_only": true, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 62.8, "matched_signals": 42, "recovery_stability_score": 0.736, "success_rate": 90.48, "ticker": "IDXX", "timing_score": 0.393, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261013123005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261013123005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261013123005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261013123005)

</details>
