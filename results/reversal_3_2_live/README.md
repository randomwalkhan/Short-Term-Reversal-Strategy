# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-08 15:20:06 EDT`
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
- Live exit ladder: `+15% / +15% / -12%`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,275.00`
- Equity: `$11,700.00`
- Realized PnL: `$1,650.00`
- Unrealized PnL: `$50.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FTNT FTNT260508C00083000       2026-04-08                   0         10      5375.0                  5425.0                5.38                  5.42       82.77         83.04            50.0                   0.93         91.89               37              1.13         57.03           56.08                  31.42
```

## Today's Closed Trades (2026-04-08)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  TSLA TSLA260515C00340000          2026-04-07         2026-04-08                23.4              30.05 1330.0   28.418803 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FTNT           92.86               42            0.74              0.43         83.53                31.42            True
  TSLA           86.21               29            1.40              3.39        345.20                46.68            True
  CSGP           83.87               31            1.62              0.45         39.29                36.79            True
  CHTR           82.14               28            1.49              2.34        222.80                33.96            True
  INSM           80.65               31            1.66              1.89        162.22                53.00            True
   ROP           80.00               30            0.75              1.88        358.03                19.33            True
 CMCSA           95.45               22            0.23              0.05         27.77                23.49           False
   EXC           88.89               27            0.10              0.03         49.03                21.02           False
  TMUS           76.92               13            1.66              2.33        199.54                22.17           False
  ADBE           74.47               47            0.30              0.50        239.93                37.47           False
  TEAM           74.42               43            0.96              0.43         64.64                51.08           False
  MSFT           74.42               43            0.16              0.41        372.12                25.09           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                             detail
2026-04-08T15:10:06.436687-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:05:05.449071-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:55:05.932900-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:50:03.439007-04:00  entry_1500        entry {"allocated_cash": 5375.0, "contract_symbol": "FTNT260508C00083000", "contracts": 10, "entry_option_price": 5.375, "matched_signals": 37, "success_rate": 91.89, "ticker": "FTNT"}
2026-04-08T14:40:04.447081-04:00 manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:35:03.430322-04:00 manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:30:06.439712-04:00 manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:25:01.442780-04:00 manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:10:06.422703-04:00 manage_1400 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:05:04.424556-04:00 manage_1400 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260408152006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260408152006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260408152006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260408152006)

</details>
