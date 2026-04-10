# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 11:00:06 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$12,705.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-320.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4080.0                44.0                  40.8      764.07        756.53          -320.0                  -7.27         100.0               21              1.48         48.92           50.95                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               25            0.52              0.86        235.69                23.67            True
  REGN          100.00               21            1.47              7.92        764.45                26.14            True
  SBUX           94.29               35            0.61              0.41         96.74                40.73            True
   WMT           92.86               14            1.44              1.30        128.57                24.68            True
  GILD           92.31               13            1.35              1.34        141.51                20.31            True
  ROST           90.48               21            1.07              1.68        224.19                24.66            True
  CDNS           90.00               10            3.64              7.17        277.94                29.62            True
  CHTR           88.89               36            0.77              1.20        222.72                29.22            True
  SNPS           88.89               18            2.78              7.89        401.47                36.22            True
  ABNB           88.24               34            1.02              0.92        128.77                41.65            True
  VRTX           88.00               25            1.46              4.57        444.79                28.30            True
  PLTR           86.21               29            2.15              1.97        129.69                58.33            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-10T11:00:06.440938-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:55:06.444820-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-10T10:40:06.424520-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:35:06.427990-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:30:06.417352-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:25:06.442890-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:10:06.432351-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:05:06.413334-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:00:05.430800-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:55:06.164206-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410110006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410110006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410110006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410110006)

</details>
