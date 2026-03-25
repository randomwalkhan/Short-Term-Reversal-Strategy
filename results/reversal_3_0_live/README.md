# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 12:30:01 EDT`
Last processed slot: `manage_1230`

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

## Portfolio Snapshot

- Cash: `$5,455.00`
- Equity: `$10,010.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$10.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                 22.78      318.55        319.64            10.0                   0.22         93.33               30              1.23         48.32           48.19                   39.5
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               22            0.85              1.17        196.56                29.12            True
   WDC           97.06               34            1.25              2.63        299.92                74.01            True
   STX           96.30               27            2.17              6.45        421.45                70.55            True
  CDNS           90.00               40            0.83              1.66        283.61                27.43            True
  ROST           90.00               20            0.76              1.16        215.30                32.83            True
  AMAT           88.89               27            1.44              3.77        372.37                51.46            True
  KLAC           87.88               33            0.98             10.79       1561.57                48.83            True
  SNPS           87.50               24            1.83              5.33        413.33                37.59            True
   BKR           86.67               30            0.66              0.29         63.36                40.11            True
    MU           86.67               15            3.82             10.56        391.00                67.96            True
  CRWD           86.05               43            0.62              1.71        392.26                45.29            True
 CMCSA           84.21               19            1.54              0.31         29.09                27.42            True
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

## Equity Curve

![Reversal 3.0 Live Equity](../../assets/reversal_3_0_live_equity.png)
