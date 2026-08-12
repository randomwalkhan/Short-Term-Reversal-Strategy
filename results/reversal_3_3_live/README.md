# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-11 20:35:03 EDT`
Last processed slot: `share_ext_2035`

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
- Equity: `$31,360.50`
- Realized PnL: `$21,073.00`
- Unrealized PnL: `$287.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  LRCX     option         option LRCX260918C00310000       2026-08-10                   1      5     13425.0                 13712.5        26.85          27.42      307.66        312.98          bid_ask_mid                      27.42                bid_ask_mid                    True           287.5                   2.14          87.1               31              1.19         68.92           66.92                  90.05                1499.0           93.0               0.03                      ok
```

## Today's Closed Trades (2026-08-11)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-08-11T11:31:47.849981-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                      {"contract_symbol": "PANW260918C00380000", "current_drop_pct": 0.6, "early_entry_score": 0.708, "early_reclaim_pct": 74.5, "entry_ask": 33.15, "entry_bid": 31.2, "entry_mode": "early", "entry_option_price": 32.175, "hypothetical_budget": 8824.0, "hypothetical_contracts": 2, "matched_signals": 46, "option_liquidity_status": "ok", "option_open_interest": 3447.0, "option_spread_pct": 6.06, "option_volume": 31.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.556, "shadow_only": true, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.6, "early_entry_score": 0.708, "early_reclaim_pct": 74.5, "matched_signals": 46, "recovery_stability_score": 0.556, "success_rate": 89.13, "ticker": "PANW", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-11T11:13:53.163975-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                     {"contract_symbol": "PANW260918C00380000", "current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 78.3, "entry_ask": 33.25, "entry_bid": 31.95, "entry_mode": "early", "entry_option_price": 32.6, "hypothetical_budget": 8824.0, "hypothetical_contracts": 2, "matched_signals": 47, "option_liquidity_status": "ok", "option_open_interest": 3447.0, "option_spread_pct": 3.99, "option_volume": 21.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.639, "shadow_only": true, "success_rate": 89.36, "ticker": "PANW", "timing_score": 0.407, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.725, "early_reclaim_pct": 78.3, "matched_signals": 47, "recovery_stability_score": 0.639, "success_rate": 89.36, "ticker": "PANW", "timing_score": 0.407, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-08-11T10:26:01.426396-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ROP260918C00400000", "current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 64.3, "entry_ask": 20.4, "entry_bid": 15.4, "entry_mode": "early", "entry_option_price": 17.9, "hypothetical_budget": 8824.0, "hypothetical_contracts": 4, "matched_signals": 32, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 34.0, "option_spread_pct": 27.93, "option_volume": 1.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.555, "shadow_only": true, "success_rate": 96.88, "ticker": "ROP", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 0.51, "early_entry_score": 0.799, "early_reclaim_pct": 64.3, "matched_signals": 32, "recovery_stability_score": 0.555, "success_rate": 96.88, "ticker": "ROP", "timing_score": 0.591, "trend_health_status": "ok"}, {"current_drop_pct": 0.73, "early_entry_score": 0.679, "early_reclaim_pct": 69.3, "matched_signals": 44, "recovery_stability_score": 0.579, "success_rate": 88.64, "ticker": "PANW", "timing_score": 0.411, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-11T00:00:05.969366-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {'saved': 93}
2026-08-10T15:10:01.692365-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T15:05:01.609183-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T15:00:04.645498-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T14:55:05.599659-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-08-10T14:50:01.766475-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"allocated_cash": 13425.0, "asset_type": "option", "contract_symbol": "LRCX260918C00310000", "contracts": 5, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 26.85, "execution_mode": "option", "matched_signals": 31, "option_liquidity_status": "ok", "option_open_interest": 1499.0, "option_spread_pct": 3.35, "option_volume": 93.0, "success_rate": 87.1, "ticker": "LRCX", "timing_score": 0.649}
2026-08-10T14:50:01.766475-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-10", "training_samples": 5614, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260811203503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260811203503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260811203503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260811203503)

</details>
