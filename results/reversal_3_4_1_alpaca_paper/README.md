# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-21 11:16:27 EDT`
Last slot: `early_entry_1115`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$93,068.59`
- Portfolio value: `$96,548.59`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  TTWO   open      early TTWO260717C00240000          2                17.0                  18.0          bid_ask_mid                       18.0                    True          3600.0           200.0               5.882353                   1
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
2026-05-21T11:16:27.628893-04:00 early_entry_1115         entry_skipped                                                          {"entry_mode": "early", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ALNY"}
2026-05-21T11:10:17.360503-04:00 early_entry_1110         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:04:07.561903-04:00 early_entry_1100         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T10:57:47.255750-04:00 early_entry_1055         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FAST"}
2026-05-21T10:51:36.138066-04:00 early_entry_1050         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FAST"}
2026-05-21T10:45:26.333850-04:00 early_entry_1045         entry_skipped                                         {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:39:14.366488-04:00 early_entry_1035         entry_skipped                                         {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:33:05.062811-04:00 early_entry_1030         entry_skipped                                         {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:26:56.960797-04:00 early_entry_1025         entry_skipped                                               {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "MAR"}
2026-05-21T10:20:47.021865-04:00 early_entry_1020         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T10:14:35.263301-04:00 early_entry_1010         entry_skipped                             {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:08:27.134192-04:00 early_entry_1005         entry_skipped                                              {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-21T10:02:15.629333-04:00 early_entry_1000         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "MELI"}
2026-05-20T12:15:57.679645-04:00 early_entry_1115          entry_filled                                                                                     {"contract_symbol": "TTWO260717C00240000", "contracts": 2, "filled_price": 17.0, "ticker": "TTWO"}
2026-05-20T11:19:03.434065-04:00 early_entry_1115 entry_order_submitted {"alpaca_order_id": "3e3c8dfc-2286-4e36-9ffb-4cf8435d27c4", "contract_symbol": "TTWO260717C00240000", "contracts": 2, "entry_mode": "early", "limit_price": "17.20", "ticker": "TTWO"}
2026-05-20T11:12:45.922551-04:00 early_entry_1110         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T11:06:27.663743-04:00 early_entry_1105         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T11:00:07.702182-04:00 early_entry_1100         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:53:49.849791-04:00 early_entry_1050         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
2026-05-20T10:47:32.363203-04:00 early_entry_1045         entry_skipped                            {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "TTWO"}
```