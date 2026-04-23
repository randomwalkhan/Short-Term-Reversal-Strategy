# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 09:55:03 EDT`
Last processed slot: `manage_1000`

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
- Equity: `$12,074.57`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$100.58`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5934.37       225.91         228.24      225.91        228.24           60.58                   1.03         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                 6000.00         7.45           7.50       65.32         66.53           40.00                   0.67        100.00               34              1.42         70.65             0.0                  73.47               19823.0          361.0               0.01                                       ok
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  DDOG           92.86               14            5.04              4.66        130.14                58.97            True
  SHOP           90.00               10            5.59              5.16        129.75                53.34            True
  ABNB           89.29               28            1.46              1.47        143.55                37.26            True
  BKNG           89.19               37            0.89              1.12        178.92                44.00            True
   ROP           86.67               30            0.87              2.23        363.77                21.92            True
  SNPS           86.67               15            3.18             10.62        472.71                42.64            True
  TSLA           85.00               20            2.71              7.35        384.36                48.19            True
  INSM           84.44               45            0.52              0.53        144.25                48.16            True
  PLTR           83.33               18            4.03              4.31        150.77                58.48            True
    MU           82.86               35            1.94              6.62        484.64                79.49            True
   ADP           81.82               11            2.69              3.80        200.06                26.51            True
  CPRT           80.00               40            0.79              0.19         33.60                14.83            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-23T09:55:03.904981-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T09:40:03.171349-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:35:00.653658-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:30:05.624647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:25:02.140928-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T00:00:05.676693-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-22T16:10:00.877040-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-22T16:05:04.723707-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-22T16:00:04.918061-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-22T15:55:02.714519-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423095503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423095503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423095503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423095503)

</details>
