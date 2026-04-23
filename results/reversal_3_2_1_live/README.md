# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 09:50:03 EDT`
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
- Equity: `$12,072.88`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$98.89`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5932.68       225.91         228.18      225.91        228.18           58.89                   1.00         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                 6000.00         7.45           7.50       65.32         67.03           40.00                   0.67        100.00               34              1.42         70.65             0.0                  73.47               19823.0          361.0               0.01                                       ok
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  SHOP           92.31               13            5.21              4.82        129.90                53.34            True
  ABNB           90.00               30            1.33              1.34        143.60                37.26            True
  BKNG           89.74               39            0.60              0.75        179.08                44.00            True
  DDOG           87.50               16            4.71              4.36        130.27                58.97            True
  SNPS           86.67               15            3.08             10.29        472.85                42.64            True
  TSLA           86.36               22            2.46              6.67        384.65                48.19            True
  CSGP           85.29               34            1.81              0.49         38.56                38.80            True
  PLTR           83.33               24            3.01              3.22        151.24                58.48            True
    MU           82.35               34            2.24              7.65        484.20                79.49            True
  INSM           82.05               39            0.84              0.85        144.12                48.16            True
  MSTR           81.58               38            1.74              2.18        178.42                72.13            True
  ORLY           80.00               20            1.38              0.91         93.53                22.27            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-23T09:40:03.171349-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:35:00.653658-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:30:05.624647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:25:02.140928-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T00:00:05.676693-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-22T16:10:00.877040-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-22T16:05:04.723707-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-22T16:00:04.918061-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-22T15:55:02.714519-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-22T15:40:01.767871-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423095003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423095003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423095003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423095003)

</details>
