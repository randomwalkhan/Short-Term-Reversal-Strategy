# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 10:45:01 EDT`
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
- Equity: `$12,556.11`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$582.12`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  INTC     option         option INTC260618C00065000       2026-04-22                   1      8     5960.00                 6500.00         7.45           8.12       65.32         66.90          540.00                   9.06        100.00               34              1.42         70.65           68.87                  73.47               19823.0          361.0               0.01                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5915.91       225.91         227.54      225.91        227.54           42.12                   0.72         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               10            1.69              2.60        218.86                25.23            True
  SHOP           91.67               12            5.37              4.96        129.83                53.34            True
  CDNS           90.91               11            3.27              7.60        328.35                46.12            True
  ABNB           89.29               28            1.52              1.53        143.52                37.26            True
  QCOM           89.29               28            0.95              0.91        135.68                21.23            True
  BKNG           89.19               37            0.84              1.06        178.95                44.00            True
  TSLA           88.89               18            3.28              8.89        383.70                48.19            True
  ORLY           88.24               34            0.91              0.60         93.66                22.27            True
  CSCO           86.96               23            0.82              0.52         89.58                27.83            True
  DDOG           86.36               22            3.59              3.33        130.71                58.97            True
  SNPS           83.33               12            3.49             11.66        472.26                42.64            True
   ADP           83.33               12            2.47              3.49        200.19                26.51            True
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

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423104501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423104501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423104501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423104501)

</details>
