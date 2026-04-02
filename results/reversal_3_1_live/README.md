# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 11:50:05 EDT`
Last processed slot: `manage_1200`

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
   WDC           97.44               39            0.81              1.68        297.01                91.06            True
  MRVL           95.35               43            0.55              0.41        106.53                92.70            True
  MPWR           91.43               35            1.00              7.83       1116.15                56.57            True
  DXCM           91.11               45            0.65              0.28         62.25                31.67            True
  UPRO           90.62               32            0.93              0.64         98.89                57.18            True
  GILD           90.62               32            0.55              0.54        140.07                21.47            True
  CDNS           89.74               39            1.12              2.19        279.25                26.25            True
   MAR           89.19               37            0.63              1.46        332.83                28.45            True
  SNPS           89.13               46            0.57              1.58        396.06                35.88            True
  ORLY           87.10               31            0.84              0.54         91.87                22.81            True
  KLAC           86.84               38            0.56              5.92       1517.30                56.48            True
  SOXL           85.29               34            1.68              0.62         52.00               138.72            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                     detail
2026-04-02T11:40:05.909108-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:35:01.344213-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:30:05.918886-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:25:05.883603-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:20:05.893680-04:00 manage_1130         exit {"contract_symbol": "NFLX260508C00096000", "pnl": 1102.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.13, "ticker": "NFLX"}
2026-04-02T11:10:05.886103-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:05:05.887015-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:00:05.878856-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:55:05.929146-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:40:05.872686-04:00 manage_1030 slot_skipped                                                                                                            {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
