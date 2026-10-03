# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-10-03 11:10:52 EDT`
Last slot: `manage_1100`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$82,718.38`
- Portfolio value: `$86,978.38`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode   contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
    ZS   open    regular ZS261120C00200000          3               14.95                  14.9          bid_ask_mid                       14.9                    True          4470.0           -15.0              -0.334448                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  MSTR MSTR261120C00160000          2026-09-25         2026-09-28               17.35              15.40          2  -390.0  -11.239193        stop_loss_hit_at_scan
  META META261120C00735000          2026-09-30         2026-10-01               48.80              43.15          1  -565.0  -11.577869        stop_loss_hit_at_scan
  MSTR MSTR261120C00155000          2026-09-29         2026-10-01               16.05              18.80          3   825.0   17.133956 take_profit_day2_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                      detail
2026-10-03T11:10:52.188548-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T11:05:48.796205-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T11:00:45.227699-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:55:41.557209-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:50:37.988822-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:45:34.470419-04:00 early_entry_1045 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:40:30.729920-04:00      manage_1030 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:35:26.245815-04:00      manage_1030 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:30:22.805468-04:00      manage_1030 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:25:18.860322-04:00      manage_1030 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:20:15.527546-04:00      manage_1030 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:15:12.108429-04:00 early_entry_1015 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:10:08.842162-04:00      manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:05:05.309155-04:00      manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T10:00:01.618411-04:00      manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T09:54:58.199498-04:00      manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T09:49:54.934199-04:00      manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T09:44:51.640505-04:00           manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T09:39:48.026679-04:00      manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-03T09:34:44.449551-04:00      manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
```