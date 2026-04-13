# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 14:14:35 EDT`
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
  REGN          100.00               29            1.12              5.89        746.35                24.22            True
   HON          100.00               15            1.14              1.87        234.26                23.73            True
   WMT           90.00               10            1.71              1.52        126.14                25.46            True
  CSCO           84.21               19            0.82              0.47         82.02                28.42            True
   EXC           83.33               12            0.99              0.34         48.43                21.28            True
    MU           82.86               35            1.13              3.32        419.17                76.70            True
   PEP           82.61               23            0.63              0.69        156.76                20.42            True
   BKR           82.14               28            0.92              0.40         62.66                35.55            True
   ADI           82.14               28            0.87              2.13        349.23                33.95            True
   KDP           81.82               11            1.66              0.31         26.44                21.09            True
  ODFL           81.25               32            0.83              1.21        207.83                24.62            True
  AMAT           80.00               25            2.09              5.85        396.99                55.88            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T14:10:03.263071-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-13T14:05:05.897417-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-13T14:00:05.918542-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-13T13:55:05.895043-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-13T13:40:03.882273-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:35:04.710153-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:30:01.722483-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:25:03.704935-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:10:04.705330-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:05:00.712110-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413141435)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413141435)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413141435)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413141435)

</details>
