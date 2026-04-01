# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 15:45:00 EDT`
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
- Equity: `$9,810.00`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$67.50`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   0                4.88                  4.95       95.56         95.81            67.5                   1.54         94.87               39              0.58         41.74           41.27                  24.42
```

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  DXCM           93.33               45            0.56              0.24         62.70                32.83            True
  ABNB           92.31               39            0.72              0.64        126.01                37.55            True
  ORLY           89.74               39            0.64              0.41         92.13                22.81            True
  MDLZ           88.24               17            0.78              0.31         57.51                24.77            True
 CMCSA           85.00               20            1.48              0.29         28.25                29.02            True
  BKNG           84.21               38            0.69             20.30       4201.62                42.14            True
   APP           82.35               34            2.12              5.91        395.47                76.97            True
   BKR           81.82               22            1.11              0.47         60.85                41.31            True
  WDAY           81.40               43            0.85              0.77        129.59                39.93            True
  CSGP           81.25               32            1.69              0.48         40.14                34.54            True
  ADSK           81.08               37            0.67              1.12        238.92                29.70            True
  FANG          100.00                2            3.85              5.33        195.50                24.73           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                            detail
2026-04-01T15:40:05.880995-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:35:05.885345-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:30:05.883058-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:25:05.904161-04:00 manage_1530 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:10:05.885233-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:05:05.887661-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T15:00:05.918391-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:55:05.885525-04:00  entry_1500 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-04-01T14:50:05.934010-04:00  entry_1500        entry {"allocated_cash": 4387.5, "contract_symbol": "NFLX260508C00096000", "contracts": 9, "entry_option_price": 4.875, "matched_signals": 39, "success_rate": 94.87, "ticker": "NFLX"}
2026-04-01T14:40:05.889929-04:00 manage_1430 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
