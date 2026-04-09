# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 14:55:00 EDT`
Last processed slot: `entry_1500`

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
  REGN REGN260515C00765000       2026-04-09                   0          1      4400.0                  4400.0                44.0                  44.0      764.07        765.26             0.0                    0.0         100.0               21              1.48         48.92           48.27                  26.04
```

## Today's Closed Trades (2026-04-09)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  FTNT FTNT260508C00083000          2026-04-08         2026-04-09               5.375               6.75 1375.0   25.581395 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               22            1.32              7.19        772.45                26.04            True
   WDC           97.22               36            0.87              2.06        337.90                87.19            True
  CDNS           90.00               10            3.47              7.03        286.49                28.11            True
  DXCM           88.64               44            0.61              0.28         65.68                33.81            True
  CTAS           87.88               33            0.62              0.76        174.26                30.38            True
  ALNY           86.96               23            2.07              4.75        325.21                41.11            True
  SNPS           85.71               28            1.89              5.42        407.84                37.77            True
  ABNB           83.33               18            2.00              1.84        130.61                41.34            True
  TTWO           80.95               21            1.90              2.70        200.97                26.08            True
  CSCO           80.95               21            0.69              0.41         83.53                27.82            True
    ZS          100.00                1           12.13             11.71        132.83                46.90           False
  SBUX           92.11               38            0.39              0.27         97.10                40.88           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-09T14:55:00.989254-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:50:03.978140-04:00  entry_1500        entry {"allocated_cash": 4400.0, "contract_symbol": "REGN260515C00765000", "contracts": 1, "entry_option_price": 44.0, "matched_signals": 21, "success_rate": 100.0, "ticker": "REGN"}
2026-04-09T14:40:04.078140-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:35:00.960951-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:30:00.902865-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:25:00.971224-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:10:01.012659-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:05:00.920582-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T14:00:05.431112-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-09T13:55:04.050612-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409145500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409145500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409145500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409145500)

</details>
