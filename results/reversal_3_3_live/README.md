# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 13:20:05 EST`
Last processed slot: `manage_1330`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  INTC           53.85               13            3.72              1.58         59.87               129.60         0.728            pass              0.214             40.3                           0.299              -37.29             -4.985            downtrend_blocked_slope           False                  False
    ZS           93.02               43            0.28              0.43        224.90                64.45         0.533            pass              0.863             87.6                           0.696               -2.97             -0.903 downtrend_blocked_slope_and_streak           False                  False
  REGN           66.67                3            3.27             22.27        963.82                48.26         0.514            pass              0.077              8.6                           0.223               16.87              2.075                                 ok           False                  False
  NVDA           78.95               19            1.24              1.80        205.92                32.59         0.505            pass              0.276             55.3                           0.646               -8.04             -0.711 downtrend_blocked_slope_and_streak           False                  False
  AVGO           75.00               28            1.12              2.60        331.02                44.04         0.503            pass              0.363             64.3                           0.452               -2.78             -0.035                                 ok           False                  False
  CSCO           82.76               29            0.41              0.29        102.84                32.31         0.501            pass              0.443             64.1                           0.437               -4.39             -0.520 downtrend_blocked_slope_and_streak           False                  False
   AEP           84.21               19            0.73              0.66        129.58                19.14         0.495 below_threshold              0.475             84.5                           0.718                1.19              0.053                                 ok           False                  False
  TEAM           96.30               27            1.63              2.18        190.12                53.65         0.493 below_threshold              0.712             49.9                           0.489              -16.66             -2.272            downtrend_blocked_slope           False                  False
  PANW           82.22               45            0.11              0.26        350.09                58.95         0.488 below_threshold              0.595             95.8                           0.613                0.74             -0.397                                 ok           False                  False
  DRAM           61.54               13            4.03              1.34         47.06                69.30         0.485 below_threshold              0.164             31.9                           0.323               -7.00             -0.210                                 ok           False                  False
  ASML           71.43                7            3.24             35.16       1537.07                44.05         0.483 below_threshold              0.142             31.4                           0.318              -10.31             -0.590            downtrend_blocked_slope           False                  False
   TXN           90.91               33            0.43              0.93        312.09                35.19         0.480 below_threshold              0.746             84.5                           0.597                9.85              1.062                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-04T12:00:04.108894-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:55:06.127851-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:50:05.872989-05:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:45:05.372887-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:40:03.980969-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:35:05.266988-05:00 early_entry_1135 early_entry_shadow  {"contract_symbol": "TXN261204C00325000", "current_drop_pct": 0.58, "early_entry_score": 0.701, "early_reclaim_pct": 79.0, "entry_ask": 9.15, "entry_bid": 8.25, "entry_mode": "early", "entry_option_price": 8.7, "hypothetical_budget": 64815.78, "hypothetical_contracts": 74, "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 128.0, "option_spread_pct": 10.34, "option_volume": 113.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.72, "shadow_only": true, "success_rate": 90.32, "ticker": "TXN", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.701, "early_reclaim_pct": 79.0, "matched_signals": 31, "recovery_stability_score": 0.72, "success_rate": 90.32, "ticker": "TXN", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-04T11:30:01.206100-05:00 early_entry_1130 early_entry_shadow {"contract_symbol": "TXN261204C00325000", "current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "entry_ask": 9.55, "entry_bid": 8.5, "entry_mode": "early", "entry_option_price": 9.025, "hypothetical_budget": 64815.78, "hypothetical_contracts": 71, "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 128.0, "option_spread_pct": 11.63, "option_volume": 113.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.671, "shadow_only": true, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.673, "early_reclaim_pct": 75.0, "matched_signals": 30, "recovery_stability_score": 0.671, "success_rate": 90.0, "ticker": "TXN", "timing_score": 0.481, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-04T11:25:01.112223-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:20:06.438963-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T11:15:06.967175-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104132005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104132005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104132005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104132005)

</details>
