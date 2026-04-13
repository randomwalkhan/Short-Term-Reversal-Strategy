# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 09:55:05 EDT`
Last processed slot: `manage_1000`

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
   HON          100.00               25            0.52              0.85        234.70                23.73            True
 CMCSA           94.12               17            0.73              0.14         27.87                24.08            True
   AEP           94.12               17            0.66              0.63        136.03                18.46            True
  SBUX           93.94               33            0.79              0.53         96.37                40.58            True
  FAST           92.31               13            2.19              0.76         48.85                26.67            True
   XEL           91.67               12            0.93              0.54         82.15                18.59            True
  NVDA           91.43               35            0.64              0.84        188.38                35.03            True
  MPWR           91.43               35            0.51              4.79       1351.80                59.12            True
  CHTR           90.48               42            0.50              0.77        218.49                30.19            True
   WMT           90.48               21            0.96              0.85        126.42                25.46            True
  MDLZ           90.00               10            1.47              0.61         58.74                22.21            True
  PCAR           89.19               37            0.66              0.59        126.94                27.57            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                      detail
2026-04-13T09:55:05.732527-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:40:00.697850-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:35:00.760791-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:30:05.721136-04:00  manage_0930         exit {"asset_type": "option", "contract_symbol": "HON260522C00235000", "pnl": -2660.0, "reason": "stop_loss_hit_at_scan", "return_pct": -45.78, "ticker": "HON"}
2026-04-13T09:30:05.721136-04:00 data_refresh data_refresh                                                                                                                                               {'saved': 99}
2026-04-10T16:00:04.433718-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:55:06.433939-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:40:05.440122-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:35:01.390117-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:30:06.443787-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413095505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413095505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413095505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413095505)

</details>
