# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 11:40:01 EDT`
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
- Equity: `$12,932.19`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$958.20`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                 6900.00         7.45           8.62       65.32         67.56           940.0                  15.77        100.00               34              1.42         70.65           69.78                  73.47               19823.0          361.0               0.01                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5891.99       225.91         226.62      225.91        226.62            18.2                   0.31         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  SHOP           93.75               16            4.43              4.10        130.20                53.34            True
  ABNB           90.00               30            1.35              1.37        143.59                37.26            True
  CDNS           90.00               10            3.59              8.34        328.03                46.12            True
  BKNG           89.19               37            0.89              1.12        178.92                44.00            True
  DDOG           88.89               27            2.45              2.27        131.17                58.97            True
  QCOM           88.89               27            1.06              1.01        135.64                21.23            True
  DXCM           86.67               45            0.65              0.29         63.29                37.31            True
  TSLA           86.36               22            2.42              6.55        384.70                48.19            True
  SNPS           85.71               14            3.24             10.81        472.63                42.64            True
  ASML           85.29               34            0.78              7.93       1440.26                53.38            True
  ISRG           84.21               38            0.71              2.41        482.59                37.51            True
   ADP           83.33               12            2.21              3.11        200.36                26.51            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T11:40:01.234723-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:35:01.179247-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:30:04.126054-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:25:01.320467-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:10:05.162914-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:05:01.126131-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:00:03.421218-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:55:01.987617-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:40:01.289444-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:35:05.170152-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423114001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423114001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423114001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423114001)

</details>
