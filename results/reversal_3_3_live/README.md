# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-15 11:50:02 EDT`
Last processed slot: `manage_1200`

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

- Cash: `$30,630.25`
- Equity: `$30,630.25`
- Realized PnL: `$20,630.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-07-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AAPL     option         option AAPL260821C00315000     11          2026-07-14         2026-07-15       11.550       13.45 2090.0   16.450216 take_profit_day1_hit_at_scan
  META     option         option META260821C00660000      2          2026-07-13         2026-07-15       46.875       54.60 1545.0   16.480000 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   TXN           90.91               22            1.88              4.01        303.83                65.52         0.582          pass              0.534             35.1                           0.447                0.59              0.262                                 ok            True                  False
   EXC           93.33               15            0.76              0.25         46.81                21.56         0.569          pass              0.562             38.8                           0.242               -0.12             -0.053                                 ok            True                  False
   ADI           84.00               25            1.45              3.99        391.04                55.85         0.567          pass              0.360             32.3                           0.350               -2.55              0.067                                 ok            True                  False
   LIN          100.00               10            1.37              5.00        520.40                20.66         0.565          pass              0.521             21.4                           0.292               -0.68             -0.307                                 ok            True                  False
   WBD           84.62               13            0.91              0.18         27.40                20.00         0.543          pass              0.297             33.3                           0.446                2.14              0.277                                 ok            True                  False
  NXPI           86.96               23            1.98              3.94        282.18                58.07         0.537          pass              0.383             19.0                           0.329               -0.99              0.227                                 ok            True                  False
  MPWR           81.82               22            3.56             34.34       1361.69                84.79         0.517          pass              0.180              0.0                           0.262               -3.98              0.068                                 ok            True                  False
  PCAR           87.50               32            0.54              0.47        123.74                31.66         0.506          pass              0.521             41.2                           0.201                2.62              0.271                                 ok            True                  False
  MDLZ           93.75               16            0.35              0.14         58.74                30.54         0.627          pass              0.703             77.7                           0.390                1.31             -0.076                                 ok           False                  False
   CSX           88.89                9            1.35              0.47         49.72                19.08         0.579          pass              0.314              6.2                           0.112                3.61              0.333                                 ok           False                  False
  QCOM           83.33               30            1.21              1.51        177.45                61.79         0.569          pass              0.383             34.7                           0.436               -4.79             -0.099           downtrend_blocked_streak           False                  False
  KLAC           75.00               12            4.61              7.43        227.19               109.33         0.569          pass              0.088              6.0                           0.243              -27.16             -2.123 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      detail
2026-07-15T11:50:02.876804-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:45:04.888686-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:40:05.824741-04:00 early_entry_1140 early_entry_shadow {"contract_symbol": "MELI260821C01860000", "current_drop_pct": 1.12, "early_entry_score": 0.719, "early_reclaim_pct": 61.4, "entry_ask": 109.0, "entry_bid": 89.0, "entry_mode": "early", "entry_option_price": 99.0, "hypothetical_budget": 15315.13, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 42.0, "option_spread_pct": 20.2, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 1.12, "early_entry_score": 0.719, "early_reclaim_pct": 61.4, "matched_signals": 30, "recovery_stability_score": 0.731, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-15T11:35:03.044078-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:30:02.764880-04:00 early_entry_1130 early_entry_shadow {"contract_symbol": "MELI260821C01860000", "current_drop_pct": 1.11, "early_entry_score": 0.72, "early_reclaim_pct": 61.8, "entry_ask": 109.0, "entry_bid": 88.7, "entry_mode": "early", "entry_option_price": 98.85, "hypothetical_budget": 15315.13, "hypothetical_contracts": 1, "matched_signals": 30, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 42.0, "option_spread_pct": 20.54, "option_volume": 23.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.806, "shadow_only": true, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.72, "early_reclaim_pct": 61.8, "matched_signals": 30, "recovery_stability_score": 0.806, "success_rate": 93.33, "ticker": "MELI", "timing_score": 0.457, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-07-15T11:25:06.537726-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:20:02.933836-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:15:06.015471-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:10:02.751788-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-15T11:05:05.849714-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260715115002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260715115002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260715115002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260715115002)

</details>
