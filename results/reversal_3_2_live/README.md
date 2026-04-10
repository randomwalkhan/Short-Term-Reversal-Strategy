# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 09:40:06 EDT`
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

- Cash: `$8,625.00`
- Equity: `$12,825.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-200.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4200.0                44.0                  42.0      764.07        764.01          -200.0                  -4.55         100.0               21              1.48         48.92             0.1                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.06               34            1.64              3.89        336.21                86.06            True
   STX           94.74               38            0.57              1.99        499.92                74.83            True
  COST           92.86               28            0.78              5.62       1029.62                13.79            True
  INSM           90.91               44            0.57              0.64        159.32                51.90            True
  ABNB           90.62               32            1.20              1.09        128.69                41.65            True
   WMT           90.62               32            0.62              0.56        128.89                24.68            True
  GILD           90.32               31            0.51              0.51        141.87                20.31            True
  VRTX           89.74               39            0.58              1.83        445.96                28.30            True
  SNPS           88.89               27            2.02              5.72        402.40                36.22            True
  DXCM           88.64               44            0.71              0.33         65.54                32.42            True
   BKR           86.11               36            0.50              0.22         63.32                35.49            True
  DDOG           85.71               14            4.37              3.33        107.55                49.83            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-10T09:40:06.426501-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:35:06.431602-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:30:06.431975-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-09T16:00:01.894335-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-09T15:55:05.644912-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-09T15:40:01.001993-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:35:00.892532-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:30:04.886669-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:25:00.951211-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:10:05.606498-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410094006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410094006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410094006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410094006)

</details>
