# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 11:40:06 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$8,625.00`
- Equity: `$12,480.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-545.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  3855.0                44.0                 38.55      764.07        746.74          -545.0                 -12.39         100.0               21              1.48         48.92            53.5                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  SBUX           93.94               33            0.70              0.48         96.72                40.73            True
   WMT           92.31               13            1.54              1.39        128.53                24.68            True
  FTNT           90.91               11            2.88              1.62         79.96                32.65            True
  ABNB           90.00               30            1.34              1.21        128.64                41.65            True
  SNPS           88.89               18            2.77              7.84        401.48                36.22            True
 CMCSA           88.89               18            0.64              0.13         28.26                24.06            True
  ROST           86.67               15            1.26              1.98        224.06                24.66            True
  DXCM           86.36               22            1.82              0.84         65.32                32.42            True
  TMUS           86.36               22            1.07              1.48        196.91                21.21            True
  PLTR           86.21               29            2.04              1.86        129.74                58.33            True
  SHOP           86.11               36            1.27              0.99        111.88                49.23            True
  TTWO           85.71               28            1.64              2.27        197.08                26.78            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T11:40:06.438272-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-10T11:35:06.456054-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-10T11:30:06.432539-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-10T11:25:06.448068-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-10T11:10:06.432650-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T11:05:06.437501-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T11:00:06.440938-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:55:06.444820-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:40:06.424520-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:35:06.427990-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410114006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410114006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410114006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410114006)

</details>
