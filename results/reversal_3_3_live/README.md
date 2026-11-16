# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 11:10:05 EST`
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
  QCOM           87.50               32            0.92              1.11        171.99                68.34         0.593          pass              0.600             64.5                           0.650                5.43              0.736                      ok            True                  False
   CEG           87.50               32            1.26              2.46        278.72                61.55         0.563          pass              0.541             46.1                           0.418                7.39              1.239                      ok            True                  False
  NXPI           92.86               14            2.07              3.85        263.44                48.08         0.548          pass              0.572             49.1                           0.662                0.91              0.321                      ok            True                  False
  AMZN           81.25               16            1.85              3.46        265.18                41.74         0.535          pass              0.232             35.2                           0.616                6.55              0.608                      ok            True                  False
  DXCM           82.35               34            1.01              0.59         83.08                50.11         0.534          pass              0.316             13.4                           0.216               -2.68             -0.420                      ok            True                  False
   HON           83.33               30            0.58              0.90        222.07                32.11         0.529          pass              0.333             19.4                           0.304               -0.85              0.016                      ok            True                  False
  SHOP           80.00               40            0.59              0.61        146.83                57.73         0.515          pass              0.504             84.3                           0.935               -6.40             -0.247                      ok            True                  False
  ALNY           70.37               27            1.91              2.21        164.09               110.81         0.723          pass              0.298             37.3                           0.568                2.46              0.161                      ok           False                  False
  FTNT           76.00               25            2.14              1.90        126.40                93.31         0.674          pass              0.267             33.2                           0.564               -1.35              0.032                      ok           False                  False
  INTC           42.86                7            6.77              2.83         58.45               143.21         0.628          pass              0.081              6.1                           0.237               -7.25              0.093                      ok           False                  False
   BKR           63.64               11            1.92              0.66         49.16                57.94         0.617          pass              0.186             39.1                           0.652               -8.16             -0.518 downtrend_blocked_slope           False                  False
  UPRO           80.00                5            3.34              3.23        137.11                68.17         0.612          pass              0.133             23.9                           0.464               -3.78             -0.121                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T11:10:05.513008-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:05:06.280493-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:00:05.564099-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "entry_ask": 10.9, "entry_bid": 10.45, "entry_mode": "early", "entry_option_price": 10.675, "hypothetical_budget": 58512.4, "hypothetical_contracts": 54, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.22, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "matched_signals": 38, "recovery_stability_score": 0.789, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T10:55:01.591806-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:50:02.516929-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:45:04.401367-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:40:04.543489-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:35:05.683081-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:30:06.080468-05:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T10:25:05.577386-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116111005)

</details>
