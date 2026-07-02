# Reversal 3.5-alpaca-paper.1

Latest checkpoint (ET): `2026-07-02 09:29:44 EDT`
Last slot: `manage_0930`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$93,784.55`
- Portfolio value: `$93,784.55`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

_None_

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  SNPS SNPS260618C00490000          2026-05-13         2026-05-15               46.20              39.90          1  -630.0  -13.636364        stop_loss_hit_at_scan
  INTC INTC260618C00110000          2026-05-18         2026-05-18                9.40               8.65          5  -375.0   -7.978723        stop_loss_hit_at_scan
  PANW PANW260618C00250000          2026-05-19         2026-05-20               16.05              13.65          3  -720.0  -14.953271        stop_loss_hit_at_scan
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
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                   detail
2026-07-01T15:07:39.185717-04:00       entry_1500         entry_skipped                                                          {"entry_mode": "regular", "option_liquidity_status": "wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "XEL"}
2026-07-01T15:01:15.862688-04:00       entry_1500         entry_skipped                                                          {"entry_mode": "regular", "option_liquidity_status": "wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "XEL"}
2026-07-01T14:54:53.334261-04:00       entry_1500         entry_skipped                             {"entry_mode": "regular", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "EXC"}
2026-07-01T14:48:31.804446-04:00       entry_1500         entry_skipped                             {"entry_mode": "regular", "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "reason": "no_trade_low_option_liquidity", "ticker": "EXC"}
2026-07-01T11:35:11.922927-04:00 early_entry_1135    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-07-01T10:42:16.967130-04:00 early_entry_1040    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T16:05:04.964285-04:00       entry_1500      entry_not_filled                                                                                                        {"contract_symbol": "DRAM260821C00071000", "status": "expired", "ticker": "DRAM"}
2026-06-29T14:52:38.392190-04:00       entry_1500 entry_order_submitted {"alpaca_order_id": "adf829b4-7582-44be-b931-21cae76df178", "contract_symbol": "DRAM260821C00071000", "contracts": 4, "entry_mode": "regular", "limit_price": "10.85", "ticker": "DRAM"}
2026-06-29T12:05:38.290090-04:00             exit           exit_filled                                                       {"contract_symbol": "DRAM260731C00073000", "exit_price": 6.5, "pnl": -1200.0, "reason": "stop_loss_hit_at_scan", "ticker": "DRAM"}
2026-06-29T11:59:05.309758-04:00 early_entry_1155    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:52:35.576964-04:00 early_entry_1150    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:45:58.449257-04:00 early_entry_1145    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:39:27.604285-04:00 early_entry_1135    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:32:53.946055-04:00 early_entry_1130    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:26:12.352944-04:00 early_entry_1125    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:15:46.404569-04:00 early_entry_1115    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:08:29.050985-04:00 early_entry_1105    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T11:01:53.158416-04:00 early_entry_1100    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:22:40.942806-04:00 early_entry_1020    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-06-29T10:15:36.101830-04:00 early_entry_1015    early_entry_shadow                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
```