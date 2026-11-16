# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 11:40:05 EST`
Last processed slot: `manage_1130`

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
   TXN           81.82               11            2.29              4.86        301.52                58.41         0.583          pass              0.265             50.5                           0.725               -1.77              0.091                      ok            True                  False
   CEG           87.88               33            1.04              2.03        278.90                61.55         0.570          pass              0.587             55.5                           0.486                7.63              1.249                      ok            True                  False
  ISRG           90.91               33            0.74              2.29        442.61                45.74         0.557          pass              0.632             44.1                           0.331                0.79             -0.272                      ok            True                  False
  AAPL           96.00               25            0.62              1.55        355.61                27.52         0.552          pass              0.651             32.0                           0.290                4.73              0.590                      ok            True                  False
   HON           82.76               29            0.72              1.13        221.98                32.11         0.525          pass              0.292             13.0                           0.216               -0.99              0.010                      ok            True                  False
  NXPI           96.43               28            1.45              2.68        263.94                48.08         0.503          pass              0.764             64.5                           0.766                1.56              0.350                      ok            True                  False
  ALNY           69.23               26            2.04              2.36        164.03               110.81         0.720          pass              0.278             33.0                           0.420                2.32              0.155                      ok           False                  False
  FTNT           76.92               26            2.05              1.83        126.44                93.31         0.674          pass              0.282             35.9                           0.471               -1.27              0.036                      ok           False                  False
  INTC           63.64               11            6.13              2.56         58.56               143.21         0.667          pass              0.118             15.0                           0.442               -6.61              0.124                      ok           False                  False
  UPRO           80.00                5            3.32              3.22        137.12                68.17         0.613          pass              0.134             24.2                           0.408               -3.77             -0.120                      ok           False                  False
   ADI           72.73               11            2.58              7.19        394.89                66.18         0.596          pass              0.186             39.9                           0.662               -6.09             -0.161                      ok           False                  False
   BKR           60.00               10            2.35              0.81         49.09                57.94         0.593          pass              0.136             25.6                           0.259               -8.56             -0.537 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T11:40:05.500831-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:35:03.430976-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:30:04.371241-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:25:06.045979-05:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "entry_ask": 11.05, "entry_bid": 10.65, "entry_mode": "early", "entry_option_price": 10.85, "hypothetical_budget": 58512.4, "hypothetical_contracts": 53, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 3.69, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.58, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T11:20:06.269332-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:15:03.556110-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:10:05.513008-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:05:06.280493-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:00:05.564099-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "entry_ask": 10.9, "entry_bid": 10.45, "entry_mode": "early", "entry_option_price": 10.675, "hypothetical_budget": 58512.4, "hypothetical_contracts": 54, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.22, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "matched_signals": 38, "recovery_stability_score": 0.789, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:55:01.591806-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116114005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116114005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116114005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116114005)

</details>
