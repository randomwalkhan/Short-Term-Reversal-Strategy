# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-08 00:15:01 EDT`
Last processed slot: `share_ext_0015`

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

- Cash: `$16,479.50`
- Equity: `$33,305.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$611.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  PYPL     option         option PYPL260918C00060000       2026-08-07                   0     94     16215.0                 16826.0         1.72           1.79       58.88          59.1          bid_ask_mid                       1.79                bid_ask_mid                    True           611.0                   3.77         94.12               17              1.51         27.86           28.49                  59.52                8843.0          464.0               0.03                      ok
```

## Today's Closed Trades (2026-08-08)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et           slot     event_type                                                                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-08-08T00:15:01.810389-04:00 share_ext_0015  market_closed                                                                                                                                                                                                                                                                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-08T00:10:01.669582-04:00 share_ext_0010  market_closed                                                                                                                                                                                                                                                                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-08T00:05:04.691660-04:00 share_ext_0005  market_closed                                                                                                                                                                                                                                                                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-08T00:00:02.608128-04:00 share_ext_0000  market_closed                                                                                                                                                                                                                                                                                                                                                                                            {"holiday_name": null, "reason": "weekend"}
2026-08-07T15:10:06.531054-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-07T15:05:04.549865-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-07T15:00:06.559995-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-07T14:55:06.579498-04:00     entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-08-07T14:50:05.673484-04:00     entry_1500          entry {"allocated_cash": 16215.0, "asset_type": "option", "contract_symbol": "PYPL260918C00060000", "contracts": 94, "early_entry_score": 0.505, "entry_mode": "regular", "entry_option_price": 1.725, "execution_mode": "option", "matched_signals": 17, "option_liquidity_status": "ok", "option_open_interest": 8843.0, "option_spread_pct": 2.9, "option_volume": 464.0, "success_rate": 94.12, "ticker": "PYPL", "timing_score": 0.693}
2026-08-07T14:50:05.673484-04:00     entry_1500 timing_overlay                                                                                                                                                                                                                                                                                                                           {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-08-07", "training_samples": 5596, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260808001501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260808001501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260808001501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260808001501)

</details>
