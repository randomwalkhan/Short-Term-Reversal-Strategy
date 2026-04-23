# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 11:30:04 EDT`
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
- Equity: `$12,698.56`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$724.57`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                 6660.00         7.45           8.32       65.32         67.59          700.00                  11.74        100.00               34              1.42         70.65           66.75                  73.47               19823.0          361.0               0.01                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5898.36       225.91         226.86      225.91        226.86           24.57                   0.42         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  SHOP           93.33               15            4.56              4.21        130.16                53.34            True
  CDNS           90.91               11            3.25              7.54        328.38                46.12            True
  ABNB           90.62               32            1.23              1.24        143.65                37.26            True
  BKNG           89.74               39            0.74              0.92        179.00                44.00            True
  QCOM           88.89               27            1.04              0.99        135.64                21.23            True
  DDOG           88.46               26            2.80              2.59        131.03                58.97            True
  DXCM           86.96               46            0.51              0.23         63.31                37.31            True
  ASML           86.49               37            0.61              6.15       1441.02                53.38            True
  TSLA           85.71               21            2.64              7.15        384.45                48.19            True
  SNPS           83.33               12            3.48             11.61        472.28                42.64            True
   ADP           83.33               12            2.13              3.00        200.40                26.51            True
    MU           81.58               38            0.67              2.30        486.50                79.49            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T11:30:04.126054-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:25:01.320467-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:10:05.162914-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:05:01.126131-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:00:03.421218-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:55:01.987617-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:40:01.289444-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:35:05.170152-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:30:04.148039-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:25:01.175688-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423113004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423113004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423113004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423113004)

</details>
