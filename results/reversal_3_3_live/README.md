# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 11:30:05 EDT`
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

- Cash: `$26,995.25`
- Equity: `$26,995.25`
- Realized PnL: `$16,995.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   TXN           88.24               17            2.47              5.38        309.15                64.14         0.591          pass              0.429             34.6                           0.592                6.41              0.538                  ok            True                  False
  META           80.95               21            1.44              6.76        666.31                55.99         0.578          pass              0.264             35.7                           0.294               17.23              1.709                  ok            True                  False
   ADI           84.21               19            2.19              6.08        393.05                55.18         0.575          pass              0.288             19.4                           0.228               -1.23             -0.028                  ok            True                  False
  QCOM           82.76               29            1.39              1.83        188.37                63.33         0.571          pass              0.448             63.4                           0.539               -1.16              0.248                  ok            True                  False
  UPRO           88.00               25            1.16              1.18        145.65                40.56         0.553          pass              0.503             44.8                           0.402                4.12              0.390                  ok            True                  False
  CSCO           94.44               18            1.34              1.14        120.82                35.64         0.540          pass              0.672             59.8                           0.551                2.06              0.331                  ok            True                  False
   LIN          100.00               17            1.04              3.84        528.14                20.88         0.535          pass              0.566             22.1                           0.300                2.59              0.050                  ok            True                  False
  NXPI           81.25               16            2.89              5.92        289.72                55.03         0.530          pass              0.179             17.6                           0.285                1.95              0.400                  ok            True                  False
  AVGO           80.95               21            2.13              5.96        397.42                49.47         0.525          pass              0.257             35.3                           0.415                5.10              0.789                  ok            True                  False
   MAR           90.91               11            1.77              4.66        374.11                19.73         0.522          pass              0.384             11.3                           0.274               -1.45              0.025                  ok            True                  False
  ABNB           93.33               15            2.18              2.27        147.65                37.12         0.521          pass              0.540             32.9                           0.414               -1.22             -0.024                  ok            True                  False
  ROST           89.29               28            0.96              1.49        222.24                30.69         0.512          pass              0.453             11.4                           0.139                5.71              0.667                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-07-13T11:30:05.079424-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:25:02.062910-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:20:02.121903-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:15:04.147580-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:10:02.119516-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "SNPS260814C00445000", "current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "entry_ask": 27.0, "entry_bid": 20.8, "entry_mode": "early", "entry_option_price": 23.9, "hypothetical_budget": 13497.63, "hypothetical_contracts": 5, "matched_signals": 39, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 25.94, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.603, "shadow_only": true, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.691, "early_reclaim_pct": 65.7, "matched_signals": 39, "recovery_stability_score": 0.603, "success_rate": 89.74, "ticker": "SNPS", "timing_score": 0.402, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T11:05:06.382767-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T11:00:04.971643-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:55:05.047187-04:00 early_entry_1055 early_entry_shadow                               {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.67, "early_entry_score": 0.744, "early_reclaim_pct": 79.8, "entry_ask": 16.1, "entry_bid": 14.1, "entry_mode": "early", "entry_option_price": 15.1, "hypothetical_budget": 13497.63, "hypothetical_contracts": 8, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 840.0, "option_spread_pct": 13.25, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.645, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.384, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.744, "early_reclaim_pct": 79.8, "matched_signals": 40, "recovery_stability_score": 0.645, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.384, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T10:50:02.084276-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:45:02.061748-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713113005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713113005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713113005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713113005)

</details>
