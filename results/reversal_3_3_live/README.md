# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 11:05:04 EDT`
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

- Cash: `$74,478.10`
- Equity: `$74,478.10`
- Realized PnL: `$64,478.10`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-09-03)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct                  exit_reason
  CPRT     option         option CPRT261016C00032500    144          2026-09-01         2026-09-03        1.650       2.800 16560.0   69.696970 take_profit_day2_hit_at_scan
  MSTR     option         option MSTR261009C00122000     20          2026-09-02         2026-09-03       11.475      16.575 10200.0   44.444444 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  DRAM           81.25               32            1.14              0.45         56.02                63.42         0.578            pass              0.438             66.8                           0.821               -3.49             -0.204                                 ok            True                  False
  REGN          100.00               16            1.34              7.99        848.61                27.66         0.543            pass              0.557             20.8                           0.360                1.69              0.038                                 ok            True                  False
  SBUX           95.24               21            0.73              0.54        106.49                21.58         0.527            pass              0.671             48.3                           0.573                1.88              0.041                                 ok            True                  False
 CMCSA           92.31               26            0.80              0.15         26.75                26.14         0.505            pass              0.577             30.6                           0.351                0.66             -0.086                                 ok            True                  False
  SOXL           83.33               36            1.43              1.06        105.89                96.37         0.587            pass              0.562             80.3                           0.916              -14.22             -1.374            downtrend_blocked_slope           False                  False
   STX           87.50               32            0.98              5.52        806.17                70.48         0.575            pass              0.652             82.5                           0.907               -5.83             -0.384 downtrend_blocked_slope_and_streak           False                  False
  MCHP           88.24               34            0.73              0.37         72.60                58.99         0.573            pass              0.668             77.1                           0.811               -4.15             -0.453            downtrend_blocked_slope           False                  False
   WDC           81.08               37            0.44              1.39        448.30                80.52         0.543            pass              0.542             92.9                           0.971               -4.72             -0.231           downtrend_blocked_streak           False                  False
    MU           86.84               38            0.11              0.77        955.75                51.19         0.535            pass              0.714             97.1                           0.931               -1.99             -0.019                                 ok           False                  False
  CSCO           90.48               42            0.11              0.08        109.42                36.36         0.510            pass              0.812             93.8                           0.774               -0.23             -0.105                                 ok           False                  False
  AMGN           97.06               34            0.05              0.16        442.77                21.97         0.494 below_threshold              0.895             95.1                           0.756                2.64              0.044                                 ok           False                  False
  AMAT           86.11               36            0.95              2.93        437.21                43.96         0.489 below_threshold              0.583             66.1                           0.840              -12.48             -1.396 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-03T11:05:04.957756-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                            {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.52, "early_entry_score": 0.758, "early_reclaim_pct": 74.4, "entry_ask": 7.5, "entry_bid": 6.8, "entry_mode": "early", "entry_option_price": 7.15, "hypothetical_budget": 37239.05, "hypothetical_contracts": 52, "matched_signals": 44, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 71.0, "option_spread_pct": 9.79, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.441, "top_candidates": [{"current_drop_pct": 0.52, "early_entry_score": 0.758, "early_reclaim_pct": 74.4, "matched_signals": 44, "recovery_stability_score": 0.687, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.441, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:59:54.471518-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:40:04.774963-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:35:03.916601-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:30:01.957262-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:25:01.994786-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                              {"contract_symbol": "CSCO261016C00110000", "current_drop_pct": 0.57, "early_entry_score": 0.675, "early_reclaim_pct": 66.3, "entry_ask": 3.5, "entry_bid": 3.35, "entry_mode": "early", "entry_option_price": 3.425, "hypothetical_budget": 37239.05, "hypothetical_contracts": 108, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2875.0, "option_spread_pct": 4.38, "option_volume": 161.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.511, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.675, "early_reclaim_pct": 66.3, "matched_signals": 37, "recovery_stability_score": 0.7, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.511, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-03T10:20:02.736149-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.58, "early_entry_score": 0.728, "early_reclaim_pct": 71.7, "entry_ask": 7.7, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 37239.05, "hypothetical_contracts": 54, "matched_signals": 40, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 71.0, "option_spread_pct": 24.82, "option_volume": 57.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.728, "early_reclaim_pct": 71.7, "matched_signals": 40, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.461, "trend_health_status": "ok"}, {"current_drop_pct": 0.53, "early_entry_score": 0.682, "early_reclaim_pct": 68.5, "matched_signals": 37, "recovery_stability_score": 0.637, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.513, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:15:01.925464-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.51, "early_entry_score": 0.76, "early_reclaim_pct": 75.0, "entry_ask": 7.7, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 37239.05, "hypothetical_contracts": 54, "matched_signals": 44, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 71.0, "option_spread_pct": 24.82, "option_volume": 57.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.781, "shadow_only": true, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.76, "early_reclaim_pct": 75.0, "matched_signals": 44, "recovery_stability_score": 0.781, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:10:01.856721-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:05:01.913040-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903110504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903110504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903110504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903110504)

</details>
