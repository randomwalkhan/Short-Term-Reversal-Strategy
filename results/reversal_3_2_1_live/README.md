# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 11:20:05 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$140.20`
- Equity: `$12,653.23`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$679.24`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                 6620.00         7.45           8.27       65.32         67.58          660.00                  11.07        100.00               34              1.42         70.65           66.26                  73.47               19823.0          361.0               0.01                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5893.03       225.91         226.65      225.91        226.65           19.24                   0.33         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  SHOP           94.12               17            4.27              3.95        130.27                53.34            True
  CDNS           90.91               11            3.23              7.50        328.40                46.12            True
  ABNB           90.62               32            1.23              1.25        143.65                37.26            True
  BKNG           89.74               39            0.65              0.82        179.05                44.00            True
  DDOG           88.89               27            2.42              2.24        131.18                58.97            True
  QCOM           88.00               25            1.17              1.11        135.59                21.23            True
  ISRG           84.62               39            0.57              1.92        482.80                37.51            True
  SNPS           84.62               13            3.37             11.25        472.44                42.64            True
  TSLA           84.21               19            2.84              7.71        384.20                48.19            True
   ADP           83.33               12            2.10              2.97        200.42                26.51            True
  MELI           82.86               35            1.14             14.88       1854.60                31.82            True
  PLTR           82.35               17            4.12              4.40        150.73                58.48            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T11:10:05.162914-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:05:01.126131-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:00:03.421218-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:55:01.987617-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:40:01.289444-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:35:05.170152-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:30:04.148039-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:25:01.175688-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:10:04.132146-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T10:05:01.148686-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423112005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423112005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423112005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423112005)

</details>
