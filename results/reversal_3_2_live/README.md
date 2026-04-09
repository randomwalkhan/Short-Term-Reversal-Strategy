# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 11:35:00 EDT`
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
  REGN          100.00               22            1.35              7.31        772.40                26.04            True
   WDC           97.14               35            1.12              2.66        337.64                87.19            True
  SBUX           93.75               32            0.71              0.49         97.00                40.88            True
  VRTX           89.19               37            0.76              2.36        442.91                28.00            True
  ALNY           88.89               36            1.40              3.21        325.87                41.11            True
  DXCM           87.80               41            0.91              0.42         65.62                33.81            True
  CTAS           86.21               29            0.90              1.11        174.12                30.38            True
  SNPS           85.71               28            1.81              5.20        407.93                37.77            True
  TTWO           84.62               39            0.84              1.18        201.62                26.08            True
  CDNS           84.62               13            2.74              5.56        287.12                28.11            True
  SHOP           82.35               17            4.17              3.51        118.60                44.40            True
  DDOG           82.35               17            4.00              3.26        115.10                46.85            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T11:35:00.921807-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:30:00.734024-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:25:04.969818-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:10:04.715349-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T11:05:00.814155-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T11:00:01.740551-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T10:55:00.703480-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T10:40:03.920046-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:35:05.721256-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:30:03.705847-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409113500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409113500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409113500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409113500)

</details>
