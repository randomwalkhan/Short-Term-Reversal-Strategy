# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-09-26 10:03:22 EDT`
Last slot: `manage_1000`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$83,864.29`
- Portfolio value: `$87,234.29`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  MSTR   open    regular MSTR261120C00160000          2               17.35                  17.0          bid_ask_mid                       17.0                    True          3400.0           -70.0              -2.017291                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
   WMT  WMT261023C00108000          2026-09-17         2026-09-21                2.72               2.25         18  -846.0  -17.279412        stop_loss_hit_at_scan
  CRWD CRWD261023C00240000          2026-09-18         2026-09-21               16.05              16.95          3   270.0    5.607477        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-09-26T10:03:22.088624-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:58:16.894562-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:53:11.098970-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:48:05.722069-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:42:59.951201-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:37:54.850008-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:32:50.528050-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:27:46.496528-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:22:42.424006-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:17:38.583609-04:00 share_ext_0915 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T09:12:34.422854-04:00 share_ext_0910 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:50:53.387553-04:00 share_ext_0850 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:45:47.733739-04:00 share_ext_0845 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:40:43.450765-04:00 share_ext_0840 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:35:39.608523-04:00 share_ext_0835 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:30:35.593128-04:00 share_ext_0830 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:25:31.572598-04:00 share_ext_0825 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:20:27.702302-04:00 share_ext_0820 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:15:23.694917-04:00 share_ext_0815 market_closed {"holiday_name": null, "reason": "weekend"}
2026-09-26T08:10:20.028219-04:00 share_ext_0810 market_closed {"holiday_name": null, "reason": "weekend"}
```