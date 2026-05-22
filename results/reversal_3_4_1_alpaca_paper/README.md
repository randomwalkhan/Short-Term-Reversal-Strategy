# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-22 17:01:58 EDT`
Last slot: `share_ext_1700`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$87,958.08`
- Portfolio value: `$96,138.08`
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
                    timestamp_et             slot            event_type                                                                                                                                                                                   detail
2026-05-22T15:40:49.867920-04:00       entry_1500          entry_filled                                                                                      {"contract_symbol": "SBUX260717C00105000", "contracts": 13, "filled_price": 3.75, "ticker": "SBUX"}
2026-05-22T14:48:54.200962-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "25ae4817-4805-468f-b6e2-b9bbabb07100", "contract_symbol": "SBUX260717C00105000", "contracts": 13, "entry_mode": "regular", "limit_price": "3.75", "ticker": "SBUX"}
2026-05-22T11:59:49.162853-04:00 early_entry_1155         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:53:28.237361-04:00 early_entry_1150         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:47:08.963058-04:00 early_entry_1145         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:40:57.259497-04:00 early_entry_1140         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:34:43.085077-04:00 early_entry_1130         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:28:32.027911-04:00 early_entry_1125         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:22:20.926392-04:00 early_entry_1120         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:16:09.558838-04:00 early_entry_1115         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:09:59.497169-04:00 early_entry_1105         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T11:03:43.624983-04:00 early_entry_1100         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:57:31.114861-04:00 early_entry_1055         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:51:20.106412-04:00 early_entry_1050         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:45:11.001838-04:00 early_entry_1045         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:38:54.830332-04:00 early_entry_1035         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:32:45.431803-04:00 early_entry_1030         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:26:28.661701-04:00 early_entry_1025         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:20:17.696794-04:00 early_entry_1020         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-22T10:14:06.428603-04:00 early_entry_1010         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
```