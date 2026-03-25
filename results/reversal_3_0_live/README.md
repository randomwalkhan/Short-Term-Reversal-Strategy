# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 13:28:02 EDT`
Last processed slot: `manage_1330`

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

- Cash: `$5,455.00`
- Equity: `$10,080.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$80.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                 23.12      318.55        319.91            80.0                   1.76         93.33               30              1.23         48.32           48.82                   39.5
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               22            0.95              1.32        196.50                29.12            True
   WDC           97.06               34            1.46              3.08        299.73                74.01            True
   STX           95.83               24            2.57              7.63        420.95                70.55            True
  CDNS           90.24               41            0.76              1.50        283.68                27.43            True
  CTAS           89.29               28            0.68              0.85        177.77                29.68            True
  KLAC           88.89               27            1.35             14.80       1559.85                48.83            True
    MU           87.50               16            3.73             10.32        391.11                67.96            True
  SNPS           87.10               31            1.38              4.03        413.89                37.59            True
  AMAT           86.96               23            1.72              4.51        372.06                51.46            True
  CHTR           85.29               34            0.89              1.36        217.02                38.80            True
  CTSH           85.29               34            0.56              0.24         60.14                32.06            True
 CMCSA           85.00               20            1.47              0.30         29.09                27.42            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
2026-03-25T09:30:01.175501-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-24T15:00:05.740108-04:00   entry_1500        entry {"allocated_cash": 4545.0, "contract_symbol": "AVGO260515C00320000", "contracts": 2, "entry_option_price": 22.725, "matched_signals": 30, "success_rate": 93.33, "ticker": "AVGO"}
2026-03-24T13:30:05.751589-04:00  manage_1330 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-24T13:25:36.643365-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-23T20:59:15.901018-04:00       manual    pre_start                                                                                                                                                       {"start_date": "2026-03-24"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
