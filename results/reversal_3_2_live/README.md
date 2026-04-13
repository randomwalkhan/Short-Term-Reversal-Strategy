# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 10:20:05 EDT`
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
 CMCSA          100.00               11            1.06              0.21         27.84                24.08            True
   XEL           93.75               16            0.80              0.46         82.18                18.59            True
   WMT           92.59               27            0.85              0.75        126.47                25.46            True
   AEP           92.31               26            0.54              0.51        136.08                18.46            True
  MPWR           91.43               35            0.63              6.01       1351.28                59.12            True
  PCAR           90.00               40            0.50              0.45        127.00                27.57            True
   MAR           90.00               30            0.91              2.26        353.13                29.84            True
  COST           90.00               30            0.68              4.76        996.43                18.13            True
  MDLZ           90.00               10            1.44              0.59         58.75                22.21            True
  ASML           87.88               33            0.75              7.78       1474.94                52.64            True
  DXCM           87.80               41            1.00              0.45         63.83                33.70            True
   AMD           84.62               39            0.66              1.13        244.56                49.57            True
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

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413102005)

</details>
