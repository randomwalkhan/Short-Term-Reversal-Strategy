# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-28 14:15:07 EDT`
Last processed slot: `manual`

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

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               34            1.21              0.72         84.68                91.28            True
   TXN           83.33               30            1.19              2.24        268.54                67.99            True
  FAST           86.36               22            1.45              0.46         45.08                39.39            True
  PLTR           89.19               37            1.03              1.03        142.66                61.16            True
  UPRO           92.31               26            1.73              1.54        126.93                41.61            True
  SNPS           93.75               16            2.89             10.10        494.21                48.57            True
  SHOP           94.87               39            0.97              0.84        123.87                56.03            True
  ISRG           90.48               21            1.44              4.73        468.96                36.51            True
  TSLA           86.11               36            0.68              1.81        377.78                46.97            True
  CHTR           92.68               41            0.43              0.53        174.38               113.25           False
  META           76.67               30            1.04              4.93        676.51                37.38           False
  COST           90.00               20            0.99              6.90        995.05                19.60           False
```

## Recent Events

```text
                    timestamp_et            slot     event_type                                                                                                                                                                                                                                                                           detail
2026-04-28T14:10:08.581603-04:00     manage_1400   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-28T14:05:09.281623-04:00     manage_1400   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-28T14:00:07.167861-04:00     manage_1400   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-28T13:58:32.846901-04:00     manage_1400   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-28T13:58:25.436100-04:00 outage_recovery recovery_audit {"action": "inserted_missed_take_profit_exit", "contract_symbol": "CMCSA260618C00027500", "option_price_at_scan": 1.62, "recovered_exit_timestamp_et": "2026-04-28T09:33:00-04:00", "scheduled_slot_timestamp_et": "2026-04-28T09:30:00-04:00", "stop": 1.1088, "target": 1.449}
2026-04-28T13:56:52.461724-04:00     manage_1400   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
       2026-04-28T09:33:00-04:00     manage_0930           exit           {"asset_type": "option", "contract_symbol": "CMCSA260618C00027500", "fill_price": 1.62, "pnl": 1872.0, "reason": "take_profit_day1_hit_at_scan", "recovered_after_power_outage": true, "return_pct": 28.57, "source": "yfinance_1m_option_history", "ticker": "CMCSA"}
2026-04-28T00:00:09.203683-04:00    data_refresh   data_refresh                                                                                                                                                                                                                                                                    {'saved': 99}
2026-04-27T16:10:05.210604-04:00     manage_1600   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T16:05:09.393931-04:00     manage_1600   slot_skipped                                                                                                                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260428141507)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260428141507)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260428141507)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260428141507)

</details>
