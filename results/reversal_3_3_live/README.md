# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 11:40:01 EST`
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

- Cash: `$136,446.55`
- Equity: `$136,446.55`
- Realized PnL: `$126,446.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-03)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG261218C00260000     34          2026-11-02         2026-11-03        18.25       21.05 9520.0   15.342466 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           91.67               12            1.00              0.47         66.18                28.20         0.600          pass              0.539             51.5                           0.614                2.70              0.263                                 ok            True                  False
   PEP           80.00               10            1.49              1.46        139.79                26.86         0.570          pass              0.128             23.7                           0.370                3.22              0.220                                 ok            True                  False
   KHC           83.33               12            1.81              0.32         24.79                33.68         0.563          pass              0.244             28.6                           0.477                2.73              0.155                                 ok            True                  False
   XEL           87.50               24            0.55              0.31         79.20                19.18         0.502          pass              0.520             58.9                           0.641                2.88              0.295                                 ok            True                  False
  TMUS           63.64               11            1.89              2.11        159.24                68.40         0.666          pass              0.167             31.2                           0.447               -0.39              0.106                                 ok           False                  False
 CMCSA           91.67               24            0.31              0.05         23.85                32.70         0.571          pass              0.708             82.0                           0.671                6.42              0.557                                 ok           False                  False
   ROP           70.00               10            1.71              5.74        477.08                37.35         0.571          pass              0.146             29.7                           0.225               18.36              1.677                                 ok           False                  False
  PAYX           76.92               26            0.24              0.20        115.41                35.36         0.555          pass              0.439             92.2                           0.857                3.34             -0.030                                 ok           False                  False
  MRVL           86.67               30            1.74              2.09        170.52                97.23         0.552          pass              0.443             25.7                           0.224              -29.94             -3.281 downtrend_blocked_slope_and_streak           False                  False
   CSX           72.73               11            1.39              0.50         51.40                27.65         0.549          pass              0.109             15.8                           0.215                5.87              0.573                                 ok           False                  False
  CTSH           82.61               23            1.65              0.75         64.77                51.60         0.537          pass              0.390             60.2                           0.697               -6.11             -1.126            downtrend_blocked_slope           False                  False
  COST           50.00                4            1.61             11.70       1035.54                19.43         0.532          pass              0.113             19.9                           0.418                3.09              0.249                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-03T11:40:01.980819-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:35:05.840286-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:30:05.077695-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:25:04.545060-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:20:06.072141-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:15:01.990433-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:10:06.114764-05:00 early_entry_1110 early_entry_shadow {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "entry_ask": 7.5, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 68223.28, "hypothetical_contracts": 99, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 18.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.633, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T11:05:06.948885-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:00:05.972600-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "entry_ask": 7.5, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 6.8, "hypothetical_budget": 68223.28, "hypothetical_contracts": 100, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 20.59, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "matched_signals": 31, "recovery_stability_score": 0.675, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T10:55:05.970636-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103114001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103114001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103114001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103114001)

</details>
