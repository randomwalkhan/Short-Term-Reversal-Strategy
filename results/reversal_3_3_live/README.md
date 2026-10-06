# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 11:20:06 EDT`
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
  DRAM           84.00               25            1.85              0.80         61.33                49.40         0.548            pass              0.315             17.7                           0.305               -4.86             -0.179                                 ok            True                  False
  ASML           80.65               31            0.64              8.32       1856.30                40.48         0.544            pass              0.352             46.8                           0.509                5.73              0.792                                 ok            True                  False
  TMUS           85.19               27            0.73              0.85        164.28                30.04         0.527            pass              0.380             25.3                           0.320                0.63             -0.082                                 ok            True                  False
  ABNB           85.71               28            1.18              1.36        163.49                40.56         0.518            pass              0.406             27.3                           0.343                0.20              0.598                                 ok            True                  False
  META           85.71               42            0.01              0.05        741.88                55.50         0.586            pass              0.707             98.7                           0.616                0.71             -0.209                                 ok           False                  False
  QCOM           90.24               41            0.11              0.13        180.73                57.17         0.569            pass              0.791             87.0                           0.741               -8.91             -1.081 downtrend_blocked_slope_and_streak           False                  False
  MPWR           92.50               40            0.23              2.42       1478.85                53.63         0.559            pass              0.855             88.5                           0.693                7.10              0.838                                 ok           False                  False
  INTC           88.57               35            1.50              1.22        115.67                74.54         0.558            pass              0.522             23.7                           0.346               -7.60             -0.745 downtrend_blocked_slope_and_streak           False                  False
  LRCX           75.00               24            2.80              6.78        342.89                55.68         0.489 below_threshold              0.203             20.3                           0.428                8.20              1.302                                 ok           False                  False
  TEAM          100.00               36            1.15              1.59        195.97                55.00         0.487 below_threshold              0.663             13.7                           0.238                3.04              0.122                                 ok           False                  False
  MELI           78.38               37            0.74              9.63       1856.48                43.88         0.480 below_threshold              0.393             54.9                           0.355                1.11              0.018                                 ok           False                  False
  DXCM          100.00                4            2.76              1.68         86.18                23.46         0.479 below_threshold              0.507             19.7                           0.358               -5.62             -0.376 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-10-06T11:20:06.022807-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:15:04.335360-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:10:04.455783-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:05:05.266345-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:00:04.190693-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "MPWR261120C01480000", "current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "entry_ask": 123.5, "entry_bid": 110.0, "entry_mode": "early", "entry_option_price": 116.75, "hypothetical_budget": 52573.4, "hypothetical_contracts": 4, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 60.0, "option_spread_pct": 11.56, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "matched_signals": 34, "recovery_stability_score": 0.589, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-06T10:55:04.412071-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:50:01.197576-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:45:05.848219-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:40:06.064214-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T10:35:04.353804-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006112006)

</details>
