# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 13:20:00 EDT`
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

- Cash: `$1,069.00`
- Equity: `$13,486.60`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$341.60`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                  6440.0          8.8            9.2      186.41        188.38           280.0                   4.55         100.0               20              1.42         38.05           35.92                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                  5977.6        739.5          747.2      739.50        747.20            61.6                   1.04         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               29            1.10              5.82        753.02                24.04            True
   HON          100.00               22            0.91              1.49        232.60                23.78            True
  MRVL           96.97               33            1.04              0.98        133.38                70.60            True
   WDC           96.88               32            2.34              6.00        363.65                85.18            True
  ALNY           91.89               37            1.24              2.95        338.15                42.77            True
   XEL           90.91               11            1.00              0.56         79.59                20.57            True
  MPWR           90.00               30            1.78             16.99       1356.14                58.76            True
   MAR           88.89               36            0.64              1.63        366.00                29.18            True
  DXCM           88.57               35            1.35              0.60         62.69                31.26            True
  FAST           88.46               26            1.05              0.33         44.48                38.71            True
  GILD           88.46               26            0.64              0.63        140.18                21.91            True
  VRTX           88.24               34            0.91              2.84        443.06                27.91            True
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

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415132000)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415132000)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415132000)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415132000)

</details>
