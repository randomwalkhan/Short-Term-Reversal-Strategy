# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 10:35:03 EDT`
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
- Equity: `$12,015.20`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$41.21`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                  5915.0       225.91          227.5      225.91         227.5           41.21                    0.7         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               30            0.54              0.83        221.86                25.07            True
  CTAS           88.57               35            0.63              0.78        175.93                25.46            True
   MAR           88.24               34            0.77              2.03        374.58                30.40            True
  FAST           87.50               24            1.32              0.42         45.52                37.98            True
  ODFL           86.11               36            0.72              1.12        223.94                29.66            True
  PAYX           84.21               38            0.78              0.51         93.46                30.98            True
  DASH           83.33               42            0.73              0.93        182.05                52.99            True
  WDAY           82.22               45            0.66              0.60        128.90                55.10            True
  CTSH           82.14               28            1.57              0.67         60.16                29.24            True
   TRI           81.82               33            2.22              1.50         96.08                39.61            True
   ADP           81.48               27            0.85              1.21        202.35                27.65            True
  GEHC           80.65               31            1.03              0.52         72.04                33.30            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-22T10:35:03.653991-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:30:00.799409-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:25:01.815083-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-22T10:10:00.802391-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T10:05:03.491496-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T10:00:03.876171-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T09:55:02.460900-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-22T09:40:05.761376-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:35:00.782755-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-22T09:30:00.737460-04:00 manage_0930 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422103503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422103503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422103503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422103503)

</details>
