# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 12:50:04 EDT`
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

- Cash: `$6,100.20`
- Equity: `$12,017.80`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$43.81`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                  5917.6       225.91          227.6      225.91         227.6           43.81                   0.75         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               34            1.49              0.69         65.96                73.47            True
   HON          100.00               23            0.85              1.32        221.65                25.07            True
   XEL           94.74               19            0.71              0.40         78.91                20.08            True
  PCAR           89.19               37            0.65              0.57        125.94                27.36            True
  GILD           88.89               27            0.89              0.83        132.94                20.00            True
  CTAS           87.88               33            0.88              1.08        175.80                25.46            True
   MAR           86.67               15            1.83              4.80        373.39                30.40            True
  PAYX           84.85               33            1.11              0.73         93.37                30.98            True
  FAST           84.62               13            2.11              0.68         45.41                37.98            True
  DASH           81.58               38            1.40              1.79        181.68                52.99            True
   ADP           81.48               27            0.84              1.19        202.36                27.65            True
  CSGP           80.95               42            0.82              0.22         38.81                40.33            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-22T12:40:00.840475-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:35:00.859246-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:30:00.662087-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:25:00.650264-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:10:04.637742-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-22T12:05:05.644708-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-22T12:00:01.845737-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-22T11:55:04.732707-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-22T11:40:03.815234-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
2026-04-22T11:35:00.638118-04:00 manage_1130 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422125004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422125004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422125004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422125004)

</details>
