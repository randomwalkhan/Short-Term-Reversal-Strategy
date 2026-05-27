# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-27 11:24:23 EDT`
Last slot: `manage_1130`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$95,726.88`
- Portfolio value: `$95,726.88`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

_None_

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
```

## Recent Events

```text
                    timestamp_et             slot           event_type                                                                                                                                                                             detail
2026-05-27T11:24:23.275408-04:00 early_entry_1120        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:18:10.299261-04:00 early_entry_1115        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:11:58.509133-04:00 early_entry_1110        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:05:52.604228-04:00 early_entry_1105        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:59:45.771179-04:00 early_entry_1055        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:53:36.022473-04:00 early_entry_1050        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:47:25.850725-04:00 early_entry_1045        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:41:11.964523-04:00 early_entry_1040        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:34:59.298014-04:00 early_entry_1030        entry_skipped                                                                                           {"budget": 5000.0, "entry_limit": 63.0, "reason": "insufficient_cash", "ticker": "SNPS"}
2026-05-27T10:28:50.092346-04:00 early_entry_1025        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:22:38.211342-04:00 early_entry_1020        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:16:27.646862-04:00 early_entry_1015        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:10:15.784488-04:00 early_entry_1010        entry_skipped                                                                                                                                  {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:10:15.784488-04:00             exit          exit_filled                                                {"contract_symbol": "PANW260717C00260000", "exit_price": 14.8, "pnl": -1130.0, "reason": "stop_loss_hit_at_scan", "ticker": "PANW"}
2026-05-27T10:04:03.735411-04:00 early_entry_1000        entry_skipped                                                                                           {"budget": 5000.0, "entry_limit": 65.0, "reason": "insufficient_cash", "ticker": "SNPS"}
2026-05-27T10:04:03.735411-04:00      manage_1000 exit_order_submitted {"alpaca_order_id": "844180c3-400a-4c6b-9f73-b3c1b512e866", "contract_symbol": "PANW260717C00260000", "limit_price": "14.05", "reason": "stop_loss_hit_at_scan", "ticker": "PANW"}
2026-05-27T09:33:35.120835-04:00             exit          exit_filled                                                 {"contract_symbol": "INTC260626C00117000", "exit_price": 15.15, "pnl": 510.0, "reason": "time_exit_at_4pm_scan", "ticker": "INTC"}
2026-05-26T16:02:53.627444-04:00             exit      exit_not_filled                                                                                                  {"contract_symbol": "INTC260626C00117000", "status": "expired", "ticker": "INTC"}
2026-05-26T16:02:53.627444-04:00      manage_1600 exit_order_submitted {"alpaca_order_id": "b44a5668-d787-4b80-917d-cff951dc8f5f", "contract_symbol": "INTC260626C00117000", "limit_price": "14.45", "reason": "time_exit_at_4pm_scan", "ticker": "INTC"}
2026-05-26T13:25:24.718183-04:00 early_entry_1110         entry_filled                                                                                {"contract_symbol": "PANW260717C00260000", "contracts": 2, "filled_price": 20.45, "ticker": "PANW"}
```