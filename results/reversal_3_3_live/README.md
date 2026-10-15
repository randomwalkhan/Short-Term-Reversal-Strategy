# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 11:05:05 EDT`
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
  META           84.38               32            0.55              2.81        736.33                55.15         0.582            pass              0.567             81.7                           0.719                1.05              0.176                                 ok            True                  False
    ZS           91.43               35            1.11              1.72        220.05                59.94         0.520            pass              0.739             71.7                           0.632                9.84              1.384                                 ok            True                   True
   CEG           85.71                7            3.16              6.18        276.89                59.82         0.552            pass              0.286             26.0                           0.438                4.55              0.730                                 ok           False                  False
  MPWR           85.71               35            0.44              3.87       1241.45                56.61         0.546            pass              0.639             88.5                           0.875               -9.07             -1.506            downtrend_blocked_slope           False                  False
  SNPS           66.67                6            3.46             11.62        474.95                52.37         0.529            pass              0.157             34.7                           0.493               -5.55             -0.297 downtrend_blocked_slope_and_streak           False                  False
  CDNS           77.78               18            1.92              4.42        327.56                37.41         0.492 below_threshold              0.263             53.3                           0.649               -7.87             -0.825 downtrend_blocked_slope_and_streak           False                  False
  CRWD           85.00               20            2.48              4.32        247.44                48.36         0.480 below_threshold              0.352             34.8                           0.632               -8.63             -0.892 downtrend_blocked_slope_and_streak           False                  False
   AEP           57.14                7            1.48              1.31        125.57                12.92         0.480 below_threshold              0.048              0.0                           0.177                3.77              0.537                                 ok           False                  False
  NVDA           83.33               12            1.97              3.05        219.99                25.52         0.472 below_threshold              0.295             48.5                           0.644               -6.03             -0.739 downtrend_blocked_slope_and_streak           False                  False
  AVGO           85.71               28            1.35              3.28        344.85                35.83         0.461 below_threshold              0.498             59.8                           0.658               -0.60             -0.301                                 ok           False                  False
    MU           90.48               42            0.23              1.48        913.50                50.57         0.458 below_threshold              0.814             96.2                           0.986              -16.88             -1.880 downtrend_blocked_slope_and_streak           False                  False
   XEL           88.57               35            0.12              0.06         75.33                17.56         0.454 below_threshold              0.649             69.5                           0.364                6.69              0.661                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-10-15T11:05:05.115302-04:00 early_entry_1105 early_entry_shadow  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "entry_ask": 14.0, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 13.775, "hypothetical_budget": 64367.4, "hypothetical_contracts": 46, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 3.27, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.632, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "top_candidates": [{"current_drop_pct": 1.11, "early_entry_score": 0.739, "early_reclaim_pct": 71.7, "matched_signals": 35, "recovery_stability_score": 0.632, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.52, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T11:00:05.305512-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "entry_ask": 14.45, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 64367.4, "hypothetical_contracts": 45, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.43, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "matched_signals": 35, "recovery_stability_score": 0.571, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:55:05.229160-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:50:05.707569-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:45:06.384302-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:40:06.514457-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:35:06.060281-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:30:05.327948-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:25:05.094605-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "entry_ask": 16.1, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 15.55, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 7.07, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:20:04.114099-04:00 early_entry_1020 early_entry_shadow   {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "entry_ask": 16.1, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.6, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.41, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "matched_signals": 36, "recovery_stability_score": 0.703, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015110505)

</details>
