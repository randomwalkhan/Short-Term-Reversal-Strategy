# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 15:20:05 EDT`
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
- Equity: `$10,960.00`
- Realized PnL: `$845.00`
- Unrealized PnL: `$115.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   WDC WDC260501C00295000       2026-04-02                   0               27.42                 28.58      294.77        295.07           115.0                   4.19         97.22               36              0.99         81.84           84.69                  91.06
```

## Today's Closed Trades (2026-04-02)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  NFLX NFLX260508C00096000          2026-04-01         2026-04-02               4.875                6.1 1102.5   25.128205 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.30               37            0.89              1.86        296.93                91.06            True
  ASML           91.67               12            3.27             31.08       1346.44                52.01            True
  DXCM           91.11               45            0.67              0.29         62.24                31.67            True
   MAR           89.47               38            0.60              1.39        332.86                28.45            True
  FAST           89.29               28            0.91              0.30         46.50                21.97            True
   CSX           88.89               27            0.57              0.16         41.37                27.84            True
  GILD           88.00               25            0.82              0.81        139.95                21.47            True
  ORLY           87.10               31            0.85              0.55         91.87                22.81            True
  KLAC           85.29               34            1.00             10.61       1515.29                56.48            True
  AMAT           84.38               32            1.38              3.41        352.34                59.65            True
 GOOGL           83.78               37            0.75              1.56        296.72                35.66            True
  BKNG           83.78               37            0.73             21.48       4175.36                42.15            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-02T15:10:05.887758-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T15:05:00.892731-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T15:00:05.892985-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:55:05.878211-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:50:05.884978-04:00  entry_1500        entry {"allocated_cash": 2742.5, "contract_symbol": "WDC260501C00295000", "contracts": 1, "entry_option_price": 27.425, "matched_signals": 36, "success_rate": 97.22, "ticker": "WDC"}
2026-04-02T14:40:05.911687-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:35:05.892322-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:30:05.929668-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:25:06.347985-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-02T14:10:05.893357-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
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
