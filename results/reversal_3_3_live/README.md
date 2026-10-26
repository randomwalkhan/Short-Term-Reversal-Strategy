# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 11:05:05 EDT`
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

- Cash: `$65,421.80`
- Equity: `$142,619.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$4,927.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 77197.5          1.1           1.18       44.42         44.37          bid_ask_mid                       1.18                bid_ask_mid                    True          4927.5                   6.82          80.0               15              0.97         20.09           26.29                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KHC           89.29               28            0.56              0.10         24.76                34.81         0.544            pass              0.507             28.2                           0.216                9.84              1.088                                 ok            True                  False
  CTSH           92.00               25            1.49              0.74         70.22                46.28         0.531            pass              0.474              0.2                           0.070               16.44              1.783                                 ok            True                  False
  INTU           88.46               26            1.33              3.19        342.02                39.39         0.500 below_threshold              0.416             11.3                           0.128               10.74              1.360                                 ok            True                  False
  TMUS           87.80               41            0.07              0.07        146.51                64.13         0.611            pass              0.758             96.2                           0.867               -3.58             -0.369            downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.36              0.61         63.54                25.23         0.572            pass              0.309             17.1                           0.221                1.84              0.321                                 ok           False                  False
   KDP           96.15               26            0.42              0.10         34.64                26.07         0.543            pass              0.718             52.5                           0.410                5.45              0.640                                 ok           False                  False
  MSTR           90.32               31            1.66              1.70        145.28                68.80         0.524            pass              0.684             72.2                           0.910               -5.96             -0.317            downtrend_blocked_slope           False                  False
   ADP           93.33               30            0.33              0.69        303.86                24.93         0.511            pass              0.646             35.3                           0.253               10.72              1.141                                 ok           False                  False
 CMCSA           66.67                3            1.92              0.30         22.56                23.68         0.505            pass              0.147             32.0                           0.343                7.62              0.903                                 ok           False                  False
  NFLX           66.67               12            2.22              1.02         65.41                35.37         0.495 below_threshold              0.063              0.0                           0.177               -8.81             -1.029 downtrend_blocked_slope_and_streak           False                  False
  TEAM          100.00               30            1.52              2.42        226.57                47.89         0.493 below_threshold              0.748             55.1                           0.602                7.89              1.034                                 ok           False                  False
  VRTX           57.14                7            2.40              8.81        520.15                29.59         0.490 below_threshold              0.060              3.5                           0.136                0.86              0.594                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-26T11:05:05.800514-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:00:05.970204-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.04, "early_entry_score": 0.823, "early_reclaim_pct": 69.2, "entry_ask": 21.9, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 20.25, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.3, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.823, "early_reclaim_pct": 69.2, "matched_signals": 35, "recovery_stability_score": 0.693, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:55:05.967996-04:00 early_entry_1055 early_entry_shadow    {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.22, "early_entry_score": 0.8, "early_reclaim_pct": 63.9, "entry_ask": 21.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 20.15, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 17.37, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.639, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 1.22, "early_entry_score": 0.8, "early_reclaim_pct": 63.9, "matched_signals": 34, "recovery_stability_score": 0.639, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:50:03.944466-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:45:06.199099-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:40:05.839697-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:35:02.828763-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:30:05.918649-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.07, "early_entry_score": 0.821, "early_reclaim_pct": 68.5, "entry_ask": 21.3, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 19.55, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 17.9, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.854, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 1.07, "early_entry_score": 0.821, "early_reclaim_pct": 68.5, "matched_signals": 35, "recovery_stability_score": 0.854, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:25:07.004993-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "entry_ask": 21.1, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 19.45, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.811, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "matched_signals": 35, "recovery_stability_score": 0.811, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:20:05.900511-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TEAM261120C00230000", "fill_price": 16.065, "pnl": -7140.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026110505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026110505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026110505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026110505)

</details>
