# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-06-02 11:26:44 EDT`
Last slot: `manage_1130`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$97,296.02`
- Portfolio value: `$97,296.02`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker          status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price  unrealized_pnl  unrealized_return_pct
  AMZN entry_submitted      early AMZN260717C00260000          4                10.8                   NaN             NaN                    NaN
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
  SBUX SBUX260717C00105000          2026-05-22         2026-05-26                3.75               3.35         13  -520.0  -10.666667        stop_loss_hit_at_scan
  INTC INTC260626C00117000          2026-05-21         2026-05-27               13.45              15.15          3   510.0   12.639405        time_exit_at_4pm_scan
  PANW PANW260717C00260000          2026-05-26         2026-05-27               20.45              14.80          2 -1130.0  -27.628362        stop_loss_hit_at_scan
  AVGO AVGO260717C00420000          2026-05-28         2026-05-29               33.40              47.35          1  1395.0   41.766467 take_profit_day1_hit_at_scan
  MRVL MRVL260717C00200000          2026-05-29         2026-06-01               26.00              31.75          1   575.0   22.115385 take_profit_day1_hit_at_scan
  CHTR CHTR260717C00150000          2026-06-01         2026-06-01                8.80               8.00          5  -400.0   -9.090909        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                    detail
2026-06-02T10:45:10.985069-04:00 early_entry_1045 entry_order_submitted    {"alpaca_order_id": "51d9bebc-535b-4ea4-9169-a36179dc3fd4", "contract_symbol": "AMZN260717C00260000", "contracts": 4, "entry_mode": "early", "limit_price": "10.90", "ticker": "AMZN"}
2026-06-02T10:39:06.042989-04:00 early_entry_1035         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-02T10:33:01.232465-04:00 early_entry_1030         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-02T10:26:54.080275-04:00 early_entry_1025         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-02T10:20:49.026891-04:00 early_entry_1020         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-02T10:14:41.660152-04:00 early_entry_1010         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-02T10:08:33.527929-04:00 early_entry_1005         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-02T10:02:27.364407-04:00 early_entry_1000         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-01T11:33:00.369304-04:00             exit           exit_filled                                                         {"contract_symbol": "CHTR260717C00150000", "exit_price": 8.0, "pnl": -400.0, "reason": "stop_loss_hit_at_scan", "ticker": "CHTR"}
2026-06-01T11:27:56.503852-04:00      manage_1130  exit_order_submitted         {"alpaca_order_id": "3b5dbe89-3ac6-41aa-bfe5-f1aeb555569f", "contract_symbol": "CHTR260717C00150000", "limit_price": "7.50", "reason": "stop_loss_hit_at_scan", "ticker": "CHTR"}
2026-06-01T11:17:48.946288-04:00 early_entry_1110          entry_filled                                                                                         {"contract_symbol": "CHTR260717C00150000", "contracts": 5, "filled_price": 8.8, "ticker": "CHTR"}
2026-06-01T11:11:40.991182-04:00 early_entry_1110 entry_order_submitted     {"alpaca_order_id": "86b16257-84f3-4a1e-8f57-17e0cb8449e0", "contract_symbol": "CHTR260717C00150000", "contracts": 5, "entry_mode": "early", "limit_price": "8.80", "ticker": "CHTR"}
2026-06-01T11:05:34.425918-04:00 early_entry_1105         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-01T11:05:34.425918-04:00             exit           exit_filled                                                 {"contract_symbol": "MRVL260717C00200000", "exit_price": 31.75, "pnl": 575.0, "reason": "take_profit_day1_hit_at_scan", "ticker": "MRVL"}
2026-06-01T10:59:27.570705-04:00 early_entry_1055         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-01T10:59:27.570705-04:00      manage_1100  exit_order_submitted {"alpaca_order_id": "9e06dd09-a5ff-4c5e-95d4-d4be59a16dc8", "contract_symbol": "MRVL260717C00200000", "limit_price": "29.70", "reason": "take_profit_day1_hit_at_scan", "ticker": "MRVL"}
2026-06-01T10:53:19.158352-04:00 early_entry_1050         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-01T10:47:11.042971-04:00 early_entry_1045         entry_skipped                                                                                                 {"budget": 5000.0, "entry_limit": 112.5, "reason": "insufficient_cash", "ticker": "ASML"}
2026-06-01T10:41:05.682630-04:00 early_entry_1040         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-06-01T10:34:59.544234-04:00 early_entry_1030         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
```