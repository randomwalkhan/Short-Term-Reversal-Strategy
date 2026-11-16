# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 10:55:01 EST`
Last processed slot: `manage_1100`

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
   CEG           87.88               33            1.20              2.35        278.77                61.55         0.560          pass              0.565             48.5                           0.459                7.45              1.242                      ok            True                  False
  ISRG           90.91               33            0.74              2.30        442.61                45.74         0.557          pass              0.632             44.0                           0.454                0.79             -0.272                      ok            True                  False
  DXCM           83.33               36            0.79              0.46         83.13                50.11         0.536          pass              0.412             32.0                           0.428               -2.47             -0.410                      ok            True                  False
  NXPI           94.44               18            2.01              3.73        263.49                48.08         0.529          pass              0.643             50.6                           0.731                0.98              0.324                      ok            True                  False
  ALNY           56.25               16            2.73              3.15        163.69               110.81         0.722          pass              0.144             10.6                           0.182                1.60              0.123                      ok           False                  False
  FTNT           70.00               20            2.34              2.09        126.33                93.31         0.683          pass              0.215             26.8                           0.459               -1.56              0.023                      ok           False                  False
  INTC           63.64               11            5.99              2.50         58.59               143.21         0.674          pass              0.125             16.9                           0.375               -6.47              0.131                      ok           False                  False
  UPRO           85.71                7            2.86              2.77        137.31                68.17         0.634          pass              0.320             34.8                           0.686               -3.31             -0.098                      ok           False                  False
   BKR           63.64               11            1.96              0.68         49.15                57.94         0.614          pass              0.182             37.8                           0.716               -8.20             -0.519 downtrend_blocked_slope           False                  False
 GOOGL           70.00               10            2.16              4.47        293.85                54.19         0.598          pass              0.174             38.1                           0.716                3.73              0.533                      ok           False                  False
  GOOG           72.73               11            2.13              4.36        290.65                52.39         0.591          pass              0.180             38.0                           0.714                2.97              0.450                      ok           False                  False
   ADI           70.00               10            2.90              8.09        394.50                66.18         0.579          pass              0.155             32.3                           0.573               -6.40             -0.176                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T10:55:01.591806-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:50:02.516929-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:45:04.401367-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:40:04.543489-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:35:05.683081-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:30:06.080468-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:25:05.577386-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:20:06.177663-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:15:06.368361-05:00 early_entry_1015 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "entry_ask": 11.45, "entry_bid": 11.0, "entry_mode": "early", "entry_option_price": 11.225, "hypothetical_budget": 58512.4, "hypothetical_contracts": 52, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.01, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.574, "shadow_only": true, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.73, "early_entry_score": 0.684, "early_reclaim_pct": 71.9, "matched_signals": 36, "recovery_stability_score": 0.574, "success_rate": 88.89, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:10:05.371308-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116105501)

</details>
