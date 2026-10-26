# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 11:00:05 EDT`
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
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 77197.5          1.1           1.18       44.42         44.33          bid_ask_mid                       1.18                bid_ask_mid                    True          4927.5                   6.82          80.0               15              0.97         20.09           26.39                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   KDP           96.00               25            0.52              0.13         34.63                26.07         0.543            pass              0.677             41.0                           0.334                5.34              0.636                                 ok            True                  False
   KHC           88.46               26            0.79              0.14         24.74                34.81         0.542            pass              0.387              0.0                           0.163                9.60              1.078                                 ok            True                  False
  CTSH           93.33               30            1.13              0.56         70.30                46.28         0.524            pass              0.607             22.1                           0.282               16.86              1.800                                 ok            True                  False
  TMUS           87.18               39            0.25              0.26        146.43                64.13         0.611            pass              0.704             86.1                           0.847               -3.75             -0.377            downtrend_blocked_slope           False                  False
  MDLZ           66.67                3            1.57              0.70         63.50                25.23         0.570            pass              0.057              0.0                           0.172                1.63              0.312                                 ok           False                  False
   ADP           93.33               30            0.32              0.68        303.87                24.93         0.511            pass              0.650             36.6                           0.276               10.73              1.142                                 ok           False                  False
  NFLX           64.29               14            1.79              0.83         65.50                35.37         0.510            pass              0.078              0.0                           0.192               -8.41             -1.009 downtrend_blocked_slope_and_streak           False                  False
  MSTR           90.00               30            2.09              2.13        145.10                68.80         0.504            pass              0.646             65.1                           0.869               -6.37             -0.337            downtrend_blocked_slope           False                  False
  VRTX           57.14                7            2.22              8.15        520.44                29.59         0.502            pass              0.060              3.3                           0.167                1.04              0.602                                 ok           False                  False
 CMCSA           66.67                3            2.03              0.32         22.55                23.68         0.499 below_threshold              0.134             28.1                           0.369                7.50              0.898                                 ok           False                  False
  TEAM          100.00               35            1.04              1.66        226.90                47.89         0.491 below_threshold              0.823             69.2                           0.693                8.42              1.056                                 ok           False                   True
  ADBE           86.67               30            1.21              2.23        262.86                39.43         0.488 below_threshold              0.459             33.0                           0.351                9.44              1.196                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-26T11:00:05.970204-04:00 early_entry_1100 early_entry_shadow {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.04, "early_entry_score": 0.823, "early_reclaim_pct": 69.2, "entry_ask": 21.9, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 20.25, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.3, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.693, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.491, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.823, "early_reclaim_pct": 69.2, "matched_signals": 35, "recovery_stability_score": 0.693, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.491, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:55:05.967996-04:00 early_entry_1055 early_entry_shadow    {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.22, "early_entry_score": 0.8, "early_reclaim_pct": 63.9, "entry_ask": 21.9, "entry_bid": 18.4, "entry_mode": "early", "entry_option_price": 20.15, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 34, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 17.37, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.639, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.486, "top_candidates": [{"current_drop_pct": 1.22, "early_entry_score": 0.8, "early_reclaim_pct": 63.9, "matched_signals": 34, "recovery_stability_score": 0.639, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.486, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:50:03.944466-04:00 early_entry_1050 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:45:06.199099-04:00 early_entry_1045 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:40:05.839697-04:00 early_entry_1040 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:35:02.828763-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:30:05.918649-04:00 early_entry_1030 early_entry_shadow {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.07, "early_entry_score": 0.821, "early_reclaim_pct": 68.5, "entry_ask": 21.3, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 19.55, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 17.9, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.854, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.489, "top_candidates": [{"current_drop_pct": 1.07, "early_entry_score": 0.821, "early_reclaim_pct": 68.5, "matched_signals": 35, "recovery_stability_score": 0.854, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.489, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:25:07.004993-04:00 early_entry_1025 early_entry_shadow  {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "entry_ask": 21.1, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 19.45, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.811, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "matched_signals": 35, "recovery_stability_score": 0.811, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:20:05.900511-04:00 early_entry_1020 early_entry_shadow                                              {"contract_symbol": "TTWO261218C00195000", "current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "entry_ask": 20.8, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 19.7, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 555.0, "option_spread_pct": 11.17, "option_volume": 802.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.685, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-26T10:20:05.900511-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TEAM261120C00230000", "fill_price": 16.065, "pnl": -7140.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026110005)

</details>
