# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 09:55:03 EDT`
Last processed slot: `manage_1000`

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
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                   4.9       95.56         95.68            22.5                   0.51         94.87               39              0.58         41.74            0.39                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               20            0.74              1.18        227.70                22.84            True
   WDC           96.55               29            3.34              6.96        294.75                91.06            True
   STX           93.10               29            2.15              6.37        420.39                80.16            True
  ASML           92.86               14            2.85             27.17       1348.12                52.01            True
  SBUX           92.59               27            0.95              0.60         90.17                36.02            True
  FTNT           92.31               39            0.96              0.55         80.92                29.50            True
  FAST           91.43               35            0.60              0.20         46.55                21.97            True
  NVDA           91.30               23            1.47              1.80        174.98                36.98            True
  DXCM           91.18               34            1.54              0.67         62.08                31.67            True
  MPWR           90.32               31            1.44             11.26       1114.68                56.57            True
  MRVL           88.89               18            3.23              2.41        105.68                92.70            True
  UPRO           88.89               18            3.16              2.20         98.26                57.18            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-02T09:55:03.086371-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:40:05.889923-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:35:05.879902-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:30:05.894961-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-01T16:00:01.918138-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:55:00.975857-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:40:05.880995-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:35:05.885345-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:30:05.883058-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:25:05.904161-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
