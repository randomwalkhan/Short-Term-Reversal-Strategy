# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 13:20:00 EDT`
Last processed slot: `manage_1330`

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
- Equity: `$12,029.63`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$55.64`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   1     26     5873.79                 5929.43       225.91         228.05      225.91        228.05           55.64                   0.95         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               34            1.03              0.48         66.06                73.47            True
   HON          100.00               25            0.84              1.31        221.66                25.07            True
   XEL           92.86               14            0.94              0.52         78.86                20.08            True
   CSX           90.00               30            0.53              0.16         43.30                16.22            True
  PCAR           89.19               37            0.71              0.63        125.91                27.36            True
  GILD           86.96               23            1.04              0.97        132.88                20.00            True
  CTAS           85.71               28            1.04              1.29        175.71                25.46            True
  PAYX           83.78               37            0.85              0.56         93.44                30.98            True
  DASH           82.93               41            0.98              1.25        181.91                52.99            True
   ADP           81.25               32            0.65              0.93        202.47                27.65            True
   MAR           81.25               16            1.75              4.61        373.47                30.40            True
  WDAY           80.49               41            1.28              1.16        128.66                55.10            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-22T13:10:03.659705-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T13:05:00.667932-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T13:00:03.792224-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T12:55:04.670092-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-22T12:40:00.840475-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:35:00.859246-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:30:00.662087-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:25:00.650264-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-22T12:10:04.637742-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-22T12:05:05.644708-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422132000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422132000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422132000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422132000)

</details>
