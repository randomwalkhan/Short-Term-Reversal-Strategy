# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 13:45:05 EDT`
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

- Cash: `$9,575.00`
- Equity: `$9,575.00`
- Realized PnL: `$-425.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-13)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
   HON     option         option HON260522C00235000      7          2026-04-10         2026-04-13          8.3         4.5 -2660.0  -45.783133 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               22            1.43              7.50        745.65                24.22            True
   HON          100.00               15            1.15              1.89        234.25                23.73            True
  MPWR           91.43               35            0.71              6.72       1350.97                59.12            True
   WMT           90.00               10            1.65              1.47        126.16                25.46            True
  GILD           86.36               22            0.97              0.95        138.62                21.48            True
   BKR           84.38               32            0.84              0.37         62.67                35.55            True
   PEP           83.33               24            0.57              0.62        156.79                20.42            True
   EXC           83.33               12            0.95              0.32         48.43                21.28            True
    MU           82.86               35            0.82              2.42        419.55                76.70            True
  ODFL           82.35               34            0.79              1.16        207.85                24.62            True
  AMAT           81.48               27            1.83              5.13        397.30                55.88            True
   ADI           81.48               27            0.97              2.38        349.12                33.95            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T13:40:03.882273-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:35:04.710153-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:30:01.722483-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:25:03.704935-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:10:04.705330-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:05:00.712110-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:00:05.702786-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T12:55:05.429445-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T12:40:05.817303-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:35:05.834542-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413134505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413134505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413134505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413134505)

</details>
