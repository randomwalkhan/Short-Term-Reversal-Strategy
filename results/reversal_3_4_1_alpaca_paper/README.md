# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-08-25 10:03:57 EDT`
Last slot: `manage_1000`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$90,190.77`
- Portfolio value: `$93,205.77`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  LRCX   open    regular LRCX261016C00310000          1               31.15                33.825          bid_ask_mid                     33.825                    True          3382.5           267.5                8.58748                   1
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  ALNY ALNY260918C00220000          2026-08-17         2026-08-19               14.20              17.60          3  1020.0   23.943662 take_profit_day1_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                   detail
2026-08-25T10:03:57.337923-04:00 early_entry_1000    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T15:00:10.175297-04:00       entry_1500          entry_filled                                                                                      {"contract_symbol": "LRCX261016C00310000", "contracts": 1, "filled_price": 31.15, "ticker": "LRCX"}
2026-08-24T14:48:44.540954-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "ef7cdf3e-4c82-4298-9375-661b666ec551", "contract_symbol": "LRCX261016C00310000", "contracts": 1, "entry_mode": "regular", "limit_price": "31.15", "ticker": "LRCX"}
2026-08-24T12:00:43.006988-04:00 early_entry_1200    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:54:26.810132-04:00 early_entry_1150    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:48:07.497791-04:00 early_entry_1145    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:41:46.984496-04:00 early_entry_1140    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:34:48.602868-04:00 early_entry_1130    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:28:28.624064-04:00 early_entry_1125    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:22:08.459230-04:00 early_entry_1120    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:15:47.839870-04:00 early_entry_1115    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:09:31.275530-04:00 early_entry_1105    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T11:03:03.993525-04:00 early_entry_1100    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:56:39.800696-04:00 early_entry_1055    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:50:17.598631-04:00 early_entry_1050    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:43:56.269078-04:00 early_entry_1040    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:37:38.798522-04:00 early_entry_1035    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:31:22.818730-04:00 early_entry_1030    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:25:07.085760-04:00 early_entry_1025    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-24T10:18:55.308217-04:00 early_entry_1015    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```