# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-03 12:25:01 EDT`
Last processed slot: `manage_1230`

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

- Cash: `$35,229.75`
- Equity: `$35,229.75`
- Realized PnL: `$25,229.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  PYPL     option         option PYPL260918C00057500     66          2026-07-31         2026-08-03        2.500      3.0550  3663.0        22.2 take_profit_day1_hit_at_scan
   CSX     option         option  CSX260918C00050000     86          2026-07-30         2026-08-03        1.925      1.7325 -1655.5       -10.0        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           94.44               18            0.83              0.36         62.16                33.81         0.601          pass              0.565             22.0                           0.193                2.53              0.530                                 ok            True                  False
   CSX           94.12               17            0.92              0.33         50.26                27.78         0.592          pass              0.503              7.0                           0.101               -0.35             -0.079                                 ok            True                  False
   EXC           95.24               21            0.68              0.22         45.73                22.49         0.549          pass              0.642             38.0                           0.252               -0.98             -0.130                                 ok            True                  False
   KDP           83.33               24            0.60              0.13         31.06                33.11         0.548          pass              0.281             14.8                           0.163                1.62              0.450                                 ok            True                  False
  AMGN          100.00               11            1.76              4.74        383.13                25.80         0.531          pass              0.507             15.8                           0.169                3.90              0.631                                 ok            True                  False
  SOXL           80.56               36            0.05              0.04        114.70               178.56         0.737          pass              0.560             99.5                           0.893              -16.19             -4.083 downtrend_blocked_slope_and_streak           False                  False
  DRAM           75.00               36            0.02              0.01         50.37               111.30         0.670          pass              0.539             99.6                           0.905               -5.09             -1.647 downtrend_blocked_slope_and_streak           False                  False
  LRCX           89.19               37            0.18              0.37        292.86                90.68         0.609          pass              0.776             96.7                           0.872               -4.65             -1.294 downtrend_blocked_slope_and_streak           False                  False
    MU           80.00               35            0.37              2.13        822.12               109.24         0.609          pass              0.510             94.3                           0.877               -5.25             -1.735 downtrend_blocked_slope_and_streak           False                  False
  AAPL           94.44               18            1.22              2.65        307.78                37.33         0.591          pass              0.619             40.5                           0.579               -6.57             -0.352 downtrend_blocked_slope_and_streak           False                  False
   PEP           84.62               26            0.43              0.42        139.38                26.18         0.555          pass              0.348             21.1                           0.168                2.58              0.479                                 ok           False                  False
  GILD           87.10               31            0.45              0.41        130.03                32.59         0.535          pass              0.531             49.6                           0.312               -2.70             -0.046           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-08-03T12:00:03.854898-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "CDNS260918C00335000", "current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "entry_ask": 25.3, "entry_bid": 22.6, "entry_mode": "early", "entry_option_price": 23.95, "hypothetical_budget": 17614.88, "hypothetical_contracts": 7, "matched_signals": 45, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 17.0, "option_spread_pct": 11.27, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.682, "early_reclaim_pct": 67.6, "matched_signals": 45, "recovery_stability_score": 0.703, "success_rate": 88.89, "ticker": "CDNS", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-03T11:55:02.829313-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:50:02.007481-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:45:01.947551-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:40:02.921785-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:35:06.072757-04:00 early_entry_1135 early_entry_shadow                                       {"contract_symbol": "CSCO260918C00115000", "current_drop_pct": 0.5, "early_entry_score": 0.697, "early_reclaim_pct": 75.4, "entry_ask": 8.45, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 8.325, "hypothetical_budget": 17614.88, "hypothetical_contracts": 21, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 5712.0, "option_spread_pct": 3.0, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.671, "shadow_only": true, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.697, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.671, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-03T11:30:04.782483-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:25:05.765544-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:20:03.871415-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-03T11:15:01.863770-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260803122501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260803122501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260803122501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260803122501)

</details>
