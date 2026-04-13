# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 12:10:04 EDT`
Last processed slot: `manage_1200`

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
  REGN          100.00               27            1.17              6.13        746.24                24.22            True
   HON          100.00               15            1.15              1.90        234.25                23.73            True
 CMCSA           94.12               17            0.73              0.14         27.87                24.08            True
  MPWR           90.91               33            1.24             11.75       1348.82                59.12            True
  PCAR           89.74               39            0.59              0.52        126.97                27.57            True
   CSX           89.29               28            0.52              0.15         42.17                21.76            True
  DXCM           85.00               20            1.98              0.89         63.64                33.70            True
  AAPL           85.00               20            1.33              2.43        259.44                21.31            True
   PEP           84.21               19            0.87              0.96        156.65                20.42            True
   EXC           83.33               12            1.05              0.36         48.42                21.28            True
    MU           81.25               32            1.82              5.37        418.29                76.70            True
  GILD           81.25               16            1.21              1.18        138.53                21.48            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T12:10:04.726532-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T12:05:04.704614-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T12:00:03.459495-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T11:55:05.724845-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T11:40:05.701560-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-13T11:35:02.700232-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-13T11:30:04.703768-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-13T11:25:03.706340-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-13T11:10:05.703884-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-13T11:05:01.703808-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413121004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413121004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413121004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413121004)

</details>
