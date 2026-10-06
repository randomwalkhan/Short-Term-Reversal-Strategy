# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 11:35:06 EDT`
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

- Cash: `$105,146.80`
- Equity: `$105,146.80`
- Realized PnL: `$95,146.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  MRVL     option         option MRVL261120C00270000     18          2026-10-05         2026-10-06        24.45       33.65 16560.0   37.627812 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           91.18               34            0.52              5.38       1477.59                53.63         0.578            pass              0.739             74.3                           0.543                6.79              0.825                                 ok            True                  False
  DRAM           84.00               25            2.02              0.87         61.30                49.40         0.538            pass              0.290              9.9                           0.149               -5.03             -0.187                                 ok            True                  False
  ABNB           82.61               23            1.37              1.58        163.39                40.56         0.534            pass              0.256             15.5                           0.232                0.00              0.589                                 ok            True                  False
  TMUS           85.71               28            0.67              0.78        164.31                30.04         0.525            pass              0.419             31.5                           0.427                0.69             -0.079                                 ok            True                  False
  INTC           87.50               32            2.07              1.68        115.47                74.54         0.541            pass              0.410              3.2                           0.195               -8.13             -0.772 downtrend_blocked_slope_and_streak           False                  False
  ASML           79.31               29            0.90             11.72       1854.84                40.48         0.539            pass              0.256             25.0                           0.252                5.45              0.780                                 ok           False                  False
    MU           92.68               41            0.02              0.18       1063.88                46.96         0.530            pass              0.887             98.5                           0.465               -2.96             -0.143                                 ok           False                  False
  AMAT           81.48               27            2.35              8.92        538.46                48.32         0.488 below_threshold              0.212              3.6                           0.146               12.08              1.563                                 ok           False                  False
  TEAM          100.00               35            1.24              1.70        195.92                55.00         0.487 below_threshold              0.664             16.1                           0.193                2.95              0.118                                 ok           False                  False
  DXCM          100.00                5            2.70              1.64         86.20                23.46         0.476 below_threshold              0.512             21.4                           0.423               -5.56             -0.374 downtrend_blocked_slope_and_streak           False                  False
  CPRT           68.42               19            1.93              0.37         27.49                34.76         0.473 below_threshold              0.193             28.7                           0.412               -5.85             -0.530 downtrend_blocked_slope_and_streak           False                  False
  LRCX           68.42               19            3.66              8.87        342.00                55.68         0.464 below_threshold              0.106              0.0                           0.223                7.24              1.262                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-10-06T11:35:06.292757-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:30:02.309961-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:25:01.397676-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:20:06.022807-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:15:04.335360-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:10:04.455783-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:05:05.266345-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:00:04.190693-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "MPWR261120C01480000", "current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "entry_ask": 123.5, "entry_bid": 110.0, "entry_mode": "early", "entry_option_price": 116.75, "hypothetical_budget": 52573.4, "hypothetical_contracts": 4, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 60.0, "option_spread_pct": 11.56, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "matched_signals": 34, "recovery_stability_score": 0.589, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-06T10:55:04.412071-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:50:01.197576-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006113506)

</details>
