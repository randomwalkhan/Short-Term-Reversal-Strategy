# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-23 15:23:08 EDT`
Last slot: `manage_1530`

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
                    timestamp_et        slot    event_type                                      detail
2026-05-23T15:23:08.727225-04:00 manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:18:04.896767-04:00 manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:13:00.878138-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:07:55.375095-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:02:50.019638-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:57:45.315711-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:52:39.381445-04:00  entry_1500 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:47:34.563967-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:42:31.016681-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:37:27.043722-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:32:23.233930-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:27:19.551799-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:22:16.165296-04:00 manage_1430 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:17:12.497057-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:12:08.746564-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:07:04.938222-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T14:02:01.222343-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T13:56:57.882187-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T13:51:54.115748-04:00 manage_1400 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T13:46:50.589497-04:00      manual market_closed {"holiday_name": null, "reason": "weekend"}
```