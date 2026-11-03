# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-03 11:45:05 EST`
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
  MDLZ           90.91               11            1.13              0.53         66.15                28.20         0.598          pass              0.493             45.3                           0.533                2.56              0.257                                 ok            True                  False
   KHC           81.82               11            1.94              0.34         24.79                33.68         0.560          pass              0.181             23.4                           0.296                2.59              0.149                                 ok            True                  False
   ADP           88.89               27            0.54              1.13        298.29                27.85         0.522          pass              0.628             75.1                           0.727                1.51             -0.168                                 ok            True                  False
  FAST           96.30               27            0.53              0.20         52.47                22.62         0.513          pass              0.709             48.1                           0.368                1.71              0.089                                 ok            True                  False
   EXC           86.96               23            0.70              0.23         46.35                22.18         0.513          pass              0.471             49.2                           0.592                7.19              0.735                                 ok            True                  False
   XEL           86.96               23            0.59              0.33         79.19                19.18         0.505          pass              0.491             56.1                           0.594                2.84              0.293                                 ok            True                  False
  TMUS           63.64               11            1.90              2.13        159.24                68.40         0.665          pass              0.165             30.5                           0.438               -0.41              0.105                                 ok           False                  False
   PEP           83.33                6            1.57              1.55        139.76                26.86         0.592          pass              0.206             19.3                           0.317                3.13              0.216                                 ok           False                  False
  PAYX           72.22               18            0.50              0.41        115.32                35.36         0.583          pass              0.363             83.8                           0.790                3.07             -0.042                                 ok           False                  False
 CMCSA           91.67               24            0.31              0.05         23.85                32.70         0.571          pass              0.708             82.0                           0.644                6.42              0.557                                 ok           False                  False
   ROP           70.00               10            1.91              6.41        476.79                37.35         0.560          pass              0.121             21.6                           0.162               18.12              1.668                                 ok           False                  False
  MRVL           86.67               30            1.67              2.01        170.55                97.23         0.556          pass              0.452             28.4                           0.262              -29.90             -3.278 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-11-03T11:45:05.991467-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:40:01.980819-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:35:05.840286-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:30:05.077695-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:25:04.545060-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:20:06.072141-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:15:01.990433-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:10:06.114764-05:00 early_entry_1110 early_entry_shadow {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "entry_ask": 7.5, "entry_bid": 6.2, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 68223.28, "hypothetical_contracts": 99, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 18.98, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.633, "shadow_only": true, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.805, "early_reclaim_pct": 69.5, "matched_signals": 32, "recovery_stability_score": 0.633, "success_rate": 96.88, "ticker": "CTAS", "timing_score": 0.496, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-11-03T11:05:06.948885-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:00:05.972600-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "CTAS261211C00225000", "current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "entry_ask": 7.5, "entry_bid": 6.1, "entry_mode": "early", "entry_option_price": 6.8, "hypothetical_budget": 68223.28, "hypothetical_contracts": 100, "matched_signals": 31, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 20.59, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.675, "shadow_only": true, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.787, "early_reclaim_pct": 65.9, "matched_signals": 31, "recovery_stability_score": 0.675, "success_rate": 96.77, "ticker": "CTAS", "timing_score": 0.498, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261103114505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261103114505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261103114505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261103114505)

</details>
