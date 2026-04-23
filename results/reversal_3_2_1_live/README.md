# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 10:15:01 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$140.20`
- Equity: `$13,172.38`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$1,198.39`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                 7080.00         7.45           8.85       65.32         66.61         1120.00                  18.79        100.00               34              1.42         70.65           77.71                  73.47               19823.0          361.0               0.01                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5952.18       225.91         228.93      225.91        228.93           78.39                   1.33         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               10            1.66              2.56        218.87                25.23            True
  DDOG           92.86               14            5.04              4.66        130.14                58.97            True
  CDNS           90.91               11            3.40              7.89        328.23                46.12            True
  ORLY           90.70               43            0.65              0.43         93.74                22.27            True
  ABNB           90.00               30            1.37              1.38        143.59                37.26            True
  SNPS           86.67               15            3.07             10.27        472.86                42.64            True
   CEG           84.21               38            0.86              1.73        286.42                42.95            True
  CSCO           84.00               25            0.62              0.39         89.63                27.83            True
  GEHC           82.86               35            0.82              0.41         71.20                33.42            True
  CSGP           82.76               29            2.37              0.64         38.49                38.80            True
    MU           80.65               31            2.72              9.28        483.50                79.49            True
  PLTR           80.00               10            5.37              5.74        150.16                58.48            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-23T10:10:04.132146-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T10:05:01.148686-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T10:00:04.240672-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T09:55:03.904981-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T09:40:03.171349-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:35:00.653658-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:30:05.624647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:25:02.140928-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T00:00:05.676693-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-22T16:10:00.877040-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423101501)

</details>
