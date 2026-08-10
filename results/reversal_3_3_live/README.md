# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 11:00:02 EDT`
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
  TEAM           84.62               39            0.58              0.60        148.81               133.30         0.810          pass              0.634             78.9                           0.594               54.59              3.924                  ok            True                  False
    MU           80.56               36            0.61              3.74        875.97               110.35         0.707          pass              0.489             76.8                           0.388               -3.11              0.694                  ok            True                  False
 CMCSA           92.86               14            1.40              0.25         25.25                44.15         0.636          pass              0.551             39.3                           0.681                9.67              0.770                  ok            True                  False
  LRCX           86.21               29            1.71              3.74        309.75                90.05         0.626          pass              0.374              6.5                           0.108                4.94              1.398                  ok            True                  False
  AMAT           88.46               26            2.08              7.87        535.77                85.88         0.622          pass              0.415              7.0                           0.091                2.13              1.243                  ok            True                  False
  TMUS           90.91               33            0.77              0.95        176.78                55.81         0.608          pass              0.705             66.8                           0.827               -0.78             -0.139                  ok            True                   True
   STX           90.32               31            0.76              4.33        810.90                91.44         0.594          pass              0.705             76.9                           0.407               -1.28              0.504                  ok            True                  False
   ROP           96.88               32            0.54              1.51        401.60                46.43         0.584          pass              0.782             58.9                           0.569                6.69              0.350                  ok            True                  False
  MDLZ           93.33               15            1.26              0.55         62.37                30.17         0.568          pass              0.555             36.5                           0.633                1.90             -0.020                  ok            True                  False
  BKNG           95.00               20            1.83              2.75        213.24                46.72         0.554          pass              0.596             24.6                           0.361               12.69              1.022                  ok            True                  False
  ORLY           88.46               26            1.24              0.81         93.18                35.75         0.526          pass              0.485             33.5                           0.540                1.96              0.410                  ok            True                  False
   HON           86.36               22            1.15              1.98        245.36                29.28         0.504          pass              0.443             47.8                           0.495               -0.96              0.007                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-10T11:00:02.784116-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TMUS260918C00175000", "current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "entry_ask": 7.0, "entry_bid": 6.5, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 15536.5, "hypothetical_contracts": 23, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 971.0, "option_spread_pct": 7.41, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "matched_signals": 33, "recovery_stability_score": 0.827, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T10:55:01.620992-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:50:05.624699-04:00 early_entry_1050 early_entry_shadow                {"contract_symbol": "PYPL260918C00060000", "current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "entry_ask": 1.59, "entry_bid": 1.52, "entry_mode": "early", "entry_option_price": 1.555, "hypothetical_budget": 15536.5, "hypothetical_contracts": 99, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 8780.0, "option_spread_pct": 4.5, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:45:01.632821-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:40:02.921350-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "PYPL260918C00060000", "fill_price": 1.5525, "pnl": -1621.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-08-10T10:35:06.500306-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:30:04.655219-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:25:03.677192-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:20:04.656698-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810110002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810110002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810110002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810110002)

</details>
