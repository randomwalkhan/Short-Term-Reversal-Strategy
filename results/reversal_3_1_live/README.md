# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 10:30:05 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$9,810.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$67.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  4.95       95.56         96.75            67.5                   1.54         94.87               39              0.58         41.74           37.74                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           96.00               25            3.52              7.34        294.58                91.06            True
  SBUX           94.59               37            0.50              0.32         90.29                36.02            True
   STX           94.44               36            1.39              4.12        421.35                80.16            True
  ROST           92.59               27            0.58              0.89        219.57                21.27            True
  MRVL           91.67               24            2.23              1.67        106.00                92.70            True
  UPRO           91.30               23            2.09              1.45         98.55                57.18            True
  DXCM           91.18               34            1.56              0.68         62.08                31.67            True
  NVDA           91.18               34            0.81              1.00        175.32                36.98            True
  AVGO           88.89               27            1.68              3.68        311.91                41.97            True
  MPWR           88.46               26            2.14             16.81       1112.31                56.57            True
  ABNB           88.24               17            1.96              1.72        124.45                36.75            True
  SNPS           87.80               41            0.89              2.48        395.68                35.88            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-02T10:30:05.885804-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:25:05.890764-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:10:05.923370-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:05:05.400756-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:00:03.566981-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:55:03.086371-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:40:05.889923-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:35:05.879902-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:30:05.894961-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-01T16:00:01.918138-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
