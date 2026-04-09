# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 12:20:04 EDT`
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
  REGN          100.00               22            1.43              7.75        772.21                26.04            True
   WDC           97.30               37            0.78              1.85        337.99                87.19            True
  ALNY           91.49               47            0.51              1.17        326.75                41.11            True
  VRTX           89.74               39            0.52              1.61        443.23                28.00            True
  ABNB           88.24               34            0.85              0.78        131.06                41.34            True
  SNPS           87.18               39            1.00              2.86        408.93                37.77            True
  TTWO           84.09               44            0.54              0.77        201.80                26.08            True
  DDOG           83.33               18            3.88              3.16        115.14                46.85            True
  BKNG           82.61               23            2.09              2.65        179.86                36.69            True
  SHOP           82.35               17            4.09              3.44        118.63                44.40            True
  CDNS           81.82               22            2.14              4.33        287.64                28.11            True
  CSCO           80.95               21            0.63              0.37         83.54                27.82            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T12:10:01.709238-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T12:05:05.701665-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T12:00:03.435227-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T11:55:00.699806-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T11:40:00.704425-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:35:00.921807-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:30:00.734024-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:25:04.969818-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-09T11:10:04.715349-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-09T11:05:00.814155-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409122004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409122004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409122004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409122004)

</details>
