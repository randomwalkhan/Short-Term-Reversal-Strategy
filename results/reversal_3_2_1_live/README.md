# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 11:20:03 EDT`
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

- Cash: `$6,100.20`
- Equity: `$11,999.86`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$25.87`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                 5899.66       225.91         226.91      225.91        226.91           25.87                   0.44         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               23            0.88              1.36        221.64                25.07            True
  CTAS           88.57               35            0.59              0.73        175.95                25.46            True
   MAR           87.88               33            0.82              2.16        374.52                30.40            True
  PAYX           84.62               39            0.77              0.50         93.46                30.98            True
  ODFL           84.38               32            0.89              1.40        223.82                29.66            True
  DASH           83.33               42            0.62              0.79        182.11                52.99            True
  FAST           81.25               16            1.68              0.54         45.47                37.98            True
  CTSH           80.77               26            1.67              0.71         60.15                29.24            True
  WDAY           80.49               41            1.17              1.06        128.71                55.10            True
  TMUS          100.00                1            4.72              6.45        192.62                23.13           False
    EA           95.24               42            0.06              0.08        203.52                 4.87           False
  GILD           91.67               36            0.38              0.35        133.14                20.00           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-22T11:10:04.790392-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T11:05:00.789352-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T11:00:02.775064-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T10:55:04.688826-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T10:40:00.720670-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:35:03.653991-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:30:00.799409-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:25:01.815083-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:10:00.802391-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T10:05:03.491496-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422112003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422112003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422112003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422112003)

</details>
