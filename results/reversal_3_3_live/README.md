# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-06 11:05:05 EDT`
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

- Cash: `$26,504.50`
- Equity: `$26,504.50`
- Realized PnL: `$16,504.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-06)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   KDP     option         option KDP260821C00033000     96          2026-07-02         2026-07-06         1.45       1.305 -1392.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  PAYX          100.00               23            1.05              0.78        106.01                31.56         0.538          pass              0.643             34.1                           0.492                7.12              0.882                  ok            True                  False
  MNST          100.00               16            1.21              0.83         97.25                16.38         0.529          pass              0.549             18.6                           0.387                5.56              0.569                  ok            True                  False
  CTSH           81.08               37            0.69              0.20         41.90                56.76         0.526          pass              0.481             73.3                           0.674               -4.58             -0.324                  ok            True                  False
   ADP           90.00               20            1.28              2.16        241.34                30.79         0.519          pass              0.494             36.3                           0.553                9.51              1.105                  ok            True                  False
  BKNG           85.19               27            1.26              1.63        183.86                41.33         0.512          pass              0.387             28.0                           0.359                6.09              0.825                  ok            True                  False
  VRTX           93.33               15            1.53              5.66        525.61                28.87         0.509          pass              0.585             48.5                           0.672               15.13              1.372                  ok            True                  False
   XEL          100.00                3            1.73              0.99         81.53                20.81         0.600          pass              0.472              4.1                           0.153                4.04              0.277                  ok           False                  False
   PEP           80.00                5            1.56              1.57        143.55                27.18         0.591          pass              0.121             20.8                           0.452               -0.04             -0.025                  ok           False                  False
   EXC           87.50                8            1.44              0.48         47.67                22.14         0.584          pass              0.282              8.0                           0.216                3.01              0.261                  ok           False                  False
   KHC          100.00                2            2.84              0.50         25.15                36.79         0.580          pass              0.513             18.2                           0.389                8.02              1.237                  ok           False                  False
   AEP           71.43                7            1.36              1.32        137.94                19.65         0.560          pass              0.130             24.7                           0.184                6.99              0.587                  ok           False                  False
  PYPL           75.00                8            1.94              0.62         45.21                34.53         0.544          pass              0.198             47.9                           0.658                4.89              0.699                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-07-06T11:05:05.715043-04:00 early_entry_1105 early_entry_shadow     {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.64, "shadow_only": true, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "top_candidates": [{"current_drop_pct": 0.95, "early_entry_score": 0.766, "early_reclaim_pct": 66.2, "matched_signals": 33, "recovery_stability_score": 0.64, "success_rate": 93.94, "ticker": "ROP", "timing_score": 0.42, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T11:00:02.142551-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "ROP260821C00360000", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "entry_ask": 21.5, "entry_bid": 15.7, "entry_mode": "early", "entry_option_price": 18.6, "hypothetical_budget": 13252.25, "hypothetical_contracts": 7, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 59.0, "option_spread_pct": 31.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.602, "shadow_only": true, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 63.5, "matched_signals": 32, "recovery_stability_score": 0.602, "success_rate": 93.75, "ticker": "ROP", "timing_score": 0.422, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-06T10:55:01.329795-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:50:01.323991-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:45:01.326292-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:40:05.174623-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:35:05.425058-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:30:05.295059-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:25:05.297833-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-06T10:20:05.672223-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260706110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260706110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260706110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260706110505)

</details>
