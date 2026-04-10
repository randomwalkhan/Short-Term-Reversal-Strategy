# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 12:05:06 EDT`
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
   HON          100.00               24            0.58              0.97        235.65                23.67            True
  SBUX           93.94               33            0.71              0.48         96.71                40.73            True
   WMT           92.86               14            1.37              1.24        128.60                24.68            True
  ABNB           90.91               33            1.10              0.99        128.73                41.65            True
  DDOG           90.91               11            5.23              3.99        107.27                49.83            True
  SNPS           90.91               11            3.57             10.11        400.51                36.22            True
  FTNT           90.00               10            2.99              1.69         79.94                32.65            True
 CMCSA           88.89               18            0.51              0.10         28.27                24.06            True
  GILD           87.50               24            0.87              0.87        141.72                20.31            True
  SHOP           86.67               30            1.71              1.34        111.73                49.23            True
  ROST           86.67               15            1.23              1.94        224.08                24.66            True
  TTWO           86.49               37            1.05              1.45        197.43                26.78            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                               detail
2026-04-10T12:05:06.416876-04:00 manage_1200 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:00:03.430473-04:00 manage_1200 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:55:06.430039-04:00 manage_1200 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:50:06.437190-04:00 manage_1200         exit {"contract_symbol": "REGN260515C00765000", "pnl": -790.0, "reason": "stop_loss_hit_at_scan", "return_pct": -17.95, "ticker": "REGN"}
2026-04-10T11:40:06.438272-04:00 manage_1130 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:35:06.456054-04:00 manage_1130 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:30:06.432539-04:00 manage_1130 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:25:06.448068-04:00 manage_1130 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:10:06.432650-04:00 manage_1100 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:05:06.437501-04:00 manage_1100 slot_skipped                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410120506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410120506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410120506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410120506)

</details>
