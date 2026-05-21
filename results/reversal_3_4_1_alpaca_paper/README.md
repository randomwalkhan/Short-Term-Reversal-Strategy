# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-20 20:02:00 EDT`
Last slot: `share_ext_2000`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$93,068.74`
- Portfolio value: `$96,348.74`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  TTWO   open      early TTWO260717C00240000          2                17.0                  16.8          bid_ask_mid                       16.8                    True          3360.0           -40.0              -1.176471                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct           exit_reason
  AVGO AVGO260612C00425000          2026-05-12         2026-05-12               28.95              24.55          1  -440.0  -15.198618 stop_loss_hit_at_scan
  INTC INTC260618C00115000          2026-05-14         2026-05-15               13.30               8.75          3 -1365.0  -34.210526 stop_loss_hit_at_scan
  SNPS SNPS260618C00490000          2026-05-13         2026-05-15               46.20              39.90          1  -630.0  -13.636364 stop_loss_hit_at_scan
  INTC INTC260618C00110000          2026-05-18         2026-05-18                9.40               8.65          5  -375.0   -7.978723 stop_loss_hit_at_scan
  PANW PANW260618C00250000          2026-05-19         2026-05-20               16.05              13.65          3  -720.0  -14.953271 stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                 detail
2026-05-20T12:15:57.679645-04:00 early_entry_1115          entry_filled                                                                                     {"contract_symbol": "TTWO260717C00240000", "contracts": 2, "filled_price": 17.0, "ticker": "TTWO"}
2026-05-20T11:19:03.434065-04:00 early_entry_1115 entry_order_submitted {"alpaca_order_id": "3e3c8dfc-2286-4e36-9ffb-4cf8435d27c4", "contract_symbol": "TTWO260717C00240000", "contracts": 2, "entry_mode": "early", "limit_price": "17.20", "ticker": "TTWO"}
2026-05-20T11:12:45.922551-04:00 early_entry_1110         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T11:06:27.663743-04:00 early_entry_1105         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T11:00:07.702182-04:00 early_entry_1100         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:53:49.849791-04:00 early_entry_1050         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:47:32.363203-04:00 early_entry_1045         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:41:13.621403-04:00 early_entry_1040         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:34:51.981061-04:00 early_entry_1030         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:28:39.432516-04:00 early_entry_1025         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:22:11.379624-04:00 early_entry_1020         entry_skipped                                                         {"entry_mode": "early", "option_liquidity_status": "wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-20T09:56:30.679364-04:00             exit           exit_filled                                                    {"contract_symbol": "PANW260618C00250000", "exit_price": 13.65, "pnl": -720.0, "reason": "stop_loss_hit_at_scan", "ticker": "PANW"}
2026-05-19T16:04:44.982187-04:00      manage_1600  exit_order_submitted     {"alpaca_order_id": "5abeb2ab-fddd-4ee5-b52a-fdeb6b88520f", "contract_symbol": "PANW260618C00250000", "limit_price": "12.85", "reason": "stop_loss_hit_at_scan", "ticker": "PANW"}
2026-05-19T16:04:44.982187-04:00             exit       exit_not_filled                                                                                                      {"contract_symbol": "PANW260618C00250000", "status": "expired", "ticker": "PANW"}
2026-05-19T12:01:32.059087-04:00      manage_1200  exit_order_submitted     {"alpaca_order_id": "583a8972-adb7-4f86-9f64-ef9b65bcd08a", "contract_symbol": "PANW260618C00250000", "limit_price": "14.00", "reason": "stop_loss_hit_at_scan", "ticker": "PANW"}
2026-05-19T10:15:11.678665-04:00 early_entry_1005          entry_filled                                                                                    {"contract_symbol": "PANW260618C00250000", "contracts": 3, "filled_price": 16.05, "ticker": "PANW"}
2026-05-19T10:09:01.081129-04:00 early_entry_1005 entry_order_submitted {"alpaca_order_id": "8567becd-cf83-4697-a41b-74ad47cad857", "contract_symbol": "PANW260618C00250000", "contracts": 3, "entry_mode": "early", "limit_price": "16.05", "ticker": "PANW"}
2026-05-19T10:02:51.168832-04:00 early_entry_1000         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-18T13:00:49.767100-04:00             exit           exit_filled                                                     {"contract_symbol": "INTC260618C00110000", "exit_price": 8.65, "pnl": -375.0, "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
2026-05-18T12:55:45.710585-04:00      manage_1300  exit_order_submitted      {"alpaca_order_id": "d0b0fc70-7e01-4e32-98de-5148e23c2d0f", "contract_symbol": "INTC260618C00110000", "limit_price": "7.85", "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
```