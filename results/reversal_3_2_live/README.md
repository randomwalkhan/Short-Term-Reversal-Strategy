# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 11:10:05 EDT`
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
   HON          100.00               15            1.20              1.98        234.21                23.73            True
   AEP           94.12               17            0.76              0.72        135.99                18.46            True
  SBUX           93.55               31            0.83              0.56         96.36                40.58            True
   WMT           92.86               14            1.25              1.11        126.31                25.46            True
  COST           92.86               14            1.04              7.28        995.35                18.13            True
 CMCSA           92.31               13            0.86              0.17         27.86                24.08            True
  MPWR           91.18               34            1.03              9.76       1349.67                59.12            True
   MAR           88.57               35            0.71              1.77        353.34                29.84            True
   CSX           88.46               26            0.57              0.17         42.17                21.76            True
  DXCM           86.84               38            1.20              0.54         63.79                33.70            True
  PCAR           86.67               30            0.98              0.87        126.82                27.57            True
  INSM           85.71               28            1.95              2.11        153.91                53.55            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T11:10:05.703884-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-13T11:05:01.703808-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-13T11:00:05.700788-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-13T10:55:05.707019-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-13T10:40:05.710710-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:35:05.426321-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:30:05.709721-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:25:05.707735-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-13T10:10:00.698595-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-13T10:05:00.712812-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413111005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413111005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413111005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413111005)

</details>
