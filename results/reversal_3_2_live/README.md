# Reversal 3.2 Live Paper Test

Last updated (ET): `2026-04-07 15:00:05 EDT`
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
- Equity: `$10,335.00`
- Realized PnL: `$320.00`
- Unrealized PnL: `$15.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  TSLA TSLA260515C00340000       2026-04-07                   0          2      4680.0                  4695.0                23.4                 23.48      340.83        340.49            15.0                   0.32         100.0               13               3.4         51.95           52.41                  42.33
```

## Today's Closed Trades (2026-04-07)

```text
ticker    contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price     pnl  return_pct           exit_reason
   HON HON260515C00230000          2026-04-06         2026-04-07                 7.4                5.8 -1120.0  -21.621622 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA          100.00               13            3.54              8.74        349.08                42.33            True
  REGN           96.97               33            0.93              4.99        760.90                25.24            True
  MRVL           96.55               29            1.50              1.15        109.02                70.84            True
  NFLX           94.87               39            0.58              0.40         98.76                26.96            True
  NVDA           92.00               25            1.39              1.73        176.90                33.70            True
  MPWR           91.43               35            1.05              8.67       1176.31                51.99            True
  UPRO           90.91               22            2.36              1.67        100.03                53.86            True
  CDNS           90.24               41            1.05              2.04        278.51                25.26            True
  COST           90.00               10            1.28              9.13       1014.63                13.04            True
  FAST           88.89               18            1.57              0.50         45.65                20.98            True
  PCAR           88.24               34            0.82              0.68        118.03                21.97            True
  ORLY           88.24               34            0.79              0.51         91.91                23.11            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                           detail
2026-04-07T15:00:05.890204-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:55:00.887138-04:00  entry_1500 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:50:04.918653-04:00  entry_1500        entry {"allocated_cash": 4680.0, "contract_symbol": "TSLA260515C00340000", "contracts": 2, "entry_option_price": 23.4, "matched_signals": 13, "success_rate": 100.0, "ticker": "TSLA"}
2026-04-07T14:40:00.896832-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:35:00.890525-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:30:00.927122-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:25:01.881173-04:00 manage_1430 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:10:00.879771-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:05:03.892395-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
2026-04-07T14:00:04.896209-04:00 manage_1400 slot_skipped                                                                                                                                                  {"reason": "already_processed"}
```

## Equity Curves

Each chart is generated from the same live equity series with no-lookahead marks. The latest point is annotated with its exact ET checkpoint time and return %.

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260407150005)

</details>

<details open>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260407150005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260407150005)

</details>
