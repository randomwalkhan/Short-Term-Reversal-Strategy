# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-15 15:46:42 EDT`
Last slot: `manual`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$97,564.61`
- Portfolio value: `$97,564.61`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker          status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price  unrealized_pnl  unrealized_return_pct
  CRWD entry_submitted      early CRWD260618C00560000          1               44.25                   NaN             NaN                    NaN
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct           exit_reason
  AVGO AVGO260612C00425000          2026-05-12         2026-05-12               28.95              24.55          1  -440.0  -15.198618 stop_loss_hit_at_scan
  INTC INTC260618C00115000          2026-05-14         2026-05-15               13.30               8.75          3 -1365.0  -34.210526 stop_loss_hit_at_scan
  SNPS SNPS260618C00490000          2026-05-13         2026-05-15               46.20              39.90          1  -630.0  -13.636364 stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot               event_type                                                                                                                                                                                                                                                                                                                                                     detail
2026-05-15T10:27:35.870371-04:00             exit              exit_filled                                                                                                                                                                                                                         {"contract_symbol": "SNPS260618C00490000", "exit_price": 39.9, "pnl": -630.0, "reason": "stop_loss_hit_at_scan", "ticker": "SNPS"}
2026-05-15T10:22:31.525931-04:00      manage_1030     exit_order_submitted                                                                                                                                                                         {"alpaca_order_id": "8fa09024-4872-4b72-ba9c-0bcfcecdc473", "contract_symbol": "SNPS260618C00490000", "limit_price": "38.60", "reason": "stop_loss_hit_at_scan", "ticker": "SNPS"}
2026-05-15T10:17:26.983517-04:00             exit              exit_filled                                                                                                                                                                                                                        {"contract_symbol": "INTC260618C00115000", "exit_price": 8.75, "pnl": -1365.0, "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
2026-05-15T10:00:59.774968-04:00 early_entry_1000    entry_order_submitted                                                                                                                                                                     {"alpaca_order_id": "e75aa353-7720-4c23-88c3-3f7f65f3813f", "contract_symbol": "CRWD260618C00560000", "contracts": 1, "entry_mode": "early", "limit_price": "47.10", "ticker": "CRWD"}
2026-05-15T10:00:59.774968-04:00      manage_1000     exit_order_submitted                                                                                                                                                                          {"alpaca_order_id": "5c375fa6-c3f6-4b83-a5eb-05811b36bc8e", "contract_symbol": "INTC260618C00115000", "limit_price": "8.65", "reason": "stop_loss_hit_at_scan", "ticker": "INTC"}
2026-05-14T14:56:46.485369-04:00       entry_1500             entry_filled                                                                                                                                                                                                                                                         {"contract_symbol": "INTC260618C00115000", "contracts": 3, "filled_price": 13.3, "ticker": "INTC"}
2026-05-14T14:50:02.003933-04:00       entry_1500    entry_order_submitted                                                                                                                                                                   {"alpaca_order_id": "1243471d-0d2b-4531-b787-bbc8875df658", "contract_symbol": "INTC260618C00115000", "contracts": 3, "entry_mode": "regular", "limit_price": "13.60", "ticker": "INTC"}
2026-05-14T10:23:06.380585-04:00 early_entry_1020            entry_skipped                                                                                                                                                                                                                                                                                                          {"entry_mode": "early", "reason": "no_candidate"}
2026-05-13T10:39:33.767755-04:00 early_entry_1020             entry_filled                                                                                                                                                                                                                                                         {"contract_symbol": "SNPS260618C00490000", "contracts": 1, "filled_price": 46.2, "ticker": "SNPS"}
2026-05-13T10:23:16.811406-04:00 early_entry_1020    entry_order_submitted                                                                                                                                                                     {"alpaca_order_id": "8bbe1576-32e5-4cb1-863a-6aed57d594fa", "contract_symbol": "SNPS260618C00490000", "contracts": 1, "entry_mode": "early", "limit_price": "47.40", "ticker": "SNPS"}
2026-05-13T10:17:04.025534-04:00 early_entry_1015            entry_skipped                                                                                                                                                                                                {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-13T10:10:54.018081-04:00 early_entry_1010            entry_skipped                                                                                                                                                                                                                                                                                                          {"entry_mode": "early", "reason": "no_candidate"}
2026-05-13T10:04:46.993511-04:00 early_entry_1000            entry_skipped                                                                                                                                                                                                                                                                                                          {"entry_mode": "early", "reason": "no_candidate"}
2026-05-12T15:54:31.789727-04:00             exit              exit_filled                                                                                                                                                                                                                        {"contract_symbol": "AVGO260612C00425000", "exit_price": 24.55, "pnl": -440.0, "reason": "stop_loss_hit_at_scan", "ticker": "AVGO"}
2026-05-12T11:05:40.979834-04:00      manage_1100     exit_order_submitted                                                                                                                                                                         {"alpaca_order_id": "79d5f44f-d6d5-4507-8c98-ff437fee09b0", "contract_symbol": "AVGO260612C00425000", "limit_price": "24.20", "reason": "stop_loss_hit_at_scan", "ticker": "AVGO"}
2026-05-12T10:15:04.282278-04:00 early_entry_1005             entry_filled                                                                                                                                                                                                                                                        {"contract_symbol": "AVGO260612C00425000", "contracts": 1, "filled_price": 28.95, "ticker": "AVGO"}
2026-05-12T10:08:53.681217-04:00 early_entry_1005    entry_order_submitted                                                                                                                                                                     {"alpaca_order_id": "38db7217-e7e8-4357-a32f-a9fbd6afdc57", "contract_symbol": "AVGO260612C00425000", "contracts": 1, "entry_mode": "early", "limit_price": "29.05", "ticker": "AVGO"}
2026-05-12T10:02:44.192841-04:00 early_entry_1000            entry_skipped                                                                                                                                                                                                                                                                  {"budget": 5000.0, "entry_limit": 50.67, "reason": "insufficient_cash", "ticker": "SNPS"}
       2026-05-11T10:55:00-04:00         recovery missed_sim_trade_blocked {"action": "block_remaining_2026-05-11_entries_no_retroactive_order", "reason": "alpaca_runner_empty_csv_crash_before_entry_window", "sim_contract_symbol": "CEG260618C00290000", "sim_entry_timestamp_et": "2026-05-11T10:05:43.962541-04:00", "sim_exit_timestamp_et": "2026-05-11T10:37:19.097633-04:00", "sim_return_pct": 15.52, "sim_ticker": "CEG"}
```