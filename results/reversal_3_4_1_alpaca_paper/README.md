# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-29 14:15:49 EDT`
Last slot: `manual`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$94,521.63`
- Portfolio value: `$97,201.63`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  MRVL   open      early MRVL260717C00200000          1                26.0                  26.2          bid_ask_mid                       26.2                    True          2620.0            20.0               0.769231                   0
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
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                    detail
2026-05-29T10:27:54.144898-04:00 early_entry_1020          entry_filled                                                                                        {"contract_symbol": "MRVL260717C00200000", "contracts": 1, "filled_price": 26.0, "ticker": "MRVL"}
2026-05-29T10:21:44.021302-04:00 early_entry_1020 entry_order_submitted    {"alpaca_order_id": "ee94ce56-1778-4d77-8317-e6df9525ca15", "contract_symbol": "MRVL260717C00200000", "contracts": 1, "entry_mode": "early", "limit_price": "26.80", "ticker": "MRVL"}
2026-05-29T10:15:35.264629-04:00 early_entry_1015         entry_skipped                                                 {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "ALNY"}
2026-05-29T10:09:25.831795-04:00 early_entry_1005         entry_skipped                                          {"entry_mode": "early", "option_liquidity_status": "low_open_interest,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "SNPS"}
2026-05-29T10:09:25.831795-04:00             exit           exit_filled                                                {"contract_symbol": "AVGO260717C00420000", "exit_price": 47.35, "pnl": 1395.0, "reason": "take_profit_day1_hit_at_scan", "ticker": "AVGO"}
2026-05-29T10:03:14.971644-04:00 early_entry_1000         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-29T10:03:14.971644-04:00      manage_1000  exit_order_submitted {"alpaca_order_id": "8e7190d6-4868-47fe-a8f2-905a885d34d4", "contract_symbol": "AVGO260717C00420000", "limit_price": "42.05", "reason": "take_profit_day1_hit_at_scan", "ticker": "AVGO"}
2026-05-28T10:07:32.783111-04:00 early_entry_1000          entry_filled                                                                                        {"contract_symbol": "AVGO260717C00420000", "contracts": 1, "filled_price": 33.4, "ticker": "AVGO"}
2026-05-28T10:01:23.351204-04:00 early_entry_1000 entry_order_submitted    {"alpaca_order_id": "a7b7954f-7027-4fe6-bc6b-040c4d748493", "contract_symbol": "AVGO260717C00420000", "contracts": 1, "entry_mode": "early", "limit_price": "36.20", "ticker": "AVGO"}
2026-05-27T15:11:39.018745-04:00       entry_1500         entry_skipped                                                           {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T15:05:23.333934-04:00       entry_1500         entry_skipped                                                           {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T14:59:13.815238-04:00       entry_1500         entry_skipped                                                           {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T14:52:59.210728-04:00       entry_1500         entry_skipped                                                           {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T11:55:12.007255-04:00 early_entry_1155         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:48:57.330665-04:00 early_entry_1145         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:42:48.973748-04:00 early_entry_1140         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:36:41.236063-04:00 early_entry_1135         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:30:32.575558-04:00 early_entry_1130         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:24:23.275408-04:00 early_entry_1120         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:18:10.299261-04:00 early_entry_1115         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
```