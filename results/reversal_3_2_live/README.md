# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 13:20:05 EDT`
Last processed slot: `manage_1330`

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
  REGN          100.00               29            1.11              6.04        772.94                26.04            True
  SBUX           93.75               32            0.79              0.54         96.98                40.88            True
  DDOG           91.67               12            4.92              4.01        114.78                46.85            True
  ALNY           89.74               39            1.10              2.53        326.17                41.11            True
  ABNB           88.24               34            1.01              0.93        131.00                41.34            True
  SNPS           84.38               32            1.59              4.58        408.20                37.77            True
  CDNS           83.33               12            2.97              6.03        286.92                28.11            True
  TTWO           82.86               35            1.25              1.77        201.37                26.08            True
  IDXX           81.08               37            0.80              3.33        590.41                27.54            True
  ISRG           80.49               41            0.77              2.51        461.21                24.21            True
  CSCO           80.00               15            1.41              0.83         83.35                27.82            True
    ZS          100.00                2           11.07             10.68        133.27                46.90           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T13:10:02.022275-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T13:05:02.897380-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T13:00:03.062847-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T12:55:00.892899-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T12:40:00.955610-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-09T12:35:05.898877-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-09T12:30:01.129323-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-09T12:25:01.881441-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-09T12:10:01.709238-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-09T12:05:05.701665-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409132005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409132005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409132005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409132005)

</details>
