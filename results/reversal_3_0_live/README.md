# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 13:06:33 EDT`
Last processed slot: `manual_refresh`

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
- Equity: `$9,920.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$-80.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                 22.32      318.55        319.28           -80.0                  -1.76         93.33               30              1.23         48.32           47.55                   39.5
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               29            0.54              0.75        196.74                29.12            True
   WDC           96.88               32            1.94              4.09        299.30                74.01            True
   STX           95.83               24            2.73              8.12        420.74                70.55            True
  KLAC           90.00               30            1.29             14.09       1560.15                48.83            True
  CDNS           89.74               39            0.93              1.84        283.53                27.43            True
  AMAT           88.46               26            1.50              3.93        372.30                51.46            True
   BKR           86.67               30            0.68              0.30         63.36                40.11            True
  CRWD           85.71               42            0.78              2.15        392.07                45.29            True
  SNPS           85.71               28            1.60              4.65        413.63                37.59            True
  CTAS           85.00               20            1.09              1.37        177.54                29.68            True
  CTSH           83.87               31            0.68              0.29         60.12                32.06            True
  BKNG           83.78               37            0.61             18.24       4282.83                41.15            True
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
