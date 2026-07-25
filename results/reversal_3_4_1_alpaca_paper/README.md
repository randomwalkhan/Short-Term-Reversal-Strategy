# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-07-25 16:16:03 EDT`
Last slot: `share_ext_1615`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$89,005.58`
- Portfolio value: `$93,135.58`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  GILD   open    regular GILD260918C00130000          7                 6.7                 6.375          bid_ask_mid                      6.375                    True          4462.5          -227.5              -4.850746                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  DRAM DRAM260731C00073000          2026-06-26         2026-06-29                8.90               6.50          5 -1200.0  -26.966292        stop_loss_hit_at_scan
  GILD GILD260821C00135000          2026-07-09         2026-07-13                5.95               3.70          8 -1800.0  -37.815126        stop_loss_hit_at_scan
  AAPL AAPL260821C00315000          2026-07-14         2026-07-15               11.60              16.60          4  2000.0   43.103448 take_profit_day1_hit_at_scan
  META META260821C00660000          2026-07-13         2026-07-15               47.35              55.90          1   855.0   18.057022 take_profit_day2_hit_at_scan
   TXN  TXN260821C00290000          2026-07-17         2026-07-21               21.05              24.00          2   590.0   14.014252 take_profit_day2_hit_at_scan
  AAPL AAPL260821C00330000          2026-07-20         2026-07-22               10.70               9.45          4  -500.0  -11.682243        stop_loss_hit_at_scan
  PYPL PYPL260821C00055000          2026-07-21         2026-07-23                3.15               2.60         15  -825.0  -17.460317        stop_loss_hit_at_scan
  PYPL PYPL260821C00055000          2026-07-22         2026-07-23                3.25               2.98         15  -405.0   -8.307692        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-07-25T16:16:03.711042-04:00 share_ext_1615 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T16:10:59.999448-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T16:05:56.658078-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T16:00:53.190768-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:55:49.462613-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:50:45.976366-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:45:42.681192-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:40:39.315061-04:00    manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:35:35.284846-04:00    manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:30:31.560046-04:00    manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:25:28.054187-04:00    manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:20:24.651318-04:00    manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:15:21.105533-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:10:17.499709-04:00     entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:05:13.651761-04:00     entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T15:00:10.247007-04:00     entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T14:55:06.579495-04:00     entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T14:50:02.788293-04:00     entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T14:44:59.250391-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-07-25T14:34:58.334298-04:00    manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
```