# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-09-19 14:18:39 EDT`
Last slot: `manage_1430`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$78,200.47`
- Portfolio value: `$86,633.47`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
   WMT   open    regular  WMT261023C00108000         18                2.72                 2.755          bid_ask_mid                      2.755                    True          4959.0            63.0               1.286765                   1
  CRWD   open    regular CRWD261023C00240000          3               16.05                14.500          bid_ask_mid                     14.500                    True          4350.0          -465.0              -9.657321                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  SHOP SHOP261016C00155000          2026-08-28         2026-09-09                9.30               2.62          5 -3340.0  -71.827957        stop_loss_hit_at_scan
  CRWD CRWD261016C00210000          2026-09-08         2026-09-09               14.45              12.80          3  -495.0  -11.418685        stop_loss_hit_at_scan
  CRWD CRWD261016C00210000          2026-09-09         2026-09-10               13.00              15.20          3   660.0   16.923077        stop_loss_hit_at_scan
  MSTR MSTR261016C00130000          2026-09-10         2026-09-11               11.70              15.40          4  1480.0   31.623932 take_profit_day1_hit_at_scan
  PYPL PYPL261016C00055000          2026-09-16         2026-09-16                1.27               1.03         39  -936.0  -18.897638        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                      detail
2026-09-19T14:18:39.474506-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T14:13:35.674825-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T14:08:31.810150-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T14:03:27.905557-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:58:24.075669-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:53:20.182511-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:48:16.053516-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:43:11.409613-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:38:07.556779-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:33:03.916944-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:27:59.808710-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:22:55.755308-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:17:51.627686-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:12:47.408942-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:07:43.273394-04:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T13:02:39.187322-04:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T12:57:35.393083-04:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T12:52:31.378778-04:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T12:47:27.437725-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-19T12:42:23.776431-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
```