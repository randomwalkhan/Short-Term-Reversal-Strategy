# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-08 15:50:04 EDT`
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

- Cash: `$6,275.00`
- Equity: `$11,875.00`
- Realized PnL: `$1,650.00`
- Unrealized PnL: `$225.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FTNT FTNT260508C00083000       2026-04-08                   0         10      5375.0                  5600.0                5.38                   5.6       82.77         83.28           225.0                   4.19         91.89               37              1.13         57.03           56.54                  31.42
```

## Today's Closed Trades (2026-04-08)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  TSLA TSLA260515C00340000          2026-04-07         2026-04-08                23.4              30.05 1330.0   28.418803 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  TSLA           86.21               29            1.30              3.14        345.30                46.68            True
  CHTR           83.87               31            1.28              2.00        222.94                33.96            True
  CSGP           82.76               29            1.90              0.53         39.25                36.79            True
  INSM           81.25               32            1.59              1.81        162.25                53.00            True
   ROP           80.00               30            0.74              1.86        358.03                19.33            True
  FTNT           93.48               46            0.47              0.27         83.60                31.42           False
  CTSH           86.36               44            0.24              0.10         61.45                24.93           False
    ZS           75.00               20            3.04              3.03        140.79                47.83           False
  TMUS           75.00               16            1.30              1.83        199.76                22.17           False
  PLTR           75.00                4            6.18              6.50        147.29                49.26           False
  PAYX           73.68               19            1.84              1.18         91.10                26.82           False
  ADBE           72.73               44            0.53              0.90        239.76                37.47           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                             detail
2026-04-08T15:40:01.444116-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:35:04.435079-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:30:06.433144-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:25:06.431552-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:10:06.436687-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:05:05.449071-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:55:05.932900-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:50:03.439007-04:00  entry_1500        entry {"allocated_cash": 5375.0, "contract_symbol": "FTNT260508C00083000", "contracts": 10, "entry_option_price": 5.375, "matched_signals": 37, "success_rate": 91.89, "ticker": "FTNT"}
2026-04-08T14:40:04.447081-04:00 manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:35:03.430322-04:00 manage_1430 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260408155004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260408155004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260408155004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260408155004)

</details>
