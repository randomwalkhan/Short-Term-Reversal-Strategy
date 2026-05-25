# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-25 12:59:48 EDT`
Last slot: `manage_1300`

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
                    timestamp_et             slot    event_type                                                     detail
2026-05-25T12:59:48.206311-04:00      manage_1300 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:54:44.233168-04:00      manage_1300 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:49:40.689460-04:00      manage_1300 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:44:37.143169-04:00           manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:39:33.546707-04:00      manage_1230 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:34:30.138558-04:00      manage_1230 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:29:26.650490-04:00      manage_1230 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:24:23.157970-04:00      manage_1230 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:19:19.667973-04:00      manage_1230 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:14:16.030415-04:00           manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:09:12.311299-04:00      manage_1200 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T12:04:08.538264-04:00      manage_1200 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:59:04.994511-04:00      manage_1200 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:54:01.197259-04:00      manage_1200 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:48:57.632004-04:00      manage_1200 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:43:54.241224-04:00 early_entry_1140 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:38:50.483069-04:00      manage_1130 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:33:46.932716-04:00      manage_1130 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:28:43.253314-04:00      manage_1130 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T11:23:39.568066-04:00      manage_1130 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```