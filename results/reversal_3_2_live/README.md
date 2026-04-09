# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 14:05:00 EDT`
Last processed slot: `manage_1400`

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

- Cash: `$13,025.00`
- Equity: `$13,025.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-09)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  FTNT FTNT260508C00083000          2026-04-08         2026-04-09               5.375               6.75 1375.0   25.581395 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               24            1.23              6.66        772.68                26.04            True
   WDC           97.14               35            0.99              2.36        337.77                87.19            True
  CDNS           90.91               11            3.31              6.70        286.63                28.11            True
  ABNB           90.32               31            1.26              1.16        130.91                41.34            True
  CTAS           87.50               32            0.67              0.82        174.24                30.38            True
  SNPS           85.71               28            1.80              5.16        407.95                37.77            True
  ALNY           85.71               28            1.78              4.07        325.50                41.11            True
  TTWO           84.00               25            1.80              2.54        201.04                26.08            True
  IDXX           81.08               37            0.80              3.31        590.42                27.54            True
  CSCO           80.00               15            1.27              0.75         83.38                27.82            True
    ZS          100.00                1           11.64             11.23        133.04                46.90           False
  SBUX           92.50               40            0.15              0.11         97.16                40.88           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T14:05:00.920582-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-09T14:00:05.431112-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-09T13:55:04.050612-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-09T13:40:03.886505-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:35:04.885893-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:30:05.578837-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:25:00.899270-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:10:02.022275-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T13:05:02.897380-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T13:00:03.062847-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409140500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409140500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409140500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409140500)

</details>
