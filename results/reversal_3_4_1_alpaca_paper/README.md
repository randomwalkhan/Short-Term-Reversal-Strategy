# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-09-21 10:13:13 EDT`
Last slot: `early_entry_1010`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$87,334.95`
- Portfolio value: `$87,334.95`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

_None_

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
                    timestamp_et             slot           event_type                                                                                                                                                                             detail
2026-09-21T10:13:13.960867-04:00 early_entry_1010   early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:07:05.437132-04:00 early_entry_1005   early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T10:00:58.816515-04:00 early_entry_1000   early_entry_shadow                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-09-21T09:55:54.956965-04:00             exit          exit_filled                                                 {"contract_symbol": "CRWD261023C00240000", "exit_price": 16.95, "pnl": 270.0, "reason": "stop_loss_hit_at_scan", "ticker": "CRWD"}
2026-09-21T09:55:54.956965-04:00             exit          exit_filled                                                   {"contract_symbol": "WMT261023C00108000", "exit_price": 2.25, "pnl": -846.0, "reason": "stop_loss_hit_at_scan", "ticker": "WMT"}
2026-09-21T09:50:50.062614-04:00      manage_1000 exit_order_submitted {"alpaca_order_id": "f04068b1-12c0-4a13-bf4f-ad1cf6b944a7", "contract_symbol": "CRWD261023C00240000", "limit_price": "13.00", "reason": "stop_loss_hit_at_scan", "ticker": "CRWD"}
2026-09-21T09:50:50.062614-04:00      manage_1000 exit_order_submitted    {"alpaca_order_id": "f50333c7-1418-46bc-be04-9cbbdd2d981e", "contract_symbol": "WMT261023C00108000", "limit_price": "2.23", "reason": "stop_loss_hit_at_scan", "ticker": "WMT"}
2026-09-20T23:58:24.765158-04:00   share_ext_2355        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:53:21.172737-04:00   share_ext_2350        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:48:17.392950-04:00   share_ext_2345        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:43:13.532990-04:00   share_ext_2340        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:38:09.741280-04:00   share_ext_2335        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:33:05.997863-04:00   share_ext_2330        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:28:02.132123-04:00   share_ext_2325        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:22:58.180654-04:00   share_ext_2320        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:17:54.313820-04:00   share_ext_2315        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:12:50.714148-04:00   share_ext_2310        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:07:46.825587-04:00   share_ext_2305        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T23:02:43.025780-04:00   share_ext_2300        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
2026-09-20T22:57:39.270094-04:00   share_ext_2255        market_closed                                                                                                                                        {"holiday_name": null, "reason": "weekend"}
```