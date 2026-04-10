# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 09:30:06 EDT`
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
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4200.0                44.0                  42.0      764.07        769.03          -200.0                  -4.55         100.0               21              1.48         48.92             0.0                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FTNT           95.24               42            0.76              0.43         80.48                32.65            True
  INTC           94.44               36            1.31              0.56         61.48                74.89            True
   WMT           92.31               26            0.86              0.78        128.80                24.68            True
  CDNS           90.91               44            0.64              1.25        280.47                29.62            True
  COST           90.32               31            0.66              4.75       1030.00                13.79            True
  GILD           88.46               26            0.65              0.64        141.81                20.31            True
  DDOG           87.18               39            0.81              0.62        108.72                49.83            True
   EXC           86.36               22            0.51              0.18         49.36                21.05            True
  PLTR           86.21               29            2.20              2.01        129.68                58.33            True
  ORLY           86.21               29            1.04              0.68         94.09                24.35            True
    MU           83.33               36            0.86              2.53        420.42                78.74            True
  CRWD           80.00               40            0.93              2.57        393.58                54.58            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-10T09:30:06.431975-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-09T16:00:01.894335-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-09T15:55:05.644912-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-09T15:40:01.001993-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:35:00.892532-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:30:04.886669-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:25:00.951211-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-09T15:10:05.606498-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-09T15:05:00.876232-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-09T15:00:05.892957-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410093006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410093006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410093006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410093006)

</details>
