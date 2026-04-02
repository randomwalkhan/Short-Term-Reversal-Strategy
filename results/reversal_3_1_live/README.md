# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 11:10:05 EDT`
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
- Equity: `$10,507.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$765.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  5.72       95.56         97.61           765.0                  17.44         94.87               39              0.58         41.74           41.59                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               10            3.68              9.81        377.05                40.57            True
   WDC           97.14               35            1.75              3.65        296.16                91.06            True
  MPWR           91.18               34            1.12              8.80       1115.74                56.57            True
  CDNS           90.48               42            0.92              1.81        279.42                26.25            True
   MAR           89.74               39            0.50              1.18        332.96                28.45            True
  AMAT           84.85               33            1.00              2.48        352.74                59.65            True
   TXN           84.85               33            0.63              0.86        195.93                33.08            True
  VRTX           84.62               39            0.80              2.51        446.19                39.75            True
    MU           82.86               35            1.55              3.99        366.14                84.85            True
   CSX           82.35               17            1.28              0.37         41.28                27.84            True
  ASML           81.82               22            1.73             16.46       1352.71                52.01            True
  TMUS           81.48               27            0.74              1.05        203.80                22.53            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T11:10:05.886103-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T11:05:05.887015-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T11:00:05.878856-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T10:55:05.929146-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-02T10:40:05.872686-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:35:05.890056-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:30:05.885804-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:25:05.890764-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-02T10:10:05.923370-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-02T10:05:05.400756-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
