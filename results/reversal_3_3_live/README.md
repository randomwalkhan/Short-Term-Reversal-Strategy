# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-19 11:50:06 EST`
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

- Cash: `$100,946.30`
- Equity: `$100,946.30`
- Realized PnL: `$90,946.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-19)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   APP     option         option APP270115C00400000     15          2026-11-18         2026-11-19        33.15      29.835 -4972.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  IDXX           97.06               34            0.94              4.61        696.50                78.12         0.695          pass              0.752             40.8                           0.607                3.16              0.208                                 ok            True                  False
  COST           81.82               11            1.08              8.25       1093.08                23.52         0.575          pass              0.150             12.4                           0.280                1.81              0.432                                 ok            True                  False
  ABNB           86.21               29            1.15              1.45        179.59                55.20         0.565          pass              0.481             44.1                           0.554                4.71             -0.099                                 ok            True                  False
 CMCSA           94.12               17            1.39              0.25         25.13                34.19         0.558          pass              0.577             32.7                           0.596               -0.24              0.268                                 ok            True                  False
  AAPL           95.65               23            0.75              1.86        351.65                27.20         0.541          pass              0.680             46.3                           0.577                1.71              0.223                                 ok            True                  False
  VRSK           80.95               21            1.68              2.37        201.29                47.31         0.538          pass              0.239             28.9                           0.460               -5.94             -0.171                                 ok            True                  False
  ODFL           87.10               31            0.95              1.16        174.61                43.99         0.529          pass              0.542             53.2                           0.725                1.69              0.398                                 ok            True                  False
   ADP           81.25               16            1.33              2.85        304.35                28.97         0.524          pass              0.207             27.0                           0.403               -1.83              0.056                                 ok            True                  False
   CEG           90.91               33            1.35              2.48        261.68                59.92         0.503          pass              0.617             40.7                           0.352                8.32              0.562                                 ok            True                  False
   KDP           80.00               10            1.57              0.39         34.84                47.14         0.618          pass              0.183             40.5                           0.589               -6.59             -0.784            downtrend_blocked_slope           False                  False
   TRI           70.00               10            2.20              1.60        103.21                60.81         0.602          pass              0.186             42.1                           0.579              -13.43             -1.028            downtrend_blocked_slope           False                  False
  UPRO           83.87               31            0.79              0.69        125.10                70.38         0.594          pass              0.480             59.3                           0.535               -2.70             -0.559 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-11-19T11:50:06.328021-05:00 early_entry_1150 early_entry_shadow              {"contract_symbol": "GILD270115C00155000", "current_drop_pct": 0.81, "early_entry_score": 0.693, "early_reclaim_pct": 67.4, "entry_ask": 16.15, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 15.1, "hypothetical_budget": 50473.15, "hypothetical_contracts": 33, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1446.0, "option_spread_pct": 13.91, "option_volume": 25.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.829, "shadow_only": true, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.47, "top_candidates": [{"current_drop_pct": 0.81, "early_entry_score": 0.693, "early_reclaim_pct": 67.4, "matched_signals": 33, "recovery_stability_score": 0.829, "success_rate": 90.91, "ticker": "GILD", "timing_score": 0.47, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-11-19T11:45:05.650251-05:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:40:04.570482-05:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:35:04.658979-05:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:30:04.584516-05:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:25:05.811336-05:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:20:04.620034-05:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:15:06.374653-05:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:10:06.458962-05:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-19T11:05:05.639741-05:00 early_entry_1105 early_entry_shadow {"contract_symbol": "CEG270115C00260000", "current_drop_pct": 0.74, "early_entry_score": 0.739, "early_reclaim_pct": 67.5, "entry_ask": 19.5, "entry_bid": 18.5, "entry_mode": "early", "entry_option_price": 19.0, "hypothetical_budget": 50473.15, "hypothetical_contracts": 26, "matched_signals": 36, "option_liquidity_status": "low_volume", "option_open_interest": 643.0, "option_spread_pct": 5.26, "option_volume": 2.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.702, "shadow_only": true, "success_rate": 91.67, "ticker": "CEG", "timing_score": 0.524, "top_candidates": [{"current_drop_pct": 0.74, "early_entry_score": 0.739, "early_reclaim_pct": 67.5, "matched_signals": 36, "recovery_stability_score": 0.702, "success_rate": 91.67, "ticker": "CEG", "timing_score": 0.524, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261119115006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261119115006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261119115006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261119115006)

</details>
