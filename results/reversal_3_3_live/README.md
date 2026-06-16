# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-16 18:30:06 EDT`
Last processed slot: `share_ext_1830`

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

- Cash: `$13,363.25`
- Equity: `$24,583.25`
- Realized PnL: `$15,985.75`
- Unrealized PnL: `$-1,402.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  DRAM     option         option DRAM260717C00069000       2026-06-16                   0     17     12622.5                 11220.0         7.43            6.6       68.52         68.69          bid_ask_mid                        6.6                bid_ask_mid                    True         -1402.5                 -11.11         90.91               11              3.59         94.78           87.06                 109.99                 846.0          111.0               0.06                      ok
```

## Today's Closed Trades (2026-06-16)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  ROST     option         option ROST260717C00240000     23          2026-06-15         2026-06-16         5.75       5.175 -1322.5       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-06-16T15:10:02.062608-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T15:05:05.056304-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T15:00:03.019624-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T14:55:06.031514-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-06-16T14:50:02.059942-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"allocated_cash": 12622.5, "asset_type": "option", "contract_symbol": "DRAM260717C00069000", "contracts": 17, "early_entry_score": 0.434, "entry_mode": "regular", "entry_option_price": 7.425, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 846.0, "option_spread_pct": 6.06, "option_volume": 111.0, "success_rate": 90.91, "ticker": "DRAM", "timing_score": 0.657}
2026-06-16T14:50:02.059942-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-16", "training_samples": 5231, "window": 5}
2026-06-16T11:52:05.052043-04:00 early_entry_1150 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T11:10:06.057140-04:00 early_entry_1110 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-16T10:36:17.030970-04:00 early_entry_1035 early_entry_shadow {"contract_symbol": "MAR260717C00400000", "current_drop_pct": 0.57, "early_entry_score": 0.842, "early_reclaim_pct": 82.6, "entry_ask": 13.9, "entry_bid": 11.5, "entry_mode": "early", "entry_option_price": 12.7, "hypothetical_budget": 12992.88, "hypothetical_contracts": 10, "matched_signals": 32, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 400.0, "option_spread_pct": 18.9, "option_volume": 13.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.854, "shadow_only": true, "success_rate": 96.88, "ticker": "MAR", "timing_score": 0.469, "top_candidates": [{"current_drop_pct": 0.57, "early_entry_score": 0.842, "early_reclaim_pct": 82.6, "matched_signals": 32, "recovery_stability_score": 0.854, "success_rate": 96.88, "ticker": "MAR", "timing_score": 0.469, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-06-16T10:36:17.030970-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "ROST260717C00240000", "fill_price": 5.175, "pnl": -1322.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "ROST"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260616183006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260616183006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260616183006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260616183006)

</details>
