# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-10 11:10:06 EDT`
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
  TEAM           84.62               39            0.80              0.84        148.71               133.30         0.799          pass              0.608             70.5                           0.508               54.24              3.914                  ok            True                  False
    MU           80.00               35            0.73              4.52        875.63               110.35         0.704          pass              0.453             72.0                           0.394               -3.23              0.688                  ok            True                  False
  SOXL           80.00               30            3.93              3.86        138.60               179.06         0.683          pass              0.267             21.6                           0.210                5.14              2.555                  ok            True                  False
  PYPL           94.12               34            0.65              0.27         58.95                60.12         0.650          pass              0.766             54.7                           0.512                4.66              0.349                  ok            True                  False
  LRCX           87.10               31            1.50              3.27        309.95                90.05         0.628          pass              0.453             20.2                           0.183                5.17              1.408                  ok            True                  False
  TMUS           92.86               28            1.03              1.27        176.64                55.81         0.627          pass              0.692             55.6                           0.726               -1.04             -0.151                  ok            True                  False
 CMCSA           92.31               13            1.64              0.29         25.24                44.15         0.627          pass              0.498             29.1                           0.395                9.41              0.759                  ok            True                  False
  AMAT           89.29               28            1.87              7.07        536.11                85.88         0.624          pass              0.479             16.3                           0.180                2.35              1.253                  ok            True                  False
  MDLZ           91.67               12            1.61              0.71         62.31                30.17         0.562          pass              0.437             18.8                           0.347                1.53             -0.036                  ok            True                  False
  BKNG           95.24               21            1.66              2.49        213.35                46.72         0.559          pass              0.624             31.7                           0.380               12.89              1.030                  ok            True                  False
  ORLY           88.00               25            1.27              0.83         93.17                35.75         0.530          pass              0.462             31.8                           0.491                1.93              0.408                  ok            True                  False
   PEP           80.00               25            0.69              0.67        138.73                22.07         0.509          pass              0.267             38.9                           0.560               -1.24             -0.275                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-08-10T11:10:06.738408-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:05:04.768952-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T11:00:02.784116-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TMUS260918C00175000", "current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "entry_ask": 7.0, "entry_bid": 6.5, "entry_mode": "early", "entry_option_price": 6.75, "hypothetical_budget": 15536.5, "hypothetical_contracts": 23, "matched_signals": 33, "option_liquidity_status": "low_volume", "option_open_interest": 971.0, "option_spread_pct": 7.41, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.827, "shadow_only": true, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.705, "early_reclaim_pct": 66.8, "matched_signals": 33, "recovery_stability_score": 0.827, "success_rate": 90.91, "ticker": "TMUS", "timing_score": 0.608, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-10T10:55:01.620992-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:50:05.624699-04:00 early_entry_1050 early_entry_shadow                {"contract_symbol": "PYPL260918C00060000", "current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "entry_ask": 1.59, "entry_bid": 1.52, "entry_mode": "early", "entry_option_price": 1.555, "hypothetical_budget": 15536.5, "hypothetical_contracts": 99, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 8780.0, "option_spread_pct": 4.5, "option_volume": 87.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.784, "early_reclaim_pct": 60.6, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.655, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-10T10:45:01.632821-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:40:02.921350-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:35:06.500306-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "PYPL260918C00060000", "fill_price": 1.5525, "pnl": -1621.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-08-10T10:35:06.500306-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-10T10:30:04.655219-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260810111006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260810111006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260810111006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260810111006)

</details>
