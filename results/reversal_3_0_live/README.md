# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-31 16:00:05 EDT`
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
 CMCSA           86.67               30            0.66              0.13         28.84                29.21            True
   LIN           86.36               22            0.70              2.45        498.21                19.51            True
   TRI           83.33               36            1.22              0.78         90.76                42.01            True
   PEP           83.33               12            0.98              1.07        156.36                18.39            True
  TMUS           81.82               11            1.83              2.74        212.77                19.67            True
  FANG          100.00               29            0.43              0.60        198.39                24.45           False
   AEP           94.29               35            0.02              0.02        131.11                18.09           False
  MDLZ           94.00               50            0.19              0.08         57.72                24.85           False
  COST           91.84               49            0.00              0.02        996.57                15.57           False
  CTAS           90.91               44            0.08              0.10        168.62                28.24           False
   EXC           88.89               27            0.18              0.06         49.08                21.45           False
   KDP           85.71               21            0.45              0.08         26.41                21.21           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-03-31T16:00:05.906472-04:00  manage_1600         exit                                         {"contract_symbol": "FANG260515C00195000", "pnl": 375.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 10.29, "ticker": "FANG"}
2026-03-31T15:00:05.885528-04:00   entry_1500        entry {"allocated_cash": 3645.0, "contract_symbol": "FANG260515C00195000", "contracts": 3, "entry_option_price": 12.15, "matched_signals": 26, "success_rate": 100.0, "ticker": "FANG"}
2026-03-31T10:30:05.893788-04:00  manage_1030         exit                                          {"contract_symbol": "FANG260515C00200000", "pnl": 390.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 11.3, "ticker": "FANG"}
2026-03-31T09:30:05.890178-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 97}
2026-03-30T16:00:01.901878-04:00  manage_1600         exit                                                {"contract_symbol": "HON260501C00225000", "pnl": -600.0, "reason": "stop_loss_hit_at_scan", "return_pct": -13.04, "ticker": "HON"}
2026-03-30T15:00:04.861501-04:00   entry_1500        entry  {"allocated_cash": 3450.0, "contract_symbol": "FANG260515C00200000", "contracts": 3, "entry_option_price": 11.5, "matched_signals": 15, "success_rate": 100.0, "ticker": "FANG"}
2026-03-27T15:00:04.241996-04:00   entry_1500        entry     {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                              {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry  {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
