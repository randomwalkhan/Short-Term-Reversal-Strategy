# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-18 10:45:06 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$71,470.80`
- Equity: `$71,470.80`
- Realized PnL: `$61,470.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   WMT     option         option WMT261023C00108000    127          2026-09-17         2026-09-18        2.565        3.05 6159.5   18.908382 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           97.06               34            1.39              1.92        196.65                82.85         0.619          pass              0.751             43.0                           0.548                9.52              1.847                                 ok            True                  False
  CTSH          100.00               15            2.52              1.09         61.41                39.55         0.524          pass              0.498              4.0                           0.144               -6.68             -0.015                                 ok            True                  False
  MSFT          100.00               21            1.19              4.15        495.97                21.82         0.507          pass              0.557             10.8                           0.176               -3.59             -0.157                                 ok            True                  False
   WBD           85.71               14            0.90              0.18         28.16                10.21         0.502          pass              0.304             25.0                           0.331               -1.36             -0.064                                 ok            True                  False
  CRWD           63.64               11            3.68              6.33        242.99                97.92         0.619          pass              0.117             16.3                           0.407               10.09              1.723                                 ok           False                  False
  PYPL           91.43               35            0.38              0.14         52.88                57.74         0.613          pass              0.746             71.0                           0.664               -6.95             -0.419            downtrend_blocked_slope           False                  False
  MRVL           78.95               38            0.93              1.58        240.08                74.50         0.583          pass              0.310             21.6                           0.197               14.21              0.786                                 ok           False                  False
  NVDA           92.31               39            0.14              0.21        219.25                45.58         0.570          pass              0.808             76.5                           0.390               -4.01             -0.629           downtrend_blocked_streak           False                  False
   EXC          100.00                6            1.10              0.33         42.50                15.46         0.570          pass              0.503             15.4                           0.238               -4.40             -0.462 downtrend_blocked_slope_and_streak           False                  False
   TRI           90.91               11            3.07              2.13         98.57                55.72         0.566          pass              0.377              7.6                           0.199              -13.72             -0.628 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               38            0.50              0.67        192.24                58.58         0.562          pass              0.865             74.1                           0.695               -1.60              0.373                                 ok           False                  False
  ADSK           84.38               32            0.99              1.52        217.99                55.63         0.547          pass              0.365             15.8                           0.219               -8.86             -0.069           downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-18T10:45:06.500204-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:40:04.793356-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:35:06.106609-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:30:04.878508-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:25:05.756600-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:20:05.884783-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "TEAM261023C00190000", "current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "entry_ask": 16.3, "entry_bid": 13.7, "entry_mode": "early", "entry_option_price": 15.0, "hypothetical_budget": 35735.4, "hypothetical_contracts": 23, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 9.0, "option_spread_pct": 17.33, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.592, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.864, "early_reclaim_pct": 73.8, "matched_signals": 38, "recovery_stability_score": 0.592, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.562, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-18T10:15:05.598179-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:10:02.340504-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"asset_type": "option", "contract_symbol": "WMT261023C00108000", "fill_price": 3.05, "pnl": 6159.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 18.91, "ticker": "WMT"}
2026-09-18T10:10:02.340504-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-18T10:05:06.381889-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260918104506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260918104506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260918104506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260918104506)

</details>
