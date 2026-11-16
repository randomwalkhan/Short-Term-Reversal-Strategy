# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-16 11:45:04 EST`
Last processed slot: `early_entry_1145`

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
   TXN           83.33               12            2.09              4.45        301.69                58.41         0.590          pass              0.325             54.6                           0.732               -1.58              0.100                      ok            True                  False
   CEG           87.88               33            1.14              2.24        278.82                61.55         0.564          pass              0.573             51.0                           0.431                7.51              1.245                      ok            True                  False
  ISRG           90.62               32            0.83              2.58        442.49                45.74         0.558          pass              0.597             37.1                           0.292                0.70             -0.276                      ok            True                  False
  AAPL           96.00               25            0.63              1.57        355.60                27.52         0.552          pass              0.648             30.9                           0.269                4.72              0.589                      ok            True                  False
   HON           82.76               29            0.69              1.07        222.00                32.11         0.527          pass              0.305             17.3                           0.288               -0.96              0.012                      ok            True                  False
  NXPI           96.55               29            1.34              2.48        264.03                48.08         0.504          pass              0.779             67.2                           0.749                1.68              0.356                      ok            True                  False
  ALNY           63.64               22            2.41              2.79        163.85               110.81         0.716          pass              0.215             21.0                           0.284                1.94              0.138                      ok           False                  False
  FTNT           76.00               25            2.16              1.92        126.40                93.31         0.673          pass              0.265             32.4                           0.432               -1.38              0.031                      ok           False                  False
  INTC           60.00               10            6.36              2.66         58.52               143.21         0.655          pass              0.101             11.8                           0.332               -6.84              0.113                      ok           False                  False
  UPRO           80.00                5            3.47              3.37        137.06                68.17         0.604          pass              0.123             20.8                           0.349               -3.92             -0.127                      ok           False                  False
   ADI           75.00               12            2.50              6.95        394.99                66.18         0.598          pass              0.199             41.9                           0.662               -6.01             -0.157                      ok           False                  False
   BKR           60.00               10            2.43              0.84         49.08                57.94         0.588          pass              0.128             23.1                           0.212               -8.63             -0.541 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    detail
2026-11-16T11:45:04.541902-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:40:05.500831-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:35:03.430976-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:30:04.371241-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:25:06.045979-05:00 early_entry_1125 early_entry_shadow   {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "entry_ask": 11.05, "entry_bid": 10.65, "entry_mode": "early", "entry_option_price": 10.85, "hypothetical_budget": 58512.4, "hypothetical_contracts": 53, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 3.69, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.58, "shadow_only": true, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.709, "early_reclaim_pct": 75.4, "matched_signals": 37, "recovery_stability_score": 0.58, "success_rate": 89.19, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-16T11:20:06.269332-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:15:03.556110-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:10:05.513008-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:05:06.280493-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-16T11:00:05.564099-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "QCOM261218C00170000", "current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "entry_ask": 10.9, "entry_bid": 10.45, "entry_mode": "early", "entry_option_price": 10.675, "hypothetical_budget": 58512.4, "hypothetical_contracts": 54, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 3371.0, "option_spread_pct": 4.22, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.789, "shadow_only": true, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "top_candidates": [{"current_drop_pct": 0.55, "early_entry_score": 0.734, "early_reclaim_pct": 78.7, "matched_signals": 38, "recovery_stability_score": 0.789, "success_rate": 89.47, "ticker": "QCOM", "timing_score": 0.582, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261116114504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261116114504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261116114504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261116114504)

</details>
