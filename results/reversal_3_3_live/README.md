# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-11 11:13:53 EDT`
Last processed slot: `early_entry_1110`

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

- Cash: `$17,648.00`
- Equity: `$32,148.00`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$1,075.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   1      5     13425.0                 14500.0        26.85           29.0      307.66        311.88          bid_ask_mid                       29.0                bid_ask_mid                    True          1075.0                   8.01          87.1               31              1.19         68.92           70.06                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-11)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           81.08               37            0.56              3.37        859.56               109.54         0.717          pass              0.492             70.6                           0.575                4.35              0.950                      ok            True                  False
  SHOP           97.14               35            1.25              1.36        154.60                81.38         0.648          pass              0.761             43.3                           0.482               17.62              2.596                      ok            True                  False
  GOOG           81.82               22            1.58              3.93        354.16                50.40         0.591          pass              0.263             25.1                           0.380                5.30              0.572                      ok            True                  False
  WDAY           82.86               35            0.59              0.76        183.87                68.85         0.580          pass              0.535             78.0                           0.605               14.67              1.444                      ok            True                  False
  CDNS           89.47               19            2.27              5.26        329.65                47.34         0.522          pass              0.406             13.8                           0.142               -5.90             -0.240                      ok            True                  False
  ROST           92.00               25            0.97              1.73        254.08                21.47         0.517          pass              0.525             17.6                           0.294                0.53              0.118                      ok            True                  False
  INSM           84.00               50            0.11              0.10        134.71               107.27         0.715          pass              0.663             95.0                           0.688               29.26              3.381                      ok           False                  False
  AMZN           73.68               19            1.91              3.73        276.49                61.51         0.628          pass              0.146              7.7                           0.255               18.15              1.887                      ok           False                  False
  MSFT           79.41               34            0.70              2.47        505.00                57.78         0.607          pass              0.358             45.9                           0.530               27.76              2.469                      ok           False                  False
  GEHC           94.87               39            0.26              0.13         72.88                58.44         0.600          pass              0.852             67.5                           0.382               13.48              0.764                      ok           False                  False
   ROP           96.97               33            0.38              1.07        403.43                46.36         0.593          pass              0.832             73.2                           0.576                2.93              0.211                      ok           False                  False
   KHC           88.89               18            0.78              0.14         24.87                36.31         0.583          pass              0.524             58.5                           0.687               -9.40             -1.021 downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-08-11T11:13:53.163975-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "PANW260918C00380000", "current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 78.3, "entry_ask": 33.25, "entry_bid": 31.95, "entry_mode": "early", "entry_option_price": 32.6, "hypothetical_budget": 8824.0, "hypothetical_contracts": 2, "matched_signals": 47, "option_liquidity_status": "ok", "option_open_interest": 3447.0, "option_spread_pct": 3.99, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.639, "shadow_only": true, "success_rate": 89.36, "ticker": "PANW", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 78.3, "matched_signals": 47, "recovery_stability_score": 0.639, "success_rate": 89.36, "ticker": "PANW", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-11T10:26:01.426396-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ROP260918C00400000", "current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 64.3, "entry_ask": 20.4, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 17.9, "hypothetical_budget": 8824.0, "hypothetical_contracts": 4, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 27.93, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.555, "shadow_only": true, "success_rate": 96.88, "ticker": "ROP", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 64.3, "matched_signals": 32, "recovery_stability_score": 0.555, "success_rate": 96.88, "ticker": "ROP", "timing_score": 0.591, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.679, "early_reclaim_pct": 69.3, "matched_signals": 44, "recovery_stability_score": 0.579, "success_rate": 88.64, "ticker": "PANW", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-11T00:00:05.969366-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-08-10T15:10:01.692365-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T15:05:01.609183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T15:00:04.645498-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T14:55:05.599659-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T14:50:01.766475-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-10", "training_samples": 5614, "window": 5}
2026-08-10T14:50:01.766475-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"allocated_cash": 13425.0, "asset_type": "option", "contract_symbol": "LRCX260918C00310000", "contracts": 5, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 26.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 3.35, "option_volume": 93.0, "success_rate": 87.1, "ticker": "LRCX", "timing_score": 0.649}
2026-08-10T12:00:04.535713-04:00 early_entry_1200 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "LRCX260918C00310000", "current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "entry_ask": 28.45, "entry_bid": 26.4, "entry_mode": "early", "entry_option_price": 27.425, "hypothetical_budget": 15536.5, "hypothetical_contracts": 5, "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 7.47, "option_volume": 47.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.687, "shadow_only": true, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.71, "early_reclaim_pct": 72.9, "matched_signals": 37, "recovery_stability_score": 0.687, "success_rate": 89.19, "ticker": "LRCX", "timing_score": 0.659, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260811111353)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260811111353)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260811111353)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260811111353)

</details>
