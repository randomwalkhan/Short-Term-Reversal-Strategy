# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 11:45:05 EDT`
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
  MRVL           95.35               43            0.51              0.38        106.55                92.70            True
  MPWR           91.89               37            0.70              5.46       1117.17                56.57            True
  CDNS           90.70               43            0.89              1.74        279.44                26.25            True
  ORLY           90.24               41            0.55              0.36         91.95                22.81            True
  KLAC           86.84               38            0.54              5.75       1517.37                56.48            True
  AMAT           86.11               36            0.91              2.26        352.83                59.65            True
  MCHP           85.71               35            0.80              0.36         65.22                45.66            True
  SOXL           85.29               34            0.75              0.27         52.14               138.72            True
  ASML           85.19               27            1.35             12.87       1354.24                52.01            True
 GOOGL           84.62               39            0.60              1.24        296.86                35.66            True
  VRTX           84.62               26            1.50              4.69        445.25                39.75            True
   TXN           83.33               30            0.93              1.28        195.75                33.08            True
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
