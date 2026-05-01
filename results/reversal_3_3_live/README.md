# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 14:05:02 EDT`
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
  MDLZ           85.00               20            0.90              0.39         61.27                26.54            True
   KDP           81.25               16            1.53              0.31         29.27                34.77            True
  QCOM           88.00               25            1.19              1.50        178.94                62.29            True
   CSX           90.00               30            0.57              0.18         45.35                28.16            True
  NXPI           80.56               36            0.47              0.97        293.17                84.73           False
   TXN           84.21               38            0.37              0.74        280.76                67.79           False
  FAST           96.88               32            0.23              0.07         44.90                40.12           False
  ASML           87.80               41            0.06              0.63       1438.72                47.82           False
   ADI           76.19               21            1.62              4.56        400.31                38.22           False
  FANG          100.00               36            0.03              0.04        205.61                30.31           False
  ORLY          100.00                3            3.36              2.34         98.40                32.49           False
   XEL           90.00               30            0.45              0.26         82.84                27.62           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-01T14:05:02.593188-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T14:00:02.753183-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T13:55:05.465592-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-05-01T13:40:06.684351-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:35:01.746076-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:30:03.675917-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:25:02.795278-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-05-01T13:10:01.603461-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T13:05:01.594771-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-05-01T13:00:03.680159-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501140502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501140502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501140502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501140502)

</details>
