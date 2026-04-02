# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 09:35:05 EDT`
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
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart view: default display is trailing `1W`, with latest ET checkpoint annotation and return % axis

## Portfolio Snapshot

- Cash: `$5,355.00`
- Equity: `$9,765.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$22.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                   4.9       95.56         96.54            22.5                   0.51         94.87               39              0.58         41.74             0.0                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               15            1.10              1.75        227.45                22.84            True
  UPRO          100.00               11            4.15              2.88         97.96                57.18            True
  INTC           96.55               29            2.21              0.74         47.71                73.32            True
  NVDA           95.24               21            1.80              2.21        174.80                36.98            True
  FTNT           93.33               45            0.62              0.35         81.00                29.50            True
   WDC           93.33               15            5.27             10.98        293.03                91.06            True
   STX           90.00               20            3.91             11.57        418.16                80.16            True
  CDNS           90.00               10            2.99              5.87        277.67                26.25            True
  ORLY           88.24               34            0.75              0.49         91.89                22.81            True
  CSCO           87.88               33            0.53              0.29         77.39                28.01            True
  FAST           87.50               24            1.17              0.38         46.47                21.97            True
  CTAS           86.67               30            0.67              0.81        171.69                29.59            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-02T09:35:05.879902-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:30:05.894961-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-01T16:00:01.918138-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:55:00.975857-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:40:05.880995-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:35:05.885345-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:30:05.883058-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:25:05.904161-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:10:05.885233-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-01T15:05:05.887661-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
