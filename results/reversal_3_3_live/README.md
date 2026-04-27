# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-27 13:55:01 EDT`
Last processed slot: `manage_1400`

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
   KDP           83.33               12            1.73              0.35         29.07                32.43            True
   WMT           86.67               15            1.49              1.35        129.34                25.05            True
  SHOP           93.55               31            1.56              1.38        125.24                57.21            True
   MAR           83.33               12            2.08              5.34        364.86                31.82            True
  AVGO           92.31               26            1.43              4.23        420.95                42.01            True
  CSCO           81.25               16            1.34              0.83         88.65                28.51            True
  ISRG           88.24               17            1.87              6.32        479.51                37.71            True
  AAPL           80.00               15            1.72              3.27        269.66                26.22            True
  ASML           80.95               21            2.48             25.26       1446.88                51.44            True
   TXN           71.43                7            2.99              5.81        274.68                67.06           False
 CMCSA           93.33               30            0.24              0.05         27.50                60.91           False
  CHTR           62.50                8            3.19              4.03        178.40               113.10           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-27T13:55:01.507336-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-27T13:40:01.413909-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:35:05.278374-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:30:03.802245-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:25:05.720735-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-27T13:10:08.731273-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T13:05:09.458541-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T13:00:08.796243-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T12:55:05.851074-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-27T12:40:05.219126-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260427135501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260427135501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260427135501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260427135501)

</details>
