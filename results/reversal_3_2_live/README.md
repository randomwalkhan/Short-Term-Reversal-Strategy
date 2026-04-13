# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 10:15:05 EDT`
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
   HON          100.00               25            0.52              0.86        234.70                23.73            True
   WDC           97.30               37            0.55              1.33        342.86                85.50            True
   STX           94.74               38            0.53              1.87        502.33                75.16            True
  SBUX           94.44               36            0.60              0.41         96.43                40.58            True
   XEL           93.75               16            0.79              0.45         82.19                18.59            True
 CMCSA           93.75               16            0.77              0.15         27.87                24.08            True
   WMT           93.10               29            0.72              0.64        126.51                25.46            True
   AEP           91.67               24            0.58              0.55        136.06                18.46            True
  MPWR           91.43               35            0.77              7.34       1350.71                59.12            True
  NVDA           91.43               35            0.56              0.73        188.43                35.03            True
  MDLZ           90.91               11            1.41              0.58         58.75                22.21            True
  PCAR           90.00               40            0.52              0.46        126.99                27.57            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                      detail
2026-04-13T10:10:00.698595-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T10:05:00.712812-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T10:00:05.716219-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:55:05.732527-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:40:00.697850-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:35:00.760791-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:30:05.721136-04:00  manage_0930         exit {"asset_type": "option", "contract_symbol": "HON260522C00235000", "pnl": -2660.0, "reason": "stop_loss_hit_at_scan", "return_pct": -45.78, "ticker": "HON"}
2026-04-13T09:30:05.721136-04:00 data_refresh data_refresh                                                                                                                                               {'saved': 99}
2026-04-10T16:00:04.433718-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:55:06.433939-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413101505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413101505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413101505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413101505)

</details>
