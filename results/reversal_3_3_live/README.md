# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-26 10:20:05 EDT`
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
   EXC     option         option EXC261218C00045000       2026-10-23                   1    657     72270.0                 73912.5          1.1           1.12       44.42         44.58          bid_ask_mid                       1.12                bid_ask_mid                    True          1642.5                   2.27          80.0               15              0.97         20.09           24.71                  20.91                 278.0           48.0               0.09                      ok
```

## Today's Closed Trades (2026-10-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  TEAM     option         option TEAM261120C00230000     40          2026-10-22         2026-10-26        17.85      16.065 -7140.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH           94.12               34            0.98              0.48         70.33                46.28         0.512            pass              0.641             17.9                           0.242               17.04              1.806                                 ok            True                  False
  TMUS           69.23               13            1.44              1.48        145.91                64.13         0.674            pass              0.087              0.0                           0.217               -4.90             -0.431            downtrend_blocked_slope           False                  False
   CEG           85.00               40            0.31              0.55        253.21                65.46         0.597            pass              0.637             81.4                           0.629              -14.03             -1.569 downtrend_blocked_slope_and_streak           False                  False
  MDLZ           87.50                8            1.11              0.49         63.59                25.23         0.591            pass              0.301             14.0                           0.290                2.11              0.333                                 ok           False                  False
  MRVL           90.00               40            0.09              0.15        228.45                64.81         0.564            pass              0.810             95.6                           0.603              -14.13             -1.461            downtrend_blocked_slope           False                  False
 CMCSA           85.71                7            1.30              0.21         22.60                23.68         0.535            pass              0.368             53.9                           0.746                8.29              0.932                                 ok           False                  False
   KDP           96.67               30            0.27              0.07         34.65                26.07         0.529            pass              0.777             63.5                           0.474                5.60              0.647                                 ok           False                  False
  MSTR           85.00               20            3.05              3.12        144.67                68.80         0.501            pass              0.397             49.0                           0.748               -7.29             -0.382            downtrend_blocked_slope           False                  False
   ADP           94.12               34            0.20              0.43        303.98                24.93         0.495 below_threshold              0.766             60.1                           0.428               10.86              1.147                                 ok           False                  False
  AAPL           90.48               21            0.90              2.19        346.79                16.45         0.492 below_threshold              0.562             53.2                           0.727                1.06              0.158                                 ok           False                  False
  TEAM          100.00               31            1.45              2.31        226.62                47.89         0.491 below_threshold              0.761             57.2                           0.728                7.97              1.037                                 ok           False                  False
  INTU           89.19               37            0.36              0.86        343.02                39.39         0.490 below_threshold              0.702             76.0                           0.624               11.82              1.404                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-10-26T10:20:05.900511-04:00 early_entry_1020 early_entry_shadow                              {"contract_symbol": "TTWO261218C00195000", "current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "entry_ask": 20.8, "entry_bid": 18.6, "entry_mode": "early", "entry_option_price": 19.7, "hypothetical_budget": 32710.9, "hypothetical_contracts": 16, "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 555.0, "option_spread_pct": 11.17, "option_volume": 802.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.685, "shadow_only": true, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "top_candidates": [{"current_drop_pct": 0.59, "early_entry_score": 0.772, "early_reclaim_pct": 68.3, "matched_signals": 39, "recovery_stability_score": 0.685, "success_rate": 92.31, "ticker": "TTWO", "timing_score": 0.454, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-26T10:20:05.900511-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"asset_type": "option", "contract_symbol": "TEAM261120C00230000", "fill_price": 16.065, "pnl": -7140.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "TEAM"}
2026-10-26T10:15:06.813436-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:10:04.818104-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T10:05:04.929222-04:00 early_entry_1005 early_entry_shadow {"contract_symbol": "ABNB261218C00170000", "current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "entry_ask": 12.55, "entry_bid": 10.05, "entry_mode": "early", "entry_option_price": 11.3, "hypothetical_budget": 1161.8, "hypothetical_contracts": 1, "matched_signals": 35, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 540.0, "option_spread_pct": 22.12, "option_volume": 5.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.623, "shadow_only": true, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "top_candidates": [{"current_drop_pct": 0.64, "early_entry_score": 0.705, "early_reclaim_pct": 62.5, "matched_signals": 35, "recovery_stability_score": 0.623, "success_rate": 91.43, "ticker": "ABNB", "timing_score": 0.462, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-10-26T10:00:02.755892-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-26T03:00:06.095406-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {'saved': 91, 'empty': 2}
2026-10-24T02:55:06.111058-04:00   share_ext_0255      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:50:04.428173-04:00   share_ext_0250      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
2026-10-24T02:45:06.637393-04:00   share_ext_0245      market_closed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"holiday_name": null, "reason": "weekend"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261026102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261026102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261026102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261026102005)

</details>
