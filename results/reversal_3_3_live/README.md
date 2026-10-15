# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 10:25:05 EDT`
Last processed slot: `manage_1030`

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
  META           81.48               27            0.87              4.49        735.62                55.15         0.590            pass              0.424             70.8                           0.631                0.72              0.161                                 ok            True                  False
    ZS           91.43               35            1.16              1.80        220.02                59.94         0.517            pass              0.734             70.3                           0.607                9.78              1.381                                 ok            True                   True
  MSTR           86.67               30            2.15              2.16        142.31                78.69         0.545            pass              0.555             63.0                           0.858              -12.68             -1.360 downtrend_blocked_slope_and_streak           False                  False
  MPWR           82.61               23            1.66             14.46       1236.91                56.61         0.545            pass              0.382             57.1                           0.520              -10.18             -1.562            downtrend_blocked_slope           False                  False
   CEG           85.71                7            3.33              6.52        276.75                59.82         0.543            pass              0.273             22.0                           0.346                4.37              0.722                                 ok           False                  False
  SNPS           71.43                7            3.27             10.98        475.22                52.37         0.537            pass              0.169             38.3                           0.680               -5.36             -0.288 downtrend_blocked_slope_and_streak           False                  False
  UPRO           88.89               27            0.93              0.98        149.94                30.64         0.488 below_threshold              0.562             54.4                           0.729                0.82              0.043                                 ok           False                  False
  AVGO           84.21               19            1.85              4.48        344.33                35.83         0.486 below_threshold              0.356             45.1                           0.722               -1.10             -0.324                                 ok           False                  False
  CDNS           81.25               16            2.38              5.48        327.11                37.41         0.483 below_threshold              0.248             42.2                           0.633               -8.30             -0.846 downtrend_blocked_slope_and_streak           False                  False
  NVDA           90.00               10            2.30              3.56        219.78                25.52         0.473 below_threshold              0.434             39.9                           0.710               -6.34             -0.754 downtrend_blocked_slope_and_streak           False                  False
   ADI           85.71               21            1.29              3.65        402.01                27.65         0.472 below_threshold              0.406             44.5                           0.238               -1.54             -0.291            downtrend_blocked_slope           False                  False
  MELI           82.98               47            0.04              0.48       1838.91                40.65         0.467 below_threshold              0.619             97.6                           0.738                9.10              0.753                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-10-15T10:25:05.094605-04:00 early_entry_1025 early_entry_shadow                                                 {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "entry_ask": 16.1, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 15.55, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 7.07, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:20:04.114099-04:00 early_entry_1020 early_entry_shadow                                                  {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "entry_ask": 16.1, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.6, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.41, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "matched_signals": 36, "recovery_stability_score": 0.703, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:15:05.162285-04:00 early_entry_1015 early_entry_shadow                           {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "entry_ask": 15.6, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.825, "hypothetical_budget": 64367.4, "hypothetical_contracts": 43, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 2833.0, "option_spread_pct": 10.46, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "matched_signals": 37, "recovery_stability_score": 0.731, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T10:10:06.336303-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:05:05.165659-04:00 early_entry_1005 early_entry_shadow               {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "entry_ask": 17.4, "entry_bid": 15.05, "entry_mode": "early", "entry_option_price": 16.225, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 2833.0, "option_spread_pct": 14.48, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.643, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "top_candidates": [{"current_drop_pct": 0.72, "early_entry_score": 0.796, "early_reclaim_pct": 81.7, "matched_signals": 37, "recovery_stability_score": 0.643, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.532, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T10:00:06.074428-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ZS261113C00217500", "current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "entry_ask": 17.75, "entry_bid": 14.9, "entry_mode": "early", "entry_option_price": 16.325, "hypothetical_budget": 64367.4, "hypothetical_contracts": 39, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 3.0, "option_spread_pct": 17.46, "option_volume": 0.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.617, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.746, "early_reclaim_pct": 74.0, "matched_signals": 35, "recovery_stability_score": 0.617, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-15T09:50:06.230467-04:00      manage_1000               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "CSCO261120C00115000", "fill_price": 5.265, "pnl": -6727.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "CSCO"}
2026-10-15T00:00:06.592550-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 91, 'empty': 2}
2026-10-14T15:10:06.171047-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-10-14T15:05:05.885010-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015102505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015102505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015102505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015102505)

</details>
