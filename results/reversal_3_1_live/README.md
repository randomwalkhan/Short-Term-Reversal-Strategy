# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 15:40:05 EDT`
Last processed slot: `manage_1530`

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
- Equity: `$9,787.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$45.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  NFLX NFLX260508C00096000       2026-04-01                   0                4.88                  4.93       95.56         95.96            45.0                   1.03         94.87               39              0.58         41.74           40.21                  24.42
```

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  ABNB           94.12               34            0.80              0.71        125.98                37.55            True
  FTNT           93.33               45            0.53              0.30         81.59                30.40            True
   LIN           88.46               26            0.56              1.93        494.93                19.67            True
 CMCSA           85.71               21            1.25              0.25         28.27                29.02            True
  BKNG           84.21               38            0.71             20.99       4201.33                42.14            True
   BKR           83.33               24            0.93              0.40         60.88                41.31            True
   APP           82.86               35            2.05              5.72        395.55                76.97            True
  WDAY           81.40               43            0.79              0.72        129.61                39.93            True
  CSGP           81.25               32            1.74              0.49         40.13                34.54            True
  ADSK           81.08               37            0.62              1.04        238.96                29.70            True
  FANG          100.00                3            3.60              4.98        195.66                24.73           False
   KDP          100.00                2            2.26              0.42         26.15                19.96           False
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
