# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 12:00:02 EDT`
Last processed slot: `manage_1200`

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
   TXN           81.82               11            2.44              4.72        275.15                67.06            True
  CHTR           90.91               33            1.24              1.56        179.46               113.10            True
   KDP           81.25               16            1.32              0.27         29.10                32.43            True
   WMT           90.48               21            1.11              1.01        129.49                25.05            True
  SHOP           94.44               36            1.09              0.96        125.42                57.21            True
  AVGO           92.00               25            1.49              4.41        420.87                42.01            True
   HON          100.00               19            1.16              1.73        212.42                25.73            True
  AAPL           81.25               16            1.56              2.96        269.79                26.22            True
  CSCO           86.36               22            1.07              0.67         88.72                28.51            True
   MAR           88.89               27            1.04              2.67        366.01                31.82            True
  ISRG           86.96               23            1.40              4.71        480.20                37.71            True
  ASML           80.95               21            2.46             25.14       1446.93                51.44            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-27T12:00:02.311606-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-27T11:55:01.521656-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-27T11:40:05.439098-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-27T11:35:01.540977-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-27T11:30:04.474363-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-27T11:25:06.457136-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-27T11:10:05.347046-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-27T11:05:01.487592-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-27T11:00:03.379794-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-27T10:55:02.486802-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427120002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427120002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427120002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427120002)

</details>
