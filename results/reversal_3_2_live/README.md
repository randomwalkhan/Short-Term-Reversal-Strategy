# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 15:35:00 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$8,625.00`
- Equity: `$13,025.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   0          1      4400.0                  4400.0                44.0                  44.0      764.07         768.1             0.0                    0.0         100.0               21              1.48         48.92            46.7                  26.04
```

## Today's Closed Trades (2026-04-09)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  FTNT FTNT260508C00083000          2026-04-08         2026-04-09               5.375               6.75 1375.0   25.581395 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               31            0.96              5.20        773.30                26.04            True
  CDNS           90.00               10            3.44              6.97        286.51                28.11            True
  CTAS           88.57               35            0.51              0.62        174.32                30.38            True
  SNPS           86.21               29            1.69              4.87        408.07                37.77            True
  ABNB           85.71               21            1.65              1.52        130.75                41.34            True
  TTWO           84.00               25            1.80              2.54        201.04                26.08            True
  ALNY           83.33               18            2.42              5.54        324.88                41.11            True
  BKNG           80.95               21            2.41              3.05        179.69                36.69            True
    ZS          100.00                1           11.99             11.57        132.89                46.90           False
  SBUX           92.11               38            0.28              0.19         97.13                40.88           False
  DXCM           90.20               51            0.21              0.10         65.76                33.81           False
  INSM           90.00               50            0.01              0.01        160.18                52.00           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-09T15:35:00.892532-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:30:04.886669-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:25:00.951211-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:10:05.606498-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:05:00.876232-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:00:05.892957-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:55:00.989254-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:50:03.978140-04:00  entry_1500        entry {"allocated_cash": 4400.0, "contract_symbol": "REGN260515C00765000", "contracts": 1, "entry_option_price": 44.0, "matched_signals": 21, "success_rate": 100.0, "ticker": "REGN"}
2026-04-09T14:40:04.078140-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:35:00.960951-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409153500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409153500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409153500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409153500)

</details>
