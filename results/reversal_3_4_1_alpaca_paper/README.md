# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-06-27 15:58:28 EDT`
Last slot: `manage_1600`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$90,534.82`
- Portfolio value: `$94,359.82`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  DRAM   open    regular DRAM260731C00073000          5                 8.9                 8.275          bid_ask_mid                      8.275                    True          4137.5          -312.5              -7.022472                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  INTC INTC260618C00115000          2026-05-14         2026-05-15               13.30               8.75          3 -1365.0  -34.210526        stop_loss_hit_at_scan
  SNPS SNPS260618C00490000          2026-05-13         2026-05-15               46.20              39.90          1  -630.0  -13.636364        stop_loss_hit_at_scan
  INTC INTC260618C00110000          2026-05-18         2026-05-18                9.40               8.65          5  -375.0   -7.978723        stop_loss_hit_at_scan
  PANW PANW260618C00250000          2026-05-19         2026-05-20               16.05              13.65          3  -720.0  -14.953271        stop_loss_hit_at_scan
  TTWO TTWO260717C00240000          2026-05-20         2026-05-21               17.00              19.00          2   400.0   11.764706 take_profit_day1_hit_at_scan
  SBUX SBUX260717C00105000          2026-05-22         2026-05-26                3.75               3.35         13  -520.0  -10.666667        stop_loss_hit_at_scan
  INTC INTC260626C00117000          2026-05-21         2026-05-27               13.45              15.15          3   510.0   12.639405        time_exit_at_4pm_scan
  PANW PANW260717C00260000          2026-05-26         2026-05-27               20.45              14.80          2 -1130.0  -27.628362        stop_loss_hit_at_scan
  AVGO AVGO260717C00420000          2026-05-28         2026-05-29               33.40              47.35          1  1395.0   41.766467 take_profit_day1_hit_at_scan
  MRVL MRVL260717C00200000          2026-05-29         2026-06-01               26.00              31.75          1   575.0   22.115385 take_profit_day1_hit_at_scan
  CHTR CHTR260717C00150000          2026-06-01         2026-06-01                8.80               8.00          5  -400.0   -9.090909        stop_loss_hit_at_scan
  AMZN AMZN260717C00260000          2026-06-02         2026-06-04               10.90               8.40          4 -1000.0  -22.935780        stop_loss_hit_at_scan
  FTNT FTNT260717C00155000          2026-06-03         2026-06-04                6.60               7.40          7   560.0   12.121212 take_profit_day1_hit_at_scan
  TEAM TEAM260717C00100000          2026-06-08         2026-06-09                9.00               8.50          5  -250.0   -5.555556        stop_loss_hit_at_scan
  PAYX PAYX260717C00100000          2026-06-11         2026-06-12                5.50               4.40          9  -990.0  -20.000000        stop_loss_hit_at_scan
  ROST ROST260717C00240000          2026-06-15         2026-06-16                5.60               4.80          8  -640.0  -14.285714        stop_loss_hit_at_scan
  DRAM DRAM260717C00069000          2026-06-16         2026-06-17                7.60               8.15          6   330.0    7.236842        stop_loss_hit_at_scan
   WMT  WMT260724C00120000          2026-06-18         2026-06-23                2.65               3.55         18  1620.0   33.962264 take_profit_day2_hit_at_scan
  MRVL MRVL260724C00310000          2026-06-22         2026-06-23               35.45              22.45          1 -1300.0  -36.671368        stop_loss_hit_at_scan
  AVGO AVGO260821C00380000          2026-06-25         2026-06-26               30.20              23.85          1  -635.0  -21.026490        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                      detail
2026-06-27T15:58:28.512703-04:00 manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:53:24.955511-04:00 manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:48:21.376086-04:00 manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:43:17.711415-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:38:14.272983-04:00 manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:33:10.524573-04:00 manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:28:06.947582-04:00 manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:23:03.413509-04:00 manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:17:59.772417-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:12:56.007994-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:07:52.227877-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T15:02:48.615212-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:57:45.011845-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:52:41.392771-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:47:37.620010-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:42:34.086522-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:37:30.396557-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:32:26.646216-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:27:22.593082-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-27T14:22:19.022640-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
```