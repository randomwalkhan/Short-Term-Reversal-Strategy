# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 13:40:05 EDT`
Last processed slot: `manage_1330`

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
   WDC           97.44               39            0.66              1.38        297.14                91.06            True
  UPRO           92.50               40            0.50              0.35         99.02                57.18            True
  ORLY           90.24               41            0.56              0.36         91.94                22.81            True
  CDNS           89.19               37            1.38              2.72        279.03                26.25            True
  GILD           88.46               26            0.72              0.71        140.00                21.47            True
   BKR           88.24               34            0.54              0.23         60.24                40.20            True
  MCHP           86.84               38            0.66              0.30         65.25                45.66            True
   MAR           86.36               22            1.31              3.06        332.15                28.45            True
  KLAC           85.29               34            0.97             10.28       1515.43                56.48            True
  SOXL           85.29               34            0.86              0.31         52.13               138.72            True
   CSX           85.00               20            0.95              0.28         41.32                27.84            True
  BKNG           84.21               38            0.68             19.98       4176.00                42.15            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T13:40:05.899103-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:35:05.898186-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:30:05.883847-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:25:05.885731-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-02T13:10:05.901781-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-02T13:05:05.894561-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-02T13:00:05.924062-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-02T12:55:05.890571-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-02T12:40:05.891955-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-02T12:35:01.890526-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
