# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 11:15:06 EDT`
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

- Cash: `$8,625.00`
- Equity: `$12,700.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-325.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4075.0                44.0                 40.75      764.07        750.17          -325.0                  -7.39         100.0               21              1.48         48.92           50.41                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               13            2.22             11.96        762.73                26.14            True
  ROST           90.91               22            1.01              1.59        224.23                24.66            True
  CDNS           90.91               11            3.24              6.38        278.28                29.62            True
   WMT           90.91               11            1.58              1.43        128.52                24.68            True
  SNPS           90.00               20            2.52              7.14        401.78                36.22            True
  FTNT           90.00               10            3.05              1.72         79.92                32.65            True
  ABNB           89.66               29            1.39              1.25        128.62                41.65            True
  SHOP           88.37               43            0.70              0.55        112.07                49.23            True
  VRTX           88.00               25            1.45              4.52        444.81                28.30            True
  TMUS           86.36               22            1.04              1.43        196.93                21.21            True
  PLTR           86.21               29            1.73              1.58        129.86                58.33            True
  TTWO           86.21               29            1.50              2.08        197.16                26.78            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T11:10:06.432650-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T11:05:06.437501-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T11:00:06.440938-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:55:06.444820-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:40:06.424520-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:35:06.427990-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:30:06.417352-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:25:06.442890-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:10:06.432351-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:05:06.413334-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410111506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410111506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410111506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410111506)

</details>
