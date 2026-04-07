# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 14:55:00 EDT`
Last processed slot: `entry_1500`

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

- Cash: `$5,640.00`
- Equity: `$10,300.00`
- Realized PnL: `$320.00`
- Unrealized PnL: `$-20.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  TSLA TSLA260515C00340000       2026-04-07                   0          2      4680.0                  4660.0                23.4                  23.3      340.83        339.26           -20.0                  -0.43         100.0               13               3.4         51.95           53.35                  42.33
```

## Today's Closed Trades (2026-04-07)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price     pnl  return_pct           exit_reason
   HON HON260515C00230000          2026-04-06         2026-04-07                 7.4                5.8 -1120.0  -21.621622 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN           96.77               31            1.13              6.02        760.46                25.24            True
  MRVL           96.15               26            1.89              1.45        108.89                70.84            True
  NFLX           94.87               39            0.60              0.41         98.75                26.96            True
  SBUX           94.59               37            0.54              0.36         94.63                40.32            True
  NVDA           91.67               24            1.49              1.85        176.85                33.70            True
  MPWR           91.43               35            1.05              8.65       1176.32                51.99            True
  UPRO           90.91               22            2.48              1.75         99.99                53.86            True
  CDNS           90.00               40            1.08              2.11        278.49                25.26            True
  COST           90.00               10            1.29              9.19       1014.61                13.04            True
  FAST           88.89               18            1.57              0.50         45.65                20.98            True
  ORLY           88.24               34            0.77              0.49         91.92                23.11            True
   KDP           88.24               17            0.80              0.14         25.64                20.32            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-07T14:55:00.887138-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:50:04.918653-04:00  entry_1500        entry {"allocated_cash": 4680.0, "contract_symbol": "TSLA260515C00340000", "contracts": 2, "entry_option_price": 23.4, "matched_signals": 13, "success_rate": 100.0, "ticker": "TSLA"}
2026-04-07T14:40:00.896832-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:35:00.890525-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:30:00.927122-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:25:01.881173-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:10:00.879771-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:05:03.892395-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:00:04.896209-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T13:55:00.552170-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407145500)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407145500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407145500)

</details>
