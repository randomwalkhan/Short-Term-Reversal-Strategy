# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 11:15:05 EDT`
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
- Equity: `$10,687.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$945.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  5.92       95.56         97.85           945.0                  21.54         94.87               39              0.58         41.74           42.85                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               11            3.65              9.73        377.09                40.57            True
   WDC           97.22               36            1.03              2.14        296.81                91.06            True
  MPWR           91.89               37            0.51              4.00       1117.80                56.57            True
  CDNS           90.70               43            0.87              1.70        279.46                26.25            True
  MCHP           87.18               39            0.54              0.25         65.27                45.66            True
  AMAT           84.85               33            1.01              2.50        352.73                59.65            True
   TXN           84.85               33            0.59              0.81        195.95                33.08            True
  TMUS           84.38               32            0.53              0.76        203.93                22.53            True
  VRTX           83.78               37            0.87              2.72        446.09                39.75            True
   CSX           83.33               18            1.10              0.32         41.30                27.84            True
    MU           82.86               35            1.50              3.86        366.20                84.85            True
   ADI           81.82               33            0.51              1.15        320.09                36.19            True
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
