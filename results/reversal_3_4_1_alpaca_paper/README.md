# Reversal 3.4.2-alpaca-paper.0

Latest checkpoint (ET): `2026-05-12 10:08:53 EDT`
Last slot: `manage_1000`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$97,104.98`
- Portfolio value: `$99,744.98`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker          status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price  unrealized_pnl  unrealized_return_pct
  AVGO entry_submitted      early AVGO260612C00425000          1                27.4                   NaN             NaN                    NaN
```

## Closed Trades

_None_

## Recent Events

```text
                    timestamp_et             slot               event_type                                                                                                                                                                                                                                                                                                                                                     detail
2026-05-12T10:08:53.681217-04:00 early_entry_1005    entry_order_submitted                                                                                                                                                                     {"alpaca_order_id": "38db7217-e7e8-4357-a32f-a9fbd6afdc57", "contract_symbol": "AVGO260612C00425000", "contracts": 1, "entry_mode": "early", "limit_price": "29.05", "ticker": "AVGO"}
2026-05-12T10:02:44.192841-04:00 early_entry_1000            entry_skipped                                                                                                                                                                                                                                                                  {"budget": 5000.0, "entry_limit": 50.67, "reason": "insufficient_cash", "ticker": "SNPS"}
       2026-05-11T10:55:00-04:00         recovery missed_sim_trade_blocked {"action": "block_remaining_2026-05-11_entries_no_retroactive_order", "reason": "alpaca_runner_empty_csv_crash_before_entry_window", "sim_contract_symbol": "CEG260618C00290000", "sim_entry_timestamp_et": "2026-05-11T10:05:43.962541-04:00", "sim_exit_timestamp_et": "2026-05-11T10:37:19.097633-04:00", "sim_return_pct": 15.52, "sim_ticker": "CEG"}
```