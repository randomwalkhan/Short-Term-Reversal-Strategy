# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 10:40:06 EDT`
Last processed slot: `manage_1030`

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
- Equity: `$12,765.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-260.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4140.0                44.0                  41.4      764.07        760.12          -260.0                  -5.91         100.0               21              1.48         48.92           50.29                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               29            1.01              5.41        765.53                26.14            True
  CDNS           90.00               10            3.56              7.01        278.01                29.62            True
  VRTX           89.19               37            0.76              2.38        445.72                28.30            True
  BKNG           88.89               36            0.84              1.04        176.15                36.59            True
  DXCM           88.57               35            1.39              0.64         65.41                32.42            True
  INSM           87.50               32            1.43              1.60        158.90                51.90            True
  TTWO           87.18               39            0.87              1.20        197.53                26.78            True
  SNPS           86.96               23            2.29              6.50        402.06                36.22            True
  GILD           85.00               20            1.07              1.07        141.63                20.31            True
   EXC           84.21               19            0.69              0.24         49.34                21.05            True
  ISRG           84.09               44            0.55              1.74        454.19                22.96            True
  PLTR           83.33               30            1.64              1.50        129.90                58.33            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T10:40:06.424520-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:35:06.427990-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:30:06.417352-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:25:06.442890-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:10:06.432351-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:05:06.413334-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:00:05.430800-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:55:06.164206-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:40:06.426501-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:35:06.431602-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410104006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410104006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410104006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410104006)

</details>
