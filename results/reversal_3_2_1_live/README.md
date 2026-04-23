# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 10:50:01 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$140.20`
- Equity: `$12,644.30`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$670.31`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                  6580.0         7.45           8.23       65.32         66.99          620.00                  10.40        100.00               34              1.42         70.65            69.3                  73.47               19823.0          361.0               0.01                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                  5924.1       225.91         227.85      225.91        227.85           50.31                   0.86         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               15            1.33              2.04        219.10                25.23            True
  TSLA           93.75               16            3.36              9.11        383.60                48.19            True
  SNPS           90.91               11            3.77             12.59        471.86                42.64            True
  CDNS           90.00               10            3.64              8.45        327.99                46.12            True
  QCOM           89.66               29            0.92              0.88        135.69                21.23            True
  BKNG           88.89               36            0.95              1.19        178.89                44.00            True
  ORLY           88.89               36            0.81              0.53         93.69                22.27            True
  ABNB           88.46               26            1.58              1.60        143.50                37.26            True
  DDOG           86.36               22            3.81              3.52        130.63                58.97            True
  INSM           84.09               44            0.62              0.62        144.21                48.16            True
  CSCO           84.00               25            0.73              0.46         89.60                27.83            True
    MU           82.86               35            1.74              5.94        484.93                79.49            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T10:40:01.289444-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:35:05.170152-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:30:04.148039-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:25:01.175688-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-23T10:10:04.132146-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T10:05:01.148686-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T10:00:04.240672-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T09:55:03.904981-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-23T09:40:03.171349-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-23T09:35:00.653658-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423105001)

</details>
