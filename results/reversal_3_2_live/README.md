# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 10:30:05 EDT`
Last processed slot: `manage_1030`

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
   HON          100.00               20            0.89              1.46        234.44                23.73            True
   WDC           97.30               37            0.59              1.41        342.82                85.50            True
   STX           94.59               37            0.71              2.50        502.06                75.16            True
  SBUX           94.44               36            0.57              0.38         96.44                40.58            True
   AEP           94.12               17            0.78              0.74        135.98                18.46            True
   WMT           91.67               24            0.91              0.81        126.44                25.46            True
  MPWR           91.18               34            1.00              9.46       1349.80                59.12            True
   XEL           90.91               11            0.98              0.57         82.14                18.59            True
  GILD           90.32               31            0.55              0.54        138.80                21.48            True
   MAR           90.00               30            0.90              2.24        353.14                29.84            True
  COST           90.00               30            0.66              4.59        996.50                18.13            True
  INSM           89.74               39            0.92              0.99        154.38                53.55            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                      detail
2026-04-13T10:30:05.709721-04:00  manage_1030 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T10:25:05.707735-04:00  manage_1030 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T10:10:00.698595-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T10:05:00.712812-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T10:00:05.716219-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:55:05.732527-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:40:00.697850-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:35:00.760791-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:30:05.721136-04:00  manage_0930         exit {"asset_type": "option", "contract_symbol": "HON260522C00235000", "pnl": -2660.0, "reason": "stop_loss_hit_at_scan", "return_pct": -45.78, "ticker": "HON"}
2026-04-13T09:30:05.721136-04:00 data_refresh data_refresh                                                                                                                                               {'saved': 99}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413103005)

</details>
