# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 10:15:05 EDT`
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
- Equity: `$9,990.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$247.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  5.15       95.56         96.14           247.5                   5.64         94.87               39              0.58         41.74           42.04                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               14            3.30              8.80        377.49                40.57            True
   WDC           96.67               30            2.92              6.08        295.13                91.06            True
   STX           94.59               37            1.23              3.63        421.56                80.16            True
  SBUX           93.55               31            0.84              0.53         90.20                36.02            True
  ROST           93.10               29            0.52              0.80        219.61                21.27            True
  MRVL           92.31               26            1.90              1.42        106.10                92.70            True
  FAST           91.67               36            0.58              0.19         46.55                21.97            True
  NVDA           91.43               35            0.76              0.93        175.35                36.98            True
  DXCM           91.18               34            1.48              0.65         62.09                31.67            True
  UPRO           90.48               21            2.47              1.72         98.43                57.18            True
  AVGO           89.66               29            1.50              3.29        312.08                41.97            True
  MPWR           88.89               27            1.92             15.06       1113.05                56.57            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-02T10:10:05.923370-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:05:05.400756-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:00:03.566981-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:55:03.086371-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:40:05.889923-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:35:05.879902-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:30:05.894961-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-01T16:00:01.918138-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:55:00.975857-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-01T15:40:05.880995-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
