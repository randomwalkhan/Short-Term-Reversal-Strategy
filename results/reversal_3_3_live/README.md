# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 11:00:06 EDT`
Last processed slot: `manage_1100`

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
  SOXL           83.87               31            0.80              0.71        126.68                94.60            True
  FAST           96.30               27            0.51              0.16         44.86                40.12            True
   KDP           88.89               27            0.61              0.13         29.35                34.77            True
  ORLY           86.67               15            1.69              1.18         98.90                32.49            True
  ASML           84.85               33            0.56              5.59       1436.59                47.82            True
   ADP           84.00               25            0.92              1.36        211.36                37.35            True
  FANG          100.00               22            1.25              1.80        204.86                30.31            True
  NXPI           69.57               23            1.46              3.01        292.30                84.73           False
   TXN           83.33               36            0.44              0.86        280.71                67.79           False
   ADI           79.17               24            1.40              3.95        400.57                38.22           False
   CSX           91.18               34            0.46              0.15         45.37                28.16           False
  QCOM           50.00                2            3.71              4.67        177.58                62.29           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-05-01T11:00:06.443199-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:55:05.545656-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:50:03.535626-04:00 manage_1100         exit {"asset_type": "option", "contract_symbol": "INTC260618C00095000", "fill_price": 13.3, "pnl": 2100.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 29.13, "ticker": "INTC"}
2026-05-01T10:40:01.653941-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:35:06.610528-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:30:01.556728-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:25:01.530323-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:10:01.610571-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:05:01.725672-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:00:02.530062-04:00 manage_1000 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501110006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501110006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501110006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501110006)

</details>
