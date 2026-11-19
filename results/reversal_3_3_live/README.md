# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 14:25:04 EST`
Last processed slot: `manage_1430`

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
   APP           94.44               18            2.98              8.14        387.42               121.61         0.767          pass              0.554             12.9                           0.110                6.51              0.307                  ok            True                  False
  IDXX           96.55               29            1.17              5.70        696.03                78.12         0.709          pass              0.684             29.0                           0.353                2.93              0.198                  ok            True                  False
   BKR           84.00               25            0.89              0.29         47.17                58.30         0.612          pass              0.426             52.8                           0.294                1.96              0.025                  ok            True                  False
  ASML           81.48               27            0.88              8.58       1391.59                65.53         0.591          pass              0.367             51.8                           0.374                1.94             -0.384                  ok            True                  False
   TXN           91.67               24            1.11              2.27        291.46                59.49         0.581          pass              0.659             65.6                           0.519                3.97              0.313                  ok            True                  False
 CMCSA           90.00               10            1.82              0.32         25.10                34.19         0.571          pass              0.363             13.2                           0.128               -0.68              0.248                  ok            True                  False
  MDLZ          100.00               15            1.04              0.49         66.36                28.83         0.570          pass              0.669             59.7                           0.730               -1.42              0.016                  ok            True                  False
  AAPL          100.00               21            0.86              2.13        351.54                27.20         0.550          pass              0.675             49.0                           0.520                1.60              0.218                  ok            True                  False
  TMUS           82.76               29            0.93              1.07        163.56                47.11         0.539          pass              0.436             60.7                           0.624                1.18              0.083                  ok            True                  False
   XEL           83.33               12            1.30              0.74         80.33                18.19         0.518          pass              0.256             34.0                           0.356               -0.96              0.050                  ok            True                  False
   EXC           81.25               16            1.10              0.35         45.87                22.38         0.511          pass              0.262             46.0                           0.477               -2.18             -0.007                  ok            True                  False
   CEG           83.33               12            3.09              5.69        260.30                59.92         0.509          pass              0.193             13.3                           0.168                6.40              0.481                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119142504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119142504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119142504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119142504)

</details>
