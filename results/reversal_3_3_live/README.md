# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-01 15:00:06 EDT`
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
    ZS           97.87               47            0.03              0.04        199.40                78.48         0.632            pass              0.953             96.5                           0.466                0.96             -0.227                                 ok           False                  False
   WBD           95.56               45            0.03              0.01         30.95                37.62         0.555            pass              0.806             50.0                           0.408                9.56              0.817                                 ok           False                  False
  AMGN            0.00                2            2.42              7.13        418.45                46.02         0.529            pass              0.103             16.6                           0.311                8.31              0.943                                 ok           False                  False
  QCOM           92.68               41            0.20              0.25        183.93                56.29         0.520            pass              0.813             74.3                           0.348               -2.67             -0.222           downtrend_blocked_streak           False                  False
   XEL           85.19               27            0.17              0.08         70.44                18.32         0.503            pass              0.565             87.8                           0.582               -4.44             -0.423            downtrend_blocked_slope           False                  False
  NFLX           68.75               16            1.85              0.90         69.19                37.25         0.497 below_threshold              0.172             27.6                           0.405               -9.31             -0.752            downtrend_blocked_slope           False                  False
  TMUS           85.71               28            0.89              1.01        162.65                33.48         0.485 below_threshold              0.472             50.4                           0.298               -2.90             -0.240                                 ok           False                  False
  ABNB           88.10               42            0.18              0.20        160.56                40.44         0.484 below_threshold              0.734             89.8                           0.779               -3.36             -0.464                                 ok           False                  False
  MDLZ           96.55               29            0.09              0.03         57.81                16.32         0.472 below_threshold              0.847             90.9                           0.472               -6.06             -0.521 downtrend_blocked_slope_and_streak           False                  False
  PANW           79.49               39            1.31              3.64        395.75                66.50         0.465 below_threshold              0.388             49.4                           0.422                4.55              0.683                                 ok           False                  False
  REGN           75.00                4            2.28             12.08        753.09                28.88         0.461 below_threshold              0.183             45.8                           0.512               -6.14             -0.718 downtrend_blocked_slope_and_streak           False                  False
   KHC           88.89                9            1.89              0.30         22.59                20.30         0.459 below_threshold              0.399             38.6                           0.443               -9.87             -0.881 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-10-01T15:00:06.279684-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-01T14:55:05.658187-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-10-01T14:50:05.514279-04:00       entry_1500      entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate"}
2026-10-01T14:50:05.514279-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-01", "training_samples": 5895, "window": 5}
2026-10-01T12:00:06.030645-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:55:01.414923-04:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                 {"contract_symbol": "STX261030C00915000", "current_drop_pct": 0.54, "early_entry_score": 0.696, "early_reclaim_pct": 82.7, "entry_ask": 80.1, "entry_bid": 67.5, "entry_mode": "early", "entry_option_price": 73.8, "hypothetical_budget": 40682.15, "hypothetical_contracts": 5, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 25.0, "option_spread_pct": 17.07, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.75, "shadow_only": true, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.54, "early_entry_score": 0.696, "early_reclaim_pct": 82.7, "matched_signals": 35, "recovery_stability_score": 0.75, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-01T11:50:04.589481-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.7, "early_entry_score": 0.683, "early_reclaim_pct": 70.7, "entry_ask": 10.25, "entry_bid": 10.1, "entry_mode": "early", "entry_option_price": 10.175, "hypothetical_budget": 40682.15, "hypothetical_contracts": 39, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 1.47, "option_volume": 55.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.627, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.602, "top_candidates": [{"current_drop_pct": 0.7, "early_entry_score": 0.683, "early_reclaim_pct": 70.7, "matched_signals": 36, "recovery_stability_score": 0.627, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.602, "trend_health_status": "ok"}, {"current_drop_pct": 0.75, "early_entry_score": 0.674, "early_reclaim_pct": 75.8, "matched_signals": 35, "recovery_stability_score": 0.757, "success_rate": 88.57, "ticker": "STX", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:45:02.515296-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-01T11:40:06.090435-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                        {"contract_symbol": "INTC261030C00119000", "current_drop_pct": 0.77, "early_entry_score": 0.673, "early_reclaim_pct": 67.8, "entry_ask": 10.25, "entry_bid": 10.05, "entry_mode": "early", "entry_option_price": 10.15, "hypothetical_budget": 40682.15, "hypothetical_contracts": 40, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 353.0, "option_spread_pct": 1.97, "option_volume": 54.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.598, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.673, "early_reclaim_pct": 67.8, "matched_signals": 36, "recovery_stability_score": 0.661, "success_rate": 88.89, "ticker": "INTC", "timing_score": 0.598, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-01T11:35:06.431749-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261001150006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261001150006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261001150006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261001150006)

</details>
