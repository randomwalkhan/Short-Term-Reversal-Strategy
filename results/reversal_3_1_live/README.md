# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 09:45:05 EDT`
Last processed slot: `manual_refresh`

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
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                   4.9       95.56         95.88            22.5                   0.51         94.87               39              0.58         41.74             0.2                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               19            0.93              1.49        227.56                22.84            True
  TSLA          100.00               14            3.30              8.81        377.49                40.57            True
   WDC           95.00               20            4.43              9.23        293.77                91.06            True
  NVDA           95.00               20            1.84              2.27        174.78                36.98            True
  INTC           94.29               35            1.53              0.51         47.81                73.32            True
 CMCSA           93.75               16            0.52              0.10         28.01                25.23            True
  ROST           93.10               29            0.52              0.80        219.61                21.27            True
  FTNT           92.50               40            0.79              0.45         80.96                29.50            True
  UPRO           92.31               13            3.97              2.75         97.99                57.18            True
   STX           92.00               25            3.11              9.21        419.17                80.16            True
  DXCM           90.91               22            1.93              0.84         62.01                31.67            True
  FAST           88.00               25            1.12              0.36         46.47                21.97            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-02T09:40:05.889923-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:35:05.879902-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:30:05.894961-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-01T16:00:01.918138-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:55:00.975857-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:40:05.880995-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:35:05.885345-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:30:05.883058-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:25:05.904161-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:10:05.885233-04:00   entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
