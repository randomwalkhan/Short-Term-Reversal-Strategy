# Reversal 3.2 Live Paper Test

Latest checkpoint (ET): `2026-04-10 10:20:06 EDT`
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
- Equity: `$13,100.00`
- Realized PnL: `$3,025.00`
- Unrealized PnL: `$75.00`
- Open positions: `1`

## Open Positions

```text
ticker     contract_symbol entry_trade_date  business_days_held  contracts  cash_spent  current_position_value  entry_option_price  current_option_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct
  REGN REGN260515C00765000       2026-04-09                   1          1      4400.0                  4475.0                44.0                 44.75      764.07         761.9            75.0                    1.7         100.0               21              1.48         48.92           52.36                  26.04
```

## Today's Closed Trades (2026-04-10)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               32            0.77              4.16        766.07                26.14            True
   WMT           92.86               14            1.39              1.25        128.59                24.68            True
  CDNS           90.91               11            3.24              6.37        278.28                29.62            True
  ROST           90.00               10            1.51              2.38        223.89                24.66            True
  BKNG           89.47               38            0.65              0.80        176.26                36.59            True
  SNPS           88.89               18            2.77              7.84        401.48                36.22            True
  SHOP           88.64               44            0.52              0.41        112.13                49.23            True
  VRTX           88.57               35            0.88              2.75        445.56                28.30            True
  INSM           88.24               34            1.30              1.46        158.97                51.90            True
  GILD           87.50               24            0.83              0.83        141.74                20.31            True
  DXCM           86.84               38            1.24              0.57         65.44                32.42            True
  TTWO           86.49               37            0.95              1.32        197.48                26.78            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-10T10:10:06.432351-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:05:06.413334-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T10:00:05.430800-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:55:06.164206-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-10T09:40:06.426501-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:35:06.431602-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-10T09:30:06.431975-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-09T16:00:01.894335-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-09T15:55:05.644912-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-09T15:40:01.001993-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260410102006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260410102006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260410102006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260410102006)

</details>
