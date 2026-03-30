# Reversal 3.0 Live Paper Test

Last updated (ET): `2026-03-30 16:00:01 EDT`
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

- Cash: `$5,527.50`
- Equity: `$8,872.50`
- Realized PnL: `$-1,022.50`
- Unrealized PnL: `$-105.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FANG FANG260515C00200000       2026-03-30                   0                11.5                 11.15       198.7        198.65          -105.0                  -3.04         100.0               15              1.56         43.31           42.31                  24.78
```

## Today's Closed Trades (2026-03-30)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
   HON HON260501C00225000          2026-03-27         2026-03-30                 9.2                8.0 -600.0  -13.043478 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               15            1.58              2.23        200.88                24.78            True
  DXCM           93.18               44            0.56              0.25         62.14                32.07            True
  INTC           91.67               12            4.55              1.37         42.54                64.48            True
  NVDA           90.91               22            1.47              1.73        166.78                32.71            True
  AVGO           88.89               18            2.43              5.11        298.49                39.28            True
  PLTR           86.67               15            3.86              3.87        141.40                49.53            True
  TSLA           86.36               22            1.89              4.78        359.78                35.33            True
   STX           84.62               13            4.66             12.40        374.75                75.41            True
  MCHP           84.62               13            3.13              1.36         61.42                36.06            True
   AMD           81.82               22            2.87              4.05        200.25                56.13            True
  MNST           80.00               30            0.71              0.36         71.68                27.35            True
   TXN           80.00               15            2.05              2.74        189.16                29.79            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                                           detail
2026-03-30T16:00:01.901878-04:00  manage_1600         exit                                               {"contract_symbol": "HON260501C00225000", "pnl": -600.0, "reason": "stop_loss_hit_at_scan", "return_pct": -13.04, "ticker": "HON"}
2026-03-30T15:00:04.861501-04:00   entry_1500        entry {"allocated_cash": 3450.0, "contract_symbol": "FANG260515C00200000", "contracts": 3, "entry_option_price": 11.5, "matched_signals": 15, "success_rate": 100.0, "ticker": "FANG"}
2026-03-27T15:00:04.241996-04:00   entry_1500        entry    {"allocated_cash": 4600.0, "contract_symbol": "HON260501C00225000", "contracts": 5, "entry_option_price": 9.2, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-03-27T10:00:06.175720-04:00  manage_1000         exit                                             {"contract_symbol": "ABNB260515C00130000", "pnl": -562.5, "reason": "stop_loss_hit_at_scan", "return_pct": -11.42, "ticker": "ABNB"}
2026-03-27T09:30:06.387888-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-26T15:00:01.983935-04:00   entry_1500        entry {"allocated_cash": 4925.0, "contract_symbol": "ABNB260515C00130000", "contracts": 5, "entry_option_price": 9.85, "matched_signals": 35, "success_rate": 94.29, "ticker": "ABNB"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                         {"contract_symbol": "AVGO260515C00320000", "pnl": -540.0, "reason": "stop_scan", "return_pct": -11.88, "ticker": "AVGO"}
2026-03-26T10:30:00.722036-04:00  manage_1030         exit                                                        {"contract_symbol": "FANG260515C00195000", "pnl": 680.0, "reason": "tp_day1_scan", "return_pct": 13.93, "ticker": "FANG"}
2026-03-26T09:30:05.730919-04:00 data_refresh data_refresh                                                                                                                                                                    {'saved': 97}
2026-03-25T15:00:03.353246-04:00   entry_1500        entry {"allocated_cash": 4880.0, "contract_symbol": "FANG260515C00195000", "contracts": 4, "entry_option_price": 12.2, "matched_signals": 25, "success_rate": 100.0, "ticker": "FANG"}
```

## Equity Curve (1W)

Trailing `1W` window. The latest point is annotated with its exact ET checkpoint time and return %. The right axis shows total return versus the $10,000 start.

![Reversal 3.0 Live Equity 1W](../../assets/reversal_3_0_live_equity.png)
