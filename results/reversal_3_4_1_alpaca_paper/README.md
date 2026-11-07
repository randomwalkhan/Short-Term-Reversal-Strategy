# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-11-07 14:22:44 EST`
Last slot: `manage_1430`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$77,138.67`
- Portfolio value: `$79,688.67`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  MDLZ exit_submitted    regular MDLZ261218C00065000         15                 3.2                   2.5          bid_ask_mid                        2.5                    True          3750.0         -1050.0                -21.875                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  META META261120C00735000          2026-09-30         2026-10-01               48.80              43.15          1  -565.0  -11.577869        stop_loss_hit_at_scan
  MSTR MSTR261120C00155000          2026-09-29         2026-10-01               16.05              18.80          3   825.0   17.133956 take_profit_day2_hit_at_scan
    ZS   ZS261120C00200000          2026-10-02         2026-10-05               14.95              17.05          3   630.0   14.046823 take_profit_day1_hit_at_scan
  SOXL SOXL261120C00165000          2026-10-05         2026-10-07               25.75              17.45          1  -830.0  -32.233010        stop_loss_hit_at_scan
   CEG  CEG261120C00300000          2026-10-07         2026-10-08               20.60              21.40          2   160.0    3.883495        stop_loss_hit_at_scan
  CSCO CSCO261120C00115000          2026-10-08         2026-10-09                7.25               8.40          6   690.0   15.862069 take_profit_day1_hit_at_scan
  CTSH CTSH261120C00060000          2026-10-09         2026-10-12                3.70               3.30         13  -520.0  -10.810811        stop_loss_hit_at_scan
   CEG  CEG261120C00290000          2026-10-12         2026-10-13               18.70              21.30          2   520.0   13.903743 take_profit_day1_hit_at_scan
  SNPS SNPS261120C00500000          2026-10-13         2026-10-14               25.50              20.00          1  -550.0  -21.568627        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-15         2026-10-16               19.50              17.10          2  -480.0  -12.307692        stop_loss_hit_at_scan
  CSCO CSCO261120C00115000          2026-10-14         2026-10-19                5.85               2.96          8 -2312.0  -49.401709        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-16         2026-10-19               17.10              14.00          2  -620.0  -18.128655        stop_loss_hit_at_scan
   ADP  ADP261120C00290000          2026-10-19         2026-10-20                9.70              10.80          5   550.0   11.340206 take_profit_day1_hit_at_scan
  TEAM TEAM261120C00230000          2026-10-22         2026-10-23               18.80              16.70          2  -420.0  -11.170213        stop_loss_hit_at_scan
   WMT  WMT261127C00119000          2026-10-27         2026-10-28                4.65               3.70         10  -950.0  -20.430108        stop_loss_hit_at_scan
  MSTR MSTR261218C00140000          2026-10-28         2026-10-30               15.50               8.80          3 -2010.0  -43.225806        stop_loss_hit_at_scan
   CEG  CEG261218C00260000          2026-10-30         2026-11-02               19.70              22.60          2   580.0   14.720812 take_profit_day1_hit_at_scan
   CEG  CEG261218C00260000          2026-11-02         2026-11-03               18.20              21.00          2   560.0   15.384615 take_profit_day1_hit_at_scan
  MDLZ MDLZ261218C00067500          2026-11-03         2026-11-04                1.40               1.65         35   875.0   17.857143 take_profit_day1_hit_at_scan
  ORLY ORLY261218C00095000          2026-11-05         2026-11-05                2.00               1.55         25 -1125.0  -22.500000        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                      detail
2026-11-07T14:22:44.321250-05:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T14:17:39.665611-05:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T14:12:35.166531-05:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T14:07:30.968887-05:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T14:02:27.001654-05:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:57:22.746220-05:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:52:18.783756-05:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:47:14.820062-05:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:42:10.873552-05:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:37:06.930611-05:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:32:02.952349-05:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:26:58.450219-05:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:21:53.802254-05:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:16:49.604145-05:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:11:44.911690-05:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:06:40.829830-05:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T13:01:36.283171-05:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T12:56:32.017465-05:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T12:51:27.544006-05:00 manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-11-07T12:46:22.868928-05:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
```