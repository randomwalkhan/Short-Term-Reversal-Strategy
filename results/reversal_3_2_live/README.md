# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 15:45:05 EDT`
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

- Cash: `$8,625.00`
- Equity: `$13,025.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   0          1      4400.0                  4400.0                44.0                  44.0      764.07        767.58             0.0                    0.0         100.0               21              1.48         48.92           46.99                  26.04
```

## Today's Closed Trades (2026-04-09)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  FTNT FTNT260508C00083000          2026-04-08         2026-04-09               5.375               6.75 1375.0   25.581395 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               29            1.02              5.55        773.15                26.04            True
  CDNS           90.00               10            3.58              7.26        286.39                28.11            True
  SNPS           86.21               29            1.77              5.09        407.98                37.77            True
  TTWO           84.00               25            1.81              2.56        201.03                26.08            True
  ALNY           83.33               18            2.40              5.50        324.89                41.11            True
  ABNB           83.33               18            1.86              1.71        130.67                41.34            True
  FANG          100.00               32            0.05              0.06        186.44                32.28           False
    ZS          100.00                1           11.98             11.56        132.90                46.90           False
  SBUX           92.11               38            0.31              0.21         97.12                40.88           False
  DXCM           90.20               51            0.17              0.08         65.77                33.81           False
  CTAS           88.57               35            0.49              0.60        174.33                30.38           False
   WBD           86.05               43            0.15              0.03         27.54                12.15           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-09T15:40:01.001993-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:35:00.892532-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:30:04.886669-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:25:00.951211-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:10:05.606498-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:05:00.876232-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:00:05.892957-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:55:00.989254-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:50:03.978140-04:00  entry_1500        entry {"allocated_cash": 4400.0, "contract_symbol": "REGN260515C00765000", "contracts": 1, "entry_option_price": 44.0, "matched_signals": 21, "success_rate": 100.0, "ticker": "REGN"}
2026-04-09T14:40:04.078140-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409154505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409154505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409154505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409154505)

</details>
