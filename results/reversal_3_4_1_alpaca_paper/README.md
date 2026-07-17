# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-07-17 19:20:32 EDT`
Last slot: `share_ext_1920`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$90,628.50`
- Portfolio value: `$94,438.50`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode    contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
   TXN   open    regular TXN260821C00290000          2               21.05                20.425          bid_ask_mid                     20.425                    True          4085.0          -125.0              -2.969121                   0
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  TTWO TTWO260717C00240000          2026-05-20         2026-05-21               17.00              19.00          2   400.0   11.764706 take_profit_day1_hit_at_scan
  SBUX SBUX260717C00105000          2026-05-22         2026-05-26                3.75               3.35         13  -520.0  -10.666667        stop_loss_hit_at_scan
  INTC INTC260626C00117000          2026-05-21         2026-05-27               13.45              15.15          3   510.0   12.639405        time_exit_at_4pm_scan
  PANW PANW260717C00260000          2026-05-26         2026-05-27               20.45              14.80          2 -1130.0  -27.628362        stop_loss_hit_at_scan
  AVGO AVGO260717C00420000          2026-05-28         2026-05-29               33.40              47.35          1  1395.0   41.766467 take_profit_day1_hit_at_scan
  MRVL MRVL260717C00200000          2026-05-29         2026-06-01               26.00              31.75          1   575.0   22.115385 take_profit_day1_hit_at_scan
  CHTR CHTR260717C00150000          2026-06-01         2026-06-01                8.80               8.00          5  -400.0   -9.090909        stop_loss_hit_at_scan
  AMZN AMZN260717C00260000          2026-06-02         2026-06-04               10.90               8.40          4 -1000.0  -22.935780        stop_loss_hit_at_scan
  FTNT FTNT260717C00155000          2026-06-03         2026-06-04                6.60               7.40          7   560.0   12.121212 take_profit_day1_hit_at_scan
  TEAM TEAM260717C00100000          2026-06-08         2026-06-09                9.00               8.50          5  -250.0   -5.555556        stop_loss_hit_at_scan
  PAYX PAYX260717C00100000          2026-06-11         2026-06-12                5.50               4.40          9  -990.0  -20.000000        stop_loss_hit_at_scan
  ROST ROST260717C00240000          2026-06-15         2026-06-16                5.60               4.80          8  -640.0  -14.285714        stop_loss_hit_at_scan
  DRAM DRAM260717C00069000          2026-06-16         2026-06-17                7.60               8.15          6   330.0    7.236842        stop_loss_hit_at_scan
   WMT  WMT260724C00120000          2026-06-18         2026-06-23                2.65               3.55         18  1620.0   33.962264 take_profit_day2_hit_at_scan
  MRVL MRVL260724C00310000          2026-06-22         2026-06-23               35.45              22.45          1 -1300.0  -36.671368        stop_loss_hit_at_scan
  AVGO AVGO260821C00380000          2026-06-25         2026-06-26               30.20              23.85          1  -635.0  -21.026490        stop_loss_hit_at_scan
  DRAM DRAM260731C00073000          2026-06-26         2026-06-29                8.90               6.50          5 -1200.0  -26.966292        stop_loss_hit_at_scan
  GILD GILD260821C00135000          2026-07-09         2026-07-13                5.95               3.70          8 -1800.0  -37.815126        stop_loss_hit_at_scan
  AAPL AAPL260821C00315000          2026-07-14         2026-07-15               11.60              16.60          4  2000.0   43.103448 take_profit_day1_hit_at_scan
  META META260821C00660000          2026-07-13         2026-07-15               47.35              55.90          1   855.0   18.057022 take_profit_day2_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                 detail
2026-07-17T14:58:14.413684-04:00       entry_1500          entry_filled                                                                                      {"contract_symbol": "TXN260821C00290000", "contracts": 2, "filled_price": 21.05, "ticker": "TXN"}
2026-07-17T14:51:05.188951-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "52b5f968-17aa-4599-8080-ade2a8edd057", "contract_symbol": "TXN260821C00290000", "contracts": 2, "entry_mode": "regular", "limit_price": "21.05", "ticker": "TXN"}
2026-07-17T11:57:02.823582-04:00 early_entry_1155    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:50:01.557607-04:00 early_entry_1150    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:43:00.631094-04:00 early_entry_1140    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:36:00.566899-04:00 early_entry_1135    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:28:57.946758-04:00 early_entry_1125    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:21:51.599042-04:00 early_entry_1120    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:14:44.698091-04:00 early_entry_1110    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:07:34.850284-04:00 early_entry_1105    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T11:00:20.804321-04:00 early_entry_1100    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:53:18.832349-04:00 early_entry_1050    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:46:15.943211-04:00 early_entry_1045    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:39:13.186774-04:00 early_entry_1035    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:32:01.875516-04:00 early_entry_1030    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:24:56.709904-04:00 early_entry_1020    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:17:47.150965-04:00 early_entry_1015    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:10:47.090257-04:00 early_entry_1010    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-17T10:03:46.763748-04:00 early_entry_1000    early_entry_shadow                                                                                                                  {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-16T15:09:32.643377-04:00       entry_1500         entry_skipped                                      {"entry_mode": "regular", "option_liquidity_status": "low_open_interest,low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "MPWR"}
```