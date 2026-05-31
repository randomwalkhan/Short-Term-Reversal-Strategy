# Reversal 3.4.4-alpaca-paper.0

Latest checkpoint (ET): `2026-05-31 09:52:21 EDT`
Last slot: `manage_1000`

## Alpaca Paper Account

- Status: `ACTIVE`
- Cash: `$94,521.56`
- Portfolio value: `$97,141.56`
- Strategy capital cap: `$10,000.00`
- Options level: `3`

## Open / Pending Positions

```text
ticker status entry_mode     contract_symbol  contracts  entry_option_price  current_option_price current_price_source  current_exit_signal_price  current_quote_reliable  position_value  unrealized_pnl  unrealized_return_pct  business_days_held
  MRVL   open      early MRVL260717C00200000          1                26.0                26.575          bid_ask_mid                     26.575                    True          2657.5            57.5               2.211538                   0
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
  AVGO AVGO260717C00420000          2026-05-28         2026-05-29               33.40              47.35          1  1395.0   41.766467 take_profit_day1_hit_at_scan
```

## Recent Events

```text
                    timestamp_et           slot    event_type                                      detail
2026-05-31T09:52:21.413645-04:00    manage_1000 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:47:18.033914-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:42:14.547102-04:00         manual market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:37:11.056115-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:32:07.477830-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:27:04.085623-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:22:00.707900-04:00    manage_0930 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:16:57.253534-04:00 share_ext_0915 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:11:53.733706-04:00 share_ext_0910 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:06:50.080961-04:00 share_ext_0905 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T09:01:46.526966-04:00 share_ext_0900 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:56:42.985694-04:00 share_ext_0855 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:51:39.407545-04:00 share_ext_0850 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:46:36.060476-04:00 share_ext_0845 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:41:32.726470-04:00 share_ext_0840 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:36:29.241524-04:00 share_ext_0835 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:31:25.597182-04:00 share_ext_0830 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:26:22.064147-04:00 share_ext_0825 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:21:18.562372-04:00 share_ext_0820 market_closed {"holiday_name": null, "reason": "weekend"}
2026-05-31T08:16:15.039999-04:00 share_ext_0815 market_closed {"holiday_name": null, "reason": "weekend"}
```