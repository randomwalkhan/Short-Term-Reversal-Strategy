# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 10:45:05 EDT`
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
- Equity: `$10,035.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$292.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   1                4.88                   5.2       95.56         97.68           292.5                   6.67         94.87               39              0.58         41.74           35.45                  24.42
```

## Today's Closed Trades (2026-04-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               13            3.52              9.40        377.23                40.57            True
   WDC           97.06               34            1.93              4.02        296.01                91.06            True
  REGN           94.12               17            1.84             10.02        772.96                26.81            True
  CDNS           90.48               42            0.90              1.77        279.43                26.25            True
   MAR           88.89               36            0.63              1.48        332.83                28.45            True
  ASML           88.57               35            0.71              6.74       1356.87                52.01            True
  MCHP           86.49               37            0.72              0.33         65.24                45.66            True
  TMUS           85.71               21            1.06              1.51        203.60                22.53            True
  BKNG           84.21               38            0.71             20.83       4175.63                42.15            True
   TXN           83.87               31            0.80              1.11        195.83                33.08            True
  INSM           83.33               36            1.15              1.33        164.29                56.47            True
    MU           82.86               35            1.34              3.44        366.37                84.85            True
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
