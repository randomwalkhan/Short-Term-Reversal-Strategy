# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 10:50:05 EDT`
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
- Equity: `$10,012.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$270.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                  5.18       95.56         97.36           270.0                   6.15         94.87               39              0.58         41.74           36.96                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           96.77               31            2.73              5.68        295.29                91.06            True
  MRVL           95.35               43            0.52              0.38        106.55                92.70            True
   STX           95.12               41            0.51              1.50        422.48                80.16            True
  REGN           94.12               17            1.84              9.99        772.97                26.81            True
  ROST           92.59               27            0.69              1.06        219.50                21.27            True
  UPRO           92.31               39            0.74              0.51         98.95                57.18            True
  MPWR           91.18               34            1.18              9.23       1115.56                56.57            True
  CDNS           89.74               39            1.17              2.29        279.21                26.25            True
  AVGO           89.74               39            0.91              1.99        312.64                41.97            True
  PCAR           89.19               37            0.75              0.62        117.39                23.75            True
   MAR           88.57               35            0.79              1.83        332.67                28.45            True
  SHOP           86.36               44            0.59              0.49        118.31                47.54            True
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
