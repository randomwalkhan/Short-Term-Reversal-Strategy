# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 11:25:06 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$13,125.50`
- Equity: `$13,125.50`
- Realized PnL: `$3,125.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-27)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct           exit_reason
   TXN     option         option TXN260618C00280000      4          2026-04-24         2026-04-27       14.475      12.175 -920.0  -15.889465 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           84.62               13            2.27              4.41        275.28                67.06            True
   KDP           81.25               16            1.33              0.27         29.10                32.43            True
  TEAM           81.25               48            0.50              0.25         71.44                79.96            True
  UPRO           92.31               39            0.64              0.57        126.75                48.54            True
  AVGO           90.91               22            1.81              5.37        420.46                42.01            True
  GILD           91.67               12            1.50              1.37        129.81                21.39            True
   MAR           86.36               22            1.29              3.32        365.73                31.82            True
   WMT           86.96               23            1.01              0.92        129.53                25.05            True
  SHOP           94.74               38            1.03              0.91        125.44                57.21            True
   HON          100.00               19            1.15              1.72        212.42                25.73            True
  AAPL           82.35               17            1.50              2.85        269.84                26.22            True
  CSCO           86.36               22            1.12              0.70         88.71                28.51            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-27T11:25:06.457136-04:00 manage_1130 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T11:10:05.347046-04:00 manage_1100 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T11:05:01.487592-04:00 manage_1100 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T11:00:03.379794-04:00 manage_1100 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:55:02.486802-04:00 manage_1100 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:40:05.458641-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:35:01.494241-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:30:01.499388-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:25:04.454229-04:00 manage_1030 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-27T10:20:02.444364-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "TXN260618C00280000", "fill_price": 12.175, "pnl": -920.0, "reason": "stop_loss_hit_at_scan", "return_pct": -15.89, "ticker": "TXN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427112506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427112506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427112506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427112506)

</details>
