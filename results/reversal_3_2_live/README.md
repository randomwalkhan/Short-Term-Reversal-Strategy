# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 13:20:00 EDT`
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
  REGN          100.00               25            1.21              6.35        746.15                24.22            True
   HON          100.00               20            0.84              1.37        234.47                23.73            True
   WMT           90.91               11            1.63              1.45        126.17                25.46            True
   EXC           89.47               19            0.74              0.25         48.46                21.28            True
  GILD           86.96               23            0.96              0.93        138.63                21.48            True
   PEP           86.36               22            0.68              0.75        156.74                20.42            True
    MU           82.86               35            0.78              2.30        419.60                76.70            True
  ODFL           82.86               35            0.68              0.99        207.93                24.62            True
   ADI           82.14               28            0.91              2.23        349.18                33.95            True
  DXCM           81.25               16            2.45              1.10         63.55                33.70            True
  CSCO           80.95               21            0.57              0.33         82.08                28.42            True
  AMAT           80.00               25            1.95              5.46        397.16                55.88            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T13:10:04.705330-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:05:00.712110-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T13:00:05.702786-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T12:55:05.429445-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-13T12:40:05.817303-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:35:05.834542-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:30:04.889814-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:25:05.699971-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:10:04.726532-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T12:05:04.704614-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413132000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413132000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413132000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413132000)

</details>
