# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 11:05:05 EDT`
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
- Equity: `$10,372.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$630.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  5.58       95.56         97.43           630.0                  14.36         94.87               39              0.58         41.74           40.31                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               10            3.68              9.83        377.05                40.57            True
   WDC           97.06               34            1.97              4.11        295.97                91.06            True
  MRVL           95.35               43            0.52              0.38        106.55                92.70            True
  MPWR           91.67               36            0.74              5.82       1117.01                56.57            True
  CDNS           90.48               42            0.95              1.86        279.39                26.25            True
   MAR           89.47               38            0.60              1.40        332.86                28.45            True
  MCHP           87.18               39            0.60              0.27         65.26                45.66            True
  KLAC           86.84               38            0.53              5.64       1517.42                56.48            True
  SOXL           85.29               34            1.37              0.50         52.04               138.72            True
  AMAT           84.38               32            1.11              2.76        352.62                59.65            True
  TMUS           84.00               25            0.81              1.15        203.76                22.53            True
   TXN           83.87               31            0.80              1.10        195.83                33.08            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T11:05:05.887015-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T11:00:05.878856-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T10:55:05.929146-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T10:40:05.872686-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:35:05.890056-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:30:05.885804-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:25:05.890764-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:10:05.923370-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:05:05.400756-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:00:03.566981-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
