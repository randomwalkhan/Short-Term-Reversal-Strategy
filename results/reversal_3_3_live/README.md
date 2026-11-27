# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-27 10:55:01 EST`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NVDA           69.23               26            1.28              1.34        148.73               127.24         0.755            pass              0.335             51.0                           0.611              -11.32             -0.934 downtrend_blocked_slope_and_streak           False                  False
   KDP           89.74               39            0.09              0.02         35.62                47.31         0.566            pass              0.767             85.9                           0.658                0.50             -0.003                                 ok           False                  False
   CEG           88.37               43            0.25              0.42        235.10                66.73         0.552            pass              0.710             77.3                           0.599              -16.77             -2.015 downtrend_blocked_slope_and_streak           False                  False
  MDLZ          100.00               29            0.35              0.17         67.74                23.85         0.534            pass              0.736             52.0                           0.310                1.52              0.044                                 ok           False                  False
   AEP           96.15               26            0.20              0.18        127.51                16.32         0.523            pass              0.652             31.1                           0.304               -1.22             -0.137                                 ok           False                  False
  PAYX           74.19               31            0.04              0.04        118.47                28.65         0.518            pass              0.461             89.7                           0.481                2.83              0.118                                 ok           False                  False
  ROST           92.31               39            0.35              0.55        223.02                44.59         0.515            pass              0.761             62.6                           0.440               -6.23             -0.475            downtrend_blocked_slope           False                  False
  ALNY           77.50               40            0.70              0.81        164.38               117.72         0.505            pass              0.418             55.9                           0.672                4.42              0.231                                 ok           False                  False
  ORLY          100.00               20            1.23              0.83         96.33                21.83         0.493 below_threshold              0.568             17.4                           0.344                4.30              0.455                                 ok           False                  False
  VRSK           86.05               43            0.14              0.21        204.67                37.92         0.473 below_threshold              0.690             93.8                           0.526               -0.90             -0.260                                 ok           False                  False
 GOOGL           84.62               39            0.00              0.01        273.10                60.73         0.466 below_threshold              0.662             99.7                           0.850               -8.57             -0.787            downtrend_blocked_slope           False                  False
  MNST           83.33               42            0.12              0.04         42.58                31.71         0.454 below_threshold              0.551             72.2                           0.548               -6.63             -0.961 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-11-27T10:55:01.508390-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:50:04.846416-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:45:04.644891-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:40:06.554285-05:00 early_entry_1040 early_entry_shadow             {"contract_symbol": "GILD270115C00175000", "current_drop_pct": 0.52, "early_entry_score": 0.718, "early_reclaim_pct": 66.5, "entry_ask": 9.2, "entry_bid": 8.3, "entry_mode": "early", "entry_option_price": 8.75, "hypothetical_budget": 51984.9, "hypothetical_contracts": 59, "matched_signals": 41, "option_liquidity_status": "low_open_interest", "option_open_interest": 0.0, "option_spread_pct": 10.29, "option_volume": 28.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.456, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.718, "early_reclaim_pct": 66.5, "matched_signals": 41, "recovery_stability_score": 0.658, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.456, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-27T10:35:05.916887-05:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:30:06.180947-05:00 early_entry_1030 early_entry_shadow {"contract_symbol": "GILD270115C00175000", "current_drop_pct": 0.5, "early_entry_score": 0.721, "early_reclaim_pct": 67.5, "entry_ask": 9.35, "entry_bid": 8.1, "entry_mode": "early", "entry_option_price": 8.725, "hypothetical_budget": 51984.9, "hypothetical_contracts": 59, "matched_signals": 41, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 0.0, "option_spread_pct": 14.33, "option_volume": 28.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.709, "shadow_only": true, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.721, "early_reclaim_pct": 67.5, "matched_signals": 41, "recovery_stability_score": 0.709, "success_rate": 90.24, "ticker": "GILD", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-27T10:25:03.693968-05:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:20:04.818619-05:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:15:06.172355-05:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-27T10:10:04.653720-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261127105501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261127105501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261127105501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261127105501)

</details>
