# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 13:00:05 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$10,845.00`
- Equity: `$10,845.00`
- Realized PnL: `$845.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-02)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  NFLX NFLX260508C00096000          2026-04-01         2026-04-02               4.875                6.1 1102.5   25.128205 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.44               39            0.65              1.35        297.15                91.06            True
  MRVL           95.00               40            0.76              0.57        106.47                92.70            True
  MPWR           91.67               36            0.84              6.55       1116.70                56.57            True
  DXCM           91.11               45            0.81              0.35         62.22                31.67            True
  UPRO           90.62               32            1.00              0.69         98.87                57.18            True
  GILD           88.46               26            0.81              0.79        139.96                21.47            True
   BKR           88.24               34            0.64              0.27         60.22                40.20            True
  SNPS           87.80               41            0.79              2.18        395.81                35.88            True
   MAR           87.50               24            1.17              2.73        332.29                28.45            True
  KLAC           87.10               31            1.20             12.82       1514.35                56.48            True
  ORLY           87.10               31            0.91              0.58         91.85                22.81            True
  MCHP           85.71               35            0.89              0.41         65.20                45.66            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T13:00:05.924062-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-02T12:55:05.890571-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-02T12:40:05.891955-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:35:01.890526-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:30:05.879539-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:25:05.909945-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:10:05.892027-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-02T12:05:05.882439-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-02T12:00:03.471000-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-02T11:55:05.888116-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
