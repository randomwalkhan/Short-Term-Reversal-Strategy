# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-31 12:08:56 EDT`
Last slot: `manage_1200`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$94,521.56`
- Portfolio value: `$97,141.56`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  MRVL   open      early MRVL260717C00200000          1                26.0                26.575          bid_ask_mid                     26.575                    True          2657.5            57.5               2.211538                   0
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
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                      detail
2026-05-31T12:08:56.652595-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T12:03:53.009648-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:58:49.431769-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:53:45.894388-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:48:42.245174-04:00      manage_1200 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:43:38.727917-04:00 early_entry_1140 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:38:35.301505-04:00      manage_1130 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:33:31.573383-04:00      manage_1130 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:28:28.004453-04:00      manage_1130 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:23:24.409519-04:00      manage_1130 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:18:20.850568-04:00      manage_1130 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:13:17.318808-04:00 early_entry_1110 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:08:13.985321-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T11:03:10.446919-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T10:58:07.100292-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T10:53:03.692523-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T10:48:00.283981-04:00      manage_1100 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T10:42:56.708543-04:00 early_entry_1040 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T10:37:53.122567-04:00      manage_1030 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T10:32:49.663952-04:00      manage_1030 market_closed {"holiday_name": null, "reason": "weekend"}
```