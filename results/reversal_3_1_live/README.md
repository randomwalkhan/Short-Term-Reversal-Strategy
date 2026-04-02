# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 11:20:05 EDT`
Last processed slot: `manage_1130`

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
   WDC           97.37               38            0.83              1.74        296.99                91.06            True
  UPRO           92.50               40            0.60              0.41         98.99                57.18            True
  MPWR           91.67               36            0.82              6.45       1116.74                56.57            True
  CDNS           89.74               39            1.11              2.18        279.26                26.25            True
   MAR           89.74               39            0.51              1.20        332.95                28.45            True
  AMAT           86.11               36            0.82              2.02        352.93                59.65            True
  MCHP           86.11               36            0.75              0.34         65.23                45.66            True
  SOXL           85.29               34            0.79              0.29         52.14               138.72            True
   CSX           85.00               20            0.97              0.28         41.32                27.84            True
  VRTX           84.85               33            1.00              3.14        445.91                39.75            True
  TMUS           84.38               32            0.51              0.74        203.93                22.53            True
 GOOGL           84.21               38            0.64              1.33        296.82                35.66            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                     detail
2026-04-02T11:20:05.893680-04:00 manage_1130         exit {"contract_symbol": "NFLX260508C00096000", "pnl": 1102.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.13, "ticker": "NFLX"}
2026-04-02T11:10:05.886103-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:05:05.887015-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:00:05.878856-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:55:05.929146-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:40:05.872686-04:00 manage_1030 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:35:05.890056-04:00 manage_1030 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:30:05.885804-04:00 manage_1030 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:25:05.890764-04:00 manage_1030 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T10:10:05.923370-04:00 manage_1000 slot_skipped                                                                                                            {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
