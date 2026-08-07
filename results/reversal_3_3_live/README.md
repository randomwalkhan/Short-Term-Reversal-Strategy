# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 11:00:05 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.76               29            2.61             16.11        874.57               110.38         0.579            pass              0.358             33.2                           0.394               -6.79              0.131                                 ok            True                  False
  INTC           84.62               39            0.78              0.54         99.58                86.24         0.576            pass              0.543             56.5                           0.319                7.27              1.437                                 ok            True                  False
  INSM           71.43               21            2.12              1.97        131.71               110.04         0.742            pass              0.241             31.2                           0.507               21.34              1.492                                 ok           False                  False
  PYPL           95.24               42            0.33              0.14         59.72                59.52         0.619            pass              0.837             58.3                           0.321                6.11              0.494                                 ok           False                  False
  TMUS           88.57               35            0.44              0.56        179.73                57.01         0.606            pass              0.682             75.5                           0.714               -0.51             -0.128                                 ok           False                  False
   CSX           92.31               26            0.59              0.21         50.61                29.04         0.543            pass              0.649             53.1                           0.621               -5.32             -0.308 downtrend_blocked_slope_and_streak           False                  False
  DRAM           76.00               25            4.08              1.47         50.81               108.98         0.522            pass              0.216             21.3                           0.327               -7.26              0.255                                 ok           False                  False
   MAR           94.29               35            0.48              1.21        359.15                38.09         0.507            pass              0.787             63.1                           0.478               -4.40             -0.849 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.97               33            0.38              0.73        273.20                34.67         0.505            pass              0.865             87.0                           0.443                8.95              0.707                                 ok           False                  False
 GOOGL           78.57               42            0.62              1.55        357.09                51.28         0.504            pass              0.383             44.2                           0.368               11.20              1.350                                 ok           False                  False
  GOOG           82.22               45            0.50              1.24        356.09                50.46         0.502            pass              0.459             49.7                           0.397               11.21              1.322                                 ok           False                  False
  ROST           94.74               38            0.15              0.27        254.19                22.77         0.496 below_threshold              0.894             88.4                           0.649                6.29              0.456                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        detail
2026-08-07T11:00:05.487197-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:55:05.454765-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:50:01.459600-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.56, "early_entry_score": 0.728, "early_reclaim_pct": 85.5, "entry_ask": 4.1, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.9, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 10.26, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.66, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.728, "early_reclaim_pct": 85.5, "matched_signals": 37, "recovery_stability_score": 0.66, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T10:45:02.357255-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:40:02.462299-04:00 early_entry_1040 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.2, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.73, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.2, "matched_signals": 37, "recovery_stability_score": 0.73, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.697, "early_reclaim_pct": 64.1, "matched_signals": 33, "recovery_stability_score": 0.711, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.609, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T10:35:01.485619-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:30:01.589091-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:25:02.606392-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                          {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "entry_ask": 3.7, "entry_bid": 2.95, "entry_mode": "early", "entry_option_price": 3.325, "hypothetical_budget": 16347.25, "hypothetical_contracts": 49, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 22.56, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.808, "shadow_only": true, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "matched_signals": 38, "recovery_stability_score": 0.808, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:20:01.443231-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:20:01.443231-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "INTC260918C00100000", "fill_price": 10.0575, "pnl": -1676.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "INTC"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807110005)

</details>
