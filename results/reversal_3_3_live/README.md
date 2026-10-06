# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 10:55:04 EDT`
Last processed slot: `manage_1100`

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
  DRAM           84.00               25            1.66              0.72         61.36                49.40         0.559            pass              0.341             26.0                           0.416               -4.68             -0.171                                 ok            True                  False
  ASML           81.25               32            0.55              7.13       1856.80                40.48         0.544            pass              0.397             54.4                           0.520                5.82              0.797                                 ok            True                  False
  TMUS           84.62               26            0.84              0.97        164.22                30.04         0.526            pass              0.299              5.5                           0.130                0.52             -0.087                                 ok            True                  False
  ABNB           85.71               28            1.13              1.30        163.51                40.56         0.523            pass              0.396             23.7                           0.311                0.25              0.600                                 ok            True                  False
  META           85.71               42            0.09              0.48        741.70                55.50         0.582            pass              0.671             86.9                           0.608                0.63             -0.213                                 ok           False                  False
  MPWR           92.11               38            0.36              3.77       1478.27                53.63         0.564            pass              0.812             82.0                           0.737                6.96              0.832                                 ok           False                  False
  QCOM           90.24               41            0.21              0.27        180.67                57.17         0.562            pass              0.750             73.6                           0.514               -9.01             -1.086 downtrend_blocked_slope_and_streak           False                  False
  INTC           88.89               36            1.33              1.08        115.73                74.54         0.562            pass              0.564             32.5                           0.306               -7.44             -0.737 downtrend_blocked_slope_and_streak           False                  False
  AMGN           75.00               12            1.46              4.12        401.22                46.96         0.515            pass              0.112             15.6                           0.233               -3.20             -0.221           downtrend_blocked_streak           False                  False
  GILD           92.86               14            1.20              1.21        144.11                20.39         0.504            pass              0.464             14.6                           0.225               -6.40             -0.619 downtrend_blocked_slope_and_streak           False                  False
  AMAT           82.76               29            1.95              7.40        539.11                48.32         0.499 below_threshold              0.311             20.1                           0.342               12.54              1.582                                 ok           False                  False
  TEAM          100.00               39            0.69              0.95        196.24                55.00         0.497 below_threshold              0.750             35.5                           0.266                3.52              0.143                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-06T10:55:04.412071-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:50:01.197576-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:45:05.848219-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:40:06.064214-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:35:04.353804-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:30:05.477700-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:25:05.769883-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "WDAY261120C00190000", "current_drop_pct": 0.67, "early_entry_score": 0.762, "early_reclaim_pct": 73.9, "entry_ask": 13.6, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.75, "hypothetical_budget": 52573.4, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 248.0, "option_spread_pct": 13.33, "option_volume": 143.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.615, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.432, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.762, "early_reclaim_pct": 73.9, "matched_signals": 37, "recovery_stability_score": 0.615, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.432, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-06T10:20:05.384079-04:00 early_entry_1020 early_entry_shadow        {"contract_symbol": "WDAY261120C00190000", "current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "entry_ask": 13.1, "entry_bid": 11.9, "entry_mode": "early", "entry_option_price": 12.5, "hypothetical_budget": 52573.4, "hypothetical_contracts": 42, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 248.0, "option_spread_pct": 9.6, "option_volume": 143.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.723, "shadow_only": true, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.758, "early_reclaim_pct": 72.7, "matched_signals": 37, "recovery_stability_score": 0.723, "success_rate": 91.89, "ticker": "WDAY", "timing_score": 0.43, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-06T10:15:05.337195-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:10:04.391057-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006105504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006105504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006105504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006105504)

</details>
