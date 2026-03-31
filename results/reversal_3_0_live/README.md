# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-31 09:30:05 EDT`
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

- Cash: `$5,527.50`
- Equity: `$9,022.50`
- Realized PnL: `$-1,022.50`
- Unrealized PnL: `$45.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FANG FANG260515C00200000       2026-03-30                   1                11.5                 11.65       198.7         199.6            45.0                    1.3         100.0               15              1.56         43.31             0.2                  24.78
```

## Today's Closed Trades (2026-03-31)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  ORLY           90.00               50            0.03              0.02         92.10                22.95           False
   EXC           89.29               28            0.10              0.03         49.10                21.45           False
   LIN           88.89               36            0.26              0.92        498.87                19.51           False
  DDOG           88.64               44            0.12              0.09        115.77                54.67           False
  TMUS           86.84               38            0.22              0.34        213.80                19.67           False
   PEP           84.38               32            0.01              0.01        156.82                18.39           False
  INTU           67.39               46            0.40              1.21        428.51                45.64           False
   CEG           66.67                3            7.90             16.51        291.51                62.02           False
  AAPL             NaN                0            0.00              0.00        248.56                16.49           False
  ABNB             NaN                0            0.00              0.00        125.14                36.06           False
  ADBE             NaN                0            0.00              0.00        241.81                42.52           False
   ADI             NaN                0            0.00              0.00        308.98                32.39           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                           detail
2026-03-31T09:30:05.890178-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-30T16:00:01.901878-04:00  manage_1600         exit                                               {"contract_symbol": "HON260501C00225000", "pnl": -600.0, "reason": "stop_loss_hit_at_scan", "return_pct": -13.04, "ticker": "HON"}
2026-03-30T15:00:04.861501-04:00   entry_1500        entry {"allocated_cash": 3450.0, "contract_symbol": "FANG260515C00200000", "contracts": 3, "entry_option_price": 11.5, "matched_signals": 15, "success_rate": 100.0, "ticker": "FANG"}
2026-03-27T15:00:04.241996-04:00   entry_1500        entry    {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                             {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                        {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                         {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
