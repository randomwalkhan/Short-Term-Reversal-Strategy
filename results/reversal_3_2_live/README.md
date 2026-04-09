# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-09 13:50:01 EDT`
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

- Cash: `$13,025.00`
- Equity: `$13,025.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-04-09)

```text
ticker     contract_symbol entry_trade_date_et exit_trade_date_et  entry_option_price  exit_option_price    pnl  return_pct                  exit_reason
  FTNT FTNT260508C00083000          2026-04-08         2026-04-09               5.375               6.75 1375.0   25.581395 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               27            1.17              6.35        772.81                26.04            True
   WDC           97.30               37            0.73              1.72        338.04                87.19            True
  CDNS           90.91               11            3.10              6.29        286.81                28.11            True
  DDOG           90.00               10            5.54              4.51        114.57                46.85            True
  CTAS           88.57               35            0.53              0.64        174.31                30.38            True
  ABNB           88.24               34            0.86              0.79        131.06                41.34            True
  ALNY           87.10               31            1.59              3.64        325.69                41.11            True
  SNPS           86.67               30            1.66              4.78        408.11                37.77            True
  IDXX           80.95               42            0.61              2.51        590.76                27.54            True
  TTWO           80.00               20            1.92              2.72        200.97                26.08            True
  CSCO           80.00               15            1.26              0.74         83.38                27.82            True
  FANG          100.00               32            0.12              0.16        186.40                32.28           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-09T13:40:03.886505-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:35:04.885893-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:30:05.578837-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:25:00.899270-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-09T13:10:02.022275-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T13:05:02.897380-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T13:00:03.062847-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T12:55:00.892899-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-09T12:40:00.955610-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-09T12:35:05.898877-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260409135001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260409135001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260409135001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260409135001)

</details>
