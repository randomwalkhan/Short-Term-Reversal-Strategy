# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-24 11:30:06 EDT`
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
   TXN           83.33               18            2.03              4.01        280.51                66.99            True
  NFLX           93.75               32            0.85              0.55         92.58                46.09            True
   WMT           87.50               16            1.37              1.27        131.49                24.33            True
  PLTR           89.74               39            0.64              0.63        141.30                64.15            True
  DDOG           86.84               38            0.87              0.78        127.53                60.38            True
  FANG          100.00               22            1.18              1.62        194.90                34.00            True
  FAST           91.89               37            0.64              0.20         45.36                38.70            True
  SHOP           94.29               35            1.11              0.97        123.81                58.07            True
  AXON           72.97               37            1.08              2.96        391.37                71.24           False
  CRWD           79.49               39            0.86              2.68        444.24                59.30           False
    ZS           76.19               42            0.77              0.72        132.66                69.17           False
   ADI           83.33               36            0.47              1.32        403.32                40.58           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-24T11:30:06.059480-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-24T11:25:04.247823-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-24T11:10:06.045106-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-24T11:05:04.237988-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-24T11:00:06.205625-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-24T10:55:02.045514-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-24T10:40:05.045051-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-24T10:35:02.034739-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-24T10:30:05.226988-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-24T10:25:05.335841-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260424113006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260424113006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260424113006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260424113006)

</details>
