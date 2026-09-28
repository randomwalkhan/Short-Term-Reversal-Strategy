# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 13:10:05 EDT`
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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           82.35               17            1.66              3.06        261.96                41.90         0.543            pass              0.241             25.8                           0.309               -2.14              0.009                                 ok            True                  False
   STX           88.24               34            0.92              5.91        914.30                54.25         0.521            pass              0.677             81.8                           0.826               12.86              1.895                                 ok            True                   True
  UPRO           92.86               14            1.85              1.97        151.36                32.02         0.518            pass              0.534             37.7                           0.311                2.51              0.560                                 ok            True                  False
  PYPL           86.67               15            1.69              0.65         54.76                60.08         0.514            pass              0.430             55.7                           0.616                0.15              0.077                                 ok            True                  False
   TRI           86.21               29            1.45              1.00         98.56                56.74         0.572            pass              0.476             42.4                           0.279               -7.81             -0.534 downtrend_blocked_slope_and_streak           False                  False
  LRCX           77.14               35            1.08              2.39        314.18                61.39         0.541            pass              0.440             73.1                           0.471               14.13              1.829                                 ok           False                  False
  SHOP           87.23               47            0.04              0.04        142.23                62.03         0.525            pass              0.743             99.0                           0.799                6.20              1.218                                 ok           False                  False
  KLAC           75.61               41            0.36              0.48        187.71                50.67         0.509            pass              0.518             89.2                           0.544               10.73              1.424                                 ok           False                  False
  MPWR           83.33               24            2.23             21.32       1358.29                54.48         0.499 below_threshold              0.358             41.9                           0.237               16.95              2.161                                 ok           False                  False
   KHC           95.65               23            0.32              0.05         23.61                20.56         0.497 below_threshold              0.708             57.2                           0.349               -2.95             -0.486 downtrend_blocked_slope_and_streak           False                  False
  AMAT           85.00               40            1.06              3.60        483.46                51.73         0.493 below_threshold              0.590             69.2                           0.466               13.12              1.723                                 ok           False                  False
  NXPI           84.00               25            1.48              2.46        237.02                39.27         0.493 below_threshold              0.418             53.8                           0.282                5.08              0.657                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-28T12:00:07.024087-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.61, "early_entry_score": 0.741, "early_reclaim_pct": 78.2, "entry_ask": 30.4, "entry_bid": 29.1, "entry_mode": "early", "entry_option_price": 29.75, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 4.37, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.704, "shadow_only": true, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.483, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.741, "early_reclaim_pct": 78.2, "matched_signals": 34, "recovery_stability_score": 0.704, "success_rate": 91.18, "ticker": "ADI", "timing_score": 0.483, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:55:06.078627-04:00 early_entry_1155 early_entry_shadow  {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.67, "early_entry_score": 0.721, "early_reclaim_pct": 76.0, "entry_ask": 30.9, "entry_bid": 29.7, "entry_mode": "early", "entry_option_price": 30.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 3.96, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.676, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.484, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.721, "early_reclaim_pct": 76.0, "matched_signals": 33, "recovery_stability_score": 0.676, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.484, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:50:06.060997-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:45:04.059310-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:40:05.053761-04:00 early_entry_1140 early_entry_shadow      {"contract_symbol": "ADI261120C00380000", "current_drop_pct": 0.74, "early_entry_score": 0.67, "early_reclaim_pct": 73.5, "entry_ask": 30.1, "entry_bid": 28.7, "entry_mode": "early", "entry_option_price": 29.4, "hypothetical_budget": 34999.15, "hypothetical_contracts": 11, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 276.0, "option_spread_pct": 4.76, "option_volume": 29.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 90.0, "ticker": "ADI", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.67, "early_reclaim_pct": 73.5, "matched_signals": 30, "recovery_stability_score": 0.556, "success_rate": 90.0, "ticker": "ADI", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-28T11:35:05.945998-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:30:05.957358-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:25:05.958568-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:20:06.180521-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T11:15:05.555577-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928131005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928131005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928131005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928131005)

</details>
