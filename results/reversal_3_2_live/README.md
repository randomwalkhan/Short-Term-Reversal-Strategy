# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 10:30:06 EDT`
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
- Equity: `$12,805.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$-220.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4180.0                44.0                  41.8      764.07        761.78          -220.0                   -5.0         100.0               21              1.48         48.92           49.39                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               32            0.79              4.25        766.03                26.14            True
   WMT           90.91               11            1.62              1.47        128.50                24.68            True
  BKNG           89.47               38            0.64              0.79        176.26                36.59            True
  SNPS           88.89               18            2.66              7.54        401.61                36.22            True
  GILD           88.46               26            0.68              0.68        141.80                20.31            True
  TTWO           87.18               39            0.88              1.22        197.53                26.78            True
  INSM           87.10               31            1.50              1.67        158.87                51.90            True
  DXCM           86.84               38            1.07              0.49         65.47                32.42            True
  ROST           86.67               15            1.24              1.95        224.07                24.66            True
  ABNB           86.49               37            0.74              0.67        128.87                41.65            True
   EXC           85.71               21            0.54              0.19         49.36                21.05            True
  ORLY           84.00               25            1.22              0.80         94.04                24.35            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-10T10:30:06.417352-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:25:06.442890-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-10T10:10:06.432351-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:05:06.413334-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:00:05.430800-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:55:06.164206-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:40:06.426501-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:35:06.431602-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:30:06.431975-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-09T16:00:01.894335-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410103006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410103006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410103006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410103006)

</details>
