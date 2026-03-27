# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-27 14:00:06 EDT`
Last processed slot: `manage_1400`

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
  INTC           96.43               28            2.21              0.68         43.81                64.25            True
  NVDA           94.44               18            1.92              2.30        170.25                31.98            True
  REGN           94.12               17            1.96             10.39        752.28                28.18            True
  AMAT           91.18               34            0.72              1.70        337.82                54.88            True
  MPWR           88.89               36            0.80              5.96       1055.73                45.70            True
  ORLY           88.57               35            0.75              0.49         92.06                20.62            True
  CTAS           88.46               26            0.91              1.07        168.39                26.37            True
  GILD           88.46               26            0.78              0.75        136.56                19.20            True
 CMCSA           88.00               25            1.15              0.23         28.62                27.69            True
  TSLA           87.50               16            3.27              8.51        368.46                34.39            True
  AVGO           87.50               16            2.73              5.91        306.88                38.20            True
   LIN           86.96               23            0.62              2.13        494.58                19.13            True
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
