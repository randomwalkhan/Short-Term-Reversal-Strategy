# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 10:55:05 EDT`
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
   HON          100.00               17            1.04              1.72        234.33                23.73            True
  COST           95.24               21            0.92              6.44        995.71                18.13            True
  SBUX           94.29               35            0.62              0.42         96.42                40.58            True
   AEP           94.12               17            0.70              0.67        136.01                18.46            True
 CMCSA           93.75               16            0.79              0.15         27.86                24.08            True
  MPWR           91.18               34            1.02              9.71       1349.69                59.12            True
   XEL           90.91               11            1.00              0.57         82.13                18.59            True
   MAR           90.62               32            0.85              2.10        353.20                29.84            True
   WMT           90.00               20            1.10              0.98        126.37                25.46            True
  DXCM           88.57               35            1.38              0.62         63.75                33.70            True
  PCAR           88.57               35            0.77              0.69        126.90                27.57            True
  GILD           87.50               24            0.87              0.85        138.67                21.48            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T10:55:05.707019-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-13T10:40:05.710710-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:35:05.426321-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:30:05.709721-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:25:05.707735-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:10:00.698595-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T10:05:00.712812-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T10:00:05.716219-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T09:55:05.732527-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T09:40:00.697850-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413105505)

</details>
