# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-18 12:20:06 EST`
Last processed slot: `manage_1230`

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

- Cash: `$105,918.80`
- Equity: `$105,918.80`
- Realized PnL: `$95,918.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-18)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP261218C00400000     17          2026-11-17         2026-11-18         31.3       28.17 -5321.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
   TXN           89.47               19            1.38              2.86        294.64                59.80         0.619          pass              0.510             45.3                           0.546               -6.33              0.171                       ok            True                  False
   ADI           90.62               32            0.82              2.19        382.73                67.50         0.612          pass              0.661             56.7                           0.565               -6.33              0.119                       ok            True                  False
   BKR           86.21               29            0.78              0.26         47.35                58.51         0.611          pass              0.488             44.9                           0.468               -5.12             -0.041                       ok            True                  False
  REGN           83.78               37            0.65              4.36        955.89                53.86         0.561          pass              0.396             19.7                           0.167                2.24              0.560                       ok            True                  False
  VRSK           80.00               25            1.40              2.01        204.45                46.89         0.551          pass              0.290             44.9                           0.613                2.32              0.178                       ok            True                  False
   CEG           91.18               34            1.02              1.91        267.25                61.66         0.547          pass              0.679             55.3                           0.479                8.15              1.137                       ok            True                  False
  INSM           83.72               43            0.75              0.64        121.59                62.27         0.536          pass              0.562             69.8                           0.767                9.95              1.106                       ok            True                  False
  SOXL           70.59               34            0.79              0.27         48.95               265.73         0.950          pass              0.509             84.8                           0.826              -26.99             -0.395  downtrend_blocked_slope           False                  False
  INTC           71.88               32            1.58              0.61         54.91               143.31         0.818          pass              0.378             49.7                           0.513               -6.81             -0.107 downtrend_blocked_streak           False                  False
  ALNY           57.89               19            2.61              2.86        155.27               110.55         0.732          pass              0.219             28.5                           0.514               -5.38             -0.065                       ok           False                  False
  LRCX           68.29               41            0.14              0.20        210.60               104.84         0.703          pass              0.550             93.2                           0.760               -4.98              0.457 downtrend_blocked_streak           False                  False
  MRVL           77.78               27            2.44              2.54        147.65               124.48         0.691          pass              0.305             40.7                           0.474               -9.19              0.115                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-11-18T12:00:06.155878-05:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:55:05.147885-05:00 early_entry_1155 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:50:04.203803-05:00 early_entry_1150 early_entry_shadow      {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "entry_ask": 6.3, "entry_bid": 5.7, "entry_mode": "early", "entry_option_price": 6.0, "hypothetical_budget": 52959.4, "hypothetical_contracts": 88, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 10.0, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.5, "matched_signals": 39, "recovery_stability_score": 0.7, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:45:05.124213-05:00 early_entry_1145 early_entry_shadow {"contract_symbol": "GILD261218C00170000", "current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "entry_ask": 6.1, "entry_bid": 5.6, "entry_mode": "early", "entry_option_price": 5.85, "hypothetical_budget": 52959.4, "hypothetical_contracts": 90, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 1168.0, "option_spread_pct": 8.55, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.694, "shadow_only": true, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.707, "early_reclaim_pct": 69.3, "matched_signals": 39, "recovery_stability_score": 0.694, "success_rate": 89.74, "ticker": "GILD", "timing_score": 0.459, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:40:04.319584-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:35:02.338548-05:00 early_entry_1135 early_entry_shadow    {"contract_symbol": "APP261218C00400000", "current_drop_pct": 0.53, "early_entry_score": 0.793, "early_reclaim_pct": 71.7, "entry_ask": 26.4, "entry_bid": 25.2, "entry_mode": "early", "entry_option_price": 25.8, "hypothetical_budget": 52959.4, "hypothetical_contracts": 20, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 1251.0, "option_spread_pct": 4.65, "option_volume": 49.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.559, "shadow_only": true, "success_rate": 91.3, "ticker": "APP", "timing_score": 0.764, "top_candidates": [{"current_drop_pct": 0.53, "early_entry_score": 0.793, "early_reclaim_pct": 71.7, "matched_signals": 46, "recovery_stability_score": 0.559, "success_rate": 91.3, "ticker": "APP", "timing_score": 0.764, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-18T11:30:05.127022-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:25:05.812808-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:20:05.157588-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-18T11:15:04.160916-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261118122006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261118122006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261118122006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261118122006)

</details>
