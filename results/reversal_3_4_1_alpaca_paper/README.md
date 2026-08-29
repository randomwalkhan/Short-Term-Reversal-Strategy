# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-08-29 09:33:10 EDT`
Last slot: `manage_0930`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$85,898.13`
- Portfolio value: `$90,173.13`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  SHOP   open    regular SHOP261016C00155000          5                 9.3                   9.1          bid_ask_mid                        9.1                    True          4550.0          -100.0              -2.150538                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  AAPL AAPL260821C00315000          2026-07-14         2026-07-15               11.60              16.60          4  2000.0   43.103448 take_profit_day1_hit_at_scan
  META META260821C00660000          2026-07-13         2026-07-15               47.35              55.90          1   855.0   18.057022 take_profit_day2_hit_at_scan
   TXN  TXN260821C00290000          2026-07-17         2026-07-21               21.05              24.00          2   590.0   14.014252 take_profit_day2_hit_at_scan
  AAPL AAPL260821C00330000          2026-07-20         2026-07-22               10.70               9.45          4  -500.0  -11.682243        stop_loss_hit_at_scan
  PYPL PYPL260821C00055000          2026-07-21         2026-07-23                3.15               2.60         15  -825.0  -17.460317        stop_loss_hit_at_scan
  PYPL PYPL260821C00055000          2026-07-22         2026-07-23                3.25               2.98         15  -405.0   -8.307692        stop_loss_hit_at_scan
  GILD GILD260918C00130000          2026-07-24         2026-07-27                6.70               8.05          7   945.0   20.149254 take_profit_day1_hit_at_scan
   CSX  CSX260918C00052500          2026-07-28         2026-07-29                1.45               1.25         34  -680.0  -13.793103        stop_loss_hit_at_scan
  FAST FAST260918C00045000          2026-07-29         2026-07-29                4.00               3.50         12  -600.0  -12.500000        stop_loss_hit_at_scan
  PYPL PYPL260918C00057500          2026-07-30         2026-07-31                2.92               2.32         16  -960.0  -20.547945        stop_loss_hit_at_scan
   CSX  CSX260918C00050000          2026-08-03         2026-08-04                1.70               1.65         29  -145.0   -2.941176        stop_loss_hit_at_scan
  INTC INTC260918C00100000          2026-08-06         2026-08-07               11.35              10.55          4  -320.0   -7.048458        stop_loss_hit_at_scan
  PYPL PYPL260918C00060000          2026-08-07         2026-08-10                1.71               1.51         28  -560.0  -11.695906        stop_loss_hit_at_scan
  LRCX LRCX260918C00310000          2026-08-10         2026-08-12               27.25              34.05          1   680.0   24.954128 take_profit_day2_hit_at_scan
  PYPL PYPL260918C00057500          2026-08-12         2026-08-13                2.86               3.65         17  1343.0   27.622378 take_profit_day1_hit_at_scan
  AMZN AMZN260918C00265000          2026-08-13         2026-08-17               10.75               8.00          4 -1100.0  -25.581395        stop_loss_hit_at_scan
  ALNY ALNY260918C00220000          2026-08-17         2026-08-19               14.20              17.60          3  1020.0   23.943662 take_profit_day1_hit_at_scan
  LRCX LRCX261016C00310000          2026-08-24         2026-08-27               31.15              30.90          1   -25.0   -0.802568        time_exit_at_4pm_scan
  MNST MNST261016C00048000          2026-08-26         2026-08-27                1.95               1.05         25 -2250.0  -46.153846        stop_loss_hit_at_scan
  MRVL MRVL261016C00240000          2026-08-27         2026-08-28               20.25              15.45          1  -480.0  -23.703704        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-29T09:33:10.862131-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T09:28:06.989999-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T09:23:02.815931-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T09:17:58.704723-04:00 share_ext_0915 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T09:12:54.447805-04:00 share_ext_0910 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T09:07:50.565905-04:00 share_ext_0905 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T09:02:46.467986-04:00 share_ext_0900 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:57:42.455361-04:00 share_ext_0855 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:52:38.427928-04:00 share_ext_0850 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:47:34.363380-04:00 share_ext_0845 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:42:30.285964-04:00 share_ext_0840 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:37:26.161478-04:00 share_ext_0835 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:32:22.173440-04:00 share_ext_0830 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:27:17.868319-04:00 share_ext_0825 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:22:13.950870-04:00 share_ext_0820 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:17:09.903464-04:00 share_ext_0815 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:12:06.014612-04:00 share_ext_0810 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:07:01.749502-04:00 share_ext_0805 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T08:01:57.711689-04:00 share_ext_0800 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-29T07:56:53.608683-04:00 share_ext_0755 market_closed {"holiday_name": null, "reason": "weekend"}
```