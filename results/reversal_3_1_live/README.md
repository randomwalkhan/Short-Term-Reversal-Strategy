# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-03-31 23:23:03 EDT`
Last processed slot: `manage_1600`

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

## Today's Closed Trades (2026-03-31)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price   pnl  return_pct                  exit_reason
  FANG FANG260515C00200000          2026-03-30         2026-03-31               11.50               12.8 390.0   11.304348 take_profit_day1_hit_at_scan
  FANG FANG260515C00195000          2026-03-31         2026-03-31               12.15               13.4 375.0   10.288066 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               22            1.08              1.51        198.00                24.73            True
 CMCSA           87.10               31            0.62              0.13         28.85                29.02            True
   LIN           86.36               22            0.69              2.42        498.22                19.67            True
   TRI           83.33               36            1.20              0.76         90.76                41.66            True
  TMUS           83.33               12            1.62              2.42        212.90                20.61            True
   PEP           83.33               12            0.99              1.09        156.35                18.57            True
  MDLZ           93.88               49            0.21              0.08         57.71                25.03           False
  COST           91.84               49            0.01              0.08        996.55                15.56           False
   EXC           89.66               29            0.08              0.03         49.10                21.44           False
   ADP           84.38               32            0.13              0.19        205.39                25.48           False
  CSGP           78.05               41            0.93              0.27         40.77                34.54           False
  PAYX           75.00               24            1.18              0.77         92.79                31.19           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-03-31T23:23:03.138021-04:00  manage_1600 slot_skipped                                                                                                                                                   {"reason": "already_processed"}
2026-03-31T23:23:03.138021-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 99}
2026-03-31T16:00:05.906472-04:00  manage_1600         exit                                         {"contract_symbol": "FANG260515C00195000", "pnl": 375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 10.29, "ticker": "FANG"}
2026-03-31T15:00:05.885528-04:00   entry_1500        entry {"allocated_cash": 3645.0, "contract_symbol": "FANG260515C00195000", "contracts": 3, "entry_option_price": 12.15, "matched_signals": 26, "success_rate": 100.0, "ticker": "FANG"}
2026-03-31T10:30:05.893788-04:00  manage_1030         exit                                          {"contract_symbol": "FANG260515C00200000", "pnl": 390.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 11.3, "ticker": "FANG"}
2026-03-31T09:30:05.890178-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 97}
2026-03-30T16:00:01.901878-04:00  manage_1600         exit                                                {"contract_symbol": "HON260501C00225000", "pnl": -600.0, "reason": "stop_loss_hit_at_scan", "return_pct": -13.04, "ticker": "HON"}
2026-03-30T15:00:04.861501-04:00   entry_1500        entry  {"allocated_cash": 3450.0, "contract_symbol": "FANG260515C00200000", "contracts": 3, "entry_option_price": 11.5, "matched_signals": 15, "success_rate": 100.0, "ticker": "FANG"}
2026-03-27T15:00:04.241996-04:00   entry_1500        entry     {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                              {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)
