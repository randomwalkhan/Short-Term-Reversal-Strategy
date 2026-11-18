# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 11:15:04 EST`
Last processed slot: `early_entry_1115`

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

- Cash: `$105,918.80`
- Equity: `$105,918.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP261218C00400000     17          2026-11-17         2026-11-18         31.3       28.17 -5321.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   APP           90.91               44            0.79              2.21        397.99               121.47         0.761          pass              0.740             57.5                           0.512               45.64              2.276                       ok            True                  False
   TXN           89.47               19            1.36              2.81        294.65                59.80         0.627          pass              0.447             24.1                           0.312               -6.31              0.172                       ok            True                  False
   BKR           87.10               31            0.55              0.18         47.38                58.51         0.619          pass              0.483             30.7                           0.174               -4.90             -0.030                       ok            True                  False
 CMCSA           91.67               24            0.57              0.10         25.27                34.73         0.574          pass              0.626             54.7                           0.340                1.27              0.291                       ok            True                  False
   ADP           86.96               23            0.98              2.12        307.38                28.72         0.541          pass              0.386             19.8                           0.155                0.57              0.183                       ok            True                  False
  COST           82.61               23            0.60              4.63       1108.09                22.66         0.539          pass              0.352             47.4                           0.369                5.45              0.630                       ok            True                  False
  META           82.14               28            0.98              4.24        617.05                41.87         0.536          pass              0.290             19.8                           0.286               -2.73              0.003                       ok            True                  False
   CEG           90.91               33            1.33              2.50        267.00                61.66         0.533          pass              0.623             41.7                           0.320                7.81              1.123                       ok            True                  False
   WMT           87.50               24            0.71              0.64        127.25                25.55         0.530          pass              0.535             62.9                           0.550               -1.98              0.005                       ok            True                  False
  GILD           88.46               26            1.02              1.22        169.74                31.94         0.509          pass              0.503             39.8                           0.388               -3.42             -0.118                       ok            True                  False
  SOXL           65.52               29            2.20              0.76         48.75               265.73         0.935          pass              0.394             58.0                           0.458              -28.03             -0.460  downtrend_blocked_slope           False                  False
  INTC           68.97               29            1.85              0.71         54.86               143.31         0.817          pass              0.332             41.1                           0.447               -7.07             -0.119 downtrend_blocked_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-18T11:15:04.160916-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:10:06.093723-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "APP261218C00400000", "current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "entry_ask": 27.1, "entry_bid": 25.2, "entry_mode": "early", "entry_option_price": 26.15, "hypothetical_budget": 52959.4, "hypothetical_contracts": 20, "matched_signals": 44, "option_liquidity_status": "ok", "option_open_interest": 1251.0, "option_spread_pct": 7.27, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.756, "early_reclaim_pct": 62.9, "matched_signals": 44, "recovery_stability_score": 0.563, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.766, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:05:06.391620-05:00 early_entry_1105 early_entry_shadow                                          {"contract_symbol": "TXN270115C00295000", "current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "entry_ask": 22.2, "entry_bid": 21.85, "entry_mode": "early", "entry_option_price": 22.025, "hypothetical_budget": 52959.4, "hypothetical_contracts": 24, "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 584.0, "option_spread_pct": 1.59, "option_volume": 159.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.634, "shadow_only": true, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.783, "early_reclaim_pct": 69.9, "matched_signals": 32, "recovery_stability_score": 0.634, "success_rate": 93.75, "ticker": "TXN", "timing_score": 0.602, "trend_health_status": "ok"}, {"current_drop_pct": 0.65, "early_entry_score": 0.767, "early_reclaim_pct": 71.4, "matched_signals": 37, "recovery_stability_score": 0.606, "success_rate": 91.89, "ticker": "CEG", "timing_score": 0.552, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T10:59:10.549422-05:00 early_entry_1055 early_entry_shadow {"contract_symbol": "CEG261224C00265000", "current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "entry_ask": 19.0, "entry_bid": 15.8, "entry_mode": "early", "entry_option_price": 17.4, "hypothetical_budget": 52959.4, "hypothetical_contracts": 30, "matched_signals": 38, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 18.39, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.787, "early_reclaim_pct": 74.0, "matched_signals": 38, "recovery_stability_score": 0.571, "success_rate": 92.11, "ticker": "CEG", "timing_score": 0.55, "trend_health_status": "ok"}, {"current_drop_pct": 0.7, "early_entry_score": 0.755, "early_reclaim_pct": 62.4, "matched_signals": 44, "recovery_stability_score": 0.576, "success_rate": 90.91, "ticker": "APP", "timing_score": 0.765, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-18T10:59:10.549422-05:00      manage_1100               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "APP261218C00400000", "fill_price": 28.17, "pnl": -5321.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "APP"}
2026-11-18T00:00:06.344355-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-11-17T15:10:05.988632-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T15:05:03.951251-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T15:00:05.898014-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-11-17T14:55:04.972939-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118111504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118111504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118111504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118111504)

</details>
