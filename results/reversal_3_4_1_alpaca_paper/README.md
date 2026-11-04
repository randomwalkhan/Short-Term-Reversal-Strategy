# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-11-04 10:40:36 EST`
Last slot: `manage_1030`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$83,067.25`
- Portfolio value: `$83,067.25`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

_None_

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  CSCO CSCO261120C00115000          2026-10-14         2026-10-19                5.85               2.96          8 -2312.0  -49.401709        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-16         2026-10-19               17.10              14.00          2  -620.0  -18.128655        stop_loss_hit_at_scan
   ADP  ADP261120C00290000          2026-10-19         2026-10-20                9.70              10.80          5   550.0   11.340206 take_profit_day1_hit_at_scan
  TEAM TEAM261120C00230000          2026-10-22         2026-10-23               18.80              16.70          2  -420.0  -11.170213        stop_loss_hit_at_scan
   WMT  WMT261127C00119000          2026-10-27         2026-10-28                4.65               3.70         10  -950.0  -20.430108        stop_loss_hit_at_scan
  MSTR MSTR261218C00140000          2026-10-28         2026-10-30               15.50               8.80          3 -2010.0  -43.225806        stop_loss_hit_at_scan
   CEG  CEG261218C00260000          2026-10-30         2026-11-02               19.70              22.60          2   580.0   14.720812 take_profit_day1_hit_at_scan
   CEG  CEG261218C00260000          2026-11-02         2026-11-03               18.20              21.00          2   560.0   15.384615 take_profit_day1_hit_at_scan
  MDLZ MDLZ261218C00067500          2026-11-03         2026-11-04                1.40               1.65         35   875.0   17.857143 take_profit_day1_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                   detail
2026-11-04T10:40:36.232601-05:00 early_entry_1040    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:40:36.232601-05:00             exit           exit_filled                                                 {"contract_symbol": "MDLZ261218C00067500", "exit_price": 1.65, "pnl": 875.0, "reason": "take_profit_day1_hit_at_scan", "ticker": "MDLZ"}
2026-11-04T10:34:21.526391-05:00 early_entry_1030    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:28:07.692660-05:00 early_entry_1025    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:21:55.123444-05:00 early_entry_1020    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:15:43.316808-05:00 early_entry_1015    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:09:27.734782-05:00 early_entry_1005    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:03:13.825406-05:00 early_entry_1000    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T09:53:05.499780-05:00      manage_1000  exit_order_submitted {"alpaca_order_id": "7db01927-46f4-4246-9596-afcc8423ca29", "contract_symbol": "MDLZ261218C00067500", "limit_price": "1.65", "reason": "take_profit_day1_hit_at_scan", "ticker": "MDLZ"}
2026-11-03T15:05:35.073971-05:00       entry_1500          entry_filled                                                                                       {"contract_symbol": "MDLZ261218C00067500", "contracts": 35, "filled_price": 1.4, "ticker": "MDLZ"}
2026-11-03T14:49:11.630760-05:00       entry_1500 entry_order_submitted {"alpaca_order_id": "31c78866-1452-43d6-bf1c-6f5449305b8d", "contract_symbol": "MDLZ261218C00067500", "contracts": 35, "entry_mode": "regular", "limit_price": "1.40", "ticker": "MDLZ"}
2026-11-03T12:00:59.557674-05:00 early_entry_1200    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:54:46.586525-05:00 early_entry_1150    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:48:35.777833-05:00 early_entry_1145    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:42:25.944735-05:00 early_entry_1140    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:36:15.220783-05:00 early_entry_1135    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:30:02.258135-05:00 early_entry_1130    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:23:49.585598-05:00 early_entry_1120    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:17:36.688937-05:00 early_entry_1115    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-03T11:11:25.532811-05:00 early_entry_1110    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```