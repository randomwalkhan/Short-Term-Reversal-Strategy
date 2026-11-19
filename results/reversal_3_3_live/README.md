# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 13:25:04 EST`
Last processed slot: `manage_1330`

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

- Cash: `$100,946.30`
- Equity: `$100,946.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00400000     15          2026-11-18         2026-11-19        33.15      29.835 -4972.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   APP           90.32               31            1.73              4.73        388.88               121.61         0.761          pass              0.640             49.4                           0.261                7.88              0.365                  ok            True                  False
  IDXX           96.00               25            1.33              6.51        695.68                78.12         0.721          pass              0.629             18.8                           0.195                2.75              0.191                  ok            True                  False
   BKR           87.10               31            0.59              0.20         47.22                58.30         0.597          pass              0.595             68.5                           0.486                2.26              0.039                  ok            True                  False
   TXN           89.47               19            1.32              2.71        291.27                59.49         0.597          pass              0.549             59.0                           0.406                3.74              0.304                  ok            True                  False
  ASML           80.00               25            1.05             10.26       1390.87                65.53         0.591          pass              0.286             42.4                           0.295                1.77             -0.391                  ok            True                  False
 GOOGL           82.76               29            0.68              1.34        281.87                55.39         0.577          pass              0.381             40.9                           0.289               -0.72             -0.155                  ok            True                  False
 CMCSA           92.86               14            1.55              0.27         25.12                34.19         0.566          pass              0.505             26.4                           0.411               -0.40              0.260                  ok            True                  False
  AAPL          100.00               19            0.98              2.41        351.41                27.20         0.556          pass              0.643             42.3                           0.438                1.48              0.212                  ok            True                  False
  REGN           83.33               36            0.82              5.42        943.21                54.27         0.548          pass              0.525             69.4                           0.631                3.86              0.511                  ok            True                  False
  TMUS           82.76               29            0.86              0.99        163.60                47.11         0.543          pass              0.445             63.6                           0.726                1.25              0.087                  ok            True                  False
   CEG           85.71               14            2.64              4.86        260.66                59.92         0.527          pass              0.310             26.0                           0.258                6.90              0.502                  ok            True                  False
   XEL           83.33               12            1.26              0.71         80.35                18.19         0.521          pass              0.263             36.2                           0.521               -0.91              0.052                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-19T12:00:04.585643-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:55:04.624666-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:50:06.328021-05:00 early_entry_1150 early_entry_shadow {"contract_symbol": "GILD270115C00155000", "current_drop_pct": 0.81, "early_entry_score": 0.693, "early_reclaim_pct": 67.4, "entry_ask": 16.15, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 15.1, "hypothetical_budget": 50473.15, "hypothetical_contracts": 33, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1446.0, "option_spread_pct": 13.91, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.829, "shadow_only": true, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.47, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.693, "early_reclaim_pct": 67.4, "matched_signals": 33, "recovery_stability_score": 0.829, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.47, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-19T11:45:05.650251-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:40:04.570482-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:35:04.658979-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:30:04.584516-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:25:05.811336-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:20:04.620034-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:15:06.374653-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119132504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119132504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119132504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119132504)

</details>
