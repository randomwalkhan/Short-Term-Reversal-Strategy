# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 10:50:05 EDT`
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
  META           84.62               26            0.91              4.68        735.54                55.15         0.597            pass              0.498             69.6                           0.552                0.68              0.159                                 ok            True                  False
    ZS           89.66               29            1.76              2.72        219.62                59.94         0.517            pass              0.601             55.1                           0.301                9.12              1.354                                 ok            True                  False
  MSTR           87.80               41            0.06              0.06        143.21                78.69         0.598            pass              0.765             98.9                           0.993              -10.81             -1.264 downtrend_blocked_slope_and_streak           False                  False
   CEG           88.89                9            2.92              5.72        277.09                59.82         0.557            pass              0.387             31.6                           0.608                4.81              0.741                                 ok           False                  False
  MPWR           82.14               28            1.09              9.47       1239.05                56.61         0.547            pass              0.448             71.9                           0.809               -9.65             -1.535            downtrend_blocked_slope           False                  False
  SNPS           66.67                6            3.74             12.55        474.55                52.37         0.514            pass              0.140             29.5                           0.307               -5.82             -0.310 downtrend_blocked_slope_and_streak           False                  False
   AEP           63.64               11            1.16              1.02        125.69                12.92         0.481 below_threshold              0.115             20.2                           0.269                4.11              0.552                                 ok           False                  False
  CDNS           76.47               17            2.27              5.24        327.21                37.41         0.478 below_threshold              0.229             44.8                           0.540               -8.20             -0.841 downtrend_blocked_slope_and_streak           False                  False
  UPRO           84.85               33            0.48              0.50        150.14                30.64         0.475 below_threshold              0.560             76.5                           0.792                1.28              0.064                                 ok           False                  False
  AVGO           81.82               22            1.69              4.09        344.50                35.83         0.474 below_threshold              0.325             49.8                           0.687               -0.94             -0.316                                 ok           False                  False
  SHOP           84.62               39            0.57              0.68        172.21                48.53         0.471 below_threshold              0.632             89.5                           0.677               15.05              1.560                                 ok           False                  False
  CRWD           81.25               16            3.03              5.29        247.02                48.36         0.469 below_threshold              0.181             20.2                           0.345               -9.15             -0.918 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-15T10:50:05.707569-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:45:06.384302-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:40:06.514457-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:35:06.060281-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:30:05.327948-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:25:05.094605-04:00 early_entry_1025 early_entry_shadow                                   {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "entry_ask": 16.1, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 15.55, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 7.07, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:20:04.114099-04:00 early_entry_1020 early_entry_shadow                                    {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "entry_ask": 16.1, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.6, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.41, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "matched_signals": 36, "recovery_stability_score": 0.703, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:15:05.162285-04:00 early_entry_1015 early_entry_shadow             {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "entry_ask": 15.6, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.825, "hypothetical_budget": 64367.4, "hypothetical_contracts": 43, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 2833.0, "option_spread_pct": 10.46, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "matched_signals": 37, "recovery_stability_score": 0.731, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T10:10:06.336303-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:05:05.165659-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "entry_ask": 17.4, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 16.225, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 2833.0, "option_spread_pct": 14.48, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "matched_signals": 37, "recovery_stability_score": 0.643, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015105005)

</details>
