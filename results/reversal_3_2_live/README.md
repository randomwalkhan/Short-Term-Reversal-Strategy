# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 12:55:06 EDT`
Last processed slot: `manage_1300`

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
  SBUX           94.12               34            0.66              0.45         96.73                40.73            True
   WMT           92.86               14            1.42              1.28        128.58                24.68            True
  DDOG           91.67               12            5.09              3.88        107.32                49.83            True
  SNPS           90.91               11            3.56             10.08        400.52                36.22            True
  ABNB           89.29               28            1.40              1.27        128.62                41.65            True
  ROST           88.89               18            1.20              1.89        224.10                24.66            True
 CMCSA           88.89               18            0.62              0.12         28.26                24.06            True
  SHOP           87.10               31            1.63              1.29        111.76                49.23            True
  TTWO           86.49               37            1.04              1.44        197.43                26.78            True
   KDP           86.36               22            0.55              0.10         26.38                20.98            True
  CHTR           86.21               29            1.37              2.14        222.31                29.22            True
  PLTR           85.71               28            2.26              2.06        129.65                58.33            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                               detail
2026-04-10T12:55:06.435366-04:00 manage_1300 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:40:06.423528-04:00 manage_1230 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:35:06.432794-04:00 manage_1230 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:30:06.458059-04:00 manage_1230 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:25:06.421672-04:00 manage_1230 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:10:06.431827-04:00 manage_1200 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:05:06.416876-04:00 manage_1200 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T12:00:03.430473-04:00 manage_1200 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:55:06.430039-04:00 manage_1200 slot_skipped                                                                                                      {"reason": "already_processed"}
2026-04-10T11:50:06.437190-04:00 manage_1200         exit {"contract_symbol": "REGN260515C00765000", "pnl": -790.0, "reason": "stop_loss_hit_at_scan", "return_pct": -17.95, "ticker": "REGN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410125506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410125506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410125506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410125506)

</details>
