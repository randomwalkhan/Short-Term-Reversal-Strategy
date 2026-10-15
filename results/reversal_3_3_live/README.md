# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-15 11:00:05 EDT`
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
  META           83.33               30            0.68              3.52        736.03                55.15         0.585            pass              0.512             77.1                           0.673                0.91              0.169                                 ok            True                  False
    ZS           91.43               35            1.01              1.56        220.12                59.94         0.526            pass              0.747             74.2                           0.571                9.95              1.388                                 ok            True                   True
   CEG           85.71                7            3.29              6.43        276.78                59.82         0.545            pass              0.276             23.0                           0.340                4.42              0.724                                 ok           False                  False
  MPWR           86.49               37            0.40              3.49       1241.61                56.61         0.537            pass              0.676             89.6                           0.912               -9.03             -1.504            downtrend_blocked_slope           False                  False
  SNPS           66.67                6            3.68             12.36        474.63                52.37         0.517            pass              0.144             30.6                           0.348               -5.76             -0.307 downtrend_blocked_slope_and_streak           False                  False
  CDNS           81.25               16            2.33              5.38        327.15                37.41         0.485 below_threshold              0.252             43.2                           0.584               -8.26             -0.844 downtrend_blocked_slope_and_streak           False                  False
   AEP           57.14                7            1.41              1.24        125.60                12.92         0.485 below_threshold              0.058              3.0                           0.119                3.85              0.541                                 ok           False                  False
  CRWD           85.00               20            2.45              4.28        247.45                48.36         0.481 below_threshold              0.354             35.4                           0.582               -8.61             -0.891 downtrend_blocked_slope_and_streak           False                  False
  UPRO           83.78               37            0.05              0.05        150.34                30.64         0.477 below_threshold              0.622             97.8                           0.883                1.72              0.084                                 ok           False                  False
  NVDA           83.33               12            1.99              3.09        219.98                25.52         0.471 below_threshold              0.293             47.8                           0.652               -6.05             -0.740 downtrend_blocked_slope_and_streak           False                  False
  AVGO           84.62               26            1.52              3.69        344.67                35.83         0.463 below_threshold              0.440             54.8                           0.666               -0.77             -0.309                                 ok           False                  False
    MU           90.24               41            0.27              1.74        913.39                50.57         0.462 below_threshold              0.806             95.6                           0.986              -16.91             -1.882 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  detail
2026-10-15T11:00:05.305512-04:00 early_entry_1100 early_entry_shadow                      {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "entry_ask": 14.45, "entry_bid": 13.55, "entry_mode": "early", "entry_option_price": 14.0, "hypothetical_budget": 64367.4, "hypothetical_contracts": 45, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.43, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.571, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "top_candidates": [{"current_drop_pct": 1.01, "early_entry_score": 0.747, "early_reclaim_pct": 74.2, "matched_signals": 35, "recovery_stability_score": 0.571, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.526, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:55:05.229160-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:50:05.707569-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:45:06.384302-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:40:06.514457-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:35:06.060281-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:30:05.327948-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-15T10:25:05.094605-04:00 early_entry_1025 early_entry_shadow                       {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "entry_ask": 16.1, "entry_bid": 15.0, "entry_mode": "early", "entry_option_price": 15.55, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 7.07, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.607, "shadow_only": true, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "top_candidates": [{"current_drop_pct": 1.16, "early_entry_score": 0.734, "early_reclaim_pct": 70.3, "matched_signals": 35, "recovery_stability_score": 0.607, "success_rate": 91.43, "ticker": "ZS", "timing_score": 0.517, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:20:04.114099-04:00 early_entry_1020 early_entry_shadow                        {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "entry_ask": 16.1, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.6, "hypothetical_budget": 64367.4, "hypothetical_contracts": 41, "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 2833.0, "option_spread_pct": 6.41, "option_volume": 20.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "top_candidates": [{"current_drop_pct": 0.77, "early_entry_score": 0.779, "early_reclaim_pct": 80.3, "matched_signals": 36, "recovery_stability_score": 0.703, "success_rate": 91.67, "ticker": "ZS", "timing_score": 0.534, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-15T10:15:05.162285-04:00 early_entry_1015 early_entry_shadow {"contract_symbol": "ZS261120C00220000", "current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "entry_ask": 15.6, "entry_bid": 14.05, "entry_mode": "early", "entry_option_price": 14.825, "hypothetical_budget": 64367.4, "hypothetical_contracts": 43, "matched_signals": 37, "option_liquidity_status": "low_volume", "option_open_interest": 2833.0, "option_spread_pct": 10.46, "option_volume": 18.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.731, "shadow_only": true, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.804, "early_reclaim_pct": 84.4, "matched_signals": 37, "recovery_stability_score": 0.731, "success_rate": 91.89, "ticker": "ZS", "timing_score": 0.538, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261015110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261015110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261015110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261015110005)

</details>
