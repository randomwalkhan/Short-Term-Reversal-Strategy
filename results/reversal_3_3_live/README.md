# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-05-01 11:40:02 EDT`
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
  NXPI           80.56               36            0.55              1.12        293.11                84.73            True
  FAST           95.65               23            0.91              0.29         44.81                40.12            True
   KDP           85.00               20            1.09              0.22         29.30                34.77            True
  FANG          100.00               22            1.21              1.74        204.88                30.31            True
   ADI           80.77               26            1.00              2.81        401.06                38.22            True
   ADP           84.85               33            0.50              0.75        211.62                37.35            True
   TXN           83.78               37            0.38              0.75        280.76                67.79           False
  ORLY          100.00                8            2.17              1.51         98.75                32.49           False
  ASML           87.18               39            0.20              2.03       1438.12                47.82           False
   CSX           90.91               33            0.48              0.15         45.36                28.16           False
  QCOM           50.00                2            3.45              4.33        177.72                62.29           False
  PCAR           82.61               23            1.23              1.02        118.36                33.58           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                 detail
2026-05-01T11:40:02.683709-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:35:01.560576-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:30:05.932738-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:25:05.698337-04:00 manage_1130 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:10:03.556649-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:05:01.560500-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T11:00:06.443199-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:55:05.545656-04:00 manage_1100 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
2026-05-01T10:50:03.535626-04:00 manage_1100         exit {"asset_type": "option", "contract_symbol": "INTC260618C00095000", "fill_price": 13.3, "pnl": 2100.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 29.13, "ticker": "INTC"}
2026-05-01T10:40:01.653941-04:00 manage_1030 slot_skipped                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260501114002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260501114002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260501114002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260501114002)

</details>
