# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-31 15:30:05 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$5,722.50`
- Equity: `$9,637.50`
- Realized PnL: `$-632.50`
- Unrealized PnL: `$270.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FANG FANG260515C00195000       2026-03-31                   0               12.15                 13.05      197.37        198.62           270.0                   7.41         100.0               26              0.65         40.69           41.29                  24.45
```

## Today's Closed Trades (2026-03-31)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price   pnl  return_pct                  exit_reason
  FANG FANG260515C00200000          2026-03-30         2026-03-31                11.5               12.8 390.0   11.304348 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  COST           96.30               27            0.80              5.58        994.19                15.57            True
  MDLZ           91.18               34            0.66              0.27         57.64                24.85            True
   LIN           87.50               16            0.88              3.09        497.94                19.51            True
   TRI           83.33               36            1.16              0.74         90.77                42.01            True
   PEP           83.33               18            0.70              0.76        156.49                18.39            True
  FANG          100.00               33            0.03              0.04        198.63                24.45           False
   XEL           93.75               32            0.03              0.02         79.16                18.55           False
   AEP           93.55               31            0.17              0.15        131.05                18.09           False
 CMCSA           91.30               46            0.17              0.03         28.89                29.21           False
   KDP           88.46               26            0.23              0.04         26.43                21.21           False
  CHTR           88.37               43            0.33              0.50        220.72                36.22           False
   EXC           87.50               24            0.44              0.15         49.05                21.45           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                            detail
2026-03-31T15:00:05.885528-04:00   entry_1500        entry {"allocated_cash": 3645.0, "contract_symbol": "FANG260515C00195000", "contracts": 3, "entry_option_price": 12.15, "matched_signals": 26, "success_rate": 100.0, "ticker": "FANG"}
2026-03-31T10:30:05.893788-04:00  manage_1030         exit                                          {"contract_symbol": "FANG260515C00200000", "pnl": 390.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 11.3, "ticker": "FANG"}
2026-03-31T09:30:05.890178-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 97}
2026-03-30T16:00:01.901878-04:00  manage_1600         exit                                                {"contract_symbol": "HON260501C00225000", "pnl": -600.0, "reason": "stop_loss_hit_at_scan", "return_pct": -13.04, "ticker": "HON"}
2026-03-30T15:00:04.861501-04:00   entry_1500        entry  {"allocated_cash": 3450.0, "contract_symbol": "FANG260515C00200000", "contracts": 3, "entry_option_price": 11.5, "matched_signals": 15, "success_rate": 100.0, "ticker": "FANG"}
2026-03-27T15:00:04.241996-04:00   entry_1500        entry     {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                              {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                     {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry  {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                         {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
