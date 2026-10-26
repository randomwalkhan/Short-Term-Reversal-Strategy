# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 11:30:06 EDT`
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

- Cash: `$65,421.80`
- Equity: `$142,619.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$4,927.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 77197.5          1.1           1.18       44.42         44.44          bid_ask_mid                       1.18                bid_ask_mid                    True          4927.5                   6.82          80.0               15              0.97         20.09           25.83                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   KHC           90.00               30            0.50              0.09         24.76                34.81         0.537            pass              0.561             35.9                           0.388                9.91              1.091                      ok            True                  False
   ADP           90.91               22            0.80              1.71        303.43                24.93         0.525            pass              0.462             12.8                           0.195               10.19              1.120                      ok            True                  False
  CTSH           87.50               16            2.31              1.14         70.05                46.28         0.525            pass              0.293              0.0                           0.150               15.47              1.745                      ok            True                  False
  TEAM          100.00               19            2.45              3.90        225.94                47.89         0.507            pass              0.594             27.6                           0.205                6.88              0.990                      ok            True                  False
  TMUS           88.64               44            0.01              0.01        146.54                64.13         0.598            pass              0.789             99.6                           0.821               -3.52             -0.366 downtrend_blocked_slope           False                  False
  MDLZ           87.50                8            1.23              0.55         63.56                25.23         0.580            pass              0.334             25.2                           0.417                1.98              0.327                      ok           False                  False
  MSTR           91.18               34            1.34              1.37        145.42                68.80         0.527            pass              0.744             77.6                           0.797               -5.65             -0.302 downtrend_blocked_slope           False                  False
   KDP           96.88               32            0.13              0.03         34.67                26.07         0.525            pass              0.855             85.2                           0.756                5.76              0.654                      ok           False                  False
 CMCSA           66.67                3            2.09              0.33         22.55                23.68         0.495 below_threshold              0.127             25.8                           0.264                7.42              0.895                      ok           False                  False
  VRTX           57.14                7            2.27              8.31        520.37                29.59         0.495 below_threshold              0.106             18.7                           0.320                1.00              0.600                      ok           False                  False
  INTU           85.71               21            1.85              4.46        341.48                39.39         0.492 below_threshold              0.290              5.1                           0.150               10.14              1.335                      ok           False                  False
  SHOP           86.05               43            0.08              0.10        168.64                41.68         0.475 below_threshold              0.679             90.2                           0.368               -5.96             -0.522 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-26T11:30:06.493290-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:25:06.575832-04:00 early_entry_1125 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:20:06.988273-04:00 early_entry_1120 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:15:05.995279-04:00 early_entry_1115 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:10:05.908583-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:05:05.800514-04:00 early_entry_1105 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T11:00:05.970204-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.04, "early_entry_score": 0.823, "early_reclaim_pct": 69.2, "entry_ask": 21.9, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 20.25, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.3, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.823, "early_reclaim_pct": 69.2, "matched_signals": 35, "recovery_stability_score": 0.693, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:55:05.967996-04:00 early_entry_1055 early_entry_shadow    {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.22, "early_entry_score": 0.8, "early_reclaim_pct": 63.9, "entry_ask": 21.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 20.15, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 17.37, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.639, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 1.22, "early_entry_score": 0.8, "early_reclaim_pct": 63.9, "matched_signals": 34, "recovery_stability_score": 0.639, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:50:03.944466-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:45:06.199099-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026113006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026113006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026113006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026113006)

</details>
