# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 13:30:01 EDT`
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
  REGN          100.00               32            0.90              4.74        746.84                24.22            True
   HON          100.00               17            1.01              1.65        234.35                23.73            True
   WMT           92.31               13            1.53              1.36        126.21                25.46            True
  MPWR           91.43               35            0.54              5.14       1351.64                59.12            True
   EXC           88.89               18            0.82              0.28         48.45                21.28            True
  GILD           87.50               24            0.86              0.84        138.67                21.48            True
    MU           82.86               35            0.91              2.69        419.44                76.70            True
  ODFL           82.86               35            0.68              0.99        207.93                24.62            True
   PEP           82.61               23            0.60              0.66        156.78                20.42            True
   ADI           82.14               28            0.94              2.30        349.16                33.95            True
  DXCM           81.25               16            2.23              1.00         63.59                33.70            True
  CSCO           80.95               21            0.61              0.35         82.07                28.42            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T13:30:01.722483-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:25:03.704935-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-13T13:10:04.705330-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:05:00.712110-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:00:05.702786-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T12:55:05.429445-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T12:40:05.817303-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:35:05.834542-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:30:04.889814-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:25:05.699971-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413133001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413133001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413133001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413133001)

</details>
