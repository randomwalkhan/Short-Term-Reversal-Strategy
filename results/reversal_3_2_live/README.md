# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 14:30:06 EDT`
Last processed slot: `manage_1430`

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
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$12,235.00`
- Equity: `$12,235.00`
- Realized PnL: `$2,235.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-10)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct           exit_reason
  REGN REGN260515C00765000          2026-04-09         2026-04-10                44.0               36.1 -790.0  -17.954545 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  ABNB           90.91               33            1.09              0.99        128.74                41.65            True
 CMCSA           90.91               11            0.92              0.18         28.23                24.06            True
  ROST           90.48               21            1.09              1.72        224.17                24.66            True
  CHTR           89.19               37            0.65              1.01        222.80                29.22            True
  SNPS           88.89               18            2.80              7.95        401.44                36.22            True
  TTWO           85.71               35            1.24              1.71        197.32                26.78            True
  DDOG           85.71               14            4.44              3.38        107.53                49.83            True
 GOOGL           85.37               41            0.52              1.17        317.98                36.19            True
   CSX           85.00               20            0.93              0.28         42.37                21.51            True
  SHOP           84.62               26            2.29              1.80        111.53                49.23            True
  ORLY           84.62               26            1.19              0.79         94.05                24.35            True
  ODFL           83.33               36            0.58              0.84        209.14                37.04            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T14:30:06.426052-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-10T14:25:06.437702-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-10T14:10:05.436380-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T14:05:04.428423-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T14:00:06.425709-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T13:55:01.428998-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T13:40:01.464603-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:35:01.473626-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:30:04.432792-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:25:06.439063-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410143006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410143006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410143006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410143006)

</details>
