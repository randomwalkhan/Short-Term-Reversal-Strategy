# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 11:55:04 EDT`
Last processed slot: `manage_1200`

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
- Equity: `$11,980.49`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$6.50`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                 5880.29       225.91         226.16      225.91        226.16             6.5                   0.11         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               23            0.93              1.45        221.60                25.07            True
   MAR           88.89               27            1.06              2.79        374.26                30.40            True
  CTAS           87.88               33            0.82              1.02        175.82                25.46            True
  GILD           86.36               22            1.07              1.00        132.86                20.00            True
  PAYX           84.62               39            0.74              0.48         93.47                30.98            True
  DASH           83.33               42            0.89              1.14        181.96                52.99            True
   ADP           81.82               33            0.61              0.87        202.50                27.65            True
  WDAY           80.95               42            1.04              0.94        128.76                55.10            True
  CSGP           80.43               46            0.59              0.16         38.84                40.33            True
  ODFL           80.00               25            1.36              2.14        223.50                29.66            True
  FAST           80.00               15            1.77              0.57         45.46                37.98            True
  REGN          100.00               47            0.08              0.40        747.19                22.93           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-22T11:55:04.732707-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-22T11:40:03.815234-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-22T11:35:00.638118-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-22T11:30:04.661182-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-22T11:25:00.817437-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-22T11:10:04.790392-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T11:05:00.789352-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T11:00:02.775064-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T10:55:04.688826-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-22T10:40:00.720670-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422115504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422115504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422115504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422115504)

</details>
