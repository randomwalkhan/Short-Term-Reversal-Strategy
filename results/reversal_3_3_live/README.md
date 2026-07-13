# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 10:55:05 EDT`
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
   TXN           87.50               16            2.71              5.92        308.92                64.14         0.581          pass              0.382             28.0                           0.472                6.14              0.526                  ok            True                  False
  QCOM           81.48               27            1.46              1.93        188.33                63.33         0.578          pass              0.395             61.5                           0.541               -1.23              0.245                  ok            True                  False
   ADI           84.21               19            2.19              6.06        393.05                55.18         0.576          pass              0.288             19.6                           0.273               -1.22             -0.027                  ok            True                  False
  UPRO           90.91               22            1.24              1.27        145.62                40.56         0.571          pass              0.551             40.8                           0.341                4.03              0.386                  ok            True                  False
  META           83.87               31            0.84              3.96        667.51                55.99         0.553          pass              0.486             62.4                           0.615               17.95              1.736                  ok            True                  False
  CSCO           94.44               18            1.34              1.14        120.82                35.64         0.540          pass              0.672             59.9                           0.658                2.07              0.331                  ok            True                  False
  AMGN           92.31               13            1.43              3.63        361.83                21.45         0.539          pass              0.497             31.6                           0.442               -0.65             -0.064                  ok            True                  False
  ABNB           93.75               16            2.01              2.09        147.72                37.12         0.525          pass              0.573             38.1                           0.477               -1.05             -0.017                  ok            True                  False
   MAR           91.67               12            1.69              4.44        374.21                19.73         0.521          pass              0.423             15.5                           0.184               -1.36              0.029                  ok            True                  False
   LIN          100.00               20            0.97              3.61        528.24                20.88         0.519          pass              0.594             25.2                           0.366                2.66              0.053                  ok            True                  False
  AVGO           80.95               21            2.32              6.51        397.18                49.47         0.513          pass              0.238             29.4                           0.298                4.89              0.780                  ok            True                  False
  ROST           90.62               32            0.61              0.96        222.47                30.69         0.512          pass              0.535             18.0                           0.187                6.07              0.683                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-13T10:55:05.047187-04:00 early_entry_1055 early_entry_shadow     {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.67, "early_entry_score": 0.744, "early_reclaim_pct": 79.8, "entry_ask": 16.1, "entry_bid": 14.1, "entry_mode": "early", "entry_option_price": 15.1, "hypothetical_budget": 13497.63, "hypothetical_contracts": 8, "matched_signals": 40, "option_liquidity_status": "low_volume", "option_open_interest": 840.0, "option_spread_pct": 13.25, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.645, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.384, "top_candidates": [{"current_drop_pct": 0.67, "early_entry_score": 0.744, "early_reclaim_pct": 79.8, "matched_signals": 40, "recovery_stability_score": 0.645, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.384, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T10:50:02.084276-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:45:02.061748-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:40:04.044917-04:00 early_entry_1040 early_entry_shadow                    {"contract_symbol": "CSCO260821C00120000", "current_drop_pct": 0.85, "early_entry_score": 0.806, "early_reclaim_pct": 74.4, "entry_ask": 7.1, "entry_bid": 6.95, "entry_mode": "early", "entry_option_price": 7.025, "hypothetical_budget": 13497.63, "hypothetical_contracts": 19, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 8106.0, "option_spread_pct": 2.14, "option_volume": 71.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.903, "shadow_only": true, "success_rate": 96.67, "ticker": "CSCO", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.806, "early_reclaim_pct": 74.4, "matched_signals": 30, "recovery_stability_score": 0.903, "success_rate": 96.67, "ticker": "CSCO", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-13T10:35:02.047813-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:30:06.369215-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:25:04.964455-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:20:02.018219-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:15:05.926049-04:00 early_entry_1015 early_entry_shadow                   {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "entry_ask": 14.0, "entry_bid": 12.6, "entry_mode": "early", "entry_option_price": 13.3, "hypothetical_budget": 13497.63, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 840.0, "option_spread_pct": 10.53, "option_volume": 123.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "matched_signals": 38, "recovery_stability_score": 0.761, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-13T10:10:04.827690-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "entry_ask": 15.1, "entry_bid": 12.2, "entry_mode": "early", "entry_option_price": 13.65, "hypothetical_budget": 13497.63, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 840.0, "option_spread_pct": 21.25, "option_volume": 123.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.769, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "matched_signals": 40, "recovery_stability_score": 0.769, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713105505)

</details>
