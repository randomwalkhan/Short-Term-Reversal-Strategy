# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-06 15:45:00 EDT`
Last processed slot: `manual_refresh`

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
- Equity: `$11,475.00`
- Realized PnL: `$1,440.00`
- Unrealized PnL: `$35.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260515C00230000       2026-04-06                   0          7      5180.0                  5215.0                 7.4                  7.45      227.61        228.05            35.0                   0.68         100.0               20               0.8         28.89           28.24                  20.57
```

## Today's Closed Trades (2026-04-06)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price   pnl  return_pct                  exit_reason
   WDC WDC260501C00295000          2026-04-02         2026-04-06              27.425             33.375 595.0   21.695533 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               23            0.58              0.94        229.05                20.57            True
 CMCSA           92.31               13            0.77              0.15         27.87                25.15            True
  FAST           88.00               25            1.10              0.36         46.15                21.85            True
   LIN           85.71               21            0.68              2.38        501.58                19.40            True
  ASML           85.19               27            1.39             12.83       1311.73                51.28            True
  TSLA           85.00               20            2.29              5.79        358.11                42.35            True
  VRTX           84.38               32            1.16              3.55        437.19                40.20            True
   EXC           83.33               18            0.70              0.24         49.23                21.30            True
  TTWO           81.82               33            1.37              1.92        199.05                26.67            True
  PANW           80.49               41            0.71              0.81        162.86                41.77            True
  DDOG           80.00               20            3.12              2.63        119.23                49.88            True
  CTAS           80.00               20            1.24              1.51        173.69                28.60            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                        detail
2026-04-06T15:40:05.890163-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T15:35:05.886061-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T15:30:05.882298-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T15:25:05.886761-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T15:10:05.888760-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T15:00:05.880499-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:55:05.887845-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:50:05.889227-04:00  entry_1500        entry {"allocated_cash": 5180.0, "contract_symbol": "HON260515C00230000", "contracts": 7, "entry_option_price": 7.4, "matched_signals": 20, "success_rate": 100.0, "ticker": "HON"}
2026-04-06T14:40:05.884687-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-06T14:35:05.889475-04:00 manage_1430 slot_skipped                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260406154500)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260406154500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260406154500)

</details>
