# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 13:00:02 EDT`
Last processed slot: `manage_1300`

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

- Cash: `$7,080.20`
- Equity: `$12,984.93`
- Realized PnL: `$2,953.99`
- Unrealized PnL: `$30.94`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   2     26     5873.79                 5904.73       225.91          227.1      225.91         227.1           30.94                   0.53         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23         7.45       8.675 980.0   16.442953 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           97.06               34            0.77              0.50         93.02                46.34            True
  SHOP           93.75               16            4.53              4.18        130.17                53.34            True
  BKNG           89.74               39            0.55              0.69        179.10                44.00            True
  DDOG           88.89               27            2.35              2.17        131.21                58.97            True
  ABNB           88.24               34            0.86              0.87        143.81                37.26            True
  QCOM           87.50               24            1.21              1.16        135.57                21.23            True
  DXCM           86.67               45            0.71              0.32         63.27                37.31            True
  ASML           86.11               36            0.65              6.52       1440.86                53.38            True
  TSLA           85.00               20            2.70              7.33        384.37                48.19            True
  SNPS           84.62               13            3.38             11.28        472.43                42.64            True
  CSCO           84.00               25            0.58              0.37         89.64                27.83            True
   ADP           83.33               12            2.43              3.43        200.22                26.51            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-23T13:00:02.294368-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-23T12:55:00.856589-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-23T12:40:04.311160-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-23T12:35:04.168358-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-23T12:30:01.242610-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-23T12:25:03.186227-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-23T12:10:04.189589-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-23T12:05:01.187665-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-23T12:00:03.198539-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-23T11:55:01.249277-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423130002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423130002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423130002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423130002)

</details>
