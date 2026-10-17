# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-10-16 23:57:28 EDT`
Last slot: `share_ext_2355`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$78,719.93`
- Portfolio value: `$84,067.93`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  CSCO exit_submitted    regular CSCO261120C00115000          8                5.85                 3.005          bid_ask_mid                      3.005                    True          2404.0         -2276.0             -48.632479                   2
   CEG           open    regular  CEG261120C00270000          2               17.10                17.250          bid_ask_mid                     17.250                    True          3450.0            30.0               0.877193                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  MNST MNST261016C00048000          2026-08-26         2026-08-27                1.95               1.05         25 -2250.0  -46.153846        stop_loss_hit_at_scan
  MRVL MRVL261016C00240000          2026-08-27         2026-08-28               20.25              15.45          1  -480.0  -23.703704        stop_loss_hit_at_scan
  SHOP SHOP261016C00155000          2026-08-28         2026-09-09                9.30               2.62          5 -3340.0  -71.827957        stop_loss_hit_at_scan
  CRWD CRWD261016C00210000          2026-09-08         2026-09-09               14.45              12.80          3  -495.0  -11.418685        stop_loss_hit_at_scan
  CRWD CRWD261016C00210000          2026-09-09         2026-09-10               13.00              15.20          3   660.0   16.923077        stop_loss_hit_at_scan
  MSTR MSTR261016C00130000          2026-09-10         2026-09-11               11.70              15.40          4  1480.0   31.623932 take_profit_day1_hit_at_scan
  PYPL PYPL261016C00055000          2026-09-16         2026-09-16                1.27               1.03         39  -936.0  -18.897638        stop_loss_hit_at_scan
   WMT  WMT261023C00108000          2026-09-17         2026-09-21                2.72               2.25         18  -846.0  -17.279412        stop_loss_hit_at_scan
  CRWD CRWD261023C00240000          2026-09-18         2026-09-21               16.05              16.95          3   270.0    5.607477        stop_loss_hit_at_scan
  MSTR MSTR261120C00160000          2026-09-25         2026-09-28               17.35              15.40          2  -390.0  -11.239193        stop_loss_hit_at_scan
  META META261120C00735000          2026-09-30         2026-10-01               48.80              43.15          1  -565.0  -11.577869        stop_loss_hit_at_scan
  MSTR MSTR261120C00155000          2026-09-29         2026-10-01               16.05              18.80          3   825.0   17.133956 take_profit_day2_hit_at_scan
    ZS   ZS261120C00200000          2026-10-02         2026-10-05               14.95              17.05          3   630.0   14.046823 take_profit_day1_hit_at_scan
  SOXL SOXL261120C00165000          2026-10-05         2026-10-07               25.75              17.45          1  -830.0  -32.233010        stop_loss_hit_at_scan
   CEG  CEG261120C00300000          2026-10-07         2026-10-08               20.60              21.40          2   160.0    3.883495        stop_loss_hit_at_scan
  CSCO CSCO261120C00115000          2026-10-08         2026-10-09                7.25               8.40          6   690.0   15.862069 take_profit_day1_hit_at_scan
  CTSH CTSH261120C00060000          2026-10-09         2026-10-12                3.70               3.30         13  -520.0  -10.810811        stop_loss_hit_at_scan
   CEG  CEG261120C00290000          2026-10-12         2026-10-13               18.70              21.30          2   520.0   13.903743 take_profit_day1_hit_at_scan
  SNPS SNPS261120C00500000          2026-10-13         2026-10-14               25.50              20.00          1  -550.0  -21.568627        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-15         2026-10-16               19.50              17.10          2  -480.0  -12.307692        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                 detail
2026-10-16T16:01:05.806617-04:00      manage_1600  exit_order_submitted      {"alpaca_order_id": "492f0ed8-6e32-46c5-96bb-669f4b6d5789", "contract_symbol": "CSCO261120C00115000", "limit_price": "2.93", "reason": "stop_loss_hit_at_scan", "ticker": "CSCO"}
2026-10-16T16:01:05.806617-04:00             exit       exit_not_filled                                                                                                      {"contract_symbol": "CSCO261120C00115000", "status": "expired", "ticker": "CSCO"}
2026-10-16T14:55:11.307347-04:00       entry_1500          entry_filled                                                                                       {"contract_symbol": "CEG261120C00270000", "contracts": 2, "filled_price": 17.1, "ticker": "CEG"}
2026-10-16T14:48:58.430801-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "dab7bd82-d416-4df2-a1ef-b9ac0b8fc68c", "contract_symbol": "CEG261120C00270000", "contracts": 2, "entry_mode": "regular", "limit_price": "17.50", "ticker": "CEG"}
2026-10-16T11:55:36.492421-04:00 early_entry_1155    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:49:27.535893-04:00 early_entry_1145    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:43:19.028629-04:00 early_entry_1140    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:37:10.612622-04:00             exit           exit_filled                                                       {"contract_symbol": "CEG261120C00270000", "exit_price": 17.1, "pnl": -480.0, "reason": "stop_loss_hit_at_scan", "ticker": "CEG"}
2026-10-16T11:37:10.612622-04:00 early_entry_1135    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:30:57.769735-04:00 early_entry_1130    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:30:57.769735-04:00      manage_1130  exit_order_submitted       {"alpaca_order_id": "98ea536a-bd09-4c24-9f6c-901b6d3948a1", "contract_symbol": "CEG261120C00270000", "limit_price": "16.90", "reason": "stop_loss_hit_at_scan", "ticker": "CEG"}
2026-10-16T11:24:48.968131-04:00 early_entry_1120    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:18:40.395637-04:00 early_entry_1115    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:12:32.457525-04:00 early_entry_1110    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:06:24.480958-04:00 early_entry_1105    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T11:00:14.913277-04:00 early_entry_1100    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:54:07.275588-04:00 early_entry_1050    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:47:58.353766-04:00 early_entry_1045    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:41:49.985590-04:00 early_entry_1040    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-16T10:35:43.743663-04:00 early_entry_1035    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```