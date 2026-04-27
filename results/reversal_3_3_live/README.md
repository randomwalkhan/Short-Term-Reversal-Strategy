# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 13:20:04 EDT`
Last processed slot: `manage_1330`

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
   KDP           82.35               17            1.25              0.26         29.11                32.43            True
   WDC           97.44               39            0.74              2.09        403.10                62.15            True
   WMT           88.24               17            1.24              1.12        129.44                25.05            True
  SHOP           93.55               31            1.37              1.20        125.31                57.21            True
  MSTR           82.93               41            0.63              0.75        170.70                71.85            True
  CSCO           81.25               16            1.35              0.84         88.65                28.51            True
  ISRG           89.47               19            1.65              5.57        479.83                37.71            True
  AVGO           90.91               22            1.87              5.52        420.39                42.01            True
   MAR           85.71               21            1.41              3.63        365.60                31.82            True
  GILD           91.67               12            1.55              1.41        129.80                21.39            True
  AAPL           81.25               16            1.59              3.02        269.77                26.22            True
  ASML           80.95               21            2.46             25.13       1446.93                51.44            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-27T13:10:08.731273-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T13:05:09.458541-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T13:00:08.796243-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T12:55:05.851074-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T12:40:05.219126-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:35:01.575164-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:30:04.476148-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:25:01.385581-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-27T12:10:05.507549-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-27T12:05:02.504333-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427132004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427132004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427132004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427132004)

</details>
