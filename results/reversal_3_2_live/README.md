# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 11:40:00 EDT`
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
  REGN          100.00               22            1.46              7.94        772.13                26.04            True
   WDC           97.06               34            1.26              2.99        337.50                87.19            True
  SBUX           93.75               32            0.78              0.53         96.98                40.88            True
  ALNY           89.47               38            1.24              2.85        326.03                41.11            True
  VRTX           88.89               36            0.82              2.54        442.83                28.00            True
  INSM           88.64               44            0.61              0.68        159.89                52.00            True
  DXCM           87.80               41            0.97              0.45         65.61                33.81            True
  CTAS           87.50               32            0.68              0.83        174.23                30.38            True
  SNPS           85.71               28            1.91              5.50        407.80                37.77            True
  DDOG           85.71               14            4.39              3.58        114.97                46.85            True
  CDNS           84.62               13            2.76              5.59        287.11                28.11            True
  TTWO           83.78               37            1.08              1.53        201.48                26.08            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T11:40:00.704425-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:35:00.921807-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:30:00.734024-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:25:04.969818-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:10:04.715349-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T11:05:00.814155-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T11:00:01.740551-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T10:55:00.703480-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T10:40:03.920046-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:35:05.721256-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409114000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409114000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409114000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409114000)

</details>
