# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 13:50:05 EDT`
Last processed slot: `manage_1400`

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
   WDC           97.22               36            1.62              3.38        296.28                91.06            True
  ASML           93.33               15            2.80             26.65       1348.34                52.01            True
  ABNB           92.50               40            0.67              0.59        124.94                36.75            True
  MPWR           91.67               36            0.77              6.07       1116.91                56.57            True
  UPRO           90.62               32            1.01              0.70         98.87                57.18            True
  DXCM           90.48               42            0.93              0.41         62.20                31.67            True
  ORLY           88.57               35            0.75              0.48         91.89                22.81            True
  CDNS           88.24               34            1.46              2.86        278.96                26.25            True
   MAR           88.00               25            1.13              2.65        332.33                28.45            True
  SNPS           87.80               41            0.68              1.90        395.93                35.88            True
  MCHP           85.29               34            0.96              0.44         65.19                45.66            True
  KLAC           85.19               27            1.53             16.28       1512.86                56.48            True
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
