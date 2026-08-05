# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 13:35:03 EDT`
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

- Cash: `$31,840.75`
- Equity: `$31,840.75`
- Realized PnL: `$21,840.75`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-05)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   PEP     option         option PEP260918C00140000     40          2026-08-04         2026-08-05          4.1        3.69 -1640.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  GEHC           94.12               34            0.65              0.32         70.12                58.11         0.627          pass              0.642             14.2                           0.283               13.73              1.700                       ok            True                  False
 CMCSA           83.33               12            1.40              0.25         24.82                44.00         0.599          pass              0.286             41.2                           0.602                4.51              1.002                       ok            True                  False
  CTAS           90.48               21            1.21              1.73        202.91                37.77         0.584          pass              0.523             37.5                           0.655               -0.09             -0.113                       ok            True                  False
  PAYX          100.00               15            0.98              0.81        118.31                35.13         0.580          pass              0.696             68.3                           0.676                7.21              0.754                       ok            True                  False
  MRVL           80.00               35            1.94              2.97        217.32               100.52         0.569          pass              0.364             46.9                           0.286                1.59              0.252                       ok            True                  False
  MSFT           80.00               35            0.89              3.06        491.50                57.86         0.548          pass              0.287             21.8                           0.290               25.13              3.065                       ok            True                  False
   ADP           96.55               29            0.51              0.96        270.21                35.53         0.517          pass              0.785             68.9                           0.536               10.75              1.143                       ok            True                  False
  CPRT           82.35               17            2.16              0.44         29.21                38.86         0.503          pass              0.232             24.0                           0.397                5.87              0.601                       ok            True                  False
  DRAM           75.00               36            0.19              0.07         54.86               109.93         0.734          pass              0.532             95.2                           0.670               -5.17             -0.558 downtrend_blocked_streak           False                  False
  SOXL           80.65               31            3.47              3.40        138.44               182.46         0.717          pass              0.382             50.9                           0.337              -16.12             -1.823 downtrend_blocked_streak           False                  False
  AMAT           90.62               32            1.13              4.32        544.77                87.24         0.656          pass              0.680             61.6                           0.408               -2.43             -0.297 downtrend_blocked_streak           False                  False
  TMUS           77.78                9            2.50              3.10        175.88                55.59         0.621          pass              0.142             26.5                           0.395               -9.51             -0.451  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                         detail
2026-08-05T12:00:04.693066-04:00 early_entry_1200 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:55:03.663510-04:00 early_entry_1155 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00 early_entry_1150 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:50:01.727726-04:00      manage_1200               exit {"asset_type": "option", "contract_symbol": "PEP260918C00140000", "fill_price": 3.69, "pnl": -1640.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PEP"}
2026-08-05T11:45:04.673736-04:00 early_entry_1145 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:40:04.834796-04:00 early_entry_1140 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:35:01.719935-04:00 early_entry_1135 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:30:04.698899-04:00 early_entry_1130 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:25:03.699168-04:00 early_entry_1125 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T11:20:04.670230-04:00 early_entry_1120 early_entry_shadow                                                                                                          {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805133503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805133503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805133503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805133503)

</details>
