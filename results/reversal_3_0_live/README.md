# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-27 09:30:06 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart view: default display is trailing `1W`, with latest ET checkpoint annotation and return % axis

## Portfolio Snapshot

- Cash: `$5,215.00`
- Equity: `$10,215.00`
- Realized PnL: `$140.00`
- Unrealized PnL: `$75.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  ABNB ABNB260515C00130000       2026-03-26                   1                9.85                  10.0      130.79         129.7            75.0                   1.52         94.29               35              0.77         51.93             0.2                  28.73
```

## Today's Closed Trades (2026-03-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC           93.94               33            1.56              0.48         43.89                64.25            True
  ABNB           93.55               31            1.23              1.13        130.58                28.75            True
  SBUX           93.33               15            1.55              0.99         90.80                29.92            True
  AVGO           92.31               39            0.95              2.05        308.54                38.20            True
  DXCM           91.67               36            1.18              0.55         65.86                25.75            True
  NVDA           91.67               36            0.57              0.69        170.95                31.98            True
  ROST           91.67               24            0.59              0.88        213.92                32.94            True
  FTNT           91.67               12            2.78              1.58         80.35                27.82            True
  CTAS           90.91               33            0.52              0.61        168.59                26.37            True
  ASML           90.62               32            0.56              5.25       1327.25                47.14            True
  FAST           90.00               30            0.71              0.22         45.01                20.37            True
  SNPS           89.74               39            0.69              1.94        401.12                31.55            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry   {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                           {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                          {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-25T15:00:03.353246-04:00   entry_1500        entry   {"allocated_cash": 4880.0, "contract_symbol": "FANG260515C00195000", "contracts": 4, "entry_option_price": 12.2, "matched_signals": 25, "success_rate": 100.0, "ticker": "FANG"}
2026-03-25T14:34:20.011472-04:00  manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-25T09:30:01.175501-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-24T15:00:05.740108-04:00   entry_1500        entry {"allocated_cash": 4545.0, "contract_symbol": "AVGO260515C00320000", "contracts": 2, "entry_option_price": 22.725, "matched_signals": 30, "success_rate": 93.33, "ticker": "AVGO"}
2026-03-24T13:30:05.751589-04:00  manage_1330 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
