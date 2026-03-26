# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-26 10:30:00 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$10,140.00`
- Equity: `$10,140.00`
- Realized PnL: `$140.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-03-26)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct  exit_reason
  AVGO AVGO260515C00320000          2026-03-24         2026-03-26              22.725             20.025 -540.0  -11.881188    stop_scan
  FANG FANG260515C00195000          2026-03-25         2026-03-26              12.200             13.900  680.0   13.934426 tp_day1_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC           95.00               20            3.37              1.11         46.70                59.50            True
   WDC           94.44               18            4.04              8.38        292.55                73.45            True
   STX           94.12               17            3.82             11.06        408.48                69.64            True
  NVDA           93.75               16            2.10              2.63        177.55                32.16            True
  AVGO           92.86               28            1.43              3.18        317.45                37.11            True
  ASML           90.91               11            3.05             29.74       1381.15                45.25            True
  PLTR           86.96               23            2.52              2.73        153.79                44.81            True
  MPWR           85.71               28            1.83             14.31       1112.53                43.00            True
  TSLA           85.29               34            1.13              3.04        384.65                32.52            True
  CTAS           83.33               12            1.65              2.04        175.98                23.67            True
 GOOGL           81.82               22            1.49              3.03        289.63                23.48            True
   ADI           81.25               32            0.63              1.41        321.43                31.26            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                           {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                          {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
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
