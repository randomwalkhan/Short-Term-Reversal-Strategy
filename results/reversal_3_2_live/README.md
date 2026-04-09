# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 10:45:00 EDT`
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
  REGN          100.00               22            1.41              7.64        772.25                26.04            True
   WDC           96.97               33            1.71              4.05        337.04                87.19            True
  UPRO           92.31               39            0.54              0.41        108.28                60.47            True
  ALNY           90.48               42            1.02              2.34        326.25                41.11            True
  GILD           90.00               30            0.52              0.51        141.32                20.46            True
  FTNT           90.00               10            3.04              1.77         82.75                30.61            True
  VRTX           88.57               35            0.86              2.68        442.77                28.00            True
   MAR           88.57               35            0.73              1.79        347.81                32.53            True
  CTAS           86.21               29            0.98              1.20        174.08                30.38            True
  DDOG           85.00               20            3.02              2.46        115.44                46.85            True
  TTWO           84.21               38            0.91              1.28        201.58                26.08            True
  TSLA           84.21               38            0.54              1.31        342.69                40.98            True
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

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409104500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409104500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409104500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409104500)

</details>
