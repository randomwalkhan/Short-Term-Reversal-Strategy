# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-22 10:57:31 EDT`
Last slot: `manage_1100`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$92,833.34`
- Portfolio value: `$97,003.34`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  INTC   open    regular INTC260626C00117000          3               13.45                  14.1          bid_ask_mid                       14.1                    True          4230.0           195.0               4.832714                   1
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
                    timestamp_et             slot            event_type                                                                                                                                                                                    detail
2026-05-22T10:57:31.114861-04:00 early_entry_1055         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:51:20.106412-04:00 early_entry_1050         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:45:11.001838-04:00 early_entry_1045         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:38:54.830332-04:00 early_entry_1035         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:32:45.431803-04:00 early_entry_1030         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:26:28.661701-04:00 early_entry_1025         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:20:17.696794-04:00 early_entry_1020         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:14:06.428603-04:00 early_entry_1010         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:07:52.347186-04:00 early_entry_1005         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:01:40.288325-04:00 early_entry_1000         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T14:54:53.036519-04:00       entry_1500          entry_filled                                                                                       {"contract_symbol": "INTC260626C00117000", "contracts": 3, "filled_price": 13.45, "ticker": "INTC"}
2026-05-21T14:48:31.785006-04:00       entry_1500 entry_order_submitted  {"alpaca_order_id": "ec033fb0-02a9-46ac-9e86-fad49d5b5473", "contract_symbol": "INTC260626C00117000", "contracts": 3, "entry_mode": "regular", "limit_price": "13.85", "ticker": "INTC"}
2026-05-21T13:57:44.888649-04:00             exit           exit_filled                                                  {"contract_symbol": "TTWO260717C00240000", "exit_price": 19.0, "pnl": 400.0, "reason": "take_profit_day1_hit_at_scan", "ticker": "TTWO"}
2026-05-21T13:52:40.103301-04:00      manage_1400  exit_order_submitted {"alpaca_order_id": "8a309bc9-b19c-4144-9daf-a4e3261cc6c0", "contract_symbol": "TTWO260717C00240000", "limit_price": "18.90", "reason": "take_profit_day1_hit_at_scan", "ticker": "TTWO"}
2026-05-21T11:59:54.060175-04:00 early_entry_1155         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:53:44.244584-04:00 early_entry_1150         entry_skipped                                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T11:47:32.644554-04:00 early_entry_1145         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:41:10.828251-04:00 early_entry_1140         entry_skipped                                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T11:34:59.275965-04:00 early_entry_1130         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:28:49.809880-04:00 early_entry_1125         entry_skipped                                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
```