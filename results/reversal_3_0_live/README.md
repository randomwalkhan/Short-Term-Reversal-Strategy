# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 15:30:01 EDT`
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
- Exit scans: `9:30 AM ET` and every hour through `3:30 PM ET`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart view: default display is trailing `1W`, with explicit ET timestamps

## Portfolio Snapshot

- Cash: `$575.00`
- Equity: `$9,700.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$-300.00`
- Open positions: `2`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FANG FANG260515C00195000       2026-03-25                   0               12.20                 12.20      195.53        195.55             0.0                    0.0        100.00               25              0.78         41.94           41.60                  29.12
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                 21.22      318.55        317.16          -300.0                   -6.6         93.33               30              1.23         48.32           47.54                  39.50
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               26            0.66              0.91        196.67                29.12            True
   WDC           96.88               32            2.16              4.55        299.10                74.01            True
   STX           95.83               24            2.72              8.08        420.76                70.55            True
  FTNT           91.11               45            0.53              0.29         79.21                26.69            True
  CDNS           89.19               37            1.05              2.09        283.42                27.43            True
  AMAT           88.89               27            1.47              3.85        372.34                51.46            True
  SNPS           87.50               24            1.82              5.30        413.35                37.59            True
  KLAC           87.50               24            1.61             17.69       1558.61                48.83            True
  CRWD           86.36               22            2.08              5.73        390.54                45.29            True
    MU           85.71               14            3.91             10.82        390.89                67.96            True
  CTAS           85.00               20            1.09              1.36        177.55                29.68            True
   BKR           81.82               22            1.00              0.44         63.30                40.11            True
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
