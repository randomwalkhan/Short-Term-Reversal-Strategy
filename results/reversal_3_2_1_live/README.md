# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 10:20:05 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while share-fallback positions also run take-profit and stop loss scans in after-hours / overnight / pre-market
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; share positions can additionally trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$6,100.20`
- Equity: `$12,014.68`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$40.69`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                 5914.48       225.91         227.48      225.91        227.48           40.69                   0.69         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FAST           91.89               37            0.60              0.19         45.62                37.98            True
  CTSH           86.49               37            0.94              0.40         60.28                29.24            True
   TRI           84.62               39            1.44              0.97         96.30                39.61            True
  BKNG           82.61               23            2.35              3.14        189.51                38.41            True
   ADP           82.35               34            0.55              0.78        202.54                27.65            True
  INTC          100.00               44            0.09              0.04         66.24                73.47           False
  TMUS          100.00                1            4.30              5.88        192.87                23.13           False
  GILD           93.18               44            0.05              0.05        133.27                20.00           False
  COST           90.00               50            0.08              0.57       1005.57                18.71           False
   MAR           89.74               39            0.36              0.94        375.05                30.40           False
  CTAS           89.47               38            0.50              0.62        176.00                25.46           False
  PAYX           85.71               42            0.49              0.32         93.54                30.98           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-22T10:10:00.802391-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T10:05:03.491496-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T10:00:03.876171-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T09:55:02.460900-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T09:40:05.761376-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:35:00.782755-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:30:00.737460-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:25:03.754012-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T00:00:03.059399-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-21T16:10:05.711167-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422102005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422102005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422102005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422102005)

</details>
