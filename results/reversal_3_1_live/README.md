# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-01 09:30:00 EDT`
Last processed slot: `manage_0930`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
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

- Cash: `$9,742.50`
- Equity: `$9,742.50`
- Realized PnL: `$-257.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-01)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               20            1.42              1.96        196.95                24.73            True
  FTNT           92.86               28            1.60              0.92         81.33                30.40            True
   LIN           88.46               26            0.57              1.98        494.91                19.67            True
   KDP           87.50               16            0.80              0.15         26.27                19.96            True
 CMCSA           85.19               27            0.86              0.17         28.31                29.02            True
   EXC           83.33               18            0.69              0.24         48.92                21.40            True
  CHTR           82.76               29            1.37              2.07        214.99                36.72            True
   BKR           81.82               22            1.15              0.49         60.84                41.31            True
  FAST           93.62               47            0.05              0.02         46.39                22.75           False
   XEL           93.33               30            0.20              0.11         79.39                18.50           False
   WMT           92.31               39            0.36              0.31        124.14                21.00           False
   AEP           92.31               26            0.37              0.34        130.93                17.74           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-04-01T09:30:00.773757-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 99}
2026-03-31T23:23:03.138021-04:00  manage_1600 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-03-31T23:23:03.138021-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 99}
2026-03-31T16:00:05.906472-04:00  manage_1600         exit                                         {"contract_symbol": "FANG260515C00195000", "pnl": 375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 10.29, "ticker": "FANG"}
2026-03-31T15:00:05.885528-04:00   entry_1500        entry {"allocated_cash": 3645.0, "contract_symbol": "FANG260515C00195000", "contracts": 3, "entry_option_price": 12.15, "matched_signals": 26, "success_rate": 100.0, "ticker": "FANG"}
2026-03-31T10:30:05.893788-04:00  manage_1030         exit                                          {"contract_symbol": "FANG260515C00200000", "pnl": 390.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 11.3, "ticker": "FANG"}
2026-03-31T09:30:05.890178-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 97}
2026-03-30T16:00:01.901878-04:00  manage_1600         exit                                                {"contract_symbol": "HON260501C00225000", "pnl": -600.0, "reason": "stop_loss_hit_at_scan", "return_pct": -13.04, "ticker": "HON"}
2026-03-30T15:00:04.861501-04:00   entry_1500        entry  {"allocated_cash": 3450.0, "contract_symbol": "FANG260515C00200000", "contracts": 3, "entry_option_price": 11.5, "matched_signals": 15, "success_rate": 100.0, "ticker": "FANG"}
2026-03-27T15:00:04.241996-04:00   entry_1500        entry     {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
