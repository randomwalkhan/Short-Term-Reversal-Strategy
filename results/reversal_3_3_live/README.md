# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-13 10:50:02 EDT`
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
   TXN           87.50               16            2.55              5.56        309.08                64.14         0.591          pass              0.396             32.4                           0.517                6.32              0.534                  ok            True                  False
   ADI           86.96               23            1.75              4.84        393.57                55.18         0.579          pass              0.437             35.7                           0.508               -0.78             -0.007                  ok            True                  False
  META           80.95               21            1.44              6.74        666.32                55.99         0.578          pass              0.264             35.8                           0.476               17.24              1.709                  ok            True                  False
  QCOM           82.76               29            1.39              1.84        188.37                63.33         0.570          pass              0.447             63.3                           0.570               -1.16              0.248                  ok            True                  False
  UPRO           88.00               25            1.10              1.13        145.68                40.56         0.557          pass              0.511             47.4                           0.382                4.17              0.393                  ok            True                  False
  AMGN           92.31               13            1.52              3.88        361.73                21.45         0.533          pass              0.483             27.0                           0.368               -0.75             -0.068                  ok            True                  False
  NXPI           84.21               19            2.57              5.26        290.00                55.03         0.533          pass              0.306             26.7                           0.424                2.29              0.414                  ok            True                  False
  MPWR           80.95               21            3.61             34.14       1338.11                78.41         0.532          pass              0.220             22.7                           0.401               -0.52             -0.094                  ok            True                  False
  CSCO           95.83               24            0.96              0.82        120.96                35.64         0.525          pass              0.760             71.2                           0.795                2.46              0.349                  ok            True                  False
  ABNB           93.33               15            2.13              2.22        147.67                37.12         0.524          pass              0.544             34.4                           0.385               -1.17             -0.022                  ok            True                  False
  AVGO           82.61               23            1.96              5.49        397.62                49.47         0.524          pass              0.330             40.5                           0.494                5.28              0.797                  ok            True                  False
   MAR           90.91               11            1.75              4.62        374.13                19.73         0.523          pass              0.386             12.1                           0.131               -1.43              0.026                  ok            True                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-07-13T10:50:02.084276-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:45:02.061748-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:40:04.044917-04:00 early_entry_1040 early_entry_shadow                    {"contract_symbol": "CSCO260821C00120000", "current_drop_pct": 0.85, "early_entry_score": 0.806, "early_reclaim_pct": 74.4, "entry_ask": 7.1, "entry_bid": 6.95, "entry_mode": "early", "entry_option_price": 7.025, "hypothetical_budget": 13497.63, "hypothetical_contracts": 19, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 8106.0, "option_spread_pct": 2.14, "option_volume": 71.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.903, "shadow_only": true, "success_rate": 96.67, "ticker": "CSCO", "timing_score": 0.493, "top_candidates": [{"current_drop_pct": 0.85, "early_entry_score": 0.806, "early_reclaim_pct": 74.4, "matched_signals": 30, "recovery_stability_score": 0.903, "success_rate": 96.67, "ticker": "CSCO", "timing_score": 0.493, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-13T10:35:02.047813-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:30:06.369215-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:25:04.964455-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:20:02.018219-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-13T10:15:05.926049-04:00 early_entry_1015 early_entry_shadow                   {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "entry_ask": 14.0, "entry_bid": 12.6, "entry_mode": "early", "entry_option_price": 13.3, "hypothetical_budget": 13497.63, "hypothetical_contracts": 10, "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 840.0, "option_spread_pct": 10.53, "option_volume": 123.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.761, "shadow_only": true, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.705, "early_reclaim_pct": 75.6, "matched_signals": 38, "recovery_stability_score": 0.761, "success_rate": 89.47, "ticker": "CRWD", "timing_score": 0.387, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-07-13T10:10:04.827690-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "CRWD260821C00185000", "current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "entry_ask": 15.1, "entry_bid": 12.2, "entry_mode": "early", "entry_option_price": 13.65, "hypothetical_budget": 13497.63, "hypothetical_contracts": 9, "matched_signals": 40, "option_liquidity_status": "wide_spread", "option_open_interest": 840.0, "option_spread_pct": 21.25, "option_volume": 123.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.769, "shadow_only": true, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.743, "early_reclaim_pct": 79.2, "matched_signals": 40, "recovery_stability_score": 0.769, "success_rate": 90.0, "ticker": "CRWD", "timing_score": 0.383, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-13T10:00:02.015857-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260713105002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260713105002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260713105002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260713105002)

</details>
