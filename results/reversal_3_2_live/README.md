# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-08 15:10:06 EDT`
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
- Live exit ladder: `+15% / +15% / -12%`
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,275.00`
- Equity: `$11,725.00`
- Realized PnL: `$1,650.00`
- Unrealized PnL: `$75.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FTNT FTNT260508C00083000       2026-04-08                   0         10      5375.0                  5450.0                5.38                  5.45       82.77         83.27            75.0                    1.4         91.89               37              1.13         57.03           55.03                  31.42
```

## Today's Closed Trades (2026-04-08)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  TSLA TSLA260515C00340000          2026-04-07         2026-04-08                23.4              30.05 1330.0   28.418803 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FTNT           93.02               43            0.70              0.41         83.54                31.42            True
  TSLA           86.67               30            1.25              3.04        345.35                46.68            True
  INSM           81.25               32            1.56              1.78        162.27                53.00            True
  CHTR           80.77               26            1.75              2.74        222.63                33.96            True
  CSGP           80.56               36            1.32              0.36         39.32                36.79            True
 CMCSA           95.45               22            0.18              0.04         27.77                23.49           False
   ROP           79.41               34            0.54              1.37        358.24                19.33           False
  TEAM           76.60               47            0.35              0.16         64.76                51.08           False
  ADBE           75.00               48            0.20              0.34        240.00                37.47           False
  PLTR           75.00                4            6.10              6.41        147.32                49.26           False
    ZS           73.91               23            2.27              2.26        141.12                47.83           False
  PAYX           73.68               19            1.77              1.13         91.12                26.82           False
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

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260408151006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260408151006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260408151006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260408151006)

</details>
