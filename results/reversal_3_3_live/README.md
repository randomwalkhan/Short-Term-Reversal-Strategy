# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 10:40:06 EDT`
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

- Cash: `$81,364.30`
- Equity: `$81,364.30`
- Realized PnL: `$71,364.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  META     option         option META261120C00735000      8          2026-09-30         2026-10-01       48.425     43.5825 -3874.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           97.78               45            0.28              0.39        199.25                78.48         0.628            pass              0.847             61.3                           0.318                0.71             -0.239                                 ok           False                  False
  AMGN           72.73               11            1.49              4.41        419.62                46.02         0.617            pass              0.167             32.8                           0.184                9.33              0.986                                 ok           False                  False
  INTC           87.50               40            0.24              0.20        120.14                73.63         0.606            pass              0.730             89.9                           0.802               10.24              0.563                                 ok           False                  False
  DRAM           80.56               36            0.10              0.04         60.34                53.77         0.577            pass              0.528             94.1                           0.615                4.36              0.111                                 ok           False                  False
  CRWD           89.13               46            0.05              0.10        264.71                63.45         0.550            pass              0.791             97.4                           0.665                7.70              0.901                                 ok           False                  False
  ASML           84.21               38            0.18              2.23       1810.71                42.37         0.538            pass              0.593             80.0                           0.607               10.97              0.961                                 ok           False                  False
   XEL           83.33               18            0.69              0.34         70.33                18.32         0.518            pass              0.346             50.5                           0.560               -4.94             -0.447            downtrend_blocked_slope           False                  False
  NXPI           86.49               37            0.21              0.35        237.38                38.88         0.501            pass              0.632             76.2                           0.675                3.98              0.374                                 ok           False                  False
  NFLX           68.42               19            1.61              0.78         69.24                37.25         0.495 below_threshold              0.184             24.8                           0.378               -9.10             -0.741            downtrend_blocked_slope           False                  False
    MU           92.31               26            1.94             14.48       1058.90                49.56         0.487 below_threshold              0.637             51.0                           0.544                6.85              0.465                                 ok           False                  False
   EXC           75.00               20            0.54              0.15         40.33                14.97         0.487 below_threshold              0.303             62.7                           0.676               -5.77             -0.579 downtrend_blocked_slope_and_streak           False                  False
  TMUS           89.47               38            0.11              0.13        163.03                33.48         0.483 below_threshold              0.769             93.8                           0.534               -2.13             -0.205                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-01T10:40:06.481988-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:35:05.852380-04:00 early_entry_1035 early_entry_shadow                                     {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.72, "early_entry_score": 0.681, "early_reclaim_pct": 70.0, "entry_ask": 9.65, "entry_bid": 9.45, "entry_mode": "early", "entry_option_price": 9.55, "hypothetical_budget": 40682.15, "hypothetical_contracts": 42, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 2.09, "option_volume": 30.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.601, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.681, "early_reclaim_pct": 70.0, "matched_signals": 36, "recovery_stability_score": 0.664, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T10:30:06.297873-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:25:05.417104-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:20:05.454377-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:20:05.454377-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {"asset_type": "option", "contract_symbol": "META261120C00735000", "fill_price": 43.5825, "pnl": -3874.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "META"}
2026-10-01T10:15:02.462190-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:10:05.306830-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:05:05.587824-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "FTNT261120C00175000", "current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "entry_ask": 17.55, "entry_bid": 15.3, "entry_mode": "early", "entry_option_price": 16.425, "hypothetical_budget": 23249.15, "hypothetical_contracts": 14, "matched_signals": 41, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 78.0, "option_spread_pct": 13.7, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.567, "shadow_only": true, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.716, "early_reclaim_pct": 66.3, "matched_signals": 41, "recovery_stability_score": 0.567, "success_rate": 90.24, "ticker": "FTNT", "timing_score": 0.444, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T10:00:05.588413-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001104006)

</details>
