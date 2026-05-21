# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-21 12:46:43 EDT`
Last slot: `manual`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$93,068.59`
- Portfolio value: `$96,688.59`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  TTWO   open      early TTWO260717C00240000          2                17.0                  18.6          bid_ask_mid                       18.6                    True          3720.0           320.0               9.411765                   1
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
                    timestamp_et             slot    event_type                                                                                                                                                      detail
2026-05-21T11:59:54.060175-04:00 early_entry_1155 entry_skipped                                                                                                           {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:53:44.244584-04:00 early_entry_1150 entry_skipped              {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T11:47:32.644554-04:00 early_entry_1145 entry_skipped                                                                                                           {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:41:10.828251-04:00 early_entry_1140 entry_skipped              {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T11:34:59.275965-04:00 early_entry_1130 entry_skipped                                                                                                           {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:28:49.809880-04:00 early_entry_1125 entry_skipped              {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T11:22:36.879635-04:00 early_entry_1120 entry_skipped              {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T11:16:27.628893-04:00 early_entry_1115 entry_skipped                               {"entry_mode": "early", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ALNY"}
2026-05-21T11:10:17.360503-04:00 early_entry_1110 entry_skipped                                                                                                           {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T11:04:07.561903-04:00 early_entry_1100 entry_skipped                                                                                                           {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T10:57:47.255750-04:00 early_entry_1055 entry_skipped {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FAST"}
2026-05-21T10:51:36.138066-04:00 early_entry_1050 entry_skipped {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FAST"}
2026-05-21T10:45:26.333850-04:00 early_entry_1045 entry_skipped              {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:39:14.366488-04:00 early_entry_1035 entry_skipped              {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:33:05.062811-04:00 early_entry_1030 entry_skipped              {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:26:56.960797-04:00 early_entry_1025 entry_skipped                    {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "MAR"}
2026-05-21T10:20:47.021865-04:00 early_entry_1020 entry_skipped                                                                                                           {"entry_mode": "early", "reason": "no_candidate"}
2026-05-21T10:14:35.263301-04:00 early_entry_1010 entry_skipped  {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "ADP"}
2026-05-21T10:08:27.134192-04:00 early_entry_1005 entry_skipped                   {"entry_mode": "early", "option_liquidity_status": "low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "FTNT"}
2026-05-21T10:02:15.629333-04:00 early_entry_1000 entry_skipped {"entry_mode": "early", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "MELI"}
```