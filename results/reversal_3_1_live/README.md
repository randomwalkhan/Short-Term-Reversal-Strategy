# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 12:45:05 EDT`
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
  MRVL           95.12               41            0.65              0.48        106.50                92.70            True
  MPWR           91.43               35            0.98              7.71       1116.21                56.57            True
  DXCM           91.11               45            0.77              0.34         62.23                31.67            True
   MAR           90.91               33            0.86              2.00        332.60                28.45            True
  SNPS           89.13               46            0.58              1.62        396.04                35.88            True
  CDNS           88.57               35            1.43              2.80        278.99                26.25            True
  GILD           88.46               26            0.69              0.68        140.01                21.47            True
  MCHP           87.18               39            0.60              0.27         65.26                45.66            True
  ORLY           87.10               31            0.86              0.55         91.86                22.81            True
  SOXL           85.29               34            1.24              0.45         52.07               138.72            True
  BKNG           85.00               40            0.61             17.79       4176.94                42.15            True
  KLAC           84.85               33            1.02             10.80       1515.21                56.48            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T12:40:05.891955-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:35:01.890526-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:30:05.879539-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:25:05.909945-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:10:05.892027-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-02T12:05:05.882439-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-02T12:00:03.471000-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-02T11:55:05.888116-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-02T11:40:05.909108-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-02T11:35:01.344213-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
