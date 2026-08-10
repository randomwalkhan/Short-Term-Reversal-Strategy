# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 11:05:04 EDT`
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

- Cash: `$31,073.00`
- Equity: `$31,073.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-10)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  PYPL     option         option PYPL260918C00060000     94          2026-08-07         2026-08-10        1.725      1.5525 -1621.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  TEAM           84.21               38            0.96              1.00        148.64               133.30         0.796          pass              0.573             64.9                           0.499               54.00              3.907                  ok            True                  False
    MU           80.00               35            0.65              4.01        875.85               110.35         0.709          pass              0.463             75.1                           0.397               -3.15              0.692                  ok            True                  False
  SOXL           80.00               30            3.89              3.82        138.61               179.06         0.685          pass              0.269             22.3                           0.239                5.18              2.556                  ok            True                  False
  PYPL           94.12               34            0.58              0.24         58.97                60.12         0.654          pass              0.780             59.4                           0.683                4.74              0.352                  ok            True                  False
  AMAT           89.29               28            1.65              6.23        536.47                85.88         0.639          pass              0.511             26.4                           0.252                2.58              1.263                  ok            True                  False
  LRCX           87.10               31            1.40              3.06        310.04                90.05         0.635          pass              0.469             25.3                           0.246                5.27              1.413                  ok            True                  False
 CMCSA           92.31               13            1.56              0.28         25.24                44.15         0.632          pass              0.509             32.5                           0.476                9.50              0.763                  ok            True                  False
  TMUS           93.10               29            0.91              1.13        176.71                55.81         0.629          pass              0.721             60.7                           0.799               -0.92             -0.146                  ok            True                  False
   ROP           96.88               32            0.66              1.84        401.46                46.43         0.576          pass              0.753             49.7                           0.555                6.56              0.345                  ok            True                  False
  MDLZ           92.86               14            1.44              0.63         62.34                30.17         0.562          pass              0.509             27.7                           0.560                1.71             -0.028                  ok            True                  False
  BKNG           95.00               20            1.86              2.79        213.22                46.72         0.552          pass              0.592             23.5                           0.317               12.66              1.020                  ok            True                  False
  ORLY           88.46               26            1.21              0.79         93.19                35.75         0.528          pass              0.490             35.0                           0.536                1.99              0.411                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-10T11:05:04.768952-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:00:02.784116-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TMUS260918C00175000", "current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "entry_ask": 7.0, "entry_bid": 6.5, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 15536.5, "hypothetical_contracts": 23, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 971.0, "option_spread_pct": 7.41, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "matched_signals": 33, "recovery_stability_score": 0.827, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T10:55:01.620992-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:50:05.624699-04:00 early_entry_1050 early_entry_shadow                {"contract_symbol": "PYPL260918C00060000", "current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "entry_ask": 1.59, "entry_bid": 1.52, "entry_mode": "early", "entry_option_price": 1.555, "hypothetical_budget": 15536.5, "hypothetical_contracts": 99, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 8780.0, "option_spread_pct": 4.5, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:45:01.632821-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:40:02.921350-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "PYPL260918C00060000", "fill_price": 1.5525, "pnl": -1621.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-08-10T10:30:04.655219-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:25:03.677192-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810110504)

</details>
