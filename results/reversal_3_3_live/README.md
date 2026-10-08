# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-08 11:25:05 EDT`
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

- Cash: `$108,579.30`
- Equity: `$108,579.30`
- Realized PnL: `$98,579.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-08)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  NVDA     option         option NVDA261120C00235000     40          2026-10-07         2026-10-08       13.075     11.7675 -5230.0  -10.000000        stop_loss_hit_at_scan
  ABNB     option         option ABNB261120C00160000     55          2026-10-06         2026-10-08        9.475     11.0500  8662.5   16.622691 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CSCO           83.33               18            1.03              0.85        117.03                34.80         0.582          pass              0.237             12.3                           0.135                9.03              1.183                                 ok            True                  False
   CEG           85.00               20            1.75              3.67        298.02                58.54         0.564          pass              0.332             25.0                           0.199               12.51              1.428                                 ok            True                  False
  MPWR           87.50               24            1.85             18.47       1418.06                55.22         0.562          pass              0.475             41.9                           0.359                4.95              0.840                                 ok            True                  False
  PANW           81.40               43            0.58              1.66        404.86                57.34         0.520          pass              0.384             31.7                           0.162                3.41              0.724                                 ok            True                  False
  UPRO           82.61               23            1.13              1.22        154.64                30.53         0.517          pass              0.321             37.7                           0.236                2.28              0.405                                 ok            True                  False
   EXC           83.33               18            0.77              0.22         41.39                16.08         0.517          pass              0.199              1.5                           0.136                2.41              0.316                                 ok            True                  False
  PYPL           87.50               16            1.66              0.64         54.68                26.06         0.511          pass              0.310              6.2                           0.199                2.74              0.155                                 ok            True                  False
  DASH           83.33               30            1.44              1.93        190.41                42.67         0.502          pass              0.297              8.3                           0.137                0.51              0.278                                 ok            True                  False
  MELI           83.33               30            1.56             20.39       1864.04                42.10         0.502          pass              0.279              2.1                           0.124                5.10              0.811                                 ok            True                  False
  MSTR           89.29               28            2.29              2.46        152.32                80.80         0.593          pass              0.539             37.2                           0.262               -7.27             -0.188           downtrend_blocked_streak           False                  False
  QCOM           86.96               23            2.18              2.71        175.96                56.66         0.562          pass              0.376             15.8                           0.188              -10.81             -1.122 downtrend_blocked_slope_and_streak           False                  False
  SOXL           79.17               24            5.05              5.61        156.50               112.38         0.553          pass              0.256             35.9                           0.434                3.12              1.000                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-08T11:25:05.197379-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:20:05.981785-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T11:15:06.509064-04:00 early_entry_1115 early_entry_shadow                {"contract_symbol": "ISRG261120C00410000", "current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "entry_ask": 27.4, "entry_bid": 24.5, "entry_mode": "early", "entry_option_price": 25.95, "hypothetical_budget": 54289.65, "hypothetical_contracts": 20, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 121.0, "option_spread_pct": 11.18, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.721, "shadow_only": true, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.75, "early_reclaim_pct": 69.2, "matched_signals": 37, "recovery_stability_score": 0.721, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.451, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:10:06.909250-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.61, "early_entry_score": 0.859, "early_reclaim_pct": 85.2, "entry_ask": 4.0, "entry_bid": 3.5, "entry_mode": "early", "entry_option_price": 3.75, "hypothetical_budget": 54289.65, "hypothetical_contracts": 144, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 13.33, "option_volume": 4.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.45, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.859, "early_reclaim_pct": 85.2, "matched_signals": 36, "recovery_stability_score": 0.623, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.45, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T11:05:04.028696-04:00 early_entry_1105 early_entry_shadow                                   {"contract_symbol": "ADI261120C00400000", "current_drop_pct": 0.69, "early_entry_score": 0.693, "early_reclaim_pct": 66.1, "entry_ask": 27.9, "entry_bid": 25.0, "entry_mode": "early", "entry_option_price": 26.45, "hypothetical_budget": 54289.65, "hypothetical_contracts": 20, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 121.0, "option_spread_pct": 10.96, "option_volume": 23.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.582, "shadow_only": true, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.502, "top_candidates": [{"current_drop_pct": 0.69, "early_entry_score": 0.693, "early_reclaim_pct": 66.1, "matched_signals": 33, "recovery_stability_score": 0.582, "success_rate": 90.91, "ticker": "ADI", "timing_score": 0.502, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-08T11:00:06.101046-04:00 early_entry_1100 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:55:06.968008-04:00 early_entry_1055 early_entry_shadow              {"contract_symbol": "ISRG261120C00410000", "current_drop_pct": 0.58, "early_entry_score": 0.736, "early_reclaim_pct": 64.7, "entry_ask": 26.4, "entry_bid": 23.5, "entry_mode": "early", "entry_option_price": 24.95, "hypothetical_budget": 54289.65, "hypothetical_contracts": 21, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 121.0, "option_spread_pct": 11.62, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.447, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.736, "early_reclaim_pct": 64.7, "matched_signals": 37, "recovery_stability_score": 0.623, "success_rate": 91.89, "ticker": "ISRG", "timing_score": 0.447, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-08T10:50:05.913383-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:45:06.914386-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-08T10:40:05.011138-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261008112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261008112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261008112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261008112505)

</details>
