# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 10:40:05 EDT`
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
- Equity: `$9,900.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$157.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  5.05       95.56         97.04           157.5                   3.59         94.87               39              0.58         41.74           37.22                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           96.88               32            2.38              4.95        295.61                91.06            True
  MRVL           95.12               41            0.63              0.47        106.51                92.70            True
  REGN           93.75               16            1.92             10.43        772.78                26.81            True
  CDNS           90.70               43            0.89              1.75        279.44                26.25            True
  PCAR           90.24               41            0.53              0.43        117.46                23.75            True
   MAR           88.89               36            0.66              1.53        332.80                28.45            True
  ASML           87.50               32            0.85              8.05       1356.31                52.01            True
  SHOP           86.36               44            0.57              0.48        118.32                47.54            True
  INSM           85.71               42            0.79              0.92        164.47                56.47            True
  SOXL           85.29               34            1.22              0.45         52.07               138.72            True
  MCHP           85.29               34            0.93              0.43         65.20                45.66            True
  BKNG           85.00               40            0.61             17.79       4176.93                42.15            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T10:40:05.872686-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:35:05.890056-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:30:05.885804-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:25:05.890764-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:10:05.923370-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:05:05.400756-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:00:03.566981-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:55:03.086371-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:40:05.889923-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-02T09:35:05.879902-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
