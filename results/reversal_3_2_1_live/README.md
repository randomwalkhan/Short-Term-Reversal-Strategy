# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 09:45:03 EDT`
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

- Cash: `$6,100.20`
- Equity: `$11,955.66`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$-18.33`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                 5855.46       225.91         225.21      225.91        225.21          -18.33                  -0.31         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FAST           92.31               39            0.50              0.16         45.63                37.98            True
  BKNG           87.50               32            1.32              1.76        190.10                38.41            True
  CTSH           85.29               34            1.16              0.49         60.24                29.24            True
  ROST           97.67               43            0.19              0.29        225.46                26.28           False
    EA           95.24               42            0.06              0.08        203.52                 4.87           False
  CHTR           93.75               48            0.02              0.04        241.93                38.39           False
  GILD           91.67               36            0.36              0.34        133.15                20.00           False
  VRTX           91.49               47            0.03              0.09        436.55                26.83           False
   WMT           91.11               45            0.09              0.08        129.56                24.14           False
   MAR           90.00               40            0.15              0.39        375.28                30.40           False
  CTAS           88.37               43            0.35              0.44        176.07                25.46           False
  COST           87.80               41            0.44              3.09       1004.49                18.71           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-22T09:40:05.761376-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:35:00.782755-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:30:00.737460-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:25:03.754012-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T00:00:03.059399-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-21T16:10:05.711167-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-21T16:05:05.720071-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-21T16:00:05.699902-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-21T15:55:05.701921-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-21T15:40:05.716931-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422094503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422094503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422094503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422094503)

</details>
