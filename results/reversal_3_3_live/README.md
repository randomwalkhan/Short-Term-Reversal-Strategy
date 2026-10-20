# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 11:20:08 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   ADP     option         option ADP261120C00290000     70          2026-10-19         2026-10-20          9.3        11.2 13300.0   20.430108 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SNPS           76.19               21            1.41              4.48        452.66                54.29         0.580            pass              0.289             52.6                           0.515              -11.28             -1.354 downtrend_blocked_slope_and_streak           False                  False
   CEG           85.71               35            0.63              1.15        262.70                59.49         0.554            pass              0.583             69.6                           0.541              -12.93             -1.427 downtrend_blocked_slope_and_streak           False                  False
  META           81.82               11            1.82              8.97        701.60                40.24         0.541            pass              0.252             47.5                           0.570               -6.26             -0.380 downtrend_blocked_slope_and_streak           False                  False
  DRAM           80.00               35            0.47              0.16         48.26                49.05         0.492 below_threshold              0.483             88.9                           0.622              -19.18             -2.658 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.30               27            0.50              1.86        532.72                21.83         0.489 below_threshold              0.759             65.5                           0.589                0.30              0.075                                 ok           False                  False
   LIN           70.59               17            0.99              3.47        501.95                13.47         0.479 below_threshold              0.148             17.7                           0.233                1.74              0.360                                 ok           False                  False
  CDNS           79.31               29            1.13              2.57        324.76                37.22         0.477 below_threshold              0.354             59.8                           0.362              -10.39             -1.265 downtrend_blocked_slope_and_streak           False                  False
 GOOGL           86.21               29            0.62              1.50        343.54                22.41         0.459 below_threshold              0.436             32.5                           0.282               -1.62             -0.227                                 ok           False                  False
  CRWD           89.74               39            0.72              1.15        227.61                50.50         0.453 below_threshold              0.725             75.6                           0.514              -18.79             -2.157 downtrend_blocked_slope_and_streak           False                  False
  ASML           78.12               32            0.50              5.73       1644.66                29.62         0.452 below_threshold              0.419             75.6                           0.492              -10.64             -1.233            downtrend_blocked_slope           False                  False
  AAPL           80.00               25            0.70              1.67        342.22                16.04         0.452 below_threshold              0.324             59.7                           0.362                2.07              0.219                                 ok           False                  False
  NVDA           82.86               35            0.04              0.06        217.06                23.81         0.451 below_threshold              0.582             97.9                           0.533               -9.30             -1.089 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-20T11:20:08.949800-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:15:05.273794-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:10:09.912817-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:05:06.503440-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T11:00:06.812644-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:55:08.897321-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:50:04.954872-04:00 early_entry_1050 early_entry_shadow  {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "entry_ask": 2.85, "entry_bid": 2.55, "entry_mode": "early", "entry_option_price": 2.7, "hypothetical_budget": 72415.9, "hypothetical_contracts": 268, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 11.11, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.604, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.765, "early_reclaim_pct": 63.6, "matched_signals": 40, "recovery_stability_score": 0.604, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:45:05.488379-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:40:06.473835-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "entry_ask": 2.85, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.675, "hypothetical_budget": 72415.9, "hypothetical_contracts": 270, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 13.08, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "matched_signals": 40, "recovery_stability_score": 0.634, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:30:06.843333-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020112008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020112008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020112008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020112008)

</details>
