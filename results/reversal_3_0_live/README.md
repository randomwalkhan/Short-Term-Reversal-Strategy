# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-26 09:30:05 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$9,951.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$-49.00`
- Open positions: `2`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FANG FANG260515C00195000       2026-03-25                   1               12.20                 12.44      195.53         198.8            96.0                   1.97        100.00               25              0.78         41.94            0.00                  29.12
  AVGO AVGO260515C00320000       2026-03-24                   2               22.72                 22.00      318.55         312.9          -145.0                  -3.19         93.33               30              1.23         48.32            1.56                  39.50
```

## Today's Closed Trades (2026-03-26)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               21            0.52              0.82        225.44                24.88            True
   WDC           95.83               24            3.11              6.44        293.38                73.45            True
  SBUX           95.83               24            0.98              0.64         92.43                29.63            True
  NVDA           95.00               20            1.75              2.18        177.74                32.16            True
   STX           94.44               18            3.62             10.47        408.73                69.64            True
  INTC           93.75               32            1.40              0.46         46.98                59.50            True
  AVGO           92.00               25            1.72              3.84        317.16                37.11            True
  CDNS           90.91               44            0.63              1.23        280.86                23.40            True
  NFLX           89.29               28            1.02              0.66         92.00                51.34            True
  SNPS           89.19               37            1.05              3.01        408.84                32.59            True
  MPWR           88.24               34            1.00              7.82       1115.31                43.00            True
    MU           86.96               23            3.03              8.11        378.61                68.24            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
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
