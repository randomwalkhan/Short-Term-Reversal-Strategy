# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 12:20:05 EDT`
Last processed slot: `manage_1230`

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
  NXPI           80.00               35            0.65              1.33        293.02                84.73            True
  FAST           96.00               25            0.62              0.20         44.85                40.12            True
   KDP           83.33               18            1.11              0.23         29.30                34.77            True
  FANG          100.00               22            1.01              1.46        205.01                30.31            True
  QCOM           80.00               15            2.02              2.54        178.49                62.29            True
   CSX           88.46               26            0.73              0.23         45.33                28.16            True
   TXN           84.21               38            0.30              0.59        280.83                67.79           False
  ORLY          100.00                7            2.34              1.63         98.70                32.49           False
  ASML           86.11               36            0.36              3.68       1437.41                47.82           False
   ADI           79.17               24            1.42              4.00        400.54                38.22           False
  PCAR           80.00               20            1.31              1.09        118.33                33.58           False
  KLAC           88.89               27            1.34             16.46       1743.30                47.77           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-05-01T12:10:05.598108-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-01T12:05:01.632568-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-01T12:00:03.636755-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-01T11:55:01.583301-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-05-01T11:40:02.683709-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-01T11:35:01.560576-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-01T11:30:05.932738-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-01T11:25:05.698337-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-05-01T11:10:03.556649-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-05-01T11:05:01.560500-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501122005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501122005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501122005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501122005)

</details>
