# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-11-17 22:58:39 EST`
Last slot: `share_ext_2255`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$76,842.63`
- Portfolio value: `$79,762.63`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker         status entry_mode    contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
   APP exit_submitted    regular APP261218C00400000          1                31.3                 29.35          bid_ask_mid                      29.35                    True          2935.0          -195.0              -6.230032                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
    ZS   ZS261120C00200000          2026-10-02         2026-10-05               14.95              17.05          3   630.0   14.046823 take_profit_day1_hit_at_scan
  SOXL SOXL261120C00165000          2026-10-05         2026-10-07               25.75              17.45          1  -830.0  -32.233010        stop_loss_hit_at_scan
   CEG  CEG261120C00300000          2026-10-07         2026-10-08               20.60              21.40          2   160.0    3.883495        stop_loss_hit_at_scan
  CSCO CSCO261120C00115000          2026-10-08         2026-10-09                7.25               8.40          6   690.0   15.862069 take_profit_day1_hit_at_scan
  CTSH CTSH261120C00060000          2026-10-09         2026-10-12                3.70               3.30         13  -520.0  -10.810811        stop_loss_hit_at_scan
   CEG  CEG261120C00290000          2026-10-12         2026-10-13               18.70              21.30          2   520.0   13.903743 take_profit_day1_hit_at_scan
  SNPS SNPS261120C00500000          2026-10-13         2026-10-14               25.50              20.00          1  -550.0  -21.568627        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-15         2026-10-16               19.50              17.10          2  -480.0  -12.307692        stop_loss_hit_at_scan
  CSCO CSCO261120C00115000          2026-10-14         2026-10-19                5.85               2.96          8 -2312.0  -49.401709        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-16         2026-10-19               17.10              14.00          2  -620.0  -18.128655        stop_loss_hit_at_scan
   ADP  ADP261120C00290000          2026-10-19         2026-10-20                9.70              10.80          5   550.0   11.340206 take_profit_day1_hit_at_scan
  TEAM TEAM261120C00230000          2026-10-22         2026-10-23               18.80              16.70          2  -420.0  -11.170213        stop_loss_hit_at_scan
   WMT  WMT261127C00119000          2026-10-27         2026-10-28                4.65               3.70         10  -950.0  -20.430108        stop_loss_hit_at_scan
  MSTR MSTR261218C00140000          2026-10-28         2026-10-30               15.50               8.80          3 -2010.0  -43.225806        stop_loss_hit_at_scan
   CEG  CEG261218C00260000          2026-10-30         2026-11-02               19.70              22.60          2   580.0   14.720812 take_profit_day1_hit_at_scan
   CEG  CEG261218C00260000          2026-11-02         2026-11-03               18.20              21.00          2   560.0   15.384615 take_profit_day1_hit_at_scan
  MDLZ MDLZ261218C00067500          2026-11-03         2026-11-04                1.40               1.65         35   875.0   17.857143 take_profit_day1_hit_at_scan
  ORLY ORLY261218C00095000          2026-11-05         2026-11-05                2.00               1.55         25 -1125.0  -22.500000        stop_loss_hit_at_scan
  MDLZ MDLZ261218C00065000          2026-11-06         2026-11-16                3.20               2.45         15 -1125.0  -23.437500        stop_loss_hit_at_scan
  QCOM QCOM261218C00170000          2026-11-16         2026-11-17               11.15               9.05          4  -840.0  -18.834081        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                 detail
2026-11-17T16:08:35.504886-05:00      manage_1600  exit_order_submitted       {"alpaca_order_id": "941d62a8-7c99-4081-973f-a64beb20d0dc", "contract_symbol": "APP261218C00400000", "limit_price": "27.60", "reason": "stop_loss_hit_at_scan", "ticker": "APP"}
2026-11-17T14:57:45.304642-05:00       entry_1500          entry_filled                                                                                       {"contract_symbol": "APP261218C00400000", "contracts": 1, "filled_price": 31.3, "ticker": "APP"}
2026-11-17T14:51:28.810470-05:00       entry_1500 entry_order_submitted {"alpaca_order_id": "d8bbe0da-b7ed-4f21-a075-d606254f2297", "contract_symbol": "APP261218C00400000", "contracts": 1, "entry_mode": "regular", "limit_price": "31.80", "ticker": "APP"}
2026-11-17T11:58:32.745337-05:00 early_entry_1155    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:52:14.987372-05:00 early_entry_1150    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:46:05.778029-05:00 early_entry_1145    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:39:51.295334-05:00 early_entry_1135    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:33:38.361264-05:00 early_entry_1130    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:27:35.488811-05:00 early_entry_1125    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:21:23.136715-05:00 early_entry_1120    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:15:09.609751-05:00 early_entry_1115    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:09:02.268898-05:00 early_entry_1105    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T11:02:51.193171-05:00 early_entry_1100    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:56:47.158804-05:00 early_entry_1055    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:50:40.159146-05:00 early_entry_1050    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:44:30.356649-05:00 early_entry_1040    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:38:23.278986-05:00 early_entry_1035    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:32:22.510911-05:00 early_entry_1030    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:26:20.282022-05:00 early_entry_1025    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-17T10:20:18.351672-05:00 early_entry_1020    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```