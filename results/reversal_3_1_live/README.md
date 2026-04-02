# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 11:00:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$10,282.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$540.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  5.48       95.56         97.33           540.0                  12.31         94.87               39              0.58         41.74           39.58                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           96.88               32            2.36              4.92        295.62                91.06            True
  MRVL           95.35               43            0.56              0.42        106.53                92.70            True
  MPWR           91.89               37            0.62              4.84       1117.43                56.57            True
  CDNS           90.48               42            0.91              1.79        279.42                26.25            True
  PCAR           90.24               41            0.55              0.45        117.46                23.75            True
   MAR           88.89               36            0.65              1.53        332.81                28.45            True
  KLAC           86.84               38            0.63              6.72       1516.96                56.48            True
  MCHP           86.49               37            0.70              0.32         65.24                45.66            True
  AMAT           86.11               36            0.91              2.25        352.83                59.65            True
  SOXL           85.29               34            1.59              0.58         52.01               138.72            True
  ASML           85.19               27            1.49             14.14       1353.70                52.01            True
  VRTX           85.00               40            0.62              1.95        446.42                39.75            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T11:00:05.878856-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T10:55:05.929146-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T10:40:05.872686-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:35:05.890056-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:30:05.885804-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:25:05.890764-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:10:05.923370-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:05:05.400756-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:00:03.566981-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T09:55:03.086371-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
