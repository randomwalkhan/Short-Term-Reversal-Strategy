# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 10:45:05 EDT`
Last processed slot: `early_entry_1045`

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
  SNPS           80.77               26            1.05              3.33        453.15                54.29         0.576            pass              0.379             64.7                           0.597              -10.96             -1.338 downtrend_blocked_slope_and_streak           False                  False
  META           84.62               13            1.68              8.31        701.88                40.24         0.540            pass              0.351             51.3                           0.711               -6.13             -0.374 downtrend_blocked_slope_and_streak           False                  False
  DRAM           78.95               38            0.05              0.02         48.32                49.05         0.500 below_threshold              0.533             98.8                           0.888              -18.84             -2.639 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.55               29            0.45              1.69        532.79                21.83         0.480 below_threshold              0.780             68.5                           0.710                0.34              0.077                                 ok           False                  False
   LIN           76.19               21            0.78              2.74        502.27                13.47         0.477 below_threshold              0.148              9.0                           0.117                1.95              0.370                                 ok           False                  False
  CDNS           83.78               37            0.58              1.33        325.29                37.22         0.467 below_threshold              0.565             79.3                           0.705               -9.90             -1.240 downtrend_blocked_slope_and_streak           False                  False
  CPRT           64.71               17            2.09              0.40         27.34                31.97         0.456 below_threshold              0.191             32.7                           0.464                0.43              0.199                                 ok           False                  False
  PANW           83.78               37            1.40              3.39        345.50                55.73         0.449 below_threshold              0.507             60.3                           0.573              -18.53             -2.207 downtrend_blocked_slope_and_streak           False                  False
   BKR           93.55               31            0.88              0.34         55.66                25.31         0.447 below_threshold              0.679             44.3                           0.387               -3.17             -0.238                                 ok           False                  False
  CRWD           90.70               43            0.48              0.77        227.77                50.50         0.445 below_threshold              0.781             83.7                           0.633              -18.60             -2.146 downtrend_blocked_slope_and_streak           False                  False
  ASML           82.05               39            0.07              0.78       1646.79                29.62         0.441 below_threshold              0.582             96.7                           0.867              -10.26             -1.213            downtrend_blocked_slope           False                  False
  AMAT           77.78               36            1.17              3.37        411.66                46.44         0.439 below_threshold              0.415             65.8                           0.664              -23.00             -3.025 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-10-20T10:45:05.488379-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:40:06.473835-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "BKR261120C00055000", "current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "entry_ask": 2.85, "entry_bid": 2.5, "entry_mode": "early", "entry_option_price": 2.675, "hypothetical_budget": 72415.9, "hypothetical_contracts": 270, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 584.0, "option_spread_pct": 13.08, "option_volume": 10.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.771, "early_reclaim_pct": 65.3, "matched_signals": 40, "recovery_stability_score": 0.634, "success_rate": 92.5, "ticker": "BKR", "timing_score": 0.413, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-20T10:30:06.843333-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:25:04.152080-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:20:05.290913-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:15:05.434773-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:10:06.028828-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:05:04.298275-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:00:02.343877-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T09:50:06.258363-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "ADP261120C00290000", "fill_price": 11.2, "pnl": 13300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.43, "ticker": "ADP"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020104505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020104505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020104505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020104505)

</details>
