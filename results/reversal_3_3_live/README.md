# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-28 13:58:25 EDT`
Last processed slot: `outage_recovery`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$14,997.50`
- Equity: `$14,997.50`
- Realized PnL: `$4,997.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-28)

```text
ticker asset_type execution_mode           instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price         pnl  return_pct                  exit_reason
 CMCSA     option         option CMCSA260618C00027500     52          2026-04-27         2026-04-28         1.26        1.62 1872.000025   28.571429 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et            slot     event_type                                                                                                                                                                                                                                                                           detail
2026-04-28T13:58:25.436100-04:00 outage_recovery recovery_audit {"action": "inserted_missed_take_profit_exit", "contract_symbol": "CMCSA260618C00027500", "option_price_at_scan": 1.62, "recovered_exit_timestamp_et": "2026-04-28T09:33:00-04:00", "scheduled_slot_timestamp_et": "2026-04-28T09:30:00-04:00", "stop": 1.1088, "target": 1.449}
2026-04-28T13:56:52.461724-04:00     manage_1400   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
       2026-04-28T09:33:00-04:00     manage_0930           exit           {"asset_type": "option", "contract_symbol": "CMCSA260618C00027500", "fill_price": 1.62, "pnl": 1872.0, "reason": "take_profit_day1_hit_at_scan", "recovered_after_power_outage": true, "return_pct": 28.57, "source": "yfinance_1m_option_history", "ticker": "CMCSA"}
2026-04-28T00:00:09.203683-04:00    data_refresh   data_refresh                                                                                                                                                                                                                                                                    {'saved': 99}
2026-04-27T16:10:05.210604-04:00     manage_1600   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T16:05:09.393931-04:00     manage_1600   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T16:00:09.657283-04:00     manage_1600   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:55:07.763445-04:00     manage_1600   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:40:07.694980-04:00     manage_1530   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T15:35:07.539962-04:00     manage_1530   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260428135828)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260428135828)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260428135828)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260428135828)

</details>
