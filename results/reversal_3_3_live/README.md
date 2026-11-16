# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 10:45:04 EST`
Last processed slot: `early_entry_1045`

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
  QCOM           88.57               35            0.79              0.96        172.06                68.34         0.584          pass              0.662             69.4                           0.548                5.57              0.741                      ok            True                  False
   CEG           87.88               33            1.17              2.28        278.79                61.55         0.562          pass              0.569             49.9                           0.425                7.49              1.243                      ok            True                  False
  ISRG           90.62               32            0.85              2.63        442.46                45.74         0.557          pass              0.594             36.0                           0.373                0.68             -0.277                      ok            True                  False
  DXCM           83.33               36            0.82              0.48         83.13                50.11         0.535          pass              0.405             29.9                           0.349               -2.49             -0.412                      ok            True                  False
  NXPI           92.86               14            2.34              4.35        263.23                48.08         0.533          pass              0.550             42.5                           0.629                0.64              0.309                      ok            True                  False
  AAPL           96.55               29            0.55              1.37        355.68                27.52         0.532          pass              0.699             39.7                           0.417                4.81              0.593                      ok            True                  False
  ALNY           56.25               16            2.75              3.18        163.68               110.81         0.721          pass              0.142              9.9                           0.172                1.58              0.122                      ok           False                  False
  FTNT           68.42               19            2.68              2.39        126.20                93.31         0.669          pass              0.176             16.2                           0.328               -1.90              0.007                      ok           False                  False
  INTC           50.00                8            6.50              2.71         58.50               143.21         0.647          pass              0.094              9.9                           0.204               -6.98              0.106                      ok           False                  False
   TRI           87.80               41            0.04              0.03        109.29                62.00         0.620          pass              0.745             91.7                           0.488              -10.62             -0.915 downtrend_blocked_slope           False                  False
   BKR           63.64               11            2.09              0.72         49.13                57.94         0.607          pass              0.168             33.7                           0.624               -8.32             -0.526 downtrend_blocked_slope           False                  False
  UPRO           80.00                5            3.45              3.35        137.07                68.17         0.605          pass              0.124             21.3                           0.381               -3.90             -0.126                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T10:45:04.401367-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:40:04.543489-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:35:05.683081-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:30:06.080468-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:25:05.577386-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:20:06.177663-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:15:06.368361-05:00 early_entry_1015 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "entry_ask": 11.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.225, "hypothetical_budget": 58512.4, "hypothetical_contracts": 52, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.01, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "matched_signals": 36, "recovery_stability_score": 0.574, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:10:05.371308-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:05:06.161722-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:00:04.523594-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116104504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116104504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116104504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116104504)

</details>
