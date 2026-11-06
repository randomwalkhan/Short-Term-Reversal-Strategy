# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 10:35:02 EST`
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

- Cash: `$123,162.80`
- Equity: `$123,162.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           93.75               16            0.88              0.23         36.79                35.93         0.580          pass              0.682             72.5                           0.812                5.44              0.608                                 ok            True                  False
 CMCSA           93.33               15            1.06              0.19         24.87                35.54         0.566          pass              0.663             72.7                           0.805                8.79              1.416                                 ok            True                  False
   KHC           85.71               14            1.78              0.31         25.19                36.03         0.535          pass              0.399             55.4                           0.758                0.28              0.339                                 ok            True                  False
  FTNT           80.77               26            1.89              1.62        121.82                92.45         0.648          pass              0.231             13.2                           0.138              -33.22             -4.922 downtrend_blocked_slope_and_streak           False                  False
  IDXX           97.78               45            0.14              0.67        670.42                77.01         0.626          pass              0.949             95.4                           0.844               19.52              2.459                                 ok           False                  False
  ISRG           87.50                8            2.10              6.88        465.57                42.48         0.569          pass              0.321             21.5                           0.211                1.42              0.372                                 ok           False                  False
  PAYX           75.00                4            2.12              1.77        118.74                35.22         0.555          pass              0.209             51.2                           0.616                0.10              0.519                                 ok           False                  False
   CSX           66.67                6            1.65              0.59         50.58                30.62         0.552          pass              0.126             23.6                           0.284               -1.58             -0.173                                 ok           False                  False
   EXC           72.73               11            1.18              0.39         46.36                23.57         0.540          pass              0.227             55.5                           0.718                3.49              0.447                                 ok           False                  False
   TRI           75.00                8            3.16              2.61        116.99                57.70         0.538          pass              0.156             34.0                           0.648               -7.14             -0.488            downtrend_blocked_slope           False                  False
   ADP           72.73               11            1.56              3.35        305.70                28.50         0.532          pass              0.232             57.5                           0.649               -0.60              0.246                                 ok           False                  False
  MDLZ           93.10               29            0.16              0.08         66.79                30.66         0.531          pass              0.815             95.3                           0.890                4.56              0.778                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         detail
2026-11-06T10:35:02.947980-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:30:05.862007-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "MSFT261218C00535000", "current_drop_pct": 0.61, "early_entry_score": 0.823, "early_reclaim_pct": 79.4, "entry_ask": 21.65, "entry_bid": 21.1, "entry_mode": "early", "entry_option_price": 21.375, "hypothetical_budget": 61581.4, "hypothetical_contracts": 28, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 3628.0, "option_spread_pct": 2.57, "option_volume": 42.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.763, "shadow_only": true, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.509, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.823, "early_reclaim_pct": 79.4, "matched_signals": 30, "recovery_stability_score": 0.763, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.509, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:25:04.812264-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:20:05.873622-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                        {"contract_symbol": "MSFT261218C00535000", "current_drop_pct": 0.56, "early_entry_score": 0.828, "early_reclaim_pct": 81.0, "entry_ask": 19.7, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 19.15, "hypothetical_budget": 61581.4, "hypothetical_contracts": 32, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 3628.0, "option_spread_pct": 5.74, "option_volume": 34.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.749, "shadow_only": true, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.512, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.828, "early_reclaim_pct": 81.0, "matched_signals": 30, "recovery_stability_score": 0.749, "success_rate": 100.0, "ticker": "MSFT", "timing_score": 0.512, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:15:06.200919-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:10:06.574666-05:00 early_entry_1010 early_entry_shadow   {"contract_symbol": "IDXX261218C00670000", "current_drop_pct": 0.61, "early_entry_score": 0.88, "early_reclaim_pct": 80.4, "entry_ask": 31.1, "entry_bid": 25.9, "entry_mode": "early", "entry_option_price": 28.5, "hypothetical_budget": 61581.4, "hypothetical_contracts": 21, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 7.0, "option_spread_pct": 18.25, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.847, "shadow_only": true, "success_rate": 97.22, "ticker": "IDXX", "timing_score": 0.651, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.88, "early_reclaim_pct": 80.4, "matched_signals": 36, "recovery_stability_score": 0.847, "success_rate": 97.22, "ticker": "IDXX", "timing_score": 0.651, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 82.4, "matched_signals": 37, "recovery_stability_score": 0.911, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.426, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T10:05:04.744572-05:00 early_entry_1005 early_entry_shadow {"contract_symbol": "IDXX261218C00660000", "current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "entry_ask": 34.8, "entry_bid": 29.0, "entry_mode": "early", "entry_option_price": 31.9, "hypothetical_budget": 61581.4, "hypothetical_contracts": 19, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 18.18, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.776, "shadow_only": true, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "top_candidates": [{"current_drop_pct": 0.88, "early_entry_score": 0.839, "early_reclaim_pct": 71.5, "matched_signals": 34, "recovery_stability_score": 0.776, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.647, "trend_health_status": "ok"}, {"current_drop_pct": 0.57, "early_entry_score": 0.715, "early_reclaim_pct": 72.0, "matched_signals": 39, "recovery_stability_score": 0.724, "success_rate": 89.74, "ticker": "TTWO", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T10:00:04.754305-05:00 early_entry_1000 early_entry_shadow {"contract_symbol": "IDXX261218C00660000", "current_drop_pct": 0.85, "early_entry_score": 0.842, "early_reclaim_pct": 72.4, "entry_ask": 34.8, "entry_bid": 28.1, "entry_mode": "early", "entry_option_price": 31.45, "hypothetical_budget": 61581.4, "hypothetical_contracts": 19, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 6.0, "option_spread_pct": 21.3, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.777, "shadow_only": true, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.648, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.842, "early_reclaim_pct": 72.4, "matched_signals": 34, "recovery_stability_score": 0.777, "success_rate": 97.06, "ticker": "IDXX", "timing_score": 0.648, "trend_health_status": "ok"}, {"current_drop_pct": 0.62, "early_entry_score": 0.696, "early_reclaim_pct": 81.0, "matched_signals": 36, "recovery_stability_score": 0.872, "success_rate": 88.89, "ticker": "SBUX", "timing_score": 0.429, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-06T09:50:05.832497-05:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "ORLY261218C00095000", "fill_price": 1.6875, "pnl": -6468.75, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ORLY"}
2026-11-06T00:00:05.873156-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 91, 'empty': 2}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106103502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106103502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106103502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106103502)

</details>
