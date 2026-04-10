# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 16:00:04 EDT`
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
- Live exit ladder: `+15% / +15% / -12%`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,425.00`
- Equity: `$12,340.00`
- Realized PnL: `$2,235.00`
- Unrealized PnL: `$105.00`
- Open positions: `1`

## Open Positions

```text
ticker    contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
   HON HON260522C00235000       2026-04-10                   0          7      5810.0                  5915.0                 8.3                  8.45      234.53        235.04           105.0                   1.81         100.0               22              0.65         29.29           28.81                  23.67
```

## Today's Closed Trades (2026-04-10)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
  REGN REGN260515C00765000          2026-04-09         2026-04-10                44.0               36.1 -790.0  -17.954545 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   AEP           95.00               20            0.61              0.58        136.90                18.33            True
   CSX           87.50               24            0.59              0.17         42.41                21.51            True
  SNPS           86.67               15            3.13              8.87        401.04                36.22            True
  PLTR           86.21               29            1.91              1.74        129.79                58.33            True
  SHOP           86.11               36            1.16              0.91        111.91                49.23            True
  DDOG           85.00               20            3.31              2.53        107.90                49.83            True
  BKNG           84.62               26            1.78              2.20        175.66                36.59            True
  TMUS           84.00               25            0.93              1.28        196.99                21.21            True
  MELI           83.78               37            1.07             13.47       1787.43                40.44            True
  ODFL           83.78               37            0.55              0.81        209.16                37.04            True
  CHTR           83.33               24            1.98              3.09        221.91                29.22            True
  MNST           82.86               35            0.62              0.33         76.05                27.62            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T16:00:04.433718-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-10T15:55:06.433939-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-10T15:40:05.440122-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-10T15:35:01.390117-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-10T15:30:06.443787-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-10T15:25:06.434467-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-10T15:10:06.450785-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-10T15:05:06.434805-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-10T15:00:06.450530-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-10T14:55:06.442916-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410160004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410160004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410160004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410160004)

</details>
