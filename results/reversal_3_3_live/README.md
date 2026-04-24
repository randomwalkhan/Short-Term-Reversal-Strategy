# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 13:35:02 EDT`
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

- Cash: `$14,045.50`
- Equity: `$14,045.50`
- Realized PnL: `$4,045.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-24)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  NVDA     option         option NVDA260618C00200000      5          2026-04-23         2026-04-24       12.325      14.475 1075.0   17.444219 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   TXN           80.00               25            1.48              2.92        280.98                66.99            True
   WMT           85.71               14            1.51              1.39        131.43                24.33            True
  FANG          100.00               23            0.84              1.15        195.10                34.00            True
  FAST           90.62               32            0.75              0.24         45.35                38.70            True
   CSX           86.36               22            1.00              0.32         46.04                27.21            True
  MRVL           96.43               28            1.63              1.89        164.75                67.12            True
  MSTR           80.95               42            0.91              1.10        172.00                74.46            True
  AAPL           81.82               22            1.24              2.37        272.42                25.85            True
  AXON           76.60               47            0.22              0.61        392.38                71.24           False
  CRWD           82.61               46            0.10              0.31        445.26                59.30           False
  NFLX           95.35               43            0.32              0.21         92.73                46.09           False
    ZS           79.59               49            0.23              0.21        132.88                69.17           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-24T13:35:02.128059-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:30:05.089136-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:25:04.273045-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:10:02.065273-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-24T13:05:02.199855-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-24T13:00:05.080480-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-24T12:55:05.083691-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-24T12:40:01.259451-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-24T12:35:05.195115-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-24T12:30:02.069429-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424133502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424133502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424133502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424133502)

</details>
