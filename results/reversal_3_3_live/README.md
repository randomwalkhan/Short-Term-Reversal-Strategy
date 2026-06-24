# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-24 09:50:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MRVL          100.00               25            1.75              3.43        277.57               157.48         0.804          pass              0.742             54.0                           0.350                2.72              0.868                      ok            True                  False
  KLAC           91.30               23            1.47              2.52        243.41                93.06         0.724          pass              0.602             47.1                           0.335               12.60              1.301                      ok            True                  False
  MCHP           93.10               29            0.88              0.57         93.01                72.77         0.626          pass              0.693             51.5                           0.334                1.06              0.562                      ok            True                  False
  ASML           95.83               24            1.93             24.00       1768.18                65.60         0.613          pass              0.641             28.8                           0.276               -1.89              0.099                      ok            True                  False
  NXPI           94.12               34            0.62              1.31        299.38                63.85         0.526          pass              0.812             74.2                           0.420                0.22              0.366                      ok            True                  False
  PANW           92.50               40            0.88              1.80        290.14                56.69         0.525          pass              0.755             56.6                           0.554               10.68              0.936                      ok            True                  False
   WDC           93.75               16            2.98             13.98        664.76                96.85         0.508          pass              0.696             79.5                           0.519               25.70              3.658                      ok            True                  False
  SOXL           93.55               31            0.38              0.61        230.57               242.24         0.962          pass              0.873             91.7                           0.557               14.02              2.478                      ok           False                  False
  MPWR           93.55               31            0.83              8.27       1420.21                86.34         0.672          pass              0.752             61.3                           0.452               -7.84             -0.720 downtrend_blocked_slope           False                  False
  LRCX           97.22               36            0.30              0.77        371.00                85.65         0.619          pass              0.926             97.0                           0.640               13.24              1.497                      ok           False                  False
   TRI           80.65               31            0.33              0.19         80.63                56.77         0.577          pass              0.451             78.8                           0.466               -2.28             -0.368                      ok           False                  False
  AMAT           97.22               36            0.02              0.07        585.85                79.43         0.549          pass              0.928             99.9                           0.656               17.34              1.890                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-24T09:20:01.109273-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-23T12:00:01.662630-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "GOOG260724C00345000", "current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "entry_ask": 15.1, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 15306.25, "hypothetical_contracts": 10, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 118.0, "option_spread_pct": 4.4, "option_volume": 45.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "matched_signals": 34, "recovery_stability_score": 0.751, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.743, "early_reclaim_pct": 90.5, "matched_signals": 32, "recovery_stability_score": 0.752, "success_rate": 90.62, "ticker": "GOOGL", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T11:20:02.932662-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "GOOG260731C00345000", "current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "entry_ask": 18.9, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 18.35, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 142.0, "option_spread_pct": 5.99, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "matched_signals": 30, "recovery_stability_score": 0.603, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T10:51:17.657217-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T10:17:41.614110-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MRVL260724C00310000", "fill_price": 31.5, "pnl": -1050.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "WMT260724C00120000", "fill_price": 3.5, "pnl": 5148.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 39.44, "ticker": "WMT"}
2026-06-23T00:00:04.979813-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-22T15:10:01.120080-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:05:02.154937-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260624095001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260624095001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260624095001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260624095001)

</details>
