# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 14:00:06 EDT`
Last processed slot: `manage_1400`

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
   HON          100.00               22            0.64              1.05        235.61                23.67            True
  DDOG           90.91               11            5.20              3.97        107.28                49.83            True
  SNPS           90.48               21            2.49              7.05        401.82                36.22            True
  ROST           90.48               21            1.09              1.72        224.17                24.66            True
  CHTR           88.57               35            1.00              1.56        222.56                29.22            True
  ABNB           88.24               34            1.08              0.98        128.74                41.65            True
 CMCSA           88.24               17            0.68              0.13         28.25                24.06            True
  TTWO           86.67               30            1.46              2.02        197.18                26.78            True
   CSX           85.71               21            0.76              0.23         42.39                21.51            True
 GOOGL           85.37               41            0.52              1.15        317.98                36.19            True
  PLTR           85.19               27            2.64              2.41        129.50                58.33            True
  ORLY           84.62               26            1.20              0.80         94.05                24.35            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T14:00:06.425709-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T13:55:01.428998-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T13:40:01.464603-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:35:01.473626-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:30:04.432792-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:25:06.439063-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:10:06.433211-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-10T13:05:06.440925-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-10T13:00:06.425125-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-10T12:55:06.435366-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410140006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410140006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410140006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410140006)

</details>
