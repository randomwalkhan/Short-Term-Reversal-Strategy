# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 11:20:01 EDT`
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
  FAST           96.30               27            0.50              0.16         44.86                40.12            True
   KDP           85.00               20            0.99              0.20         29.31                34.77            True
  FANG          100.00               21            1.36              1.95        204.79                30.31            True
   ADP           83.87               31            0.67              0.99        211.52                37.35            True
  NXPI           75.00               28            1.11              2.28        292.61                84.73           False
   TXN           84.21               38            0.26              0.52        280.86                67.79           False
  ORLY          100.00                8            2.13              1.48         98.76                32.49           False
  AXON           84.78               46            0.12              0.33        401.62                68.71           False
  ASML           86.84               38            0.28              2.79       1437.79                47.82           False
   ADI           79.17               24            1.29              3.64        400.70                38.22           False
   CSX           90.91               33            0.48              0.15         45.36                28.16           False
  PCAR           80.95               21            1.29              1.07        118.34                33.58           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-05-01T11:10:03.556649-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:05:01.560500-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:00:06.443199-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:55:05.545656-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:50:03.535626-04:00 manage_1100         exit {"asset_type": "option", "contract_symbol": "INTC260618C00095000", "fill_price": 13.3, "pnl": 2100.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 29.13, "ticker": "INTC"}
2026-05-01T10:40:01.653941-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:35:06.610528-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:30:01.556728-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:25:01.530323-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:10:01.610571-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501112001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501112001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501112001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501112001)

</details>
