# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-10 10:10:04 EDT`
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

- Cash: `$69,741.10`
- Equity: `$69,741.10`
- Realized PnL: `$59,741.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261009C00135000     34          2026-09-09         2026-09-10        10.85       9.765 -3689.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           80.65               31            1.66              1.54        132.04               104.12         0.666            pass              0.410             62.0                           0.798                5.93              0.591                                 ok            True                  False
   KHC          100.00               11            0.75              0.13         24.55                28.60         0.610            pass              0.618             50.0                           0.375                0.10             -0.103                                 ok            True                  False
   STX           85.19               27            2.39             14.83        879.57                74.71         0.536            pass              0.409             34.6                           0.422                2.17              0.520                                 ok            True                  False
   CEG           87.50               16            1.52              3.13        292.56                32.56         0.514            pass              0.432             46.9                           0.305                3.55              0.684                                 ok            True                  False
  WDAY           93.02               43            0.20              0.27        185.94                77.13         0.629            pass              0.871             87.1                           0.601               -2.66             -0.501 downtrend_blocked_slope_and_streak           False                  False
  AMGN          100.00               19            0.91              2.50        390.20                44.45         0.623            pass              0.640             39.3                           0.277              -11.95             -1.197 downtrend_blocked_slope_and_streak           False                  False
  MRVL           74.29               35            1.52              2.50        233.94                80.25         0.559            pass              0.417             65.0                           0.607               -5.58             -0.158           downtrend_blocked_streak           False                  False
  ADBE           96.00               25            1.40              2.51        253.79                48.69         0.557            pass              0.655             33.2                           0.326               -8.11             -1.357 downtrend_blocked_slope_and_streak           False                  False
  INTU           97.56               41            0.27              0.60        313.68                48.73         0.520            pass              0.890             79.5                           0.680               -9.48             -1.284 downtrend_blocked_slope_and_streak           False                  False
  REGN          100.00               22            1.11              6.26        804.97                27.92         0.508            pass              0.671             46.7                           0.311               -1.97              0.049           downtrend_blocked_streak           False                  False
   KDP           84.00               25            1.15              0.26         31.97                29.72         0.496 below_threshold              0.320             21.4                           0.254               -1.55              0.052           downtrend_blocked_streak           False                  False
  FAST           95.83               24            0.88              0.30         48.66                20.91         0.491 below_threshold              0.653             36.8                           0.440               -5.45             -0.428 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-09-10T10:10:04.284123-04:00 early_entry_1010 early_entry_shadow                               {"contract_symbol": "MSFT261016C00500000", "current_drop_pct": 0.52, "early_entry_score": 0.74, "early_reclaim_pct": 97.5, "entry_ask": 13.2, "entry_bid": 12.6, "entry_mode": "early", "entry_option_price": 12.9, "hypothetical_budget": 34870.55, "hypothetical_contracts": 27, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 24351.0, "option_spread_pct": 4.65, "option_volume": 115.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.728, "shadow_only": true, "success_rate": 90.32, "ticker": "MSFT", "timing_score": 0.32, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.74, "early_reclaim_pct": 97.5, "matched_signals": 31, "recovery_stability_score": 0.728, "success_rate": 90.32, "ticker": "MSFT", "timing_score": 0.32, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-10T10:05:04.263972-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "INSM261016C00130000", "current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.2, "entry_ask": 7.1, "entry_bid": 4.2, "entry_mode": "early", "entry_option_price": 5.65, "hypothetical_budget": 34870.55, "hypothetical_contracts": 61, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 146.0, "option_spread_pct": 51.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.801, "shadow_only": true, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "top_candidates": [{"current_drop_pct": 0.98, "early_entry_score": 0.683, "early_reclaim_pct": 72.2, "matched_signals": 37, "recovery_stability_score": 0.801, "success_rate": 89.19, "ticker": "INSM", "timing_score": 0.417, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-10T10:00:02.289278-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-10T09:50:01.115358-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "MSTR261009C00135000", "fill_price": 9.765, "pnl": -3689.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-10T00:00:06.085098-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-09-09T16:05:01.918481-04:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "CRWD261016C00210000", "fill_price": 12.87, "pnl": -3718.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CRWD"}
2026-09-09T15:10:06.054053-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-09T15:05:04.869479-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-09T15:00:02.977003-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-09-09T14:55:04.050096-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260910101004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260910101004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260910101004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260910101004)

</details>
