# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 11:10:02 EDT`
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

- Cash: `$32,694.50`
- Equity: `$32,694.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  INTC     option         option INTC260918C00100000     15          2026-08-06         2026-08-07       11.175     10.0575 -1676.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  PYPL           94.29               35            0.51              0.21         59.69                59.52         0.651          pass              0.722             36.5                           0.198                5.92              0.486                                 ok            True                  False
  TMUS           88.57               35            0.52              0.65        179.69                57.01         0.601          pass              0.670             71.5                           0.675               -0.58             -0.132                                 ok            True                   True
   ADP           96.43               28            0.63              1.21        272.99                34.67         0.521          pass              0.808             78.5                           0.356                8.67              0.695                                 ok            True                  False
  INSM           71.43               21            2.24              2.08        131.66               110.04         0.736          pass              0.228             27.2                           0.453               21.19              1.487                                 ok           False                  False
    MU           79.41               34            1.63             10.05        877.16               110.38         0.610          pass              0.396             58.3                           0.663               -5.85              0.176                                 ok           False                  False
  DRAM           77.78               27            3.05              1.10         50.97               108.98         0.585          pass              0.295             41.2                           0.617               -6.26              0.304                                 ok           False                  False
   CSX           92.31               26            0.61              0.22         50.61                29.04         0.542          pass              0.644             51.6                           0.669               -5.34             -0.308 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           90.62               32            0.11              0.05         62.73                30.17         0.537          pass              0.759             91.7                           0.548                3.57              0.184                                 ok           False                  False
   MAR           93.75               32            0.58              1.47        359.04                38.09         0.519          pass              0.730             55.0                           0.478               -4.50             -0.853 downtrend_blocked_slope_and_streak           False                  False
   PEP           81.82               33            0.07              0.06        138.41                22.07         0.505          pass              0.534             93.8                           0.677                1.25             -0.118                                 ok           False                  False
  GOOG           83.33               48            0.21              0.53        356.39                50.46         0.504          pass              0.575             78.7                           0.711               11.53              1.335                                 ok           False                  False
 GOOGL           80.43               46            0.29              0.72        357.44                51.28         0.503          pass              0.484             74.2                           0.691               11.57              1.366                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-08-07T11:10:02.535508-04:00 early_entry_1110 early_entry_shadow   {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.6, "early_entry_score": 0.724, "early_reclaim_pct": 84.3, "entry_ask": 4.1, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 7.59, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.611, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.724, "early_reclaim_pct": 84.3, "matched_signals": 37, "recovery_stability_score": 0.611, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}, {"current_drop_pct": 0.52, "early_entry_score": 0.67, "early_reclaim_pct": 71.5, "matched_signals": 35, "recovery_stability_score": 0.675, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:05:03.367045-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                          {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.68, "early_entry_score": 0.704, "early_reclaim_pct": 82.3, "entry_ask": 4.1, "entry_bid": 3.8, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 7.59, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.68, "early_entry_score": 0.704, "early_reclaim_pct": 82.3, "matched_signals": 36, "recovery_stability_score": 0.617, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:00:05.487197-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:55:05.454765-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:50:01.459600-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.56, "early_entry_score": 0.728, "early_reclaim_pct": 85.5, "entry_ask": 4.1, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.9, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 10.26, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.66, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.728, "early_reclaim_pct": 85.5, "matched_signals": 37, "recovery_stability_score": 0.66, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T10:45:02.357255-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:40:02.462299-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.2, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.73, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.2, "matched_signals": 37, "recovery_stability_score": 0.73, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 64.1, "matched_signals": 33, "recovery_stability_score": 0.711, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.609, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T10:35:01.485619-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:30:01.589091-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:25:02.606392-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "entry_ask": 3.7, "entry_bid": 2.95, "entry_mode": "early", "entry_option_price": 3.325, "hypothetical_budget": 16347.25, "hypothetical_contracts": 49, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 22.56, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.808, "shadow_only": true, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "matched_signals": 38, "recovery_stability_score": 0.808, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807111002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807111002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807111002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807111002)

</details>
