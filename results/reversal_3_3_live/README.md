# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 10:35:05 EST`
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

- Cash: `$117,024.80`
- Equity: `$117,024.80`
- Realized PnL: `$107,024.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  QCOM           84.00               25            1.40              1.69        171.74                68.34         0.602          pass              0.404             45.9                           0.355                4.92              0.713                      ok            True                  False
   CEG           87.50               32            1.30              2.55        278.68                61.55         0.560          pass              0.535             44.1                           0.323                7.34              1.237                      ok            True                  False
  DXCM           83.33               36            0.74              0.43         83.15                50.11         0.540          pass              0.426             36.6                           0.346               -2.41             -0.408                      ok            True                  False
  ISRG           92.31               39            0.53              1.65        442.88                45.74         0.534          pass              0.754             59.7                           0.500                1.00             -0.262                      ok            True                  False
   HON           82.76               29            0.60              0.94        222.06                32.11         0.534          pass              0.278              8.2                           0.230               -0.87              0.015                      ok            True                  False
  MSFT           96.88               32            0.61              2.25        522.91                36.51         0.530          pass              0.761             53.7                           0.401                2.67             -0.073                      ok            True                  False
  AAPL           96.67               30            0.52              1.29        355.72                27.52         0.528          pass              0.716             43.4                           0.379                4.84              0.595                      ok            True                  False
  NXPI           91.67               12            2.61              4.85        263.01                48.08         0.528          pass              0.485             35.9                           0.650                0.36              0.296                      ok            True                  False
  ALNY           61.11               18            2.67              3.08        163.72               110.81         0.720          pass              0.163             12.7                           0.220                1.67              0.126                      ok           False                  False
  FTNT           68.42               19            2.70              2.41        126.19                93.31         0.667          pass              0.173             15.5                           0.227               -1.93              0.006                      ok           False                  False
  INTC           60.00               10            6.45              2.69         58.51               143.21         0.653          pass              0.083              5.9                           0.158               -6.94              0.108                      ok           False                  False
   BKR           60.00               10            2.59              0.90         49.06                57.94         0.579          pass              0.112             17.9                           0.321               -8.78             -0.549 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T10:35:05.683081-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:30:06.080468-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:25:05.577386-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:20:06.177663-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:15:06.368361-05:00 early_entry_1015 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "entry_ask": 11.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.225, "hypothetical_budget": 58512.4, "hypothetical_contracts": 52, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.01, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "matched_signals": 36, "recovery_stability_score": 0.574, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:10:05.371308-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:05:06.161722-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:00:04.523594-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T09:20:05.612126-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {'saved': 91, 'empty': 2}
2026-11-06T16:10:06.061391-05:00      manage_1600               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"asset_type": "option", "contract_symbol": "MDLZ261218C00065000", "fill_price": 2.79, "pnl": -6138.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116103505)

</details>
