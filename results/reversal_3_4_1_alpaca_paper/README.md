# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-08-17 07:35:14 EDT`
Last slot: `share_ext_0735`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$89,086.48`
- Portfolio value: `$92,346.48`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  AMZN   open    regular AMZN260918C00265000          4               10.75                   8.2     last_price_stale                        NaN                   False          3280.0         -1020.0              -23.72093                   2
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  PYPL PYPL260918C00060000          2026-08-07         2026-08-10                1.71               1.51         28  -560.0  -11.695906        stop_loss_hit_at_scan
  LRCX LRCX260918C00310000          2026-08-10         2026-08-12               27.25              34.05          1   680.0   24.954128 take_profit_day2_hit_at_scan
  PYPL PYPL260918C00057500          2026-08-12         2026-08-13                2.86               3.65         17  1343.0   27.622378 take_profit_day1_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-08-16T23:59:36.333699-04:00 share_ext_2355 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:54:32.767975-04:00 share_ext_2350 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:49:28.787777-04:00 share_ext_2345 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:44:24.354072-04:00 share_ext_2340 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:39:20.588633-04:00 share_ext_2335 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:34:16.709135-04:00 share_ext_2330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:29:12.937619-04:00 share_ext_2325 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:24:09.296024-04:00 share_ext_2320 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:19:05.217548-04:00 share_ext_2315 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:14:01.664220-04:00 share_ext_2310 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:08:57.811760-04:00 share_ext_2305 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T23:03:53.967497-04:00 share_ext_2300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:58:50.079628-04:00 share_ext_2255 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:53:46.237551-04:00 share_ext_2250 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:48:42.361103-04:00 share_ext_2245 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:43:38.610445-04:00 share_ext_2240 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:38:35.037856-04:00 share_ext_2235 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:33:31.391700-04:00 share_ext_2230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:28:27.681534-04:00 share_ext_2225 market_closed {"holiday_name": null, "reason": "weekend"}
2026-08-16T22:23:23.750095-04:00 share_ext_2220 market_closed {"holiday_name": null, "reason": "weekend"}
```