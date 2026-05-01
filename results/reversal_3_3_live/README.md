# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 14:00:02 EDT`
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
  MDLZ           85.00               20            0.83              0.36         61.29                26.54            True
   KDP           81.25               16            1.51              0.31         29.27                34.77            True
  QCOM           90.00               30            0.86              1.09        179.11                62.29            True
   CSX           89.66               29            0.59              0.19         45.35                28.16            True
  NXPI           80.56               36            0.47              0.96        293.18                84.73           False
   TXN           84.21               38            0.36              0.70        280.78                67.79           False
  FAST           96.97               33            0.19              0.06         44.90                40.12           False
  ASML           87.80               41            0.07              0.72       1438.68                47.82           False
  FANG          100.00               35            0.11              0.16        205.56                30.31           False
   ADI           77.27               22            1.55              4.36        400.39                38.22           False
  ORLY          100.00                3            3.45              2.40         98.37                32.49           False
  PCAR           81.25               16            1.70              1.41        118.19                33.58           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-01T14:00:02.753183-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T13:55:05.465592-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T13:40:06.684351-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:35:01.746076-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:30:03.675917-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:25:02.795278-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:10:01.603461-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T13:05:01.594771-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T13:00:03.680159-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T12:55:01.554647-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501140002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501140002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501140002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501140002)

</details>
