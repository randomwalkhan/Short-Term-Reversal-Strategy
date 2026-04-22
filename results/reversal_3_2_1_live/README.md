# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 13:50:00 EDT`
Last processed slot: `manage_1400`

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
- Equity: `$12,035.03`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$61.04`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                 5934.82       225.91         228.26      225.91        228.26           61.04                   1.04         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               35            0.99              0.46         66.06                73.47            True
   HON          100.00               25            0.73              1.14        221.73                25.07            True
  PCAR           87.88               33            0.85              0.75        125.86                27.36            True
   MAR           86.67               15            1.82              4.79        373.40                30.40            True
  CTAS           84.62               26            1.10              1.36        175.68                25.46            True
  PAYX           83.78               37            0.89              0.58         93.43                30.98            True
  DASH           83.33               42            0.72              0.92        182.06                52.99            True
  CSGP           83.33               30            2.29              0.62         38.64                40.33            True
  GILD           83.33               18            1.16              1.08        132.83                20.00            True
   EXC           82.61               23            0.57              0.19         46.19                15.78            True
   ADP           81.48               27            0.82              1.17        202.37                27.65            True
  FAST           80.00               15            1.88              0.60         45.44                37.98            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-22T13:40:03.695776-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-22T13:35:00.811201-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-22T13:30:03.669742-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-22T13:25:05.672659-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-22T13:10:03.659705-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T13:05:00.667932-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T13:00:03.792224-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T12:55:04.670092-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T12:40:00.840475-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:35:00.859246-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422135000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422135000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422135000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422135000)

</details>
