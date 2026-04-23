# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 11:35:01 EDT`
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
- Equity: `$12,813.00`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$839.01`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                  6780.0         7.45           8.48       65.32         67.51          820.00                  13.76        100.00               34              1.42         70.65           68.66                  73.47               19823.0          361.0               0.01                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                  5892.8       225.91         226.65      225.91        226.65           19.01                   0.32         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  SHOP           93.75               16            4.51              4.16        130.18                53.34            True
  CDNS           90.91               11            3.26              7.57        328.36                46.12            True
  ABNB           90.62               32            1.16              1.17        143.68                37.26            True
  QCOM           89.66               29            0.92              0.87        135.70                21.23            True
  BKNG           89.19               37            0.89              1.12        178.92                44.00            True
  DDOG           88.89               27            2.33              2.16        131.22                58.97            True
  DXCM           86.96               46            0.54              0.24         63.31                37.31            True
  ASML           85.71               35            0.68              6.90       1440.70                53.38            True
  TSLA           85.71               21            2.61              7.07        384.48                48.19            True
  SNPS           84.62               13            3.36             11.21        472.45                42.64            True
  ISRG           83.78               37            0.84              2.86        482.40                37.51            True
  MELI           80.00               30            1.35             17.56       1853.45                31.82            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T11:35:01.179247-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:30:04.126054-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:25:01.320467-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-23T11:10:05.162914-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:05:01.126131-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T11:00:03.421218-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:55:01.987617-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-23T10:40:01.289444-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:35:05.170152-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:30:04.148039-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423113501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423113501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423113501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423113501)

</details>
