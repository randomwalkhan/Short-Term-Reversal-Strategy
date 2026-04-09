# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 15:55:05 EDT`
Last processed slot: `manage_1600`

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
  REGN REGN260515C00765000       2026-04-09                   0          1      4400.0                  4400.0                44.0                  44.0      764.07         767.2             0.0                    0.0         100.0               21              1.48         48.92            47.2                  26.04
```

## Today's Closed Trades (2026-04-09)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  FTNT FTNT260508C00083000          2026-04-08         2026-04-09               5.375               6.75 1375.0   25.581395 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               29            1.06              5.77        773.06                26.04            True
   WDC           97.37               38            0.53              1.26        338.24                87.19            True
  CDNS           90.91               11            3.31              6.71        286.63                28.11            True
  ALNY           87.50               24            1.99              4.56        325.30                41.11            True
  ABNB           85.71               21            1.69              1.55        130.73                41.34            True
  SNPS           85.29               34            1.40              4.03        408.43                37.77            True
   TRI           84.21               38            1.38              0.83         85.75                31.47            True
   CEG           80.95               42            0.68              1.35        283.69                56.91            True
  CSCO           80.95               21            0.59              0.34         83.55                27.82            True
  TTWO           80.00               20            1.93              2.74        200.96                26.08            True
   ROP           80.00               20            1.64              4.10        354.10                17.33            True
    ZS          100.00                1           11.41             11.01        133.13                46.90           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-09T15:55:05.644912-04:00 manage_1600 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:40:01.001993-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:35:00.892532-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:30:04.886669-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:25:00.951211-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:10:05.606498-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:05:00.876232-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T15:00:05.892957-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:55:00.989254-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:50:03.978140-04:00  entry_1500        entry {"allocated_cash": 4400.0, "contract_symbol": "REGN260515C00765000", "contracts": 1, "entry_option_price": 44.0, "matched_signals": 21, "success_rate": 100.0, "ticker": "REGN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409155505)

</details>
