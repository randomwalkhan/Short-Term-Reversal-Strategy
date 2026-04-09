# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 10:50:04 EDT`
Last processed slot: `manage_1100`

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
  REGN          100.00               18            1.75              9.49        771.46                26.04            True
   WDC           96.88               32            2.00              4.74        336.75                87.19            True
   MAR           90.62               32            0.87              2.12        347.67                32.53            True
  VRTX           88.57               35            0.88              2.74        442.74                28.00            True
  ALNY           87.50               32            1.53              3.50        325.75                41.11            True
  CTAS           85.19               27            1.06              1.29        174.04                30.38            True
  DXCM           84.62               26            1.71              0.79         65.46                33.81            True
  TTWO           84.38               32            1.35              1.90        201.31                26.08            True
  MELI           84.21               38            1.01             12.61       1770.34                40.32            True
  MCHP           83.33               30            1.13              0.56         70.49                45.14            True
  DDOG           83.33               18            3.57              2.91        115.25                46.85            True
    MU           82.86               35            1.18              3.37        405.29                78.65            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T10:40:03.920046-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:35:05.721256-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:30:03.705847-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:25:03.711004-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-09T10:10:03.861770-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-09T10:05:05.524975-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-09T10:00:02.890491-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-09T09:55:03.701126-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-09T09:40:00.730980-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-09T09:35:00.721623-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409105004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409105004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409105004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409105004)

</details>
