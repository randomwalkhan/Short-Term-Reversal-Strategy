# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-17 10:20:02 EDT`
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

- Cash: `$65,311.30`
- Equity: `$65,311.30`
- Realized PnL: `$55,311.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-17)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TRI           94.12               34            0.61              0.43        101.12                57.96         0.591          pass              0.779             61.3                           0.646               -4.89             -0.537 downtrend_blocked_slope_and_streak           False                  False
   WMT           85.71               35            0.42              0.31        107.37                39.87         0.543          pass              0.511             45.8                           0.417                0.90              0.097                                 ok           False                  False
  ADSK           86.49               37            0.46              0.71        220.01                56.33         0.541          pass              0.623             72.0                           0.659               -9.28             -0.448 downtrend_blocked_slope_and_streak           False                  False
  CHTR           89.74               39            0.97              0.92        134.61                64.77         0.520          pass              0.507              0.8                           0.154              -15.90             -1.357 downtrend_blocked_slope_and_streak           False                  False
  ADBE           97.22               36            0.65              1.15        250.01                47.92         0.518          pass              0.829             67.8                           0.657              -11.05             -1.054 downtrend_blocked_slope_and_streak           False                  False
   EXC           95.65               23            0.19              0.06         42.42                15.25         0.518          pass              0.718             60.0                           0.345               -2.74             -0.421 downtrend_blocked_slope_and_streak           False                  False
   ADP           96.43               28            0.32              0.62        272.93                24.48         0.517          pass              0.812             80.0                           0.751               -2.53             -0.136                                 ok           False                  False
  INTU          100.00               35            0.59              1.32        317.57                44.10         0.511          pass              0.787             56.3                           0.354               -7.78             -0.550 downtrend_blocked_slope_and_streak           False                  False
   PEP           90.91               22            0.19              0.18        134.26                14.34         0.511          pass              0.578             51.9                           0.357               -3.56             -0.349            downtrend_blocked_slope           False                  False
  VRSK           92.59               27            1.28              1.63        181.05                41.00         0.511          pass              0.532             10.7                           0.127               -4.39             -0.338            downtrend_blocked_slope           False                  False
 CMCSA           92.31               13            2.09              0.35         23.58                34.54         0.503          pass              0.410              3.9                           0.165              -13.33             -1.375 downtrend_blocked_slope_and_streak           False                  False
  CTSH          100.00               38            0.37              0.16         61.78                43.69         0.501          pass              0.853             72.0                           0.600               -2.81             -0.097                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                            detail
2026-09-17T10:20:02.157972-04:00 early_entry_1020 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:15:01.263166-04:00 early_entry_1015 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T10:10:05.493565-04:00 early_entry_1010 early_entry_shadow                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-17T09:20:04.341541-04:00     data_refresh       data_refresh                                                                                                                                                         {'saved': 92, 'empty': 1}
2026-09-16T15:35:01.538068-04:00      manage_1530               exit {"asset_type": "option", "contract_symbol": "PYPL261016C00055000", "fill_price": 1.116, "pnl": -3434.8, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PYPL"}
2026-09-16T15:10:01.578825-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-09-16T15:05:01.537613-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-09-16T15:00:06.128176-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-09-16T14:55:02.603343-04:00       entry_1500       slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-09-16T14:50:31.812161-04:00       entry_1500     timing_overlay                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-09-16", "training_samples": 5761, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260917102002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260917102002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260917102002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260917102002)

</details>
