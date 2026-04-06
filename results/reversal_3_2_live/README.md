# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 15:20:05 EDT`
Last processed slot: `manage_1530`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: GitHub-native `1D / 1W / 1M`, default open panel is `1W`

## Portfolio Snapshot

- Cash: `$6,260.00`
- Equity: `$11,545.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$105.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   0          7      5180.0                  5285.0                 7.4                  7.55      227.61        227.49           105.0                   2.03         100.0               20               0.8         28.89           29.46                  20.57
```

## Today's Closed Trades (2026-04-06)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price   pnl  return_pct                  exit_reason
   WDC WDC260501C00295000          2026-04-02         2026-04-06              27.425             33.375 595.0   21.695533 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               19            0.83              1.34        228.88                20.57            True
   XEL           95.24               21            0.55              0.31         80.61                19.13            True
 CMCSA           90.00               10            0.91              0.18         27.85                25.15            True
   EXC           88.24               17            0.73              0.25         49.22                21.30            True
  ASML           87.10               31            1.14             10.53       1312.72                51.28            True
  FAST           86.96               23            1.31              0.42         46.12                21.85            True
   LIN           85.71               14            0.97              3.42        501.13                19.40            True
  TSLA           85.00               20            2.47              6.24        357.91                42.35            True
  VRTX           84.62               39            0.68              2.09        437.81                40.20            True
  DDOG           84.00               25            2.54              2.14        119.44                49.88            True
  CTAS           83.33               24            1.12              1.37        173.75                28.60            True
  TTWO           80.65               31            1.43              2.01        199.01                26.67            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                        detail
2026-04-06T15:10:05.888760-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T15:00:05.880499-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:55:05.887845-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:50:05.889227-04:00  entry_1500        entry {"allocated_cash": 5180.0, "contract_symbol": "HON260515C00230000", "contracts": 7, "entry_option_price": 7.4, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-04-06T14:40:05.884687-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:35:05.889475-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:30:05.890964-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:25:05.885384-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:10:05.888996-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:05:05.887839-04:00 manage_1400 slot_skipped                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png)

</details>
