# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-23 10:04:15 EDT`
Last slot: `manage_1000`

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
2026-05-23T10:04:15.900862-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:59:12.372110-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:54:08.948056-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:49:05.467188-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:44:02.109658-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:38:58.668954-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:33:55.257245-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:28:51.907180-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:23:48.453215-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:18:45.081241-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:13:41.615276-04:00 share_ext_0910 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:08:38.207822-04:00 share_ext_0905 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T09:03:34.764970-04:00 share_ext_0900 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T08:58:31.376172-04:00 share_ext_0855 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T08:53:27.931822-04:00 share_ext_0850 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T08:48:24.499468-04:00 share_ext_0845 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T08:43:20.999195-04:00 share_ext_0840 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T08:38:17.625938-04:00 share_ext_0835 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T08:33:13.955843-04:00 share_ext_0830 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-23T08:28:10.513000-04:00 share_ext_0825 market_closed {"holiday_name": null, "reason": "weekend"}
```