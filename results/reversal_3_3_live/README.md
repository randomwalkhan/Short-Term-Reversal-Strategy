# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 12:50:06 EST`
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
   APP           90.70               43            0.92              2.53        389.83               121.61         0.742          pass              0.778             73.0                           0.472                8.76              0.402                  ok            True                  False
  IDXX           96.43               28            1.19              5.82        695.97                78.12         0.713          pass              0.673             27.4                           0.375                2.90              0.197                  ok            True                  False
   TXN           89.47               19            1.46              2.98        291.15                59.49         0.588          pass              0.536             54.9                           0.497                3.60              0.297                  ok            True                  False
  ASML           81.48               27            0.94              9.17       1391.34                65.53         0.587          pass              0.357             48.5                           0.372                1.88             -0.386                  ok            True                  False
  ABNB           80.95               21            1.64              2.07        179.32                55.20         0.575          pass              0.265             36.2                           0.430                4.19             -0.122                  ok            True                  False
   ADI           91.89               37            0.61              1.64        381.28                66.90         0.566          pass              0.771             72.4                           0.507                5.16              0.259                  ok            True                  False
 CMCSA           93.75               16            1.45              0.26         25.13                34.19         0.560          pass              0.556             31.1                           0.564               -0.30              0.265                  ok            True                  False
  REGN           82.35               34            0.89              5.89        943.00                54.27         0.556          pass              0.478             66.7                           0.615                3.79              0.508                  ok            True                  False
  COST           90.48               21            0.70              5.37       1094.32                23.52         0.544          pass              0.536             43.0                           0.606                2.19              0.449                  ok            True                  False
  AAPL           95.65               23            0.74              1.82        351.67                27.20         0.541          pass              0.710             56.5                           0.678                1.73              0.224                  ok            True                  False
  TMUS           82.14               28            0.99              1.14        163.53                47.11         0.541          pass              0.405             58.1                           0.736                1.12              0.081                  ok            True                  False
  VRSK           84.38               32            0.79              1.12        201.83                47.31         0.528          pass              0.516             66.6                           0.702               -5.09             -0.130                  ok            True                  False
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

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119125006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119125006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119125006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119125006)

</details>
