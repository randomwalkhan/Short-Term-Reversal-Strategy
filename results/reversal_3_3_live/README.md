# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 13:15:03 EDT`
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

- Cash: `$17,667.50`
- Equity: `$17,667.50`
- Realized PnL: `$7,667.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00095000      7          2026-04-30         2026-05-01         10.3        13.3 2100.0   29.126214 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NXPI           80.00               35            0.62              1.27        293.04                84.73            True
   KDP           80.00               15            1.58              0.33         29.26                34.77            True
  MDLZ           83.33               24            0.62              0.27         61.33                26.54            True
  QCOM           90.00               30            0.82              1.04        179.14                62.29            True
   CSX           90.00               30            0.57              0.18         45.35                28.16            True
   TXN           83.33               36            0.45              0.88        280.70                67.79           False
  FAST           96.55               29            0.38              0.12         44.88                40.12           False
  ORLY          100.00                3            2.69              1.87         98.60                32.49           False
  FANG          100.00               31            0.29              0.42        205.45                30.31           False
  ASML           87.80               41            0.05              0.54       1438.76                47.82           False
   ADI           79.17               24            1.29              3.64        400.70                38.22           False
  PCAR           82.35               17            1.60              1.33        118.23                33.58           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-01T13:10:01.603461-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T13:05:01.594771-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T13:00:03.680159-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T12:55:01.554647-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T12:40:03.610739-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-01T12:35:01.589809-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-01T12:30:05.627366-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-01T12:25:01.554662-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-05-01T12:10:05.598108-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-01T12:05:01.632568-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501131503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501131503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501131503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501131503)

</details>
