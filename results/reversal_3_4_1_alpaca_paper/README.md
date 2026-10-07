# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-10-07 10:50:43 EDT`
Last slot: `manage_1100`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$87,003.06`
- Portfolio value: `$87,003.06`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

_None_

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  PYPL PYPL260918C00060000          2026-08-07         2026-08-10                1.71               1.51         28  -560.0  -11.695906        stop_loss_hit_at_scan
  LRCX LRCX260918C00310000          2026-08-10         2026-08-12               27.25              34.05          1   680.0   24.954128 take_profit_day2_hit_at_scan
  PYPL PYPL260918C00057500          2026-08-12         2026-08-13                2.86               3.65         17  1343.0   27.622378 take_profit_day1_hit_at_scan
  AMZN AMZN260918C00265000          2026-08-13         2026-08-17               10.75               8.00          4 -1100.0  -25.581395        stop_loss_hit_at_scan
  ALNY ALNY260918C00220000          2026-08-17         2026-08-19               14.20              17.60          3  1020.0   23.943662 take_profit_day1_hit_at_scan
  LRCX LRCX261016C00310000          2026-08-24         2026-08-27               31.15              30.90          1   -25.0   -0.802568        time_exit_at_4pm_scan
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
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                  detail
2026-10-07T10:50:43.494777-04:00 early_entry_1050    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:44:27.843203-04:00 early_entry_1040    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:38:10.250817-04:00 early_entry_1035    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:31:51.363163-04:00 early_entry_1030    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:25:32.450628-04:00 early_entry_1025    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:19:15.354443-04:00 early_entry_1015    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:12:53.095250-04:00 early_entry_1010    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:06:35.838038-04:00 early_entry_1005    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:00:12.728106-04:00 early_entry_1000    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-07T10:00:12.728106-04:00             exit           exit_filled                                                     {"contract_symbol": "SOXL261120C00165000", "exit_price": 17.45, "pnl": -830.0, "reason": "stop_loss_hit_at_scan", "ticker": "SOXL"}
2026-10-07T09:55:08.694126-04:00      manage_1000  exit_order_submitted      {"alpaca_order_id": "5c761d4e-7dee-4459-a032-661b31dcb339", "contract_symbol": "SOXL261120C00165000", "limit_price": "17.05", "reason": "stop_loss_hit_at_scan", "ticker": "SOXL"}
2026-10-06T16:01:49.612798-04:00       entry_1500      entry_not_filled                                                                                                       {"contract_symbol": "ABNB261120C00160000", "status": "expired", "ticker": "ABNB"}
2026-10-06T14:49:14.283865-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "6a971e9f-ec13-4c0b-93c1-08a7b1ce6b13", "contract_symbol": "ABNB261120C00160000", "contracts": 5, "entry_mode": "regular", "limit_price": "9.60", "ticker": "ABNB"}
2026-10-06T12:00:44.232676-04:00 early_entry_1200    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:54:22.492889-04:00 early_entry_1150    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:47:57.272118-04:00 early_entry_1145    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:41:39.139031-04:00 early_entry_1140    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:35:14.411335-04:00 early_entry_1135    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:28:58.294909-04:00 early_entry_1125    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-06T11:22:33.513388-04:00 early_entry_1120    early_entry_shadow                                                                                                                   {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```