# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-09-03 10:59:54 EDT`
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
  DRAM           83.33               30            1.67              0.66         55.93                63.42         0.560            pass              0.432             51.2                           0.638               -4.01             -0.229                                 ok            True                  False
  REGN          100.00               16            1.31              7.79        848.69                27.66         0.545            pass              0.563             22.7                           0.385                1.73              0.040                                 ok            True                  False
  SBUX           94.12               17            0.94              0.70        106.42                21.58         0.537            pass              0.577             33.3                           0.512                1.66              0.032                                 ok            True                  False
 CMCSA           92.00               25            0.86              0.16         26.74                26.14         0.507            pass              0.548             25.8                           0.314                0.61             -0.089                                 ok            True                  False
    MU           85.71               35            0.89              5.98        953.52                51.19         0.505            pass              0.601             77.0                           0.761               -2.75             -0.055                                 ok            True                  False
  MCHP           87.88               33            0.86              0.44         72.57                58.99         0.571            pass              0.639             72.9                           0.744               -4.28             -0.459            downtrend_blocked_slope           False                  False
  SOXL           82.35               34            2.30              1.72        105.61                96.37         0.544            pass              0.482             68.3                           0.852              -14.98             -1.415            downtrend_blocked_slope           False                  False
   STX           84.62               26            2.16             12.23        803.30                70.48         0.536            pass              0.467             61.2                           0.766               -6.96             -0.439 downtrend_blocked_slope_and_streak           False                  False
  SNPS           92.00               50            0.09              0.26        415.86                57.94         0.526            pass              0.833             86.8                           0.422                4.44              0.698                                 ok           False                  False
   WDC           79.31               29            1.57              4.93        446.79                80.52         0.521            pass              0.403             74.8                           0.856               -5.80             -0.282 downtrend_blocked_slope_and_streak           False                  False
  CSCO           90.24               41            0.36              0.28        109.34                36.36         0.500            pass              0.759             78.7                           0.662               -0.48             -0.116                                 ok           False                  False
  PAYX          100.00               35            0.03              0.03        123.99                25.89         0.498 below_threshold              0.903             95.6                           0.408                0.85              0.066                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-09-03T10:59:54.471518-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:40:04.774963-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:35:03.916601-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:30:01.957262-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:25:01.994786-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                              {"contract_symbol": "CSCO261016C00110000", "current_drop_pct": 0.57, "early_entry_score": 0.675, "early_reclaim_pct": 66.3, "entry_ask": 3.5, "entry_bid": 3.35, "entry_mode": "early", "entry_option_price": 3.425, "hypothetical_budget": 37239.05, "hypothetical_contracts": 108, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2875.0, "option_spread_pct": 4.38, "option_volume": 161.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.7, "shadow_only": true, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.511, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.675, "early_reclaim_pct": 66.3, "matched_signals": 37, "recovery_stability_score": 0.7, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.511, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-09-03T10:20:02.736149-04:00 early_entry_1020 early_entry_shadow {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.58, "early_entry_score": 0.728, "early_reclaim_pct": 71.7, "entry_ask": 7.7, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 37239.05, "hypothetical_contracts": 54, "matched_signals": 40, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 71.0, "option_spread_pct": 24.82, "option_volume": 57.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.661, "shadow_only": true, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.461, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.728, "early_reclaim_pct": 71.7, "matched_signals": 40, "recovery_stability_score": 0.661, "success_rate": 90.0, "ticker": "INSM", "timing_score": 0.461, "trend_health_status": "ok"}, {"current_drop_pct": 0.53, "early_entry_score": 0.682, "early_reclaim_pct": 68.5, "matched_signals": 37, "recovery_stability_score": 0.637, "success_rate": 89.19, "ticker": "CSCO", "timing_score": 0.513, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:15:01.925464-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                           {"contract_symbol": "INSM261016C00125000", "current_drop_pct": 0.51, "early_entry_score": 0.76, "early_reclaim_pct": 75.0, "entry_ask": 7.7, "entry_bid": 6.0, "entry_mode": "early", "entry_option_price": 6.85, "hypothetical_budget": 37239.05, "hypothetical_contracts": 54, "matched_signals": 44, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 71.0, "option_spread_pct": 24.82, "option_volume": 57.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.781, "shadow_only": true, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.442, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.76, "early_reclaim_pct": 75.0, "matched_signals": 44, "recovery_stability_score": 0.781, "success_rate": 90.91, "ticker": "INSM", "timing_score": 0.442, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-09-03T10:10:01.856721-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:05:01.913040-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-03T10:00:03.820107-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260903105954)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260903105954)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260903105954)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260903105954)

</details>
