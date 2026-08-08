# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-08-08 09:38:17 EDT`
Last slot: `manage_0930`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$87,138.70`
- Portfolio value: `$92,234.70`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  PYPL   open    regular PYPL260918C00060000         28                1.71                  1.79          bid_ask_mid                       1.79                    True          5012.0           224.0               4.678363                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  PAYX PAYX260717C00100000          2026-06-11         2026-06-12                5.50               4.40          9  -990.0  -20.000000        stop_loss_hit_at_scan
  ROST ROST260717C00240000          2026-06-15         2026-06-16                5.60               4.80          8  -640.0  -14.285714        stop_loss_hit_at_scan
  DRAM DRAM260717C00069000          2026-06-16         2026-06-17                7.60               8.15          6   330.0    7.236842        stop_loss_hit_at_scan
   WMT  WMT260724C00120000          2026-06-18         2026-06-23                2.65               3.55         18  1620.0   33.962264 take_profit_day2_hit_at_scan
  MRVL MRVL260724C00310000          2026-06-22         2026-06-23               35.45              22.45          1 -1300.0  -36.671368        stop_loss_hit_at_scan
  AVGO AVGO260821C00380000          2026-06-25         2026-06-26               30.20              23.85          1  -635.0  -21.026490        stop_loss_hit_at_scan
  DRAM DRAM260731C00073000          2026-06-26         2026-06-29                8.90               6.50          5 -1200.0  -26.966292        stop_loss_hit_at_scan
  GILD GILD260821C00135000          2026-07-09         2026-07-13                5.95               3.70          8 -1800.0  -37.815126        stop_loss_hit_at_scan
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
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-08T09:38:17.461017-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T09:33:13.661675-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T09:28:10.034595-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T09:23:06.319869-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T09:18:02.618580-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T09:12:59.036532-04:00 share_ext_0910 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T09:07:55.095169-04:00 share_ext_0905 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T09:02:51.384661-04:00 share_ext_0900 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:57:47.586619-04:00 share_ext_0855 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:52:43.916987-04:00 share_ext_0850 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:47:40.202569-04:00 share_ext_0845 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:42:36.637886-04:00 share_ext_0840 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:37:32.854001-04:00 share_ext_0835 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:32:29.300107-04:00 share_ext_0830 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:27:25.471824-04:00 share_ext_0825 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:22:21.965909-04:00 share_ext_0820 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:17:18.394670-04:00 share_ext_0815 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:12:14.925393-04:00 share_ext_0810 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:07:11.429643-04:00 share_ext_0805 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-08T08:02:07.776564-04:00 share_ext_0800 market_closed {"holiday_name": null, "reason": "weekend"}
```