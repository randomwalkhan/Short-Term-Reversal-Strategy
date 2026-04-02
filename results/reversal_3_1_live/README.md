# Reversal 3.1 Live Paper Test

Last updated (ET): `2026-04-02 16:00:05 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$10,930.00`
- Realized PnL: `$845.00`
- Unrealized PnL: `$85.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   WDC WDC260501C00295000       2026-04-02                   0               27.42                 28.28      294.77        294.97            85.0                    3.1         97.22               36              0.99         81.84           84.05                  91.06
```

## Today's Closed Trades (2026-04-02)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  NFLX NFLX260508C00096000          2026-04-01         2026-04-02               4.875                6.1 1102.5   25.128205 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.30               37            0.90              1.87        296.93                91.06            True
  REGN           93.33               15            1.98             10.78        772.63                26.81            True
  ASML           91.67               12            3.13             29.77       1347.00                52.01            True
  FAST           90.62               32            0.71              0.23         46.53                21.97            True
   CSX           89.29               28            0.53              0.15         41.37                27.84            True
  CDNS           88.89               45            0.52              1.03        279.75                26.25            True
  ORLY           88.57               35            0.74              0.48         91.90                22.81            True
 GOOGL           84.62               39            0.59              1.23        296.86                35.66            True
   TXN           83.87               31            0.73              1.00        195.87                33.08            True
  ODFL           83.33               36            0.82              1.14        199.14                46.64            True
  AMAT           83.33               30            1.51              3.73        352.20                59.65            True
  MNST           82.86               35            0.55              0.28         72.65                21.32            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-02T16:00:05.925792-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-02T15:55:05.893858-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-02T15:40:05.898407-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-02T15:35:05.886679-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-02T15:30:05.889337-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-02T15:25:05.929228-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-02T15:10:05.887758-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-02T15:05:00.892731-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-02T15:00:05.892985-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-02T14:55:05.878211-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
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
