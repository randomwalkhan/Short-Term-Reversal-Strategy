# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 09:45:05 EDT`
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
   WDC           97.22               36            0.79              1.91        342.61                85.50            True
  NFLX           94.74               38            0.63              0.46        102.84                26.26            True
   WMT           94.44               18            1.15              1.02        126.35                25.46            True
   STX           94.12               34            1.18              4.15        501.35                75.16            True
  FAST           92.86               14            2.03              0.70         48.87                26.67            True
   AEP           92.31               26            0.54              0.51        136.08                18.46            True
   XEL           92.31               13            0.87              0.50         82.17                18.59            True
  NVDA           92.00               25            1.42              1.87        187.94                35.03            True
  SBUX           91.30               23            1.17              0.79         96.26                40.58            True
  MPWR           91.18               34            1.04              9.88       1349.61                59.12            True
  UPRO           90.32               31            1.05              0.81        109.66                57.82            True
 CMCSA           90.00               20            0.54              0.10         27.89                24.08            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                      detail
2026-04-13T09:40:00.697850-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:35:00.760791-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:30:05.721136-04:00  manage_0930         exit {"asset_type": "option", "contract_symbol": "HON260522C00235000", "pnl": -2660.0, "reason": "stop_loss_hit_at_scan", "return_pct": -45.78, "ticker": "HON"}
2026-04-13T09:30:05.721136-04:00 data_refresh data_refresh                                                                                                                                               {'saved': 99}
2026-04-10T16:00:04.433718-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:55:06.433939-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:40:05.440122-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:35:01.390117-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:30:06.443787-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:25:06.434467-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413094505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413094505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413094505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413094505)

</details>
