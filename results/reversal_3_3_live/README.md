# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 11:25:06 EST`
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
  QCOM           89.19               37            0.64              0.77        172.14                68.34         0.582          pass              0.709             75.4                           0.580                5.73              0.748                      ok            True                   True
   CEG           87.88               33            0.98              1.91        278.95                61.55         0.574          pass              0.595             58.0                           0.499                7.69              1.252                      ok            True                  False
  ISRG           90.91               33            0.76              2.36        442.58                45.74         0.556          pass              0.627             42.4                           0.380                0.77             -0.273                      ok            True                  False
  AMZN           81.25               16            1.88              3.51        265.15                41.74         0.533          pass              0.229             34.2                           0.531                6.52              0.607                      ok            True                  False
  DXCM           82.35               34            1.07              0.62         83.06                50.11         0.529          pass              0.324             16.0                           0.237               -2.74             -0.423                      ok            True                  False
   HON           82.76               29            0.73              1.14        221.97                32.11         0.525          pass              0.261              2.7                           0.116               -1.00              0.010                      ok            True                  False
  NXPI           95.65               23            1.64              3.05        263.78                48.08         0.521          pass              0.718             59.6                           0.685                1.36              0.341                      ok            True                  False
  ALNY           70.37               27            1.84              2.12        164.13               110.81         0.727          pass              0.306             39.9                           0.608                2.54              0.164                      ok           False                  False
  INTC           63.64               11            5.94              2.48         58.60               143.21         0.677          pass              0.127             17.6                           0.394               -6.43              0.133                      ok           False                  False
  FTNT           77.78               27            2.03              1.81        126.45                93.31         0.671          pass              0.290             36.6                           0.469               -1.24              0.038                      ok           False                  False
   TRI           87.80               41            0.04              0.03        109.29                62.00         0.621          pass              0.748             92.6                           0.505              -10.62             -0.915 downtrend_blocked_slope           False                  False
  UPRO           80.00                5            3.18              3.09        137.18                68.17         0.620          pass              0.144             27.3                           0.377               -3.63             -0.114                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T11:25:06.045979-05:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "entry_ask": 11.05, "entry_bid": 10.65, "entry_mode": "early", "entry_option_price": 10.85, "hypothetical_budget": 58512.4, "hypothetical_contracts": 53, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 3.69, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.58, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T11:20:06.269332-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:15:03.556110-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:10:05.513008-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:05:06.280493-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:00:05.564099-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "entry_ask": 10.9, "entry_bid": 10.45, "entry_mode": "early", "entry_option_price": 10.675, "hypothetical_budget": 58512.4, "hypothetical_contracts": 54, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.22, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "matched_signals": 38, "recovery_stability_score": 0.789, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:55:01.591806-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:50:02.516929-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:45:04.401367-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:40:04.543489-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116112506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116112506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116112506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116112506)

</details>
