# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-27 16:00:06 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$4,977.50`
- Equity: `$9,477.50`
- Realized PnL: `$-422.50`
- Unrealized PnL: `$-100.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260501C00225000       2026-03-27                   0                 9.2                   9.0      223.64        223.12          -100.0                  -2.17         100.0               20              0.68         39.47            38.9                  24.88
```

## Today's Closed Trades (2026-03-27)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
  ABNB ABNB260515C00130000          2026-03-26         2026-03-27                9.85              8.725 -562.5   -11.42132 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               17            0.91              1.43        224.56                24.88            True
   STX           94.74               38            0.74              1.95        377.95                75.37            True
  NVDA           93.75               16            2.24              2.69        170.09                31.98            True
  INTC           93.10               29            2.13              0.66         43.82                64.25            True
  CDNS           90.00               10            3.15              6.20        277.96                23.06            True
  REGN           90.00               10            2.51             13.31        751.02                28.18            True
  GILD           90.00               10            1.92              1.84        136.09                19.20            True
  AVGO           87.50               16            2.82              6.11        306.79                38.20            True
 CMCSA           85.71               21            1.36              0.27         28.60                27.69            True
   LIN           85.71               14            0.88              3.06        494.18                19.13            True
  PLTR           85.00               20            3.05              3.15        146.21                48.38            True
  MRVL           85.00               20            2.87              1.96         96.84                74.63            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                           detail
2026-03-27T15:00:04.241996-04:00   entry_1500        entry    {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                             {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                         {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                        {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-25T15:00:03.353246-04:00   entry_1500        entry {"allocated_cash": 4880.0, "contract_symbol": "FANG260515C00195000", "contracts": 4, "entry_option_price": 12.2, "matched_signals": 25, "success_rate": 100.0, "ticker": "FANG"}
2026-03-25T14:34:20.011472-04:00  manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-03-25T09:30:01.175501-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
