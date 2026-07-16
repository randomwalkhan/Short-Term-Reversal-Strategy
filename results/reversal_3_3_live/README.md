# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-16 12:45:02 EDT`
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

- Cash: `$29,224.25`
- Equity: `$29,224.25`
- Realized PnL: `$19,224.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   ADI     option         option ADI260821C00380000      4          2026-07-15         2026-07-16        35.15      31.635 -1406.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           81.25               16            4.38             41.50       1334.87                84.79         0.577          pass              0.153              7.2                           0.159               -6.44             -0.050                                 ok            True                  False
  UPRO           88.46               26            1.02              1.05        145.42                41.96         0.561          pass              0.502             37.8                           0.326                1.82              0.271                                 ok            True                  False
  CRWD           81.82               22            1.98              2.87        205.54                56.35         0.523          pass              0.297             38.8                           0.238                4.91              0.673                                 ok            True                  False
  BKNG           86.21               29            0.96              1.22        182.28                43.83         0.520          pass              0.457             37.5                           0.253                1.58             -0.212                                 ok            True                  False
  KLAC           81.82               22            2.50              3.93        222.81               109.33         0.703          pass              0.317             39.6                           0.311              -27.45             -2.141 downtrend_blocked_slope_and_streak           False                  False
  AMAT           84.21               19            2.31              9.39        575.41                98.89         0.689          pass              0.386             48.2                           0.290              -21.71             -1.483 downtrend_blocked_slope_and_streak           False                  False
  ASML           94.12               34            0.43              5.45       1812.94                66.00         0.635          pass              0.849             83.2                           0.500               -9.15             -0.627                                 ok           False                  False
  META           75.00               16            1.80              8.57        677.64                54.55         0.606          pass              0.175             25.0                           0.190                9.16              1.326                                 ok           False                  False
   TXN           85.71                7            3.67              7.73        297.88                65.52         0.589          pass              0.250             12.9                           0.220               -2.66              0.113                                 ok           False                  False
   ADI           76.92               13            2.87              7.85        387.60                55.85         0.577          pass              0.123             14.9                           0.179               -4.39             -0.019                                 ok           False                  False
  LRCX           85.71               14            4.60             10.81        330.80                98.70         0.561          pass              0.253              6.0                           0.117              -26.16             -1.960 downtrend_blocked_slope_and_streak           False                  False
  MSTR           64.29               28            3.76              2.56         96.37               100.18         0.558          pass              0.203              9.0                           0.164                7.91              0.261                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-07-16T12:00:02.316099-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:55:05.282861-04:00 early_entry_1155 early_entry_shadow    {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.62, "early_entry_score": 0.77, "early_reclaim_pct": 80.9, "entry_ask": 16.9, "entry_bid": 16.1, "entry_mode": "early", "entry_option_price": 16.5, "hypothetical_budget": 14612.13, "hypothetical_contracts": 8, "matched_signals": 42, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 4.85, "option_volume": 72.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.646, "shadow_only": true, "success_rate": 90.48, "ticker": "CRWD", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.62, "early_entry_score": 0.77, "early_reclaim_pct": 80.9, "matched_signals": 42, "recovery_stability_score": 0.646, "success_rate": 90.48, "ticker": "CRWD", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:50:01.317315-04:00 early_entry_1150 early_entry_shadow   {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.88, "early_entry_score": 0.734, "early_reclaim_pct": 73.0, "entry_ask": 16.7, "entry_bid": 15.75, "entry_mode": "early", "entry_option_price": 16.225, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 5.86, "option_volume": 72.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.61, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.479, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.734, "early_reclaim_pct": 73.0, "matched_signals": 40, "recovery_stability_score": 0.61, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.479, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:45:04.302520-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:40:01.166933-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:35:06.405776-04:00 early_entry_1135 early_entry_shadow {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.74, "early_entry_score": 0.753, "early_reclaim_pct": 77.2, "entry_ask": 16.1, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 15.75, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 41, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 4.44, "option_volume": 71.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.758, "shadow_only": true, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.753, "early_reclaim_pct": 77.2, "matched_signals": 41, "recovery_stability_score": 0.758, "success_rate": 90.24, "ticker": "CRWD", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:30:06.170773-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T11:25:01.178080-04:00 early_entry_1125 early_entry_shadow    {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 82.5, "entry_ask": 16.0, "entry_bid": 15.6, "entry_mode": "early", "entry_option_price": 15.8, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 43, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 2.53, "option_volume": 62.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.663, "shadow_only": true, "success_rate": 90.7, "ticker": "CRWD", "timing_score": 0.478, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.781, "early_reclaim_pct": 82.5, "matched_signals": 43, "recovery_stability_score": 0.663, "success_rate": 90.7, "ticker": "CRWD", "timing_score": 0.478, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:20:02.331594-04:00 early_entry_1120 early_entry_shadow  {"contract_symbol": "CRWD260821C00205000", "current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "entry_ask": 16.55, "entry_bid": 15.65, "entry_mode": "early", "entry_option_price": 16.1, "hypothetical_budget": 14612.13, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "ok", "option_open_interest": 3361.0, "option_spread_pct": 5.59, "option_volume": 62.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.566, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.746, "early_reclaim_pct": 77.0, "matched_signals": 40, "recovery_stability_score": 0.566, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.487, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-16T11:15:01.227761-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260716124502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260716124502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260716124502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260716124502)

</details>
