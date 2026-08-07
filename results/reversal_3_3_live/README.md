# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 12:15:01 EDT`
Last processed slot: `manual`

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
    MU           80.56               36            0.58              3.56        879.95               110.38         0.670          pass              0.511             85.3                           0.795               -4.84              0.225                                 ok            True                  False
  PYPL           92.86               28            1.02              0.43         59.60                59.52         0.657          pass              0.578             16.4                           0.239                5.38              0.462                                 ok            True                  False
  TMUS           88.89               18            1.58              2.00        179.11                57.01         0.641          pass              0.392             12.6                           0.113               -1.65             -0.181                                 ok            True                  False
   ADP           96.43               28            0.86              1.64        272.81                34.67         0.505          pass              0.783             70.8                           0.373                8.42              0.685                                 ok            True                  False
  INSM           58.33               12            3.52              3.26        131.15               110.04         0.686          pass              0.111              9.9                           0.217               19.61              1.427                                 ok           False                  False
  ALNY           88.37               43            0.23              0.34        215.97               128.30         0.628          pass              0.760             91.3                           0.678              -20.66             -3.031            downtrend_blocked_slope           False                  False
  DRAM           78.12               32            2.33              0.84         51.08               108.98         0.603          pass              0.372             55.1                           0.680               -5.56              0.338                                 ok           False                  False
  PAYX          100.00               25            0.38              0.32        119.99                34.54         0.575          pass              0.730             57.5                           0.335                6.49              0.411                                 ok           False                  False
  GOOG           79.49               39            0.66              1.65        355.91                50.46         0.527          pass              0.345             33.0                           0.216               11.02              1.315                                 ok           False                  False
 GOOGL           75.68               37            0.71              1.78        356.99                51.28         0.526          pass              0.340             35.8                           0.230               11.09              1.346                                 ok           False                  False
   MAR           93.75               32            0.52              1.32        359.11                38.09         0.523          pass              0.745             59.7                           0.394               -4.44             -0.851 downtrend_blocked_slope_and_streak           False                  False
  AAPL           93.18               44            0.19              0.41        312.23                37.99         0.505          pass              0.804             67.4                           0.328               -6.37             -1.065 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-07T12:00:04.348993-04:00 early_entry_1200 early_entry_shadow     {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 83.2, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.6, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.707, "early_reclaim_pct": 83.2, "matched_signals": 36, "recovery_stability_score": 0.6, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:55:05.632607-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.61, "early_entry_score": 0.724, "early_reclaim_pct": 84.1, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.724, "early_reclaim_pct": 84.1, "matched_signals": 37, "recovery_stability_score": 0.603, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:50:01.513920-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:45:01.522063-04:00 early_entry_1145 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.65, "early_entry_score": 0.706, "early_reclaim_pct": 83.1, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.616, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "top_candidates": [{"current_drop_pct": 0.65, "early_entry_score": 0.706, "early_reclaim_pct": 83.1, "matched_signals": 36, "recovery_stability_score": 0.616, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.467, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:40:01.565358-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.0, "entry_ask": 4.2, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.95, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 12.66, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.648, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.727, "early_reclaim_pct": 85.0, "matched_signals": 37, "recovery_stability_score": 0.648, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:35:06.439574-04:00 early_entry_1135 early_entry_shadow  {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.66, "early_entry_score": 0.705, "early_reclaim_pct": 82.7, "entry_ask": 4.1, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.9, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 10.26, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.466, "top_candidates": [{"current_drop_pct": 0.66, "early_entry_score": 0.705, "early_reclaim_pct": 82.7, "matched_signals": 36, "recovery_stability_score": 0.658, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.466, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:30:01.519424-04:00 early_entry_1130 early_entry_shadow    {"contract_symbol": "ORLY260918C00092000", "current_drop_pct": 0.69, "early_entry_score": 0.703, "early_reclaim_pct": 82.1, "entry_ask": 4.1, "entry_bid": 3.7, "entry_mode": "early", "entry_option_price": 3.9, "hypothetical_budget": 16347.25, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 574.0, "option_spread_pct": 10.26, "option_volume": 50.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.703, "early_reclaim_pct": 82.1, "matched_signals": 36, "recovery_stability_score": 0.58, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-07T11:25:01.515249-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:20:02.542614-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T11:15:01.509027-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807121501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807121501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807121501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807121501)

</details>
