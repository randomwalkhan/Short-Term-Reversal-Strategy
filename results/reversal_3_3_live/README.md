# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 10:55:06 EDT`
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
  AMGN           80.00               15            1.36              4.02        419.79                46.02         0.610            pass              0.211             38.8                           0.326                9.48              0.992                                 ok            True                  False
  INTC           87.50               40            0.47              0.40        120.06                73.63         0.591            pass              0.700             80.1                           0.755                9.98              0.552                                 ok           False                  False
  DRAM           79.41               34            0.48              0.20         60.27                53.77         0.563            pass              0.432             71.9                           0.613                3.97              0.094                                 ok           False                  False
   WBD           95.56               45            0.02              0.00         30.95                37.62         0.557            pass              0.881             75.0                           0.408                9.58              0.818                                 ok           False                  False
  ASML           83.78               37            0.36              4.57       1809.71                42.37         0.532            pass              0.511             59.1                           0.427               10.77              0.953                                 ok           False                  False
   XEL           82.35               17            0.71              0.35         70.33                18.32         0.522            pass              0.309             49.0                           0.579               -4.96             -0.448            downtrend_blocked_slope           False                  False
  QCOM           92.68               41            0.18              0.24        183.94                56.29         0.521            pass              0.817             75.7                           0.544               -2.65             -0.222           downtrend_blocked_streak           False                  False
   EXC           82.35               17            0.63              0.18         40.32                14.97         0.506            pass              0.330             56.8                           0.632               -5.85             -0.583 downtrend_blocked_slope_and_streak           False                  False
  NXPI           85.71               35            0.48              0.80        237.19                38.88         0.494 below_threshold              0.506             45.9                           0.420                3.70              0.362                                 ok           False                  False
  NFLX           68.75               16            1.96              0.96         69.17                37.25         0.490 below_threshold              0.114              8.4                           0.240               -9.42             -0.758            downtrend_blocked_slope           False                  False
  TMUS           87.88               33            0.45              0.51        162.86                33.48         0.488 below_threshold              0.637             75.0                           0.435               -2.46             -0.220                                 ok           False                  False
  PANW           80.95               42            0.75              2.09        396.41                66.50         0.484 below_threshold              0.487             71.0                           0.573                5.14              0.709                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-10-01T10:55:06.231186-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:50:06.456306-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:45:05.877463-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:40:06.481988-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:35:05.852380-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.72, "early_entry_score": 0.681, "early_reclaim_pct": 70.0, "entry_ask": 9.65, "entry_bid": 9.45, "entry_mode": "early", "entry_option_price": 9.55, "hypothetical_budget": 40682.15, "hypothetical_contracts": 42, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 2.09, "option_volume": 30.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.664, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.601, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.681, "early_reclaim_pct": 70.0, "matched_signals": 36, "recovery_stability_score": 0.664, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.601, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T10:30:06.297873-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:25:05.417104-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:20:05.454377-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T10:20:05.454377-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"asset_type": "option", "contract_symbol": "META261120C00735000", "fill_price": 43.5825, "pnl": -3874.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "META"}
2026-10-01T10:15:02.462190-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001105506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001105506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001105506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001105506)

</details>
