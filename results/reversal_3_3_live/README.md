# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-07-09 03:15:02 EDT`
Last processed slot: `share_ext_0315`

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

- Cash: `$431.75`
- Equity: `$26,749.75`
- Realized PnL: `$15,746.75`
- Unrealized PnL: `$1,003.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PAYX     option         option PAYX260821C00110000       2026-07-08                   1     50     12625.0                 13250.0         2.53           2.65      106.22        106.61     last_price_stale                        NaN                unavailable                   False           625.0                   4.95         100.0               12              1.76         27.87            3.13                  32.70                 820.0          338.0               0.06                      ok
   CSX     option         option  CSX260821C00047500       2026-07-07                   2     54     12690.0                 13068.0         2.35           2.42       48.48         48.00     last_price_stale                        NaN                unavailable                   False           378.0                   2.98          91.3               23              0.68         28.35            0.00                  21.52                2967.0           20.0               0.09                      ok
```

## Today's Closed Trades (2026-07-09)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-07-09T00:00:06.857915-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-07-08T15:10:05.590905-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-08T15:05:01.586553-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-08T15:00:04.551542-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-08T14:55:01.624651-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-07-08T14:50:06.638018-04:00       entry_1500                   entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"allocated_cash": 12625.0, "asset_type": "option", "contract_symbol": "PAYX260821C00110000", "contracts": 50, "early_entry_score": 0.586, "entry_mode": "regular", "entry_option_price": 2.525, "execution_mode": "option", "matched_signals": 12, "option_liquidity_status": "ok", "option_open_interest": 820.0, "option_spread_pct": 5.94, "option_volume": 338.0, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.558}
2026-07-08T14:50:06.638018-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"early_entry_score": 0.565, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 4.0, "option_spread_pct": 27.1, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "UPRO", "timing_score": 0.578}
2026-07-08T14:50:06.638018-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"early_entry_score": 0.647, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 102.0, "option_spread_pct": 13.04, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MDLZ", "timing_score": 0.606}
2026-07-08T14:50:06.638018-04:00       entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-07-08", "training_samples": 5443, "window": 5}
2026-07-08T12:00:02.532330-04:00 early_entry_1200      early_entry_shadow {"contract_symbol": "TMUS260821C00185000", "current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "entry_ask": 9.7, "entry_bid": 9.2, "entry_mode": "early", "entry_option_price": 9.45, "hypothetical_budget": 6528.38, "hypothetical_contracts": 6, "matched_signals": 35, "option_liquidity_status": "low_volume", "option_open_interest": 378.0, "option_spread_pct": 5.29, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.622, "shadow_only": true, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "top_candidates": [{"current_drop_pct": 0.56, "early_entry_score": 0.689, "early_reclaim_pct": 82.5, "matched_signals": 35, "recovery_stability_score": 0.622, "success_rate": 88.57, "ticker": "TMUS", "timing_score": 0.458, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260709031502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260709031502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260709031502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260709031502)

</details>
