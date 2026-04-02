# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 15:30:05 EDT`
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

- Cash: `$8,102.50`
- Equity: `$10,965.00`
- Realized PnL: `$845.00`
- Unrealized PnL: `$120.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   WDC WDC260501C00295000       2026-04-02                   0               27.42                 28.62      294.77        293.96           120.0                   4.38         97.22               36              0.99         81.84           86.74                  91.06
```

## Today's Closed Trades (2026-04-02)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  NFLX NFLX260508C00096000          2026-04-01         2026-04-02               4.875                6.1 1102.5   25.128205 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.22               36            1.27              2.64        296.60                91.06            True
  FAST           90.00               30            0.85              0.28         46.51                21.97            True
  ASML           90.00               10            3.49             33.19       1345.54                52.01            True
  CDNS           88.89               45            0.51              1.00        279.76                26.25            True
   MAR           88.89               36            0.65              1.53        332.81                28.45            True
  GILD           88.46               26            0.72              0.70        140.00                21.47            True
  ORLY           88.24               34            0.77              0.50         91.89                22.81            True
   CSX           88.00               25            0.59              0.17         41.37                27.84            True
  KLAC           85.71               35            0.88              9.32       1515.84                56.48            True
  AMAT           84.38               32            1.39              3.44        352.32                59.65            True
   TXN           83.87               31            0.81              1.11        195.82                33.08            True
    MU           83.78               37            0.90              2.31        366.86                84.85            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-02T15:30:05.889337-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T15:25:05.929228-04:00 manage_1530 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T15:10:05.887758-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T15:05:00.892731-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T15:00:05.892985-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:55:05.878211-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:50:05.884978-04:00  entry_1500        entry {"allocated_cash": 2742.5, "contract_symbol": "WDC260501C00295000", "contracts": 1, "entry_option_price": 27.425, "matched_signals": 36, "success_rate": 97.22, "ticker": "WDC"}
2026-04-02T14:40:05.911687-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:35:05.892322-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:30:05.929668-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.1 Live Equity 1D](../../assets/reversal_3_1_live_equity_1d.png)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.1 Live Equity 1W](../../assets/reversal_3_1_live_equity.png)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.1 Live Equity 1M](../../assets/reversal_3_1_live_equity_1m.png)

</details>
