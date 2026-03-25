# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-25 14:30:01 EDT`
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
- Equity: `$9,915.00`
- Realized PnL: `$0.00`
- Unrealized PnL: `$-85.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  AVGO AVGO260515C00320000       2026-03-24                   1               22.72                  22.3      318.55        318.87           -85.0                  -1.87         93.33               30              1.23         48.32           47.96                   39.5
```

## Today's Closed Trades (2026-03-25)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               23            0.84              1.17        196.56                29.12            True
   WDC           97.37               38            0.61              1.28        300.50                74.01            True
   STX           97.30               37            0.88              2.62        423.10                70.55            True
  AMAT           91.43               35            0.52              1.35        373.41                51.46            True
  CDNS           90.24               41            0.73              1.45        283.70                27.43            True
  KLAC           89.19               37            0.54              5.97       1563.63                48.83            True
    MU           88.89               18            3.45              9.56        391.43                67.96            True
  SNPS           87.50               24            1.95              5.68        413.18                37.59            True
  CTAS           85.71               21            1.05              1.31        177.57                29.68            True
  CRWD           84.62               26            1.51              4.16        391.21                45.29            True
  CTSH           84.38               32            0.62              0.26         60.13                32.06            True
  BKNG           82.86               35            0.67             20.23       4281.98                41.15            True
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
