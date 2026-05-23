# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-23 17:09:22 EDT`
Last slot: `share_ext_1705`

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
                    timestamp_et           slot    event_type                                      detail
2026-05-23T17:09:22.881323-04:00 share_ext_1705 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T17:04:19.393529-04:00 share_ext_1700 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:59:15.995483-04:00 share_ext_1655 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:54:12.202463-04:00 share_ext_1650 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:49:08.704493-04:00 share_ext_1645 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:44:05.219144-04:00 share_ext_1640 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:39:01.708429-04:00 share_ext_1635 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:33:58.066747-04:00 share_ext_1630 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:28:54.642111-04:00 share_ext_1625 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:23:51.219505-04:00 share_ext_1620 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:18:47.792492-04:00 share_ext_1615 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:13:44.370194-04:00 share_ext_1610 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:08:40.803629-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T16:03:37.317110-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:58:33.698541-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:53:29.948148-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:48:26.498069-04:00    manage_1600 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:43:23.088402-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:38:19.717557-04:00    manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T15:33:16.194697-04:00    manage_1530 market_closed {"holiday_name": null, "reason": "weekend"}
```