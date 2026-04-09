# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 09:45:03 EDT`
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
  REGN          100.00               22            1.36              7.39        772.36                26.04            True
   HON          100.00               19            0.88              1.42        231.86                24.73            True
  FTNT           92.31               39            0.93              0.54         83.28                30.61            True
  CDNS           90.48               42            0.91              1.85        288.71                28.11            True
  ABNB           90.32               31            1.27              1.17        130.90                41.34            True
  VRTX           88.46               26            1.33              4.13        442.15                28.00            True
  CTAS           87.88               33            0.60              0.74        174.27                30.38            True
  SNPS           87.50               40            0.70              2.00        409.30                37.77            True
  DXCM           86.84               38            1.17              0.54         65.57                33.81            True
  MCHP           86.49               37            0.66              0.33         70.59                45.14            True
  BKNG           86.11               36            1.02              1.29        180.45                36.69            True
  SHOP           85.71               42            0.80              0.67        119.81                44.40            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                     detail
2026-04-09T09:40:00.730980-04:00  manage_0930 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T09:35:00.721623-04:00  manage_0930 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T09:30:04.707036-04:00  manage_0930         exit {"contract_symbol": "FTNT260508C00083000", "pnl": 1375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.58, "ticker": "FTNT"}
2026-04-09T09:30:04.707036-04:00 data_refresh data_refresh                                                                                                                              {'saved': 99}
2026-04-08T16:00:06.439697-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:55:05.442130-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:40:01.444116-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:35:04.435079-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:30:06.433144-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:25:06.431552-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409094503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409094503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409094503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409094503)

</details>
