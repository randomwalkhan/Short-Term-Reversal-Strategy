# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 10:00:03 EDT`
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
- Equity: `$9,562.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$-180.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  4.68       95.56          95.7          -180.0                   -4.1         94.87               39              0.58         41.74            48.5                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               23            0.52              0.83        227.84                22.84            True
   WDC           96.55               29            2.98              6.20        295.07                91.06            True
   STX           94.44               36            1.47              4.36        421.25                80.16            True
  SBUX           94.12               34            0.67              0.43         90.25                36.02            True
  FTNT           93.33               45            0.62              0.35         81.00                29.50            True
  NVDA           92.59               27            1.02              1.25        175.21                36.98            True
  FAST           91.89               37            0.56              0.18         46.55                21.97            True
  MPWR           91.43               35            1.04              8.15       1116.02                56.57            True
  DXCM           90.48               42            0.93              0.41         62.20                31.67            True
  UPRO           90.48               21            2.63              1.82         98.39                57.18            True
  MRVL           89.47               19            2.99              2.23        105.75                92.70            True
  AVGO           86.96               23            2.00              4.39        311.61                41.97            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-02T10:00:03.566981-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:55:03.086371-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:40:05.889923-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:35:05.879902-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:30:05.894961-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-01T16:00:01.918138-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:55:00.975857-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:40:05.880995-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:35:05.885345-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-01T15:30:05.883058-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
