# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-08 13:55:06 EDT`
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
  FTNT           92.86               28            1.59              0.93         83.32                31.42            True
  INSM           83.33               36            1.15              1.31        162.47                53.00            True
  CSGP           82.35               34            1.52              0.42         39.30                36.79            True
  PLTR           80.00               10            4.70              4.94        147.95                49.26            True
  CHTR           88.10               42            0.42              0.66        223.52                33.96           False
  TSLA           85.00               40            0.28              0.68        346.36                46.68           False
   ROP           80.56               36            0.43              1.09        358.36                19.33           False
   APP           78.79               33            2.30              6.59        407.61                67.83           False
  PAYX           76.92               26            1.29              0.83         91.26                26.82           False
   ADP           76.47               17            1.17              1.66        202.90                22.69           False
  TEAM           76.09               46            0.51              0.23         64.73                51.08           False
    ZS           76.00               25            2.09              2.08        141.20                47.83           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-08T13:55:06.425726-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-08T13:41:40.211226-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-08T13:35:06.448096-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-08T13:30:06.427797-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-08T13:25:05.429044-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-08T13:10:06.427222-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-08T13:05:03.422664-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-08T13:00:06.429648-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-08T12:55:06.421626-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-08T12:40:05.425689-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260408135506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260408135506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260408135506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260408135506)

</details>
