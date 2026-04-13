# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 12:35:05 EDT`
Last processed slot: `manage_1230`

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
  REGN          100.00               24            1.24              6.52        746.07                24.22            True
   HON          100.00               20            0.92              1.51        234.42                23.73            True
   CSX           88.46               26            0.56              0.16         42.17                21.76            True
  GILD           87.50               24            0.86              0.84        138.67                21.48            True
  DXCM           85.00               20            1.92              0.86         63.65                33.70            True
   PEP           85.00               20            0.80              0.88        156.68                20.42            True
  ODFL           83.33               36            0.59              0.85        207.98                24.62            True
   EXC           83.33               12            0.96              0.33         48.43                21.28            True
   ADI           82.14               28            0.96              2.35        349.13                33.95            True
    MU           81.82               33            1.58              4.64        418.60                76.70            True
  TMUS           81.25               16            1.53              2.10        194.81                20.04            True
  AMAT           80.00               25            1.93              5.41        397.18                55.88            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-13T12:35:05.834542-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:30:04.889814-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:25:05.699971-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-13T12:10:04.726532-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T12:05:04.704614-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T12:00:03.459495-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T11:55:05.724845-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-13T11:40:05.701560-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-13T11:35:02.700232-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-13T11:30:04.703768-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413123505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413123505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413123505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413123505)

</details>
