# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-08-18 23:44:02 EDT`
Last slot: `share_ext_2340`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$88,026.09`
- Portfolio value: `$92,256.09`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  ALNY exit_submitted    regular ALNY260918C00220000          3                14.2                  16.1          bid_ask_mid                       16.1                    True          4830.0           570.0              13.380282                   1
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  MRVL MRVL260724C00310000          2026-06-22         2026-06-23               35.45              22.45          1 -1300.0  -36.671368        stop_loss_hit_at_scan
  AVGO AVGO260821C00380000          2026-06-25         2026-06-26               30.20              23.85          1  -635.0  -21.026490        stop_loss_hit_at_scan
  DRAM DRAM260731C00073000          2026-06-26         2026-06-29                8.90               6.50          5 -1200.0  -26.966292        stop_loss_hit_at_scan
  GILD GILD260821C00135000          2026-07-09         2026-07-13                5.95               3.70          8 -1800.0  -37.815126        stop_loss_hit_at_scan
  AAPL AAPL260821C00315000          2026-07-14         2026-07-15               11.60              16.60          4  2000.0   43.103448 take_profit_day1_hit_at_scan
  META META260821C00660000          2026-07-13         2026-07-15               47.35              55.90          1   855.0   18.057022 take_profit_day2_hit_at_scan
   TXN  TXN260821C00290000          2026-07-17         2026-07-21               21.05              24.00          2   590.0   14.014252 take_profit_day2_hit_at_scan
  AAPL AAPL260821C00330000          2026-07-20         2026-07-22               10.70               9.45          4  -500.0  -11.682243        stop_loss_hit_at_scan
  PYPL PYPL260821C00055000          2026-07-21         2026-07-23                3.15               2.60         15  -825.0  -17.460317        stop_loss_hit_at_scan
  PYPL PYPL260821C00055000          2026-07-22         2026-07-23                3.25               2.98         15  -405.0   -8.307692        stop_loss_hit_at_scan
  GILD GILD260918C00130000          2026-07-24         2026-07-27                6.70               8.05          7   945.0   20.149254 take_profit_day1_hit_at_scan
   CSX  CSX260918C00052500          2026-07-28         2026-07-29                1.45               1.25         34  -680.0  -13.793103        stop_loss_hit_at_scan
  FAST FAST260918C00045000          2026-07-29         2026-07-29                4.00               3.50         12  -600.0  -12.500000        stop_loss_hit_at_scan
  PYPL PYPL260918C00057500          2026-07-30         2026-07-31                2.92               2.32         16  -960.0  -20.547945        stop_loss_hit_at_scan
   CSX  CSX260918C00050000          2026-08-03         2026-08-04                1.70               1.65         29  -145.0   -2.941176        stop_loss_hit_at_scan
  INTC INTC260918C00100000          2026-08-06         2026-08-07               11.35              10.55          4  -320.0   -7.048458        stop_loss_hit_at_scan
  PYPL PYPL260918C00060000          2026-08-07         2026-08-10                1.71               1.51         28  -560.0  -11.695906        stop_loss_hit_at_scan
  LRCX LRCX260918C00310000          2026-08-10         2026-08-12               27.25              34.05          1   680.0   24.954128 take_profit_day2_hit_at_scan
  PYPL PYPL260918C00057500          2026-08-12         2026-08-13                2.86               3.65         17  1343.0   27.622378 take_profit_day1_hit_at_scan
  AMZN AMZN260918C00265000          2026-08-13         2026-08-17               10.75               8.00          4 -1100.0  -25.581395        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                    detail
2026-08-18T16:02:33.448939-04:00      manage_1600  exit_order_submitted {"alpaca_order_id": "e06d7825-d7d0-497e-b432-ebfd8ee6918f", "contract_symbol": "ALNY260918C00220000", "limit_price": "15.30", "reason": "take_profit_day1_hit_at_scan", "ticker": "ALNY"}
2026-08-18T10:34:30.591828-04:00 early_entry_1030    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T14:54:42.398505-04:00       entry_1500          entry_filled                                                                                        {"contract_symbol": "ALNY260918C00220000", "contracts": 3, "filled_price": 14.2, "ticker": "ALNY"}
2026-08-17T14:48:20.935662-04:00       entry_1500 entry_order_submitted  {"alpaca_order_id": "4fd07ca1-6b58-4b6b-b271-d5003cd265b9", "contract_symbol": "ALNY260918C00220000", "contracts": 3, "entry_mode": "regular", "limit_price": "14.30", "ticker": "ALNY"}
2026-08-17T11:55:21.589049-04:00 early_entry_1155    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:49:01.044926-04:00 early_entry_1145    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:42:45.146081-04:00 early_entry_1140    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:36:25.051734-04:00 early_entry_1135    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:30:03.422895-04:00 early_entry_1130    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:23:47.494369-04:00 early_entry_1120    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:17:28.077612-04:00 early_entry_1115    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:11:06.181584-04:00 early_entry_1110    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T11:04:52.489352-04:00 early_entry_1100    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:58:35.185973-04:00 early_entry_1055    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:52:17.250784-04:00 early_entry_1050    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:45:59.834111-04:00 early_entry_1045    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:39:45.503795-04:00 early_entry_1035    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:33:30.021079-04:00 early_entry_1030    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:27:15.865032-04:00 early_entry_1025    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-17T10:21:01.510073-04:00 early_entry_1020    early_entry_shadow                                                                                                                     {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```