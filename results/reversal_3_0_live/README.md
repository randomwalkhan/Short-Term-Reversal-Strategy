# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-30 15:30:02 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_only_filtered`
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

- Cash: `$1,527.50`
- Equity: `$9,237.50`
- Realized PnL: `$-422.50`
- Unrealized PnL: `$-340.00`
- Open positions: `2`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FANG FANG260515C00200000       2026-03-30                   0                11.5                  11.7      198.70        197.83            60.0                   1.74         100.0               15              1.56         43.31           45.54                  24.78
   HON  HON260501C00225000       2026-03-27                   1                 9.2                   8.4      223.64        222.86          -400.0                  -8.70         100.0               20              0.68         39.47           36.99                  24.88
```

## Today's Closed Trades (2026-03-30)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               14            1.85              2.61        200.72                24.78            True
  NVDA           95.24               21            1.68              1.97        166.68                32.71            True
  DXCM           93.33               45            0.51              0.22         62.15                32.07            True
  CDNS           90.70               43            0.87              1.65        271.06                24.46            True
  NFLX           90.32               31            0.93              0.61         93.17                21.54            True
   STX           90.00               10            5.77             15.34        373.49                75.41            True
 GOOGL           87.18               39            0.67              1.28        273.79                25.79            True
  SHOP           86.67               45            0.63              0.49        111.64                50.38            True
  TSLA           85.71               21            2.48              6.28        359.14                35.33            True
  GOOG           84.21               38            0.68              1.30        273.20                24.24            True
  AVGO           83.33               12            3.42              7.19        297.60                39.28            True
  KLAC           80.00               10            4.16             42.01       1425.21                53.64            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                           detail
2026-03-30T15:00:04.861501-04:00   entry_1500        entry {"allocated_cash": 3450.0, "contract_symbol": "FANG260515C00200000", "contracts": 3, "entry_option_price": 11.5, "matched_signals": 15, "success_rate": 100.0, "ticker": "FANG"}
2026-03-27T15:00:04.241996-04:00   entry_1500        entry    {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                             {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                         {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                        {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-25T15:00:03.353246-04:00   entry_1500        entry {"allocated_cash": 4880.0, "contract_symbol": "FANG260515C00195000", "contracts": 4, "entry_option_price": 12.2, "matched_signals": 25, "success_rate": 100.0, "ticker": "FANG"}
2026-03-25T14:34:20.011472-04:00  manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
