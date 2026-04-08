# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-08 14:40:04 EDT`
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

- Cash: `$11,650.00`
- Equity: `$11,650.00`
- Realized PnL: `$1,650.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-08)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  TSLA TSLA260515C00340000          2026-04-07         2026-04-08                23.4              30.05 1330.0   28.418803 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FTNT           92.11               38            1.10              0.64         83.44                31.42            True
  TSLA           87.10               31            1.21              2.94        345.39                46.68            True
  CHTR           82.76               29            1.35              2.12        222.89                33.96            True
  CSGP           82.35               34            1.56              0.43         39.30                36.79            True
   ROP           80.00               30            0.76              1.92        358.01                19.33            True
 CMCSA           95.45               22            0.13              0.02         27.78                23.49           False
  CTSH           86.36               44            0.21              0.09         61.45                24.93           False
  PLTR           83.33                6            5.22              5.48        147.72                49.26           False
  INSM           79.31               29            1.77              2.02        162.16                53.00           False
    ZS           76.92               26            1.94              1.93        141.26                47.83           False
   ADP           76.47               17            1.43              2.04        202.73                22.69           False
   TRI           75.00               24            2.46              1.52         87.80                31.02           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-08T14:40:04.447081-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-08T14:35:03.430322-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-08T14:30:06.439712-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-08T14:25:01.442780-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-08T14:10:06.422703-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-08T14:05:04.424556-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-08T14:00:06.430912-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-08T13:55:06.425726-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-08T13:41:40.211226-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-08T13:35:06.448096-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260408144004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260408144004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260408144004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260408144004)

</details>
