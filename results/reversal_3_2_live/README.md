# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 14:25:06 EDT`
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
   HON          100.00               25            0.55              0.90        235.67                23.67            True
 CMCSA          100.00               10            0.93              0.18         28.23                24.06            True
  ABNB           90.62               32            1.20              1.08        128.70                41.65            True
  CHTR           89.47               38            0.59              0.92        222.84                29.22            True
  ROST           89.47               19            1.19              1.87        224.11                24.66            True
  SNPS           88.24               17            2.89              8.18        401.34                36.22            True
  TTWO           85.71               35            1.24              1.72        197.31                26.78            True
   CSX           85.00               20            0.93              0.28         42.37                21.51            True
  SHOP           84.62               26            2.35              1.85        111.51                49.23            True
  DDOG           84.62               13            4.76              3.63        107.42                49.83            True
  BKNG           83.33               24            2.10              2.60        175.49                36.59            True
   EXC           83.33               12            1.01              0.35         49.29                21.05            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T14:25:06.437702-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-10T14:10:05.436380-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T14:05:04.428423-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T14:00:06.425709-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T13:55:01.428998-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-10T13:40:01.464603-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:35:01.473626-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:30:04.432792-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:25:06.439063-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-10T13:10:06.433211-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410142506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410142506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410142506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410142506)

</details>
