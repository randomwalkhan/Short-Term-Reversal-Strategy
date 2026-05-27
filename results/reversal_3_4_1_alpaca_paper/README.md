# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-26 23:05:08 EDT`
Last slot: `share_ext_2305`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$88,222.43`
- Portfolio value: `$96,652.43`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  INTC exit_submitted    regular INTC260626C00117000          3               13.45                 15.70          bid_ask_mid                      15.70                    True          4710.0           675.0              16.728625                   2
  PANW           open      early PANW260717C00260000          2               20.45                 20.15          bid_ask_mid                      20.15                    True          4030.0           -60.0              -1.466993                   0
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
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                    detail
2026-05-26T16:02:53.627444-04:00      manage_1600  exit_order_submitted        {"alpaca_order_id": "b44a5668-d787-4b80-917d-cff951dc8f5f", "contract_symbol": "INTC260626C00117000", "limit_price": "14.45", "reason": "time_exit_at_4pm_scan", "ticker": "INTC"}
2026-05-26T16:02:53.627444-04:00             exit       exit_not_filled                                                                                                         {"contract_symbol": "INTC260626C00117000", "status": "expired", "ticker": "INTC"}
2026-05-26T13:25:24.718183-04:00 early_entry_1110          entry_filled                                                                                       {"contract_symbol": "PANW260717C00260000", "contracts": 2, "filled_price": 20.45, "ticker": "PANW"}
2026-05-26T11:12:09.227523-04:00 early_entry_1110 entry_order_submitted    {"alpaca_order_id": "f018255d-8911-447e-8321-8e1f5bf59752", "contract_symbol": "PANW260717C00260000", "contracts": 2, "entry_mode": "early", "limit_price": "20.45", "ticker": "PANW"}
2026-05-26T11:05:57.430326-04:00 early_entry_1105         entry_skipped                               {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "ROST"}
2026-05-26T10:59:42.328626-04:00 early_entry_1055         entry_skipped                                                 {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TEAM"}
2026-05-26T10:59:42.328626-04:00             exit           exit_filled                                                        {"contract_symbol": "SBUX260717C00105000", "exit_price": 3.35, "pnl": -520.0, "reason": "stop_loss_hit_at_scan", "ticker": "SBUX"}
2026-05-26T10:53:29.366120-04:00      manage_1100  exit_order_submitted         {"alpaca_order_id": "adda5fbd-15fc-422c-9b62-83850aec48a0", "contract_symbol": "SBUX260717C00105000", "limit_price": "2.92", "reason": "stop_loss_hit_at_scan", "ticker": "SBUX"}
2026-05-26T10:53:29.366120-04:00 early_entry_1050         entry_skipped                                                 {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TEAM"}
2026-05-26T10:47:18.644238-04:00 early_entry_1045         entry_skipped                                                 {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TEAM"}
2026-05-26T10:41:06.481605-04:00 early_entry_1040         entry_skipped                                                                                                                                         {"entry_mode": "early", "reason": "no_candidate"}
2026-05-26T10:34:54.291795-04:00 early_entry_1030         entry_skipped                               {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-26T10:28:36.599915-04:00 early_entry_1025         entry_skipped                               {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-26T10:28:36.599915-04:00      manage_1030  exit_order_submitted {"alpaca_order_id": "dea66ffd-9a9b-4909-96a1-65758b153680", "contract_symbol": "INTC260626C00117000", "limit_price": "15.50", "reason": "take_profit_day2_hit_at_scan", "ticker": "INTC"}
2026-05-26T10:22:24.472094-04:00 early_entry_1020         entry_skipped                               {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "ADSK"}
2026-05-26T10:16:13.343478-04:00 early_entry_1015         entry_skipped                                                            {"entry_mode": "early", "option_liquidity_status": "wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-26T10:09:53.668214-04:00 early_entry_1005         entry_skipped                               {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-26T10:03:44.720190-04:00 early_entry_1000         entry_skipped            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,no_two_sided_quote,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-25T23:57:31.407523-04:00   share_ext_2355         market_closed                                                                                                                                {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:52:27.970798-04:00   share_ext_2350         market_closed                                                                                                                                {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```