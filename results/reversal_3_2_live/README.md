# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 10:35:05 EDT`
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
   HON          100.00               22            0.62              1.02        234.62                23.73            True
  SBUX           94.29               35            0.61              0.41         96.42                40.58            True
   AEP           93.33               15            0.84              0.80        135.96                18.46            True
   WMT           93.10               29            0.72              0.64        126.51                25.46            True
   XEL           92.31               13            0.92              0.53         82.15                18.59            True
  MPWR           91.43               35            0.62              5.84       1351.35                59.12            True
  INSM           90.00               40            0.87              0.94        154.41                53.55            True
  COST           90.00               30            0.66              4.59        996.50                18.13            True
   MAR           89.29               28            0.98              2.42        353.06                29.84            True
  PCAR           89.19               37            0.70              0.63        126.92                27.57            True
  ASML           88.57               35            0.55              5.70       1475.84                52.64            True
  DXCM           86.84               38            1.27              0.57         63.78                33.70            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-13T10:35:05.426321-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:30:05.709721-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:25:05.707735-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:10:00.698595-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T10:05:00.712812-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T10:00:05.716219-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T09:55:05.732527-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T09:40:00.697850-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-13T09:35:00.760791-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-13T09:30:05.721136-04:00 data_refresh data_refresh                   {'saved': 99}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413103505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413103505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413103505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413103505)

</details>
