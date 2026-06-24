# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-24 10:10:01 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$30,612.50`
- Equity: `$30,612.50`
- Realized PnL: `$20,612.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-24)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  SOXL           93.10               29            1.18              1.90        230.60               242.24         0.954            pass              0.798             75.6                           0.625               13.40              2.453                      ok            True                  False
  MRVL          100.00               23            2.48              4.85        276.96               157.48         0.774            pass              0.685             40.4                           0.325                1.96              0.834                      ok            True                  False
  KLAC           93.94               33            0.84              1.43        243.88                93.06         0.705            pass              0.805             69.9                           0.751               13.32              1.330                      ok            True                   True
  MCHP           93.33               30            0.69              0.45         93.07                72.77         0.633            pass              0.739             62.4                           0.534                1.26              0.571                      ok            True                  False
  ASML           96.00               25            1.81             22.53       1768.80                65.60         0.615            pass              0.661             33.2                           0.424               -1.77              0.104                      ok            True                  False
  PANW           90.00               30            1.75              3.57        289.39                56.69         0.533            pass              0.495             13.8                           0.194                9.71              0.896                      ok            True                  False
  NXPI           92.00               25            1.55              3.25        298.55                63.85         0.520            pass              0.579             35.8                           0.190               -0.71              0.324                      ok            True                  False
  FTNT           96.77               31            1.22              1.27        147.46                46.74         0.515            pass              0.684             30.9                           0.259                5.64              0.434                      ok            True                  False
  CDNS           94.44               36            0.75              2.00        378.20                55.93         0.501            pass              0.767             52.8                           0.528               -3.76             -0.195                      ok            True                  False
   WDC           93.75               16            3.09             14.51        664.53                96.85         0.500 below_threshold              0.693             78.8                           0.617               25.55              3.653                      ok            True                  False
  MPWR           92.86               28            1.06             10.56       1419.23                86.34         0.676            pass              0.682             50.6                           0.481               -8.05             -0.731 downtrend_blocked_slope           False                  False
   TXN           94.12               34            0.12              0.25        304.25                65.59         0.622            pass              0.874             91.9                           0.606                5.33              0.911                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-24T10:10:01.169006-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                           {"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "entry_mode": "early", "error": "KLAC: no call expiries found in the 21-40 trading-day window.", "matched_signals": 33, "reason": "shadow_option_unavailable", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "top_candidates": [{"current_drop_pct": 0.84, "early_entry_score": 0.805, "early_reclaim_pct": 69.9, "matched_signals": 33, "recovery_stability_score": 0.751, "success_rate": 93.94, "ticker": "KLAC", "timing_score": 0.705, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-24T10:05:01.111815-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-24T10:00:02.286958-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                 {"contract_symbol": "LRCX260724C00370000", "current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "entry_ask": 35.3, "entry_bid": 32.3, "entry_mode": "early", "entry_option_price": 33.8, "hypothetical_budget": 15306.25, "hypothetical_contracts": 4, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 114.0, "option_spread_pct": 8.88, "option_volume": 38.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.655, "shadow_only": true, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.898, "early_reclaim_pct": 94.3, "matched_signals": 33, "recovery_stability_score": 0.655, "success_rate": 96.97, "ticker": "LRCX", "timing_score": 0.62, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-24T09:20:01.109273-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-23T12:00:01.662630-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "GOOG260724C00345000", "current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "entry_ask": 15.1, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 15306.25, "hypothetical_contracts": 10, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 118.0, "option_spread_pct": 4.4, "option_volume": 45.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "matched_signals": 34, "recovery_stability_score": 0.751, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.743, "early_reclaim_pct": 90.5, "matched_signals": 32, "recovery_stability_score": 0.752, "success_rate": 90.62, "ticker": "GOOGL", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T11:20:02.932662-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "GOOG260731C00345000", "current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "entry_ask": 18.9, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 18.35, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 142.0, "option_spread_pct": 5.99, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "matched_signals": 30, "recovery_stability_score": 0.603, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T10:51:17.657217-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T10:17:41.614110-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "WMT260724C00120000", "fill_price": 3.5, "pnl": 5148.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 39.44, "ticker": "WMT"}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MRVL260724C00310000", "fill_price": 31.5, "pnl": -1050.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260624101001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260624101001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260624101001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260624101001)

</details>
