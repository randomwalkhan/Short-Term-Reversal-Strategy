# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-06-21 15:02:55 EDT`
Last slot: `entry_1500`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$90,531.22`
- Portfolio value: `$94,401.22`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode    contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
   WMT   open    regular WMT260724C00120000         18                2.65                 2.555          bid_ask_mid                      2.555                    True          4599.0          -171.0              -3.584906                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  AVGO AVGO260612C00425000          2026-05-12         2026-05-12               28.95              24.55          1  -440.0  -15.198618        stop_loss_hit_at_scan
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
```

## Recent Events

```text
                    timestamp_et        slot    event_type                                      detail
2026-06-21T15:02:55.958953-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:57:52.478956-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:52:48.775806-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:47:45.271511-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:42:41.631278-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:37:38.182399-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:32:34.573696-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:27:31.020934-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:22:27.384373-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:17:23.697562-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:12:20.003288-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:07:16.448193-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T14:02:12.872664-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T13:57:09.068438-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T13:52:05.464386-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T13:47:01.964388-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T13:41:58.469800-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T13:36:54.913484-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T13:31:51.285341-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
2026-06-21T13:26:47.646839-04:00 manage_1330 market_closed {"holiday_name": null, "reason": "weekend"}
```