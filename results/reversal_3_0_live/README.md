# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-26 15:00:01 EDT`
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

- Cash: `$5,215.00`
- Equity: `$10,140.00`
- Realized PnL: `$140.00`
- Unrealized PnL: `$0.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  ABNB ABNB260515C00130000       2026-03-26                   0                9.85                  9.85      130.79        130.82             0.0                    0.0         94.29               35              0.77         51.93           51.93                  28.73
```

## Today's Closed Trades (2026-03-26)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct  exit_reason
  AVGO AVGO260515C00320000          2026-03-24         2026-03-26              22.725             20.025 -540.0  -11.881188    stop_scan
  FANG FANG260515C00195000          2026-03-25         2026-03-26              12.200             13.900  680.0   13.934426 tp_day1_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  ABNB           94.29               35            0.77              0.71        131.50                28.73            True
  SBUX           91.67               12            1.89              1.23         92.17                29.63            True
  PLTR           90.91               11            4.23              4.58        153.00                44.81            True
   WMT           90.32               31            0.64              0.55        122.82                23.35            True
  GILD           90.00               30            0.57              0.55        138.02                23.55            True
  AVGO           88.89               18            2.26              5.03        316.65                37.11            True
  PCAR           87.88               33            0.82              0.67        116.05                24.57            True
  SNPS           85.71               28            1.49              4.27        408.30                32.59            True
  SHOP           84.00               25            2.43              2.02        117.56                51.12            True
  TSLA           82.35               17            2.99              8.07        382.49                32.52            True
   TXN           81.25               32            0.50              0.69        196.47                29.17            True
  MELI           80.49               41            0.71              8.10       1636.00                35.73            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
2026-03-26T15:00:01.983935-04:00   entry_1500        entry   {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                           {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                          {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-25T15:00:03.353246-04:00   entry_1500        entry   {"allocated_cash": 4880.0, "contract_symbol": "FANG260515C00195000", "contracts": 4, "entry_option_price": 12.2, "matched_signals": 25, "success_rate": 100.0, "ticker": "FANG"}
2026-03-25T14:34:20.011472-04:00  manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-25T09:30:01.175501-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-24T15:00:05.740108-04:00   entry_1500        entry {"allocated_cash": 4545.0, "contract_symbol": "AVGO260515C00320000", "contracts": 2, "entry_option_price": 22.725, "matched_signals": 30, "success_rate": 93.33, "ticker": "AVGO"}
2026-03-24T13:30:05.751589-04:00  manage_1330 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-24T13:25:36.643365-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
