# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-29 07:26:20 EDT`
Last slot: `share_ext_0725`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$92,386.67`
- Portfolio value: `$95,936.67`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  AVGO   open      early AVGO260717C00420000          1                33.4                  36.0     last_price_stale                        NaN                   False          3600.0           260.0               7.784431                   1
```

## Closed Trades

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price  contracts     pnl  return_pct                  exit_reason
  AVGO AVGO260612C00425000          2026-05-12         2026-05-12               28.95              24.55          1  -440.0  -15.198618        stop_loss_hit_at_scan
  INTC INTC260618C00115000          2026-05-14         2026-05-15               13.30               8.75          3 -1365.0  -34.210526        stop_loss_hit_at_scan
  SNPS SNPS260618C00490000          2026-05-13         2026-05-15               46.20              39.90          1  -630.0  -13.636364        stop_loss_hit_at_scan
  INTC INTC260618C00110000          2026-05-18         2026-05-18                9.40               8.65          5  -375.0   -7.978723        stop_loss_hit_at_scan
  PANW PANW260618C00250000          2026-05-19         2026-05-20               16.05              13.65          3  -720.0  -14.953271        stop_loss_hit_at_scan
  TTWO TTWO260717C00240000          2026-05-20         2026-05-21               17.00              19.00          2   400.0   11.764706 take_profit_day1_hit_at_scan
  SBUX SBUX260717C00105000          2026-05-22         2026-05-26                3.75               3.35         13  -520.0  -10.666667        stop_loss_hit_at_scan
  INTC INTC260626C00117000          2026-05-21         2026-05-27               13.45              15.15          3   510.0   12.639405        time_exit_at_4pm_scan
  PANW PANW260717C00260000          2026-05-26         2026-05-27               20.45              14.80          2 -1130.0  -27.628362        stop_loss_hit_at_scan
```

## Recent Events

```text
                    timestamp_et             slot            event_type                                                                                                                                                                                 detail
2026-05-28T10:07:32.783111-04:00 early_entry_1000          entry_filled                                                                                     {"contract_symbol": "AVGO260717C00420000", "contracts": 1, "filled_price": 33.4, "ticker": "AVGO"}
2026-05-28T10:01:23.351204-04:00 early_entry_1000 entry_order_submitted {"alpaca_order_id": "a7b7954f-7027-4fe6-bc6b-040c4d748493", "contract_symbol": "AVGO260717C00420000", "contracts": 1, "entry_mode": "early", "limit_price": "36.20", "ticker": "AVGO"}
2026-05-27T15:11:39.018745-04:00       entry_1500         entry_skipped                                                        {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T15:05:23.333934-04:00       entry_1500         entry_skipped                                                        {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T14:59:13.815238-04:00       entry_1500         entry_skipped                                                        {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T14:52:59.210728-04:00       entry_1500         entry_skipped                                                        {"entry_mode": "regular", "option_liquidity_status": "low_volume", "reason": "no_trade_low_option_liquidity", "ticker": "NXPI"}
2026-05-27T11:55:12.007255-04:00 early_entry_1155         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:48:57.330665-04:00 early_entry_1145         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:42:48.973748-04:00 early_entry_1140         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:36:41.236063-04:00 early_entry_1135         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:30:32.575558-04:00 early_entry_1130         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:24:23.275408-04:00 early_entry_1120         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:18:10.299261-04:00 early_entry_1115         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:11:58.509133-04:00 early_entry_1110         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T11:05:52.604228-04:00 early_entry_1105         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:59:45.771179-04:00 early_entry_1055         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:53:36.022473-04:00 early_entry_1050         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:47:25.850725-04:00 early_entry_1045         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:41:11.964523-04:00 early_entry_1040         entry_skipped                                                                                                                                      {"entry_mode": "early", "reason": "no_candidate"}
2026-05-27T10:34:59.298014-04:00 early_entry_1030         entry_skipped                                                                                               {"budget": 5000.0, "entry_limit": 63.0, "reason": "insufficient_cash", "ticker": "SNPS"}
```