# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 10:35:05 EDT`
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
- Equity: `$9,855.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$112.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                   5.0       95.56         97.17           112.5                   2.56         94.87               39              0.58         41.74           36.23                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               13            3.42              9.14        377.34                40.57            True
   WDC           96.88               32            2.38              4.97        295.60                91.06            True
  MRVL           94.59               37            0.91              0.68        106.42                92.70            True
  ABNB           93.33               30            1.30              1.14        124.70                36.75            True
 CMCSA           92.31               13            0.77              0.15         27.99                25.23            True
  MPWR           91.18               34            1.14              8.97       1115.67                56.57            True
  AVGO           90.91               33            1.13              2.47        312.43                41.97            True
  PCAR           90.24               41            0.59              0.48        117.44                23.75            True
  DXCM           89.74               39            1.15              0.50         62.16                31.67            True
   MAR           88.00               25            1.11              2.59        332.35                28.45            True
  CHTR           87.18               39            0.56              0.85        215.91                36.36            True
  CDNS           87.10               31            1.55              3.05        278.88                26.25            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-02T10:35:05.890056-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:30:05.885804-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:25:05.890764-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:10:05.923370-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:05:05.400756-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:00:03.566981-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:55:03.086371-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:40:05.889923-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:35:05.879902-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:30:05.894961-04:00 data_refresh data_refresh                   {'saved': 99}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
