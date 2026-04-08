# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-08 16:00:06 EDT`
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
- Equity: `$11,700.00`
- Realized PnL: `$1,650.00`
- Unrealized PnL: `$50.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  FTNT FTNT260508C00083000       2026-04-08                   0         10      5375.0                  5425.0                5.38                  5.43       82.77         83.51            50.0                   0.93         91.89               37              1.13         57.03           53.42                  31.42
```

## Today's Closed Trades (2026-04-08)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  TSLA TSLA260515C00340000          2026-04-07         2026-04-08                23.4              30.05 1330.0   28.418803 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           85.71               35            0.97              1.52        223.15                33.96            True
  CSGP           83.87               31            1.67              0.46         39.28                36.79            True
  TSLA           82.86               35            0.98              2.37        345.63                46.68            True
  CTSH           82.35               34            0.80              0.34         61.34                24.93            True
  INSM           80.00               30            1.75              1.99        162.18                53.00            True
   ROP           80.00               30            0.83              2.09        357.94                19.33            True
  FTNT           93.62               47            0.25              0.15         83.66                31.42           False
  DDOG           88.89               45            0.03              0.03        116.53                49.79           False
   ADP           76.47               17            1.50              2.14        202.69                22.69           False
  TEAM           76.09               46            0.68              0.31         64.70                51.08           False
    ZS           75.00               20            2.98              2.97        140.82                47.83           False
  PLTR           75.00                4            6.11              6.42        147.32                49.26           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                             detail
2026-04-08T16:00:06.439697-04:00 manage_1600 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:55:05.442130-04:00 manage_1600 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:40:01.444116-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:35:04.435079-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:30:06.433144-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:25:06.431552-04:00 manage_1530 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:10:06.436687-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T15:05:05.449071-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:55:05.932900-04:00  entry_1500 slot_skipped                                                                                                                                                    {"reason": "already_processed"}
2026-04-08T14:50:03.439007-04:00  entry_1500        entry {"allocated_cash": 5375.0, "contract_symbol": "FTNT260508C00083000", "contracts": 10, "entry_option_price": 5.375, "matched_signals": 37, "success_rate": 91.89, "ticker": "FTNT"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260408160006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260408160006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260408160006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260408160006)

</details>
