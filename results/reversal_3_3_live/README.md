# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 10:25:07 EDT`
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

- Cash: `$65,421.80`
- Equity: `$139,334.30`
- Realized PnL: `$127,691.80`
- Unrealized PnL: `$1,642.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 73912.5          1.1           1.12       44.42         44.53          bid_ask_mid                       1.12                bid_ask_mid                    True          1642.5                   2.27          80.0               15              0.97         20.09           25.05                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH           93.94               33            1.06              0.52         70.32                46.28         0.513            pass              0.608             10.7                           0.165               16.94              1.802                                 ok            True                  False
  TMUS           60.00               10            1.64              1.68        145.82                64.13         0.667            pass              0.091              8.2                           0.210               -5.09             -0.441            downtrend_blocked_slope           False                  False
   CEG           87.10               31            0.88              1.57        252.78                65.46         0.618            pass              0.533             47.3                           0.430              -14.52             -1.595 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           87.50                8            1.08              0.48         63.59                25.23         0.592            pass              0.307             15.9                           0.266                2.14              0.334                                 ok           False                  False
  MRVL           90.00               40            0.36              0.57        228.27                64.81         0.547            pass              0.770             82.9                           0.597              -14.36             -1.473            downtrend_blocked_slope           False                  False
 CMCSA           87.50                8            1.21              0.19         22.61                23.68         0.536            pass              0.425             57.0                           0.725                8.39              0.936                                 ok           False                  False
   KDP           96.55               29            0.33              0.08         34.65                26.07         0.532            pass              0.747             55.8                           0.395                5.54              0.644                                 ok           False                  False
  INTU           88.89               36            0.40              0.97        342.97                39.39         0.493 below_threshold              0.678             72.9                           0.556               11.77              1.402                                 ok           False                  False
  TEAM          100.00               35            1.05              1.67        226.89                47.89         0.490 below_threshold              0.823             69.0                           0.811                8.41              1.055                                 ok           False                   True
   ADP           94.59               37            0.04              0.09        304.12                24.93         0.486 below_threshold              0.892             91.5                           0.525               11.04              1.154                                 ok           False                  False
  META           80.95               21            1.15              5.19        640.40                42.27         0.486 below_threshold              0.370             74.1                           0.686              -14.50             -1.803 downtrend_blocked_slope_and_streak           False                  False
  MSTR           87.50               16            3.79              3.88        144.35                68.80         0.484 below_threshold              0.398             36.7                           0.692               -8.00             -0.417            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-10-26T10:25:07.004993-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "TEAM261127C00225000", "current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "entry_ask": 21.1, "entry_bid": 17.8, "entry_mode": "early", "entry_option_price": 19.45, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 35, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 16.97, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.811, "shadow_only": true, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "top_candidates": [{"current_drop_pct": 1.05, "early_entry_score": 0.823, "early_reclaim_pct": 69.0, "matched_signals": 35, "recovery_stability_score": 0.811, "success_rate": 100.0, "ticker": "TEAM", "timing_score": 0.49, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:20:05.900511-04:00 early_entry_1020 early_entry_shadow                                             {"contract_symbol": "TTWO261218C00195000", "current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "entry_ask": 20.8, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 19.7, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 555.0, "option_spread_pct": 11.17, "option_volume": 802.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.685, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-26T10:20:05.900511-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "TEAM261120C00230000", "fill_price": 16.065, "pnl": -7140.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-10-26T10:15:06.813436-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:10:04.818104-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:05:04.929222-04:00 early_entry_1005 early_entry_shadow                {"contract_symbol": "ABNB261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "entry_ask": 12.55, "entry_bid": 10.05, "entry_mode": "early", "entry_option_price": 11.3, "hypothetical_budget": 1161.8, "hypothetical_contracts": 1, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 540.0, "option_spread_pct": 22.12, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "matched_signals": 35, "recovery_stability_score": 0.623, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:00:02.755892-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T03:00:06.095406-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           {'saved': 91, 'empty': 2}
2026-10-24T02:55:06.111058-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:50:04.428173-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026102507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026102507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026102507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026102507)

</details>
