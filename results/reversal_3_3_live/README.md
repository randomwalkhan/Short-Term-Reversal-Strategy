# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-28 10:20:06 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$69,998.30`
- Equity: `$69,998.30`
- Realized PnL: `$59,998.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MSTR     option         option MSTR261120C00160000     20          2026-09-25         2026-09-28       17.775     15.9975 -3555.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MSTR           94.29               35            0.77              0.85        158.24               104.19         0.729            pass              0.846             75.2                           0.443               14.93              2.489                                 ok            True                  False
   CEG           82.35               17            1.74              3.21        261.89                41.90         0.537            pass              0.210             15.8                           0.197               -2.23              0.005                                 ok            True                  False
  UPRO           89.47               19            1.53              1.63        151.50                32.02         0.518            pass              0.405             13.6                           0.225                2.84              0.574                                 ok            True                  False
  MPWR           83.33               24            2.04             19.49       1359.08                54.48         0.511            pass              0.374             46.9                           0.279               17.17              2.170                                 ok            True                  False
  MSFT          100.00               17            1.38              4.98        514.03                25.07         0.504            pass              0.644             49.0                           0.696                0.72              0.230                                 ok            True                  False
  PYPL           91.30               23            1.20              0.46         54.84                60.08         0.503            pass              0.644             68.6                           0.782                0.65              0.099                                 ok            True                  False
  NXPI           85.71               28            1.10              1.84        237.29                39.27         0.503            pass              0.519             65.6                           0.385                5.48              0.674                                 ok            True                  False
  WDAY           91.18               34            0.76              1.01        189.02                50.22         0.500 below_threshold              0.754             82.0                           0.893               -3.19             -0.215                                 ok            True                   True
   TRI           87.50               32            1.08              0.75         98.67                56.74         0.579            pass              0.576             57.0                           0.753               -7.47             -0.517 downtrend_blocked_slope_and_streak           False                  False
  AMGN           86.84               38            0.15              0.44        414.42                46.27         0.574            pass              0.675             82.9                           0.410                8.52              1.115                                 ok           False                  False
   WBD           95.35               43            0.05              0.01         30.86                38.15         0.559            pass              0.899             81.0                           0.475                9.77              1.280                                 ok           False                  False
  LRCX           76.47               34            1.36              3.01        313.92                61.39         0.528            pass              0.411             66.2                           0.361               13.80              1.816                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-09-28T10:20:06.719133-04:00 early_entry_1020 early_entry_shadow    {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "entry_ask": 13.9, "entry_bid": 10.7, "entry_mode": "early", "entry_option_price": 12.3, "hypothetical_budget": 34999.15, "hypothetical_contracts": 28, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 26.02, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.893, "shadow_only": true, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "top_candidates": [{"current_drop_pct": 0.76, "early_entry_score": 0.754, "early_reclaim_pct": 82.0, "matched_signals": 34, "recovery_stability_score": 0.893, "success_rate": 91.18, "ticker": "WDAY", "timing_score": 0.5, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:15:02.047493-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "entry_ask": 13.9, "entry_bid": 9.8, "entry_mode": "early", "entry_option_price": 11.85, "hypothetical_budget": 34999.15, "hypothetical_contracts": 29, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 34.6, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.949, "shadow_only": true, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 87.9, "matched_signals": 36, "recovery_stability_score": 0.949, "success_rate": 91.67, "ticker": "WDAY", "timing_score": 0.505, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:10:05.010808-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T10:05:05.986578-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "WDAY261030C00187500", "current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "entry_ask": 11.7, "entry_bid": 8.2, "entry_mode": "early", "entry_option_price": 9.95, "hypothetical_budget": 34999.15, "hypothetical_contracts": 35, "matched_signals": 33, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 35.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.871, "shadow_only": true, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "top_candidates": [{"current_drop_pct": 0.89, "early_entry_score": 0.731, "early_reclaim_pct": 78.9, "matched_signals": 33, "recovery_stability_score": 0.871, "success_rate": 90.91, "ticker": "WDAY", "timing_score": 0.497, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-28T10:00:06.220548-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-28T09:50:05.886543-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "MSTR261120C00160000", "fill_price": 15.9975, "pnl": -3555.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MSTR"}
2026-09-28T03:00:06.642645-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 92, 'empty': 1}
2026-09-26T02:55:04.179839-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:50:05.866610-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-09-26T02:45:06.222669-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260928102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260928102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260928102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260928102006)

</details>
