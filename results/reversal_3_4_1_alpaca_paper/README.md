# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-19 16:04:44 EDT`
Last slot: `manage_1600`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$92,373.93`
- Portfolio value: `$95,808.93`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  PANW exit_submitted      early PANW260618C00250000          3               16.05                 13.15          bid_ask_mid                      13.15                    True          3945.0          -870.0             -18.068536                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct           exit_reason
  AVGO AVGO260612C00425000          2026-05-12         2026-05-12               28.95              24.55          1  -440.0  -15.198618 stop_loss_hit_at_scan
  INTC INTC260618C00115000          2026-05-14         2026-05-15               13.30               8.75          3 -1365.0  -34.210526 stop_loss_hit_at_scan
  SNPS SNPS260618C00490000          2026-05-13         2026-05-15               46.20              39.90          1  -630.0  -13.636364 stop_loss_hit_at_scan
  INTC INTC260618C00110000          2026-05-18         2026-05-18                9.40               8.65          5  -375.0   -7.978723 stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                   detail
2026-05-19T16:04:44.982187-04:00      manage_1600  exit_order_submitted       {"alpaca_order_id": "5abeb2ab-fddd-4ee5-b52a-fdeb6b88520f", "contract_symbol": "PANW260618C00250000", "limit_price": "12.85", "reason": "stop_loss_hit_at_scan", "ticker": "PANW"}
2026-05-19T16:04:44.982187-04:00             exit       exit_not_filled                                                                                                        {"contract_symbol": "PANW260618C00250000", "status": "expired", "ticker": "PANW"}
2026-05-19T12:01:32.059087-04:00      manage_1200  exit_order_submitted       {"alpaca_order_id": "583a8972-adb7-4f86-9f64-ef9b65bcd08a", "contract_symbol": "PANW260618C00250000", "limit_price": "14.00", "reason": "stop_loss_hit_at_scan", "ticker": "PANW"}
2026-05-19T10:15:11.678665-04:00 early_entry_1005          entry_filled                                                                                      {"contract_symbol": "PANW260618C00250000", "contracts": 3, "filled_price": 16.05, "ticker": "PANW"}
2026-05-19T10:09:01.081129-04:00 early_entry_1005 entry_order_submitted   {"alpaca_order_id": "8567becd-cf83-4697-a41b-74ad47cad857", "contract_symbol": "PANW260618C00250000", "contracts": 3, "entry_mode": "early", "limit_price": "16.05", "ticker": "PANW"}
2026-05-19T10:02:51.168832-04:00 early_entry_1000         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-18T13:00:49.767100-04:00             exit           exit_filled                                                       {"contract_symbol": "INTC260618C00110000", "exit_price": 8.65, "pnl": -375.0, "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
2026-05-18T12:55:45.710585-04:00      manage_1300  exit_order_submitted        {"alpaca_order_id": "d0b0fc70-7e01-4e32-98de-5148e23c2d0f", "contract_symbol": "INTC260618C00110000", "limit_price": "7.85", "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
2026-05-18T11:24:39.449679-04:00 early_entry_1105          entry_filled                                                                                        {"contract_symbol": "INTC260618C00110000", "contracts": 5, "filled_price": 9.4, "ticker": "INTC"}
2026-05-18T11:08:20.679676-04:00 early_entry_1105 entry_order_submitted    {"alpaca_order_id": "66a4794c-2ceb-4b7d-b398-79b62129fb14", "contract_symbol": "INTC260618C00110000", "contracts": 5, "entry_mode": "early", "limit_price": "9.40", "ticker": "INTC"}
2026-05-18T10:43:30.017496-04:00 early_entry_1040         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
2026-05-15T16:01:52.248476-04:00 early_entry_1000      entry_not_filled                                                                                                        {"contract_symbol": "CRWD260618C00560000", "status": "expired", "ticker": "CRWD"}
2026-05-15T10:27:35.870371-04:00             exit           exit_filled                                                       {"contract_symbol": "SNPS260618C00490000", "exit_price": 39.9, "pnl": -630.0, "reason": "stop_loss_hit_at_scan", "ticker": "SNPS"}
2026-05-15T10:22:31.525931-04:00      manage_1030  exit_order_submitted       {"alpaca_order_id": "8fa09024-4872-4b72-ba9c-0bcfcecdc473", "contract_symbol": "SNPS260618C00490000", "limit_price": "38.60", "reason": "stop_loss_hit_at_scan", "ticker": "SNPS"}
2026-05-15T10:17:26.983517-04:00             exit           exit_filled                                                      {"contract_symbol": "INTC260618C00115000", "exit_price": 8.75, "pnl": -1365.0, "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
2026-05-15T10:00:59.774968-04:00 early_entry_1000 entry_order_submitted   {"alpaca_order_id": "e75aa353-7720-4c23-88c3-3f7f65f3813f", "contract_symbol": "CRWD260618C00560000", "contracts": 1, "entry_mode": "early", "limit_price": "47.10", "ticker": "CRWD"}
2026-05-15T10:00:59.774968-04:00      manage_1000  exit_order_submitted        {"alpaca_order_id": "5c375fa6-c3f6-4b83-a5eb-05811b36bc8e", "contract_symbol": "INTC260618C00115000", "limit_price": "8.65", "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
2026-05-14T14:56:46.485369-04:00       entry_1500          entry_filled                                                                                       {"contract_symbol": "INTC260618C00115000", "contracts": 3, "filled_price": 13.3, "ticker": "INTC"}
2026-05-14T14:50:02.003933-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "1243471d-0d2b-4531-b787-bbc8875df658", "contract_symbol": "INTC260618C00115000", "contracts": 3, "entry_mode": "regular", "limit_price": "13.60", "ticker": "INTC"}
2026-05-14T10:23:06.380585-04:00 early_entry_1020         entry_skipped                                                                                                                                        {"entry_mode": "early", "reason": "no_candidate"}
```