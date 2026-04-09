# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 11:05:00 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`
- Live exit ladder: `+15% / +15% / -12%`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$13,025.00`
- Equity: `$13,025.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-09)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  FTNT FTNT260508C00083000          2026-04-08         2026-04-09               5.375               6.75 1375.0   25.581395 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               21            1.50              8.16        772.03                26.04            True
   WDC           96.67               30            2.36              5.59        336.38                87.19            True
  SBUX           94.12               34            0.62              0.42         97.03                40.88            True
   MAR           89.66               29            0.92              2.23        347.62                32.53            True
  ALNY           88.89               27            1.90              4.35        325.38                41.11            True
  DXCM           88.57               35            1.38              0.64         65.53                33.81            True
  VRTX           88.57               35            0.86              2.68        442.77                28.00            True
  DDOG           85.71               14            4.44              3.62        114.95                46.85            True
  CTAS           85.19               27            1.04              1.27        174.04                30.38            True
  MCHP           84.85               33            0.99              0.49         70.52                45.14            True
  MELI           84.62               39            0.93             11.56       1770.79                40.32            True
  TTWO           84.00               25            1.73              2.44        201.08                26.08            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T11:05:00.814155-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T11:00:01.740551-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T10:55:00.703480-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T10:40:03.920046-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:35:05.721256-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:30:03.705847-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:25:03.711004-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:10:03.861770-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-09T10:05:05.524975-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-09T10:00:02.890491-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409110500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409110500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409110500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409110500)

</details>
