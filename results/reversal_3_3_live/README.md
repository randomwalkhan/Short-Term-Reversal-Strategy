# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-20 10:20:05 EDT`
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

- Cash: `$144,831.80`
- Equity: `$144,831.80`
- Realized PnL: `$134,831.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-20)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
   ADP     option         option ADP261120C00290000     70          2026-10-19         2026-10-20          9.3        11.2 13300.0   20.430108 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   CEG           88.89               27            1.16              2.15        262.27                59.49         0.576            pass              0.538             43.3                           0.550              -13.41             -1.452 downtrend_blocked_slope_and_streak           False                  False
  SNPS           81.48               27            1.02              3.24        453.19                54.29         0.572            pass              0.407             65.6                           0.819              -10.93             -1.337 downtrend_blocked_slope_and_streak           False                  False
  META           80.00               10            2.01              9.93        701.18                40.24         0.534            pass              0.179             41.8                           0.687               -6.45             -0.389 downtrend_blocked_slope_and_streak           False                  False
    ZS           93.33               45            0.13              0.20        212.45                62.14         0.529            pass              0.893             94.7                           0.890                0.00             -0.266                                 ok           False                  False
  DRAM           84.38               32            0.70              0.24         48.23                49.05         0.504            pass              0.564             83.5                           0.943              -19.37             -2.669 downtrend_blocked_slope_and_streak           False                  False
  MSFT           96.43               28            0.49              1.83        532.74                21.83         0.483 below_threshold              0.766             66.0                           0.715                0.30              0.075                                 ok           False                  False
  CDNS           83.33               36            0.67              1.52        325.21                37.22         0.467 below_threshold              0.538             76.3                           0.888               -9.97             -1.244 downtrend_blocked_slope_and_streak           False                  False
   LIN           82.14               28            0.49              1.73        502.70                13.47         0.462 below_threshold              0.273             16.6                           0.165                2.25              0.383                                 ok           False                  False
  ASML           76.67               30            0.61              7.08       1644.09                29.62         0.460 below_threshold              0.389             69.9                           0.786              -10.75             -1.238            downtrend_blocked_slope           False                  False
  PANW           85.00               40            1.11              2.69        345.80                55.73         0.450 below_threshold              0.584             68.4                           0.846              -18.29             -2.194 downtrend_blocked_slope_and_streak           False                  False
  CPRT           58.33               12            2.64              0.51         27.29                31.97         0.449 below_threshold              0.098             13.4                           0.195               -0.13              0.173                                 ok           False                  False
  IDXX           93.02               43            0.25              0.98        555.38                25.12         0.443 below_threshold              0.713             40.4                           0.328                7.56              1.016                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                detail
2026-10-20T10:20:05.290913-04:00 early_entry_1020 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:15:05.434773-04:00 early_entry_1015 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:10:06.028828-04:00 early_entry_1010 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:05:04.298275-04:00 early_entry_1005 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T10:00:02.343877-04:00 early_entry_1000 early_entry_shadow                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-20T09:50:06.258363-04:00      manage_1000               exit {"asset_type": "option", "contract_symbol": "ADP261120C00290000", "fill_price": 11.2, "pnl": 13300.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.43, "ticker": "ADP"}
2026-10-20T00:00:06.202426-04:00     data_refresh       data_refresh                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-10-19T15:10:06.181493-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-10-19T15:07:09.479134-04:00       entry_1500       slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-10-19T14:50:05.293487-04:00       entry_1500     timing_overlay                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-19", "training_samples": 6120, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261020102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261020102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261020102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261020102005)

</details>
