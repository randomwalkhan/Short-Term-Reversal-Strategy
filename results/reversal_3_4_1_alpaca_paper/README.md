# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-23 13:16:29 EDT`
Last slot: `manual`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$87,957.73`
- Portfolio value: `$96,137.73`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  INTC   open    regular INTC260626C00117000          3               13.45                 13.05          bid_ask_mid                      13.05                    True          3915.0          -120.0              -2.973978                   1
  SBUX   open    regular SBUX260717C00105000         13                3.75                  3.70          bid_ask_mid                       3.70                    True          4810.0           -65.0              -1.333333                   0
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
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                      detail
2026-05-23T13:16:29.603443-04:00           manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T13:11:26.127355-04:00      manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T13:06:22.201740-04:00      manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T13:01:18.664231-04:00      manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:56:15.302164-04:00      manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:51:11.802185-04:00      manage_1300 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:46:08.384209-04:00           manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:41:04.977873-04:00      manage_1230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:36:01.520622-04:00      manage_1230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:30:58.029527-04:00      manage_1230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:25:54.615251-04:00      manage_1230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:20:51.169168-04:00      manage_1230 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:15:47.146302-04:00           manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:10:43.621266-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:05:40.094629-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T12:00:36.428216-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T11:55:32.935632-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T11:50:29.552104-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T11:45:26.107189-04:00 early_entry_1145 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T11:40:22.724835-04:00      manage_1130 market_closed {"holiday_name": null, "reason": "weekend"}
```