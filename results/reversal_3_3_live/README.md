# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 11:35:05 EDT`
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

- Cash: `$128,734.80`
- Equity: `$128,734.80`
- Realized PnL: `$118,734.80`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-15)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  CSCO     option         option CSCO261120C00115000    115          2026-10-14         2026-10-15         5.85       5.265 -6727.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    ZS           92.59               27            1.86              2.87        219.56                59.94         0.526            pass              0.660             52.6                           0.357                9.01              1.349                                 ok            True                  False
  META           85.71               35            0.28              1.47        736.91                55.15         0.581            pass              0.649             90.5                           0.790                1.31              0.188                                 ok           False                  False
   CEG           88.89                9            2.87              5.62        277.13                59.82         0.559            pass              0.391             32.7                           0.634                4.86              0.743                                 ok           False                  False
  SNPS           71.43                7            3.05             10.25        475.54                52.37         0.549            pass              0.182             42.5                           0.666               -5.15             -0.278 downtrend_blocked_slope_and_streak           False                  False
  MPWR           87.50               40            0.25              2.17       1242.18                56.61         0.529            pass              0.734             93.6                           0.734               -8.89             -1.497            downtrend_blocked_slope           False                  False
  CDNS           77.78               18            1.68              3.88        327.80                37.41         0.505            pass              0.281             59.1                           0.726               -7.65             -0.814 downtrend_blocked_slope_and_streak           False                  False
  AVGO           85.00               20            1.79              4.34        344.39                35.83         0.484 below_threshold              0.389             46.8                           0.512               -1.04             -0.321                                 ok           False                  False
   AEP           62.50                8            1.38              1.22        125.61                12.92         0.484 below_threshold              0.094             15.3                           0.363                3.87              0.542                                 ok           False                  False
   ADI           88.46               26            0.80              2.27        402.60                27.65         0.473 below_threshold              0.576             65.5                           0.433               -1.06             -0.269                                 ok           False                  False
  NVDA           83.33               12            2.05              3.18        219.94                25.52         0.467 below_threshold              0.288             46.2                           0.563               -6.11             -0.743 downtrend_blocked_slope_and_streak           False                  False
  CRWD           80.00               15            3.18              5.54        246.91                48.36         0.466 below_threshold              0.129             16.4                           0.255               -9.29             -0.925 downtrend_blocked_slope_and_streak           False                  False
  PANW           77.78               27            2.10              5.52        372.67                49.46         0.464 below_threshold              0.283             40.9                           0.468               -7.34             -0.718 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-15T11:35:05.966288-04:00 early_entry_1135 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:30:05.086968-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:25:06.119732-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:20:05.131214-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T11:15:06.283716-04:00 early_entry_1115 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "entry_ask": 15.15, "entry_bid": 13.9, "entry_mode": "early", "entry_option_price": 14.525, "hypothetical_budget": 64367.4, "hypothetical_contracts": 44, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 8.61, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.665, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.4, "matched_signals": 35, "recovery_stability_score": 0.665, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:10:05.939660-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "entry_ask": 14.15, "entry_bid": 13.6, "entry_mode": "early", "entry_option_price": 13.875, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.96, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "top_candidates": [{"current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:05:05.115302-04:00 early_entry_1105 early_entry_shadow   {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "entry_ask": 14.0, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 13.775, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.27, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "matched_signals": 35, "recovery_stability_score": 0.632, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:00:05.305512-04:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "entry_ask": 14.45, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 64367.4, "hypothetical_contracts": 45, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.43, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "matched_signals": 35, "recovery_stability_score": 0.571, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:55:05.229160-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:50:05.707569-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015113505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015113505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015113505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015113505)

</details>
