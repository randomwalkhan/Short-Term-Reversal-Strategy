# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 14:50:05 EDT`
Last processed slot: `entry_1500`

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
    ZS           97.87               47            0.02              0.03        199.41                78.48         0.632            pass              0.955             97.2                           0.484                0.97             -0.227                                 ok           False                  False
  AMGN            0.00                2            2.39              7.06        418.48                46.02         0.531            pass              0.105             17.4                           0.417                8.33              0.944                                 ok           False                  False
  NFLX           70.59               17            1.70              0.83         69.22                37.25         0.502            pass              0.197             33.2                           0.492               -9.18             -0.746            downtrend_blocked_slope           False                  False
   XEL           86.21               29            0.13              0.07         70.45                18.32         0.494 below_threshold              0.613             90.3                           0.630               -4.41             -0.422            downtrend_blocked_slope           False                  False
  TMUS           85.71               28            0.88              1.01        162.65                33.48         0.485 below_threshold              0.473             50.7                           0.280               -2.89             -0.240                                 ok           False                  False
  ABNB           87.18               39            0.56              0.63        160.38                40.44         0.476 below_threshold              0.638             68.6                           0.668               -3.72             -0.482                                 ok           False                  False
  MDLZ           96.55               29            0.11              0.05         57.80                16.32         0.470 below_threshold              0.838             88.2                           0.488               -6.08             -0.523 downtrend_blocked_slope_and_streak           False                  False
   PEP           76.47               17            0.73              0.64        126.44                14.74         0.470 below_threshold              0.145             17.1                           0.282               -5.88             -0.429            downtrend_blocked_slope           False                  False
   KHC           88.89                9            1.79              0.28         22.60                20.30         0.465 below_threshold              0.409             41.9                           0.508               -9.77             -0.876 downtrend_blocked_slope_and_streak           False                  False
 CMCSA           83.72               43            0.02              0.00         21.76                32.06         0.464 below_threshold              0.639             97.7                           0.664               -5.04             -0.636 downtrend_blocked_slope_and_streak           False                  False
  PANW           78.95               38            1.42              3.95        395.62                66.50         0.464 below_threshold              0.369             45.2                           0.446                4.43              0.678                                 ok           False                  False
  BKNG           81.25               32            1.12              1.28        162.36                39.63         0.458 below_threshold              0.359             44.5                           0.456               -5.54             -0.429            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-10-01T14:50:05.514279-04:00       entry_1500      entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate"}
2026-10-01T14:50:05.514279-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-01", "training_samples": 5895, "window": 5}
2026-10-01T12:00:06.030645-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:55:01.414923-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "STX261030C00915000", "current_drop_pct": 0.54, "early_entry_score": 0.696, "early_reclaim_pct": 82.7, "entry_ask": 80.1, "entry_bid": 67.5, "entry_mode": "early", "entry_option_price": 73.8, "hypothetical_budget": 40682.15, "hypothetical_contracts": 5, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 25.0, "option_spread_pct": 17.07, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.696, "early_reclaim_pct": 82.7, "matched_signals": 35, "recovery_stability_score": 0.75, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T11:50:04.589481-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.7, "early_entry_score": 0.683, "early_reclaim_pct": 70.7, "entry_ask": 10.25, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 10.175, "hypothetical_budget": 40682.15, "hypothetical_contracts": 39, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 1.47, "option_volume": 55.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.683, "early_reclaim_pct": 70.7, "matched_signals": 36, "recovery_stability_score": 0.627, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.602, "trend_health_status": "ok"}, {"current_drop_pct": 0.75, "early_entry_score": 0.674, "early_reclaim_pct": 75.8, "matched_signals": 35, "recovery_stability_score": 0.757, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:45:02.515296-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:40:06.090435-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.77, "early_entry_score": 0.673, "early_reclaim_pct": 67.8, "entry_ask": 10.25, "entry_bid": 10.05, "entry_mode": "early", "entry_option_price": 10.15, "hypothetical_budget": 40682.15, "hypothetical_contracts": 40, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 1.97, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.673, "early_reclaim_pct": 67.8, "matched_signals": 36, "recovery_stability_score": 0.661, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:35:06.431749-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:30:05.726555-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:25:06.486320-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.79, "early_entry_score": 0.671, "early_reclaim_pct": 66.9, "entry_ask": 9.8, "entry_bid": 9.55, "entry_mode": "early", "entry_option_price": 9.675, "hypothetical_budget": 40682.15, "hypothetical_contracts": 42, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 2.58, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.563, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.596, "top_candidates": [{"current_drop_pct": 0.79, "early_entry_score": 0.671, "early_reclaim_pct": 66.9, "matched_signals": 36, "recovery_stability_score": 0.563, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.596, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001145005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001145005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001145005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001145005)

</details>
