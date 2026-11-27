# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 14:04:44 EST`
Last processed slot: `manage_1400`

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

- Cash: `$103,969.80`
- Equity: `$103,969.80`
- Realized PnL: `$93,969.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score     timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
   KDP           87.50               32            0.51              0.13         35.58                47.31         0.578              pass              0.552             49.3                           0.423                0.08             -0.022                  ok            True                  False
  MDLZ          100.00               22            0.69              0.33         67.67                23.85         0.557              pass              0.554              6.0                           0.256                1.17              0.028                  ok            True                  False
  INSM           85.71               49            0.06              0.07        170.28                97.01         0.693              pass              0.606             61.5                           0.344               44.16              4.305                  ok           False                  False
   AEP           96.15               26            0.20              0.17        127.52                16.32         0.523              pass              0.657             32.6                           0.360               -1.22             -0.136                  ok           False                  False
  PAYX           72.41               29            0.30              0.25        118.38                28.65         0.510              pass              0.332             51.4                           0.390                2.56              0.106                  ok           False                  False
  VRSK           82.86               35            0.49              0.70        204.46                37.92         0.499   below_threshold              0.530             79.0                           0.472               -1.24             -0.275                  ok           False                  False
  ALNY           74.29               35            1.23              1.42        164.12               117.72         0.499   below_threshold              0.297             26.7                           0.267                3.86              0.207                  ok           False                  False
  ORLY          100.00               34            0.55              0.37         96.53                21.83         0.445   below_threshold              0.794             63.2                           0.639                5.02              0.486                  ok           False                   True
   KHC           91.30               46            0.11              0.02         26.50                29.10         0.433   below_threshold              0.823             92.7                           0.756                8.17              0.606                  ok           False                  False
  VRTX             NaN                0            5.28             20.85        555.18                36.27           NaN no_signal_history                NaN              NaN                           0.662               -1.53              0.205                  ok           False                  False
  AAPL             NaN                0            0.00              0.00        358.43                28.52           NaN no_signal_history                NaN              NaN                           0.325                1.00              0.008                  ok           False                  False
  ABNB             NaN                0            0.00              0.00        178.91                56.84           NaN no_signal_history                NaN              NaN                           0.390               -1.23             -0.670                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-27T11:50:45.862448-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T11:16:30.878853-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T11:05:06.537341-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T11:00:04.580198-05:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:55:01.508390-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:50:04.846416-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:45:04.644891-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:40:06.554285-05:00 early_entry_1040 early_entry_shadow             {"contract_symbol": "GILD270115C00175000", "current_drop_pct": 0.52, "early_entry_score": 0.718, "early_reclaim_pct": 66.5, "entry_ask": 9.2, "entry_bid": 8.3, "entry_mode": "early", "entry_option_price": 8.75, "hypothetical_budget": 51984.9, "hypothetical_contracts": 59, "matched_signals": 41, "option_liquidity_status": "low_open_interest", "option_open_interest": 0.0, "option_spread_pct": 10.29, "option_volume": 28.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.456, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.718, "early_reclaim_pct": 66.5, "matched_signals": 41, "recovery_stability_score": 0.658, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.456, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-27T10:35:05.916887-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:30:06.180947-05:00 early_entry_1030 early_entry_shadow {"contract_symbol": "GILD270115C00175000", "current_drop_pct": 0.5, "early_entry_score": 0.721, "early_reclaim_pct": 67.5, "entry_ask": 9.35, "entry_bid": 8.1, "entry_mode": "early", "entry_option_price": 8.725, "hypothetical_budget": 51984.9, "hypothetical_contracts": 59, "matched_signals": 41, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 0.0, "option_spread_pct": 14.33, "option_volume": 28.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.709, "shadow_only": true, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.721, "early_reclaim_pct": 67.5, "matched_signals": 41, "recovery_stability_score": 0.709, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127140444)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127140444)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127140444)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127140444)

</details>
