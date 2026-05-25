# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-25 15:51:49 EDT`
Last slot: `manage_1600`

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
                    timestamp_et        slot    event_type                                                     detail
2026-05-25T15:51:49.136575-04:00 manage_1600 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:46:45.799724-04:00      manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:41:42.344998-04:00 manage_1530 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:36:38.571264-04:00 manage_1530 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:31:34.871794-04:00 manage_1530 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:26:31.395779-04:00 manage_1530 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:21:27.921652-04:00 manage_1530 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:16:24.475929-04:00      manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:11:20.911906-04:00  entry_1500 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:06:17.413460-04:00  entry_1500 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T15:01:13.922192-04:00  entry_1500 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:56:10.417461-04:00  entry_1500 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:51:07.014474-04:00  entry_1500 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:46:03.535492-04:00      manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:41:00.019397-04:00 manage_1430 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:35:56.365719-04:00 manage_1430 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:30:52.922619-04:00 manage_1430 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:25:49.352440-04:00 manage_1430 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:20:45.673849-04:00 manage_1430 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T14:15:42.210720-04:00      manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```