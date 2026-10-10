# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-10-10 14:57:16 EDT`
Last slot: `entry_1500`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$83,041.54`
- Portfolio value: `$87,201.54`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  CTSH exit_submitted    regular CTSH261120C00060000         13                 3.7                  3.35          bid_ask_mid                       3.35                    True          4355.0          -455.0              -9.459459                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
    ZS   ZS261120C00200000          2026-10-02         2026-10-05               14.95              17.05          3   630.0   14.046823 take_profit_day1_hit_at_scan
  SOXL SOXL261120C00165000          2026-10-05         2026-10-07               25.75              17.45          1  -830.0  -32.233010        stop_loss_hit_at_scan
   CEG  CEG261120C00300000          2026-10-07         2026-10-08               20.60              21.40          2   160.0    3.883495        stop_loss_hit_at_scan
  CSCO CSCO261120C00115000          2026-10-08         2026-10-09                7.25               8.40          6   690.0   15.862069 take_profit_day1_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-10T14:57:16.103895-04:00     entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T14:52:11.566152-04:00     entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T14:47:07.151783-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T14:42:02.195428-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T14:36:57.573148-04:00    manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T14:31:52.705233-04:00    manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T14:26:47.648753-04:00    manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T13:48:30.618236-04:00    manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T13:43:26.787796-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T13:38:22.867494-04:00    manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T13:33:19.041659-04:00    manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T13:28:15.314022-04:00    manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T13:23:10.942394-04:00    manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T12:26:14.060446-04:00    manage_1230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T11:07:32.098952-04:00    manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T08:05:50.717259-04:00 share_ext_0805 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T05:29:16.995689-04:00 share_ext_0525 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T04:38:21.412519-04:00 share_ext_0435 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T04:33:17.680246-04:00 share_ext_0430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-10T04:28:13.665702-04:00 share_ext_0425 market_closed {"holiday_name": null, "reason": "weekend"}
```