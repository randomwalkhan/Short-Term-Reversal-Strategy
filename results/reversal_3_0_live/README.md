# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-27 13:00:06 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$9,577.50`
- Equity: `$9,577.50`
- Realized PnL: `$-422.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-03-27)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
  ABNB ABNB260515C00130000          2026-03-26         2026-03-27                9.85              8.725 -562.5   -11.42132 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               21            0.51              0.80        224.83                24.88            True
  REGN           94.12               17            1.96             10.39        752.28                28.18            True
  INTC           93.94               33            1.76              0.54         43.87                64.25            True
  NVDA           90.91               22            1.44              1.73        170.50                31.98            True
  CTAS           90.32               31            0.65              0.77        168.52                26.37            True
  ORLY           90.00               40            0.62              0.40         92.10                20.62            True
  AVGO           90.00               20            2.15              4.65        307.42                38.20            True
  ASML           88.89               27            0.92              8.53       1325.85                47.14            True
 CMCSA           88.46               26            1.03              0.21         28.63                27.69            True
  GILD           87.50               24            0.85              0.82        136.53                19.20            True
  CDNS           86.67               30            1.59              3.13        279.28                23.06            True
  TSLA           85.71               21            2.37              6.17        369.46                34.39            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                             detail
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                               {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry   {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                           {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                          {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-25T15:00:03.353246-04:00   entry_1500        entry   {"allocated_cash": 4880.0, "contract_symbol": "FANG260515C00195000", "contracts": 4, "entry_option_price": 12.2, "matched_signals": 25, "success_rate": 100.0, "ticker": "FANG"}
2026-03-25T14:34:20.011472-04:00  manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-03-25T09:30:01.175501-04:00 data_refresh data_refresh                                                                                                                                                                      {'saved': 97}
2026-03-24T15:00:05.740108-04:00   entry_1500        entry {"allocated_cash": 4545.0, "contract_symbol": "AVGO260515C00320000", "contracts": 2, "entry_option_price": 22.725, "matched_signals": 30, "success_rate": 93.33, "ticker": "AVGO"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
