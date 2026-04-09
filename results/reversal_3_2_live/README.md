# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 12:25:01 EDT`
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
  REGN          100.00               22            1.46              7.93        772.13                26.04            True
   WDC           97.37               38            0.53              1.25        338.24                87.19            True
  SBUX           94.12               34            0.60              0.41         97.04                40.88            True
  ALNY           90.91               44            0.80              1.83        326.46                41.11            True
  VRTX           89.47               38            0.66              2.05        443.04                28.00            True
  ABNB           88.24               34            1.07              0.98        130.98                41.34            True
  SNPS           87.18               39            1.09              3.13        408.82                37.77            True
  DDOG           84.62               13            4.75              3.87        114.84                46.85            True
  TTWO           83.72               43            0.62              0.87        201.76                26.08            True
  SHOP           82.35               17            4.28              3.60        118.56                44.40            True
   ROP           81.48               27            1.21              3.01        354.56                17.33            True
  BKNG           80.95               21            2.34              2.97        179.73                36.69            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T12:25:01.881441-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-09T12:10:01.709238-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T12:05:05.701665-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T12:00:03.435227-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T11:55:00.699806-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T11:40:00.704425-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:35:00.921807-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:30:00.734024-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:25:04.969818-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:10:04.715349-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409122501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409122501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409122501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409122501)

</details>
