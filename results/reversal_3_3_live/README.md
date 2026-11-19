# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 12:55:03 EST`
Last processed slot: `manage_1300`

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
   APP           91.30               46            0.57              1.55        390.25               121.61         0.745          pass              0.826             83.5                           0.502                9.15              0.419                  ok            True                  False
  IDXX           96.97               33            0.98              4.78        696.42                78.12         0.698          pass              0.744             40.4                           0.543                3.12              0.207                  ok            True                  False
  ASML           81.82               33            0.54              5.26       1393.02                65.53         0.575          pass              0.471             70.5                           0.470                2.29             -0.368                  ok            True                  False
   TXN           92.59               27            0.94              1.93        291.60                59.49         0.574          pass              0.719             70.9                           0.563                4.15              0.321                  ok            True                  False
  ABNB           80.95               21            1.70              2.15        179.29                55.20         0.571          pass              0.257             33.6                           0.343                4.12             -0.125                  ok            True                  False
 CMCSA           93.75               16            1.51              0.27         25.13                34.19         0.556          pass              0.547             28.3                           0.504               -0.36              0.262                  ok            True                  False
  AAPL          100.00               22            0.81              2.01        351.59                27.20         0.547          pass              0.691             52.0                           0.601                1.65              0.220                  ok            True                  False
  REGN           84.21               38            0.68              4.51        943.60                54.27         0.545          pass              0.577             74.5                           0.668                4.01              0.517                  ok            True                  False
  COST           86.36               22            0.63              4.84       1094.55                23.52         0.538          pass              0.450             48.7                           0.628                2.26              0.452                  ok            True                  False
  VRSK           85.29               34            0.69              0.97        201.89                47.31         0.522          pass              0.566             70.9                           0.747               -4.99             -0.126                  ok            True                  False
   XEL           86.67               15            1.17              0.66         80.37                18.19         0.511          pass              0.385             40.9                           0.699               -0.82              0.056                  ok            True                  False
   ADP           85.00               20            1.20              2.56        304.47                28.97         0.511          pass              0.354             34.3                           0.479               -1.70              0.062                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119125503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119125503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119125503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119125503)

</details>
