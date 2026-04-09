# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 13:15:00 EDT`
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
  REGN          100.00               24            1.23              6.66        772.67                26.04            True
  SBUX           94.12               34            0.60              0.41         97.04                40.88            True
  ABNB           90.91               33            1.09              1.00        130.97                41.34            True
  ALNY           90.70               43            0.96              2.19        326.31                41.11            True
  SNPS           86.67               30            1.62              4.67        408.16                37.77            True
  DDOG           84.62               13            4.70              3.84        114.86                46.85            True
  CDNS           84.62               13            2.69              5.46        287.16                28.11            True
  TTWO           82.86               35            1.26              1.78        201.37                26.08            True
  IDXX           81.58               38            0.75              3.09        590.52                27.54            True
  ISRG           80.95               42            0.72              2.33        461.28                24.21            True
    ZS          100.00                2           10.76             10.38        133.40                46.90           False
   WDC           97.44               39            0.40              0.96        338.37                87.19           False
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

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409131500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409131500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409131500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409131500)

</details>
