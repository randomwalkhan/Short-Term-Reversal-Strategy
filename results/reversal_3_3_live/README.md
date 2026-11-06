# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 11:35:06 EST`
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

- Cash: `$123,162.80`
- Equity: `$123,162.80`
- Realized PnL: `$113,162.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-06)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  ORLY     option         option ORLY261218C00095000    345          2026-11-05         2026-11-06        1.875      1.6875 -6468.75       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MDLZ           93.75               16            0.57              0.27         66.71                30.66         0.585          pass              0.716             83.6                           0.600                4.14              0.759                                 ok            True                  False
   KDP           96.15               26            0.56              0.14         36.83                35.93         0.542          pass              0.809             82.6                           0.743                5.78              0.623                                 ok            True                  False
  COST           80.95               21            0.63              4.70       1063.58                23.23         0.531          pass              0.368             71.9                           0.631                5.69              0.729                                 ok            True                  False
   PEP           83.33               18            1.03              1.03        142.27                27.68         0.524          pass              0.399             68.1                           0.546                4.03              0.652                                 ok            True                  False
  ORLY           93.75               16            1.39              0.89         91.11                25.42         0.511          pass              0.622             54.8                           0.517                0.33              0.126                                 ok            True                  False
  CTAS           95.00               20            1.07              1.69        225.69                27.57         0.508          pass              0.706             62.9                           0.609               -0.05              0.299                                 ok            True                  False
  FTNT           85.37               41            0.78              0.67        122.22                92.45         0.633          pass              0.599             64.1                           0.692              -32.47             -4.871 downtrend_blocked_slope_and_streak           False                  False
  MSTR           88.24               34            0.84              0.76        128.98                81.05         0.567          pass              0.649             70.9                           0.653              -12.18             -1.049            downtrend_blocked_slope           False                  False
  ISRG           85.71                7            2.27              7.43        465.34                42.48         0.564          pass              0.254             15.2                           0.246                1.24              0.364                                 ok           False                  False
 CMCSA           83.33                6            2.08              0.36         24.79                35.54         0.552          pass              0.283             46.4                           0.276                7.67              1.369                                 ok           False                  False
  PAYX           75.00                4            2.19              1.83        118.72                35.22         0.551          pass              0.204             49.5                           0.490                0.03              0.516                                 ok           False                  False
   KHC           85.71                7            2.26              0.40         25.15                36.03         0.548          pass              0.337             43.1                           0.458               -0.21              0.316                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-06T11:35:06.887510-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:30:05.913627-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:25:05.831838-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:20:05.913571-05:00 early_entry_1120 early_entry_shadow  {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "entry_ask": 2.25, "entry_bid": 2.09, "entry_mode": "early", "entry_option_price": 2.17, "hypothetical_budget": 61581.4, "hypothetical_contracts": 283, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 7.37, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "matched_signals": 39, "recovery_stability_score": 0.55, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:15:06.867015-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:10:06.064757-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:05:04.861391-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:00:05.853352-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "entry_ask": 2.4, "entry_bid": 2.28, "entry_mode": "early", "entry_option_price": 2.34, "hypothetical_budget": 61581.4, "hypothetical_contracts": 263, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 5.13, "option_volume": 85.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.583, "shadow_only": true, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "matched_signals": 37, "recovery_stability_score": 0.583, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:55:05.752017-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:50:06.578402-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106113506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106113506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106113506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106113506)

</details>
