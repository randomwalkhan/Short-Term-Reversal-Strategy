# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-23 15:35:07 EDT`
Last processed slot: `manage_1530`

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

## Today's Closed Trades (2026-06-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   WMT     option         option  WMT260724C00120000     52          2026-06-18         2026-06-23         2.51         3.5  5148.0   39.442231 take_profit_day2_hit_at_scan
  MRVL     option         option MRVL260724C00310000      3          2026-06-22         2026-06-23        35.00        31.5 -1050.0  -10.000000        stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  AVGO           82.35               17            2.43              6.68        389.27                76.66         0.631            pass              0.343             56.8                           0.518               -3.38              0.144                                 ok            True                  False
  FAST           90.48               21            1.05              0.34         45.97                23.77         0.514            pass              0.499             31.7                           0.248               -0.79             -0.151                                 ok            True                  False
   LIN           96.00               25            0.73              2.63        515.58                18.72         0.503            pass              0.707             52.1                           0.286                2.20              0.115                                 ok            True                  False
  MRVL          100.00                2            9.08             19.56        299.48               151.43         0.530            pass              0.489             12.1                           0.336               -3.09              0.993                                 ok           False                  False
  INTU           77.78               45            0.01              0.02        257.76                62.45         0.529            pass              0.549             98.8                           0.520              -15.63             -1.457 downtrend_blocked_slope_and_streak           False                  False
  SHOP           84.09               44            0.18              0.13        107.92                55.98         0.523            pass              0.616             84.8                           0.493               -2.70             -0.188                                 ok           False                  False
  CSCO           94.29               35            0.49              0.41        121.35                40.78         0.520            pass              0.854             84.8                           0.637               -2.59             -0.147           downtrend_blocked_streak           False                  False
  UPRO           85.71                7            3.80              3.76        139.81                49.83         0.510            pass              0.268             21.4                           0.344               -1.82              0.317                                 ok           False                  False
  PCAR           87.50                8            2.25              1.89        119.31                32.72         0.508            pass              0.257              2.2                           0.206               -0.86              0.105                                 ok           False                  False
  CTSH           81.82               22            1.48              0.43         41.64                52.33         0.504            pass              0.249             23.5                           0.309              -22.23             -2.569 downtrend_blocked_slope_and_streak           False                  False
  ODFL           91.43               35            0.57              0.88        219.14                45.20         0.489 below_threshold              0.788             89.4                           0.493              -11.64             -1.478 downtrend_blocked_slope_and_streak           False                  False
  INTC           83.33               12            5.21              5.14        138.74                94.51         0.480 below_threshold              0.281             43.5                           0.522               21.16              2.462                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-06-23T12:00:01.662630-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "GOOG260724C00345000", "current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "entry_ask": 15.1, "entry_bid": 14.45, "entry_mode": "early", "entry_option_price": 14.775, "hypothetical_budget": 15306.25, "hypothetical_contracts": 10, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 118.0, "option_spread_pct": 4.4, "option_volume": 45.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.773, "early_reclaim_pct": 91.4, "matched_signals": 34, "recovery_stability_score": 0.751, "success_rate": 91.18, "ticker": "GOOG", "timing_score": 0.405, "trend_health_status": "ok"}, {"current_drop_pct": 0.77, "early_entry_score": 0.743, "early_reclaim_pct": 90.5, "matched_signals": 32, "recovery_stability_score": 0.752, "success_rate": 90.62, "ticker": "GOOGL", "timing_score": 0.419, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T11:20:02.932662-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                  {"contract_symbol": "GOOG260731C00345000", "current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "entry_ask": 18.9, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 18.35, "hypothetical_budget": 15306.25, "hypothetical_contracts": 8, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 142.0, "option_spread_pct": 5.99, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.8, "early_reclaim_pct": 89.6, "matched_signals": 30, "recovery_stability_score": 0.603, "success_rate": 93.33, "ticker": "GOOG", "timing_score": 0.425, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-06-23T10:51:17.657217-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T10:17:41.614110-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "MRVL260724C00310000", "fill_price": 31.5, "pnl": -1050.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
2026-06-23T09:35:06.707471-04:00      manage_0930               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "WMT260724C00120000", "fill_price": 3.5, "pnl": 5148.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 39.44, "ticker": "WMT"}
2026-06-23T00:00:04.979813-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-06-22T15:10:01.120080-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:05:02.154937-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-06-22T15:00:02.230019-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260623153507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260623153507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260623153507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260623153507)

</details>
