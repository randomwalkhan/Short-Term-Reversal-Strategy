# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-10-30 23:59:51 EDT`
Last slot: `share_ext_2355`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$77,115.18`
- Portfolio value: `$80,875.18`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode    contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
   CEG   open    regular CEG261218C00260000          2                19.7                  20.8          bid_ask_mid                       20.8                    True          4160.0           220.0               5.583756                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
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
  CSCO CSCO261120C00115000          2026-10-14         2026-10-19                5.85               2.96          8 -2312.0  -49.401709        stop_loss_hit_at_scan
   CEG  CEG261120C00270000          2026-10-16         2026-10-19               17.10              14.00          2  -620.0  -18.128655        stop_loss_hit_at_scan
   ADP  ADP261120C00290000          2026-10-19         2026-10-20                9.70              10.80          5   550.0   11.340206 take_profit_day1_hit_at_scan
  TEAM TEAM261120C00230000          2026-10-22         2026-10-23               18.80              16.70          2  -420.0  -11.170213        stop_loss_hit_at_scan
   WMT  WMT261127C00119000          2026-10-27         2026-10-28                4.65               3.70         10  -950.0  -20.430108        stop_loss_hit_at_scan
  MSTR MSTR261218C00140000          2026-10-28         2026-10-30               15.50               8.80          3 -2010.0  -43.225806        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                 detail
2026-10-30T14:58:24.426355-04:00       entry_1500          entry_filled                                                                                       {"contract_symbol": "CEG261218C00260000", "contracts": 2, "filled_price": 19.7, "ticker": "CEG"}
2026-10-30T14:52:12.691492-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "a6f747c1-2804-48a6-99dc-e2a8fbce4aa9", "contract_symbol": "CEG261218C00260000", "contracts": 2, "entry_mode": "regular", "limit_price": "20.20", "ticker": "CEG"}
2026-10-30T11:59:23.959526-04:00 early_entry_1155    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:53:14.421258-04:00 early_entry_1150    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:47:04.657676-04:00 early_entry_1145    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:40:52.776981-04:00 early_entry_1140    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:34:32.922126-04:00 early_entry_1130    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:28:15.841704-04:00 early_entry_1125    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:21:57.751956-04:00 early_entry_1120    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:15:39.357902-04:00 early_entry_1115    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:09:28.109080-04:00 early_entry_1105    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T11:03:18.277904-04:00 early_entry_1100    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:57:09.958516-04:00 early_entry_1055    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:51:02.999240-04:00 early_entry_1050    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:44:54.308536-04:00 early_entry_1040    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:38:46.565299-04:00 early_entry_1035    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:32:38.383824-04:00 early_entry_1030    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:26:11.990274-04:00 early_entry_1025    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:19:44.872781-04:00 early_entry_1015    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-30T10:13:37.964405-04:00 early_entry_1010    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```