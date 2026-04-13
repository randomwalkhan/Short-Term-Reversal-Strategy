# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 14:35:05 EDT`
Last processed slot: `manage_1430`

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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$13,145.00`
- Equity: `$13,145.00`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  PLTR     option         option PLTR260522C00125000      5          2026-04-10         2026-04-13        12.06       13.88 910.0   15.091211 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               22            1.44              7.55        745.64                24.22            True
   HON          100.00               13            1.25              2.06        234.18                23.73            True
   PEP           85.00               20            0.81              0.89        156.68                20.42            True
  CSCO           83.33               18            1.07              0.62         81.96                28.42            True
   EXC           83.33               12            1.12              0.38         48.41                21.28            True
    MU           82.86               35            0.88              2.60        419.47                76.70            True
   BKR           80.77               26            1.05              0.46         62.63                35.55            True
  ODFL           80.65               31            0.94              1.37        207.76                24.62            True
   ADI           80.65               31            0.70              1.72        349.40                33.95            True
  AMAT           80.00               25            2.07              5.78        397.02                55.88            True
   KDP           80.00               10            1.67              0.31         26.44                21.09            True
  FANG          100.00               32            0.14              0.19        188.12                32.11           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T14:35:05.900098-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-13T14:30:05.902792-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-13T14:25:05.905782-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-13T13:40:03.882273-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:35:04.710153-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:30:01.722483-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:25:03.704935-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:10:04.705330-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:05:00.712110-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:00:05.702786-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413143505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413143505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413143505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413143505)

</details>
