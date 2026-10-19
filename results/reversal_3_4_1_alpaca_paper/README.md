# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-10-19 09:56:06 EDT`
Last slot: `manage_1000`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$81,087.55`
- Portfolio value: `$83,987.55`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode    contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
   CEG   open    regular CEG261120C00270000          2                17.1                  16.8          bid_ask_mid                       16.8                    True          3360.0           -60.0              -1.754386                   1
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  CTSH CTSH261120C00060000          2026-10-09         2026-10-12                3.70               3.30         13  -520.0  -10.810811        stop_loss_hit_at_scan
   CEG  CEG261120C00290000          2026-10-12         2026-10-13               18.70              21.30          2   520.0   13.903743 take_profit_day1_hit_at_scan
  SNPS SNPS261120C00500000          2026-10-13         2026-10-14               25.50              20.00          1  -550.0  -21.568627        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-15         2026-10-16               19.50              17.10          2  -480.0  -12.307692        stop_loss_hit_at_scan
  CSCO CSCO261120C00115000          2026-10-14         2026-10-19                5.85               2.96          8 -2312.0  -49.401709        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                                                                                              detail
2026-10-19T09:30:36.077934-04:00           exit   exit_filled {"contract_symbol": "CSCO261120C00115000", "exit_price": 2.96, "pnl": -2312.0, "reason": "stop_loss_hit_at_scan", "ticker": "CSCO"}
2026-10-18T23:56:33.636019-04:00 share_ext_2355 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:51:29.276340-04:00 share_ext_2350 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:46:25.297281-04:00 share_ext_2345 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:41:21.252312-04:00 share_ext_2340 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:36:17.284351-04:00 share_ext_2335 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:31:13.305592-04:00 share_ext_2330 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:26:09.321086-04:00 share_ext_2325 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:21:05.348597-04:00 share_ext_2320 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:16:01.384262-04:00 share_ext_2315 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:10:57.387534-04:00 share_ext_2310 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:05:53.381714-04:00 share_ext_2305 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T23:00:49.345601-04:00 share_ext_2300 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T22:55:45.564162-04:00 share_ext_2255 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T22:50:41.556805-04:00 share_ext_2250 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T22:45:37.601443-04:00 share_ext_2245 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T22:40:33.387549-04:00 share_ext_2240 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T22:35:29.371816-04:00 share_ext_2235 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T22:30:25.348007-04:00 share_ext_2230 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
2026-10-18T22:25:20.273899-04:00 share_ext_2225 market_closed                                                                                         {"holiday_name": null, "reason": "weekend"}
```