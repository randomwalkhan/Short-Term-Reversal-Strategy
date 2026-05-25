# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-25 00:55:48 EDT`
Last slot: `share_ext_0055`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$87,957.73`
- Portfolio value: `$96,137.73`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  INTC   open    regular INTC260626C00117000          3               13.45                 13.05          bid_ask_mid                      13.05                    True          3915.0          -120.0              -2.973978                   1
  SBUX   open    regular SBUX260717C00105000         13                3.75                  3.70          bid_ask_mid                       3.70                    True          4810.0           -65.0              -1.333333                   0
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
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                                     detail
2026-05-25T00:55:48.708218-04:00 share_ext_0055 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:50:44.592628-04:00 share_ext_0050 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:45:40.520320-04:00 share_ext_0045 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:40:36.228910-04:00 share_ext_0040 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:35:31.980766-04:00 share_ext_0035 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:30:27.096787-04:00 share_ext_0030 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:25:22.584937-04:00 share_ext_0025 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:20:17.268700-04:00 share_ext_0020 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:15:11.682297-04:00 share_ext_0015 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:10:06.874655-04:00 share_ext_0010 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T00:05:01.680592-04:00 share_ext_0005 market_closed {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-24T23:59:56.968159-04:00 share_ext_2355 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:54:52.526503-04:00 share_ext_2350 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:49:48.018081-04:00 share_ext_2345 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:44:43.826788-04:00 share_ext_2340 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:39:39.045216-04:00 share_ext_2335 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:34:34.084379-04:00 share_ext_2330 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:29:29.387775-04:00 share_ext_2325 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:24:24.587170-04:00 share_ext_2320 market_closed                {"holiday_name": null, "reason": "weekend"}
2026-05-24T23:19:19.692453-04:00 share_ext_2315 market_closed                {"holiday_name": null, "reason": "weekend"}
```