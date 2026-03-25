# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 13:30:01 EDT`
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
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                 23.12      318.55        319.61            80.0                   1.76         93.33               30              1.23         48.32           49.08                   39.5
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               22            0.95              1.32        196.50                29.12            True
   WDC           97.06               34            1.38              2.91        299.80                74.01            True
   STX           96.15               26            2.37              7.03        421.21                70.55            True
  CDNS           90.24               41            0.78              1.56        283.65                27.43            True
  KLAC           90.00               30            1.29             14.09       1560.15                48.83            True
  CTAS           89.29               28            0.69              0.86        177.76                29.68            True
  SNPS           87.50               32            1.27              3.69        414.04                37.59            True
  AMAT           86.36               22            1.88              4.92        371.88                51.46            True
  CTSH           86.11               36            0.51              0.21         60.15                32.06            True
  CHTR           85.71               35            0.80              1.22        217.08                38.80            True
    MU           85.71               14            3.91             10.82        390.89                67.96            True
 CMCSA           85.00               20            1.44              0.29         29.09                27.42            True
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
