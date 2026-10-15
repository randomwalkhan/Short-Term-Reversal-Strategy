# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 11:10:05 EDT`
Last processed slot: `manage_1100`

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
  META           84.38               32            0.55              2.85        736.32                55.15         0.582            pass              0.566             81.4                           0.753                1.04              0.175                                 ok            True                  False
    ZS           91.18               34            1.25              1.93        219.96                59.94         0.518            pass              0.715             68.2                           0.619                9.69              1.378                                 ok            True                   True
  MPWR           85.29               34            0.51              4.45       1241.20                56.61         0.548            pass              0.616             86.8                           0.823               -9.13             -1.509            downtrend_blocked_slope           False                  False
   CEG           83.33                6            3.62              7.09        276.50                59.82         0.530            pass              0.187             15.1                           0.233                4.05              0.708                                 ok           False                  False
  SNPS           66.67                6            3.44             11.56        474.98                52.37         0.530            pass              0.158             35.1                           0.512               -5.53             -0.296 downtrend_blocked_slope_and_streak           False                  False
  CDNS           77.78               18            2.02              4.67        327.46                37.41         0.486 below_threshold              0.254             50.8                           0.626               -7.97             -0.830 downtrend_blocked_slope_and_streak           False                  False
   AEP           57.14                7            1.48              1.31        125.57                12.92         0.479 below_threshold              0.076              9.2                           0.183                3.77              0.537                                 ok           False                  False
  AVGO           81.82               22            1.66              4.01        344.53                35.83         0.476 below_threshold              0.328             50.8                           0.558               -0.91             -0.315                                 ok           False                  False
  CRWD           84.21               19            2.69              4.70        247.28                48.36         0.473 below_threshold              0.307             29.1                           0.490               -8.84             -0.902 downtrend_blocked_slope_and_streak           False                  False
  NVDA           81.82               11            2.16              3.35        219.87                25.52         0.466 below_threshold              0.232             43.4                           0.581               -6.21             -0.748 downtrend_blocked_slope_and_streak           False                  False
    MU           90.48               42            0.21              1.37        913.54                50.57         0.459 below_threshold              0.815             96.5                           0.927              -16.86             -1.880 downtrend_blocked_slope_and_streak           False                  False
   XEL           88.57               35            0.13              0.07         75.33                17.56         0.453 below_threshold              0.639             66.1                           0.348                6.68              0.660                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-15T11:10:05.939660-04:00 early_entry_1110 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "entry_ask": 14.15, "entry_bid": 13.6, "entry_mode": "early", "entry_option_price": 13.875, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.96, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.619, "shadow_only": true, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "top_candidates": [{"current_drop_pct": 1.25, "early_entry_score": 0.715, "early_reclaim_pct": 68.2, "matched_signals": 34, "recovery_stability_score": 0.619, "success_rate": 91.18, "ticker": "ZS", "timing_score": 0.518, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:05:05.115302-04:00 early_entry_1105 early_entry_shadow   {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "entry_ask": 14.0, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 13.775, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.27, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "matched_signals": 35, "recovery_stability_score": 0.632, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:00:05.305512-04:00 early_entry_1100 early_entry_shadow  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "entry_ask": 14.45, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 64367.4, "hypothetical_contracts": 45, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.43, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "matched_signals": 35, "recovery_stability_score": 0.571, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:55:05.229160-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:50:05.707569-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:45:06.384302-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:40:06.514457-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:35:06.060281-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:30:05.327948-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:25:05.094605-04:00 early_entry_1025 early_entry_shadow   {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "entry_ask": 16.1, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 15.55, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 7.07, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015111005)

</details>
