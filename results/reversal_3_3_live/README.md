# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 12:55:05 EDT`
Last processed slot: `manage_1300`

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
   KDP           82.35               17            1.21              0.25         29.11                32.43            True
   WMT           87.50               16            1.28              1.16        129.42                25.05            True
  SHOP           94.12               34            1.30              1.14        125.34                57.21            True
  AVGO           90.91               22            1.79              5.30        420.49                42.01            True
  ISRG           89.47               19            1.62              5.46        479.88                37.71            True
  GILD           90.91               11            1.66              1.51        129.75                21.39            True
  AAPL           80.00               15            1.67              3.17        269.70                26.22            True
   MAR           88.89               27            1.04              2.67        366.00                31.82            True
  CSCO           86.36               22            1.10              0.69         88.72                28.51            True
  TSLA           88.89               36            0.73              1.93        375.47                48.15            True
   TXN           66.67                6            3.11              6.04        274.58                67.06           False
  CHTR           72.73               11            2.93              3.69        178.55               113.10           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-27T12:55:05.851074-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T12:40:05.219126-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:35:01.575164-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:30:04.476148-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:25:01.385581-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:10:05.507549-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-27T12:05:02.504333-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-27T12:00:02.311606-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-27T11:55:01.521656-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-27T11:40:05.439098-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427125505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427125505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427125505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427125505)

</details>
