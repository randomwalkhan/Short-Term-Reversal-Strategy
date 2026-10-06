# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-06 11:40:04 EDT`
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
  DRAM           84.00               25            2.10              0.91         61.28                49.40         0.534            pass              0.280              6.6                           0.111               -5.10             -0.191                                 ok            True                  False
  TMUS           84.62               26            0.84              0.97        164.23                30.04         0.526            pass              0.327             14.8                           0.315                0.52             -0.087                                 ok            True                  False
  ABNB           85.71               28            1.22              1.40        163.47                40.56         0.516            pass              0.400             25.3                           0.340                0.16              0.596                                 ok            True                  False
  MPWR           91.18               34            0.48              4.94       1477.77                53.63         0.580            pass              0.745             76.4                           0.501                6.84              0.827                                 ok           False                  False
  QCOM           90.24               41            0.00              0.00        180.79                57.17         0.575            pass              0.831            100.0                           0.777               -8.82             -1.077 downtrend_blocked_slope_and_streak           False                  False
  INTC           87.50               32            1.86              1.51        115.54                74.54         0.553            pass              0.441             12.9                           0.186               -7.94             -0.762 downtrend_blocked_slope_and_streak           False                  False
  ASML           79.31               29            0.95             12.43       1854.53                40.48         0.536            pass              0.242             20.5                           0.195                5.39              0.778                                 ok           False                  False
    MU           92.68               41            0.10              0.78       1063.63                46.96         0.525            pass              0.872             93.7                           0.436               -3.04             -0.147                                 ok           False                  False
   ADI           92.86               42            0.00              0.01        419.09                32.73         0.491 below_threshold              0.889             99.0                           0.503                7.35              0.918                                 ok           False                  False
  AMAT           81.48               27            2.36              8.97        538.43                48.32         0.487 below_threshold              0.211              3.1                           0.109               12.06              1.562                                 ok           False                  False
  TEAM          100.00               34            1.36              1.87        195.85                55.00         0.486 below_threshold              0.632              7.8                           0.113                2.83              0.113                                 ok           False                  False
  MCHP           93.02               43            0.12              0.07         81.46                36.65         0.482 below_threshold              0.792             65.5                           0.336                7.35              0.824                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       detail
2026-10-06T11:40:04.013409-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:35:06.292757-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:30:02.309961-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:25:01.397676-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:20:06.022807-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:15:04.335360-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:10:04.455783-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:05:05.266345-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:00:04.190693-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "MPWR261120C01480000", "current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "entry_ask": 123.5, "entry_bid": 110.0, "entry_mode": "early", "entry_option_price": 116.75, "hypothetical_budget": 52573.4, "hypothetical_contracts": 4, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 60.0, "option_spread_pct": 11.56, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.589, "shadow_only": true, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.728, "early_reclaim_pct": 70.8, "matched_signals": 34, "recovery_stability_score": 0.589, "success_rate": 91.18, "ticker": "MPWR", "timing_score": 0.574, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-06T10:55:04.412071-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261006114004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261006114004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261006114004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261006114004)

</details>
