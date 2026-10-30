# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-30 06:25:04 EDT`
Last processed slot: `share_ext_0625`

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

- Cash: `$61,734.30`
- Equity: `$125,489.30`
- Realized PnL: `$113,336.80`
- Unrealized PnL: `$2,152.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  MSTR     option         option MSTR261218C00140000       2026-10-29                   1     41     61602.5                 63755.0        15.02          15.55      141.06        132.17     last_price_stale                        NaN                unavailable                   False          2152.5                   3.49         86.96               23              2.82         69.46             0.0                  71.12                1665.0           96.0               0.02                      ok
```

## Today's Closed Trades (2026-10-30)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     detail
2026-10-30T00:00:05.693119-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {'saved': 91, 'empty': 2}
2026-10-29T15:10:05.741220-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T15:05:04.728633-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T15:00:04.604775-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T14:55:06.721591-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            {"reason": "already_processed"}
2026-10-29T14:50:05.643869-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"allocated_cash": 61602.5, "asset_type": "option", "contract_symbol": "MSTR261218C00140000", "contracts": 41, "early_entry_score": 0.432, "entry_mode": "regular", "entry_option_price": 15.025, "execution_mode": "option", "matched_signals": 23, "option_liquidity_status": "ok", "option_open_interest": 1665.0, "option_spread_pct": 2.33, "option_volume": 96.0, "success_rate": 86.96, "ticker": "MSTR", "timing_score": 0.554}
2026-10-29T14:50:05.643869-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-29", "training_samples": 6227, "window": 5}
2026-10-29T12:00:05.637930-04:00 early_entry_1200 early_entry_shadow    {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.02, "early_entry_score": 0.747, "early_reclaim_pct": 76.4, "entry_ask": 14.7, "entry_bid": 14.3, "entry_mode": "early", "entry_option_price": 14.5, "hypothetical_budget": 61668.4, "hypothetical_contracts": 42, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 2.76, "option_volume": 136.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.658, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.594, "top_candidates": [{"current_drop_pct": 1.02, "early_entry_score": 0.747, "early_reclaim_pct": 76.4, "matched_signals": 34, "recovery_stability_score": 0.658, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.594, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:55:05.739980-04:00 early_entry_1155 early_entry_shadow {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.04, "early_entry_score": 0.745, "early_reclaim_pct": 76.0, "entry_ask": 14.8, "entry_bid": 14.35, "entry_mode": "early", "entry_option_price": 14.575, "hypothetical_budget": 61668.4, "hypothetical_contracts": 42, "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 3.09, "option_volume": 136.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.667, "shadow_only": true, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.593, "top_candidates": [{"current_drop_pct": 1.04, "early_entry_score": 0.745, "early_reclaim_pct": 76.0, "matched_signals": 34, "recovery_stability_score": 0.667, "success_rate": 91.18, "ticker": "MSTR", "timing_score": 0.593, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
2026-10-29T11:50:04.572626-04:00 early_entry_1150 early_entry_shadow {"contract_symbol": "MSTR261218C00145000", "current_drop_pct": 1.17, "early_entry_score": 0.722, "early_reclaim_pct": 72.9, "entry_ask": 14.95, "entry_bid": 14.55, "entry_mode": "early", "entry_option_price": 14.75, "hypothetical_budget": 61668.4, "hypothetical_contracts": 41, "matched_signals": 33, "option_liquidity_status": "ok", "option_open_interest": 1797.0, "option_spread_pct": 2.71, "option_volume": 135.0, "reason": "shadow_mode_no_order", "recovery_stability_score": 0.703, "shadow_only": true, "success_rate": 90.91, "ticker": "MSTR", "timing_score": 0.591, "top_candidates": [{"current_drop_pct": 1.17, "early_entry_score": 0.722, "early_reclaim_pct": 72.9, "matched_signals": 33, "recovery_stability_score": 0.703, "success_rate": 90.91, "ticker": "MSTR", "timing_score": 0.591, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": true}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261030062504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261030062504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261030062504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261030062504)

</details>
