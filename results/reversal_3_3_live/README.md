# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 14:05:04 EDT`
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
   WMT           86.67               15            1.46              1.35        131.45                24.33            True
  FAST           88.89               27            1.11              0.35         45.30                38.70            True
  FANG          100.00               25            0.77              1.06        195.14                34.00            True
   CSX           86.96               23            0.92              0.30         46.05                27.21            True
  MRVL           96.43               28            1.62              1.88        164.75                67.12            True
  AAPL           85.71               21            1.27              2.44        272.39                25.85            True
  MDLZ           83.33               24            0.59              0.24         57.61                22.00            True
  MSTR           80.95               42            0.89              1.07        172.01                74.46            True
   TXN           79.17               24            1.61              3.18        280.87                66.99           False
  AXON           76.60               47            0.07              0.19        392.56                71.24           False
  NFLX           95.00               40            0.48              0.31         92.69                46.09           False
   KHC           75.86               29            0.25              0.04         21.95                25.99           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-24T14:05:04.100469-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-24T14:00:02.276536-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-24T13:55:05.319263-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-24T13:40:02.186193-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:35:02.128059-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:30:05.089136-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:25:04.273045-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-24T13:10:02.065273-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-24T13:05:02.199855-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-24T13:00:05.080480-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424140504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424140504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424140504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424140504)

</details>
