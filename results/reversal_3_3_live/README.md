# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-06 11:25:05 EST`
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
   KDP           95.65               23            0.64              0.16         36.82                35.93         0.555          pass              0.782             80.1                           0.785                5.69              0.619                                 ok            True                  False
 CMCSA           92.31               13            1.50              0.26         24.84                35.54         0.551          pass              0.587             61.3                           0.466                8.31              1.396                                 ok            True                  False
  COST           81.82               22            0.53              3.95       1063.90                23.23         0.532          pass              0.411             76.4                           0.651                5.80              0.734                                 ok            True                  False
   PEP           88.24               17            1.07              1.06        142.25                27.68         0.531          pass              0.520             66.9                           0.598                3.99              0.650                                 ok            True                  False
  CTAS           94.12               17            1.27              2.01        225.55                27.57         0.513          pass              0.642             56.0                           0.606               -0.25              0.290                                 ok            True                  False
  ORLY          100.00               14            1.71              1.09         91.02                25.42         0.509          pass              0.611             44.5                           0.350                0.01              0.111                                 ok            True                  False
  FTNT           83.78               37            1.11              0.95        122.10                92.45         0.635          pass              0.492             49.1                           0.480              -32.69             -4.886 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           95.00               20            0.49              0.23         66.72                30.66         0.566          pass              0.781             85.8                           0.663                4.22              0.763                                 ok           False                  False
  ISRG           85.71                7            2.28              7.47        465.32                42.48         0.563          pass              0.253             14.8                           0.290                1.23              0.364                                 ok           False                  False
   KHC           85.71                7            2.25              0.40         25.15                36.03         0.549          pass              0.338             43.5                           0.549               -0.20              0.317                                 ok           False                  False
  PAYX           75.00                4            2.22              1.86        118.70                35.22         0.549          pass              0.201             48.8                           0.584                0.00              0.514                                 ok           False                  False
   CSX           66.67                6            1.79              0.64         50.56                30.62         0.544          pass              0.106             17.3                           0.353               -1.71             -0.180                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-11-06T11:25:05.831838-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:20:05.913571-05:00 early_entry_1120 early_entry_shadow  {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "entry_ask": 2.25, "entry_bid": 2.09, "entry_mode": "early", "entry_option_price": 2.17, "hypothetical_budget": 61581.4, "hypothetical_contracts": 283, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 7.37, "option_volume": 91.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.55, "shadow_only": true, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.748, "early_reclaim_pct": 84.5, "matched_signals": 39, "recovery_stability_score": 0.55, "success_rate": 89.74, "ticker": "SBUX", "timing_score": 0.415, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T11:15:06.867015-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:10:06.064757-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:05:04.861391-05:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T11:00:05.853352-05:00 early_entry_1100 early_entry_shadow {"contract_symbol": "SBUX261218C00110000", "current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "entry_ask": 2.4, "entry_bid": 2.28, "entry_mode": "early", "entry_option_price": 2.34, "hypothetical_budget": 61581.4, "hypothetical_contracts": 263, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 12765.0, "option_spread_pct": 5.13, "option_volume": 85.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.583, "shadow_only": true, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.716, "early_reclaim_pct": 82.8, "matched_signals": 37, "recovery_stability_score": 0.583, "success_rate": 89.19, "ticker": "SBUX", "timing_score": 0.423, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-06T10:55:05.752017-05:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:50:06.578402-05:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:45:05.896863-05:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-06T10:40:04.864524-05:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261106112505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261106112505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261106112505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261106112505)

</details>
