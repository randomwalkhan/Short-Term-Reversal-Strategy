# Reversal 3.4.2-alpaca-paper.0

Latest checkpoint (ET): `2026-05-12 13:37:43 EDT`
Last slot: `manage_1330`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$97,104.98`
- Portfolio value: `$99,149.98`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  AVGO exit_submitted      early AVGO260612C00425000          1               28.95                 20.25          2025.0          -870.0             -30.051813                   0
```

## Closed Trades

_None_

## Recent Events

```text
                    timestamp_et             slot               event_type                                                                                                                                                                                                                                                                                                                                                     detail
2026-05-12T11:05:40.979834-04:00      manage_1100     exit_order_submitted                                                                                                                                                                         {"alpaca_order_id": "79d5f44f-d6d5-4507-8c98-ff437fee09b0", "contract_symbol": "AVGO260612C00425000", "limit_price": "24.20", "reason": "stop_loss_hit_at_scan", "ticker": "AVGO"}
2026-05-12T10:15:04.282278-04:00 early_entry_1005             entry_filled                                                                                                                                                                                                                                                        {"contract_symbol": "AVGO260612C00425000", "contracts": 1, "filled_price": 28.95, "ticker": "AVGO"}
2026-05-12T10:08:53.681217-04:00 early_entry_1005    entry_order_submitted                                                                                                                                                                     {"alpaca_order_id": "38db7217-e7e8-4357-a32f-a9fbd6afdc57", "contract_symbol": "AVGO260612C00425000", "contracts": 1, "entry_mode": "early", "limit_price": "29.05", "ticker": "AVGO"}
2026-05-12T10:02:44.192841-04:00 early_entry_1000            entry_skipped                                                                                                                                                                                                                                                                  {"budget": 5000.0, "entry_limit": 50.67, "reason": "insufficient_cash", "ticker": "SNPS"}
       2026-05-11T10:55:00-04:00         recovery missed_sim_trade_blocked {"action": "block_remaining_2026-05-11_entries_no_retroactive_order", "reason": "alpaca_runner_empty_csv_crash_before_entry_window", "sim_contract_symbol": "CEG260618C00290000", "sim_entry_timestamp_et": "2026-05-11T10:05:43.962541-04:00", "sim_exit_timestamp_et": "2026-05-11T10:37:19.097633-04:00", "sim_return_pct": 15.52, "sim_ticker": "CEG"}
```