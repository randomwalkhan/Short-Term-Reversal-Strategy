# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 12:10:05 EDT`
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
   WDC           97.50               40            0.59              1.22        297.21                91.06            True
  MRVL           94.59               37            0.86              0.64        106.43                92.70            True
  MPWR           91.67               36            0.80              6.24       1116.84                56.57            True
  DXCM           91.30               46            0.55              0.24         62.27                31.67            True
  UPRO           90.62               32            1.02              0.71         98.87                57.18            True
  GILD           90.62               32            0.54              0.53        140.07                21.47            True
  CDNS           89.74               39            1.08              2.12        279.28                26.25            True
  AVGO           89.74               39            0.62              1.35        312.91                41.97            True
   MAR           89.66               29            0.94              2.19        332.52                28.45            True
  KLAC           87.18               39            0.50              5.36       1517.54                56.48            True
  ORLY           87.10               31            0.84              0.54         91.87                22.81            True
  SOXL           84.85               33            1.86              0.68         51.97               138.72            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                     detail
2026-04-02T12:10:05.892027-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T12:05:05.882439-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T12:00:03.471000-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:55:05.888116-04:00 manage_1200 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:40:05.909108-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:35:01.344213-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:30:05.918886-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:25:05.883603-04:00 manage_1130 slot_skipped                                                                                                            {"reason": "already_processed"}
2026-04-02T11:20:05.893680-04:00 manage_1130         exit {"contract_symbol": "NFLX260508C00096000", "pnl": 1102.5, "reason": "take_profit_day1_hit_at_scan", "return_pct": 25.13, "ticker": "NFLX"}
2026-04-02T11:10:05.886103-04:00 manage_1100 slot_skipped                                                                                                            {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
