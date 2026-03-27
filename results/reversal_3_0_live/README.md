# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-27 14:30:06 EDT`
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
   HON          100.00               20            0.69              1.09        224.70                24.88            True
  INTC           96.15               26            2.40              0.74         43.78                64.25            True
  NVDA           94.44               18            1.87              2.25        170.28                31.98            True
  REGN           93.75               16            2.01             10.66        752.16                28.18            True
  AVGO           91.30               23            1.99              4.31        307.57                38.20            True
  AMAT           91.18               34            0.80              1.91        337.73                54.88            True
  KLAC           89.47               38            0.51              5.16       1448.92                53.70            True
  MPWR           88.89               36            0.86              6.38       1055.54                45.70            True
  GILD           86.96               23            0.94              0.90        136.49                19.20            True
  ORLY           86.21               29            1.07              0.69         91.97                20.62            True
  CHTR           86.11               36            0.73              1.11        218.03                37.58            True
   AMD           85.71               35            1.16              1.65        203.06                56.22            True
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
