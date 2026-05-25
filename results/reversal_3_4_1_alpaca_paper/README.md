# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-25 10:53:18 EDT`
Last slot: `manage_1100`

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
2026-05-25T10:53:18.099004-04:00      manage_1100 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:48:14.619141-04:00      manage_1100 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:43:10.886105-04:00 early_entry_1040 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:38:07.308161-04:00      manage_1030 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:33:03.739795-04:00      manage_1030 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:28:00.172944-04:00      manage_1030 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:22:56.562697-04:00      manage_1030 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:17:52.610208-04:00 early_entry_1015 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:12:48.998803-04:00 early_entry_1010 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:07:45.242567-04:00      manage_1000 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T10:02:41.703578-04:00      manage_1000 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:57:38.209560-04:00      manage_1000 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:52:34.538947-04:00      manage_1000 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:47:31.043803-04:00           manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:42:27.435412-04:00           manual market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:37:23.941795-04:00      manage_0930 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:32:20.418626-04:00      manage_0930 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:27:16.193217-04:00      manage_0930 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:22:12.471308-04:00      manage_0930 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T09:17:08.599251-04:00   share_ext_0915 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```