# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-10-18 21:24:29 EDT`
Last slot: `share_ext_2120`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$78,719.75`
- Portfolio value: `$84,067.75`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  CSCO exit_submitted    regular CSCO261120C00115000          8                5.85                 3.005          bid_ask_mid                      3.005                    True          2404.0         -2276.0             -48.632479                   2
   CEG           open    regular  CEG261120C00270000          2               17.10                17.250          bid_ask_mid                     17.250                    True          3450.0            30.0               0.877193                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  CTSH CTSH261120C00060000          2026-10-09         2026-10-12                3.70               3.30         13  -520.0  -10.810811        stop_loss_hit_at_scan
   CEG  CEG261120C00290000          2026-10-12         2026-10-13               18.70              21.30          2   520.0   13.903743 take_profit_day1_hit_at_scan
  SNPS SNPS261120C00500000          2026-10-13         2026-10-14               25.50              20.00          1  -550.0  -21.568627        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-15         2026-10-16               19.50              17.10          2  -480.0  -12.307692        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-10-18T21:24:29.986715-04:00 share_ext_2120 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T21:19:25.933123-04:00 share_ext_2115 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T21:14:21.756759-04:00 share_ext_2110 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T21:09:17.539840-04:00 share_ext_2105 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T21:04:13.480339-04:00 share_ext_2100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:59:09.300709-04:00 share_ext_2055 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:54:05.296927-04:00 share_ext_2050 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:49:01.194582-04:00 share_ext_2045 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:43:57.145979-04:00 share_ext_2040 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:38:52.516745-04:00 share_ext_2035 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:33:48.317049-04:00 share_ext_2030 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:28:44.249332-04:00 share_ext_2025 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:23:39.923432-04:00 share_ext_2020 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:18:35.681151-04:00 share_ext_2015 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:13:31.533214-04:00 share_ext_2010 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:08:27.713621-04:00 share_ext_2005 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T20:03:23.637714-04:00 share_ext_2000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T19:58:19.818924-04:00 share_ext_1955 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T19:53:15.667142-04:00 share_ext_1950 market_closed {"holiday_name": null, "reason": "weekend"}
2026-10-18T19:48:11.719502-04:00 share_ext_1945 market_closed {"holiday_name": null, "reason": "weekend"}
```