# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 14:34:20 EDT`
Last processed slot: `manage_1430`

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
- Equity: `$9,885.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$-115.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                 22.15      318.55        318.98          -115.0                  -2.53         93.33               30              1.23         48.32           47.68                   39.5
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               26            0.70              0.96        196.65                29.12            True
   STX           97.30               37            0.97              2.88        422.99                70.55            True
   WDC           97.14               35            0.92              1.93        300.22                74.01            True
  AMAT           91.18               34            0.63              1.66        373.28                51.46            True
  CDNS           90.00               40            0.81              1.61        283.63                27.43            True
  KLAC           89.19               37            0.64              6.97       1563.20                48.83            True
    MU           88.89               18            3.42              9.46        391.48                67.96            True
  SNPS           87.50               24            1.86              5.41        413.30                37.59            True
   BKR           87.10               31            0.57              0.25         63.38                40.11            True
 CMCSA           84.21               19            1.57              0.32         29.08                27.42            True
  CRWD           84.00               25            1.56              4.28        391.15                45.29            True
  CTSH           83.33               30            0.69              0.29         60.12                32.06            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
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
