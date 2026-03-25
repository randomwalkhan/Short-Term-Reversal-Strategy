# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 15:00:03 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_only_filtered`
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every hour through `3:30 PM ET`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart view: default display is trailing `1W`, with explicit ET timestamps

## Portfolio Snapshot

- Cash: `$575.00`
- Equity: `$9,865.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$-135.00`
- Open positions: `2`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FANG FANG260515C00195000       2026-03-25                   0               12.20                 12.20      195.53        195.55             0.0                   0.00        100.00               25              0.78         41.94           41.94                  29.12
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                 22.05      318.55        317.20          -135.0                  -2.97         93.33               30              1.23         48.32           49.34                  39.50
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               25            0.78              1.07        196.60                29.12            True
   STX           97.06               34            1.38              4.09        422.47                70.55            True
   WDC           96.88               32            1.94              4.09        299.30                74.01            True
  ASML           90.62               32            0.57              5.57       1397.03                46.54            True
  FTNT           90.48               42            0.67              0.37         79.18                26.69            True
  AMAT           89.66               29            1.29              3.37        372.54                51.46            True
  KLAC           88.46               26            1.45             15.93       1559.36                48.83            True
  CDNS           88.24               34            1.36              2.72        283.16                27.43            True
  GOOG           87.18               39            0.51              1.03        288.76                23.16            True
  CRWD           86.36               22            2.13              5.85        390.48                45.29            True
    MU           85.71               14            3.87             10.72        390.93                67.96            True
  SNPS           84.21               19            2.36              6.86        412.68                37.59            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
2026-03-25T15:00:03.353246-04:00   entry_1500        entry   {"allocated_cash": 4880.0, "contract_symbol": "FANG260515C00195000", "contracts": 4, "entry_option_price": 12.2, "matched_signals": 25, "success_rate": 100.0, "ticker": "FANG"}
2026-03-25T14:34:20.011472-04:00  manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-25T09:30:01.175501-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-24T15:00:05.740108-04:00   entry_1500        entry {"allocated_cash": 4545.0, "contract_symbol": "AVGO260515C00320000", "contracts": 2, "entry_option_price": 22.725, "matched_signals": 30, "success_rate": 93.33, "ticker": "AVGO"}
2026-03-24T13:30:05.751589-04:00  manage_1330 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-24T13:25:36.643365-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-23T20:59:15.901018-04:00       manual    pre_start                                                                                                                                                       {"start_date": "2026-03-24"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
