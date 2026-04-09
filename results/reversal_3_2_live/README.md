# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 14:45:04 EDT`
Last processed slot: `manual`

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
  REGN          100.00               22            1.44              7.83        772.18                26.04            True
   WDC           97.22               36            0.90              2.13        337.87                87.19            True
  CDNS           90.00               10            3.58              7.26        286.39                28.11            True
  ALNY           88.89               27            1.88              4.30        325.41                41.11            True
  CTAS           88.57               35            0.57              0.69        174.29                30.38            True
  SNPS           85.19               27            2.05              5.87        407.64                37.77            True
  ABNB           83.33               18            1.96              1.81        130.63                41.34            True
  ISRG           80.77               26            1.24              4.01        460.56                24.21            True
  CSCO           80.00               20            0.80              0.47         83.50                27.82            True
    ZS          100.00                1           12.12             11.70        132.84                46.90           False
  SBUX           92.11               38            0.35              0.24         97.11                40.88           False
  VRTX           91.30               46            0.23              0.71        443.61                28.00           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T14:40:04.078140-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-09T14:35:00.960951-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-09T14:30:00.902865-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-09T14:25:00.971224-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-09T14:10:01.012659-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-09T14:05:00.920582-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-09T14:00:05.431112-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-09T13:55:04.050612-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-09T13:40:03.886505-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:35:04.885893-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409144504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409144504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409144504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409144504)

</details>
