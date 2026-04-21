# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 16:00:05 EDT`
Last processed slot: `manage_1600`

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
- Equity: `$11,965.54`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$-8.45`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   0     26     5873.79                 5865.34       225.91         225.59      225.91        225.59           -8.45                  -0.14         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-21)

```text
ticker asset_type execution_mode instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price        pnl  return_pct           exit_reason
   HON      share share_fallback        HON     23          2026-04-20         2026-04-21   229.925003  222.725006 -165.59993   -3.131455 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  ROST           94.44               18            1.17              1.86        227.45                25.78            True
  ALNY           92.86               42            0.87              1.89        310.13                46.90            True
  NVDA           92.86               28            1.16              1.64        201.36                32.81            True
  UPRO           92.00               25            2.21              1.92        123.66                53.04            True
  CHTR           91.43               35            1.14              1.95        243.85                38.05            True
  SBUX           91.30               23            1.16              0.81         98.61                31.75            True
   AEP           90.91               11            1.03              0.96        132.87                13.52            True
  BKNG           90.00               40            0.60              0.80        191.69                38.46            True
  VRTX           90.00               40            0.59              1.81        438.40                26.84            True
  SHOP           90.00               20            3.06              2.90        133.90                55.61            True
  GILD           90.00               10            1.90              1.81        135.10                18.88            True
   MAR           88.24               34            0.83              2.19        377.78                30.20            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-21T16:00:05.699902-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-21T15:55:05.701921-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-21T15:40:05.716931-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-21T15:35:05.716188-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-21T15:30:05.732127-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-21T15:25:01.726215-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-21T15:10:05.707514-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-21T15:05:05.718333-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-21T15:00:05.722865-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-21T14:55:05.717229-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421160005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421160005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421160005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421160005)

</details>
