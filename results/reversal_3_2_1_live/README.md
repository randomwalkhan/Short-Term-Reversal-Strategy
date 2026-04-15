# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 13:15:02 EDT`
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

- Cash: `$1,069.00`
- Equity: `$13,480.44`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$335.44`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 6440.00          8.8           9.20      186.41        188.09          280.00                   4.55         100.0               20              1.42         38.05           36.72                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5971.44        739.5         746.43      739.50        746.43           55.44                   0.94         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               25            1.20              6.36        752.79                24.04            True
   HON          100.00               20            0.97              1.59        232.56                23.78            True
  MRVL           97.14               35            0.92              0.87        133.43                70.60            True
   WDC           96.88               32            2.38              6.10        363.60                85.18            True
   XEL           91.67               12            0.94              0.52         79.61                20.57            True
  ALNY           91.18               34            1.43              3.41        337.95                42.77            True
  MPWR           90.00               30            1.75             16.74       1356.25                58.76            True
  VRTX           90.00               30            1.14              3.55        442.76                27.91            True
   MAR           88.89               36            0.71              1.83        365.92                29.18            True
  FAST           88.46               26            1.06              0.33         44.48                38.71            True
  GILD           88.46               26            0.64              0.63        140.18                21.91            True
  DXCM           87.10               31            1.49              0.66         62.67                31.26            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-15T13:10:05.907908-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-15T13:05:05.431021-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-15T13:00:04.718911-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-15T12:55:04.722953-04:00 manage_1300 slot_skipped {"reason": "already_processed"}
2026-04-15T12:40:05.426776-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:35:00.710440-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:30:04.719379-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:25:01.751378-04:00 manage_1230 slot_skipped {"reason": "already_processed"}
2026-04-15T12:10:03.719067-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
2026-04-15T12:05:05.700528-04:00 manage_1200 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415131502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415131502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415131502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415131502)

</details>
