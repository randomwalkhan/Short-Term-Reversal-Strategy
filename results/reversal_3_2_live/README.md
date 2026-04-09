# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 09:30:04 EDT`
Last processed slot: `manage_0930`

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
  REGN          100.00               29            1.15              6.26        772.85                26.04            True
   HON          100.00               14            1.11              1.81        231.69                24.73            True
  SBUX           93.75               32            0.70              0.48         97.01                40.88            True
  ALNY           91.30               46            0.62              1.42        326.64                41.11            True
  CDNS           90.70               43            0.75              1.52        288.85                28.11            True
  VRTX           89.19               37            0.73              2.27        442.95                28.00            True
  DXCM           88.64               44            0.76              0.35         65.65                33.81            True
   MAR           88.57               35            0.67              1.62        347.88                32.53            True
  INSM           87.80               41            0.73              0.82        159.83                52.00            True
  ABNB           87.80               41            0.59              0.55        131.17                41.34            True
  GILD           86.96               23            0.89              0.89        141.16                20.46            True
  MDLZ           86.67               15            0.88              0.36         58.67                23.90            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                     detail
2026-04-09T09:30:04.707036-04:00  manage_0930         exit {"contract_symbol": "FTNT260508C00083000", "pnl": 1375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.58, "ticker": "FTNT"}
2026-04-09T09:30:04.707036-04:00 data_refresh data_refresh                                                                                                                              {'saved': 99}
2026-04-08T16:00:06.439697-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:55:05.442130-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:40:01.444116-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:35:04.435079-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:30:06.433144-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:25:06.431552-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:10:06.436687-04:00   entry_1500 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:05:05.449071-04:00   entry_1500 slot_skipped                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409093004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409093004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409093004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409093004)

</details>
