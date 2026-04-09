# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 10:15:05 EDT`
Last processed slot: `manual`

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
  REGN          100.00               19            1.62              8.77        771.77                26.04            True
   WDC           97.06               34            1.63              3.87        337.12                87.19            True
  UPRO           92.11               38            0.68              0.52        108.24                60.47            True
  ALNY           89.74               39            1.08              2.48        326.19                41.11            True
  VRTX           89.66               29            1.19              3.70        442.33                28.00            True
  FTNT           88.89               18            2.17              1.27         82.97                30.61            True
  DDOG           88.46               26            2.23              1.82        115.72                46.85            True
  DXCM           87.80               41            0.92              0.43         65.62                33.81            True
  CTAS           87.10               31            0.76              0.93        174.19                30.38            True
  INSM           86.84               38            1.07              1.20        159.67                52.00            True
  SNPS           85.71               21            2.43              6.97        407.17                37.77            True
  TTWO           82.86               35            1.22              1.72        201.39                26.08            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                     detail
2026-04-09T10:10:03.861770-04:00  manage_1000 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T10:05:05.524975-04:00  manage_1000 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T10:00:02.890491-04:00  manage_1000 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T09:55:03.701126-04:00  manage_1000 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T09:40:00.730980-04:00  manage_0930 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T09:35:00.721623-04:00  manage_0930 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T09:30:04.707036-04:00  manage_0930         exit {"contract_symbol": "FTNT260508C00083000", "pnl": 1375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.58, "ticker": "FTNT"}
2026-04-09T09:30:04.707036-04:00 data_refresh data_refresh                                                                                                                              {'saved': 99}
2026-04-08T16:00:06.439697-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:55:05.442130-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409101505)

</details>
