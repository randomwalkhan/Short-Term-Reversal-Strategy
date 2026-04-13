# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 10:05:00 EDT`
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
   HON          100.00               21            0.71              1.16        234.56                23.73            True
   WDC           97.22               36            0.80              1.92        342.61                85.50            True
   STX           94.59               37            0.62              2.19        502.19                75.16            True
   WMT           93.10               29            0.74              0.65        126.51                25.46            True
  FAST           91.67               12            2.26              0.78         48.84                26.67            True
  MPWR           91.43               35            0.88              8.38       1350.26                59.12            True
  GILD           90.32               31            0.56              0.55        138.80                21.48            True
  COST           90.00               30            0.68              4.73        996.44                18.13            True
   AEP           90.00               10            1.09              1.04        135.86                18.46            True
  CTAS           88.89               36            0.52              0.64        174.66                29.11            True
  DXCM           88.64               44            0.66              0.29         63.89                33.70            True
  PCAR           88.57               35            0.79              0.70        126.89                27.57            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                      detail
2026-04-13T10:05:00.712812-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T10:00:05.716219-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:55:05.732527-04:00  manage_1000 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:40:00.697850-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:35:00.760791-04:00  manage_0930 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-13T09:30:05.721136-04:00  manage_0930         exit {"asset_type": "option", "contract_symbol": "HON260522C00235000", "pnl": -2660.0, "reason": "stop_loss_hit_at_scan", "return_pct": -45.78, "ticker": "HON"}
2026-04-13T09:30:05.721136-04:00 data_refresh data_refresh                                                                                                                                               {'saved': 99}
2026-04-10T16:00:04.433718-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:55:06.433939-04:00  manage_1600 slot_skipped                                                                                                                             {"reason": "already_processed"}
2026-04-10T15:40:05.440122-04:00  manage_1530 slot_skipped                                                                                                                             {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413100500)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413100500)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413100500)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413100500)

</details>
