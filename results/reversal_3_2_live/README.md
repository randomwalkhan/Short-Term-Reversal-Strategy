# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 09:35:00 EDT`
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
  REGN          100.00               33            0.71              3.86        773.87                26.04            True
  FTNT           92.00               25            1.71              1.00         83.08                30.61            True
  NVDA           91.43               35            0.55              0.71        181.78                34.26            True
  VRTX           89.74               39            0.61              1.90        443.10                28.00            True
   MAR           89.47               38            0.52              1.26        348.04                32.53            True
  CTAS           88.57               35            0.52              0.64        174.32                30.38            True
  MDLZ           88.24               17            0.73              0.30         58.70                23.90            True
  INSM           87.80               41            0.76              0.86        159.81                52.00            True
  CDNS           87.10               31            1.55              3.15        288.15                28.11            True
  DXCM           86.67               30            1.60              0.73         65.48                33.81            True
  SNPS           86.11               36            1.29              3.70        408.58                37.77            True
  ABNB           85.71               21            1.72              1.58        130.72                41.34            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                     detail
2026-04-09T09:35:00.721623-04:00  manage_0930 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-09T09:30:04.707036-04:00  manage_0930         exit {"contract_symbol": "FTNT260508C00083000", "pnl": 1375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.58, "ticker": "FTNT"}
2026-04-09T09:30:04.707036-04:00 data_refresh data_refresh                                                                                                                              {'saved': 99}
2026-04-08T16:00:06.439697-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:55:05.442130-04:00  manage_1600 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:40:01.444116-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:35:04.435079-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:30:06.433144-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:25:06.431552-04:00  manage_1530 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-08T15:10:06.436687-04:00   entry_1500 slot_skipped                                                                                                            {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409093500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409093500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409093500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409093500)

</details>
