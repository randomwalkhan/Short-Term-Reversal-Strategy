# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 13:15:06 EDT`
Last processed slot: `manual`

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
   HON          100.00               20            0.75              1.24        235.53                23.67            True
  SBUX           93.94               33            0.72              0.49         96.71                40.73            True
  DDOG           91.67               12            5.04              3.84        107.33                49.83            True
  GILD           90.91               11            1.53              1.52        141.44                20.31            True
  ABNB           90.62               32            1.18              1.07        128.70                41.65            True
  ROST           89.47               19            1.14              1.80        224.14                24.66            True
 CMCSA           88.24               17            0.65              0.13         28.25                24.06            True
  SNPS           86.67               15            3.08              8.73        401.10                36.22            True
  TTWO           86.49               37            1.11              1.54        197.39                26.78            True
   KDP           86.36               22            0.59              0.11         26.37                20.98            True
  CHTR           86.21               29            1.41              2.20        222.29                29.22            True
  SHOP           85.71               28            2.07              1.63        111.61                49.23            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T13:10:06.433211-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-10T13:05:06.440925-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-10T13:00:06.425125-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-10T12:55:06.435366-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-10T12:40:06.423528-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-10T12:35:06.432794-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-10T12:30:06.458059-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-10T12:25:06.421672-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-10T12:10:06.431827-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-10T12:05:06.416876-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410131506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410131506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410131506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410131506)

</details>
