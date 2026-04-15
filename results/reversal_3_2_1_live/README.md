# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 09:40:04 EDT`
Last processed slot: `manage_0930`

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
- Equity: `$13,110.12`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$-38.12`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5982.88        739.5         747.86      739.50        747.86           66.88                   1.13         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 6055.00          8.8           8.65      186.41        186.00         -105.00                  -1.70         100.0               20              1.42         38.05            43.6                  30.53                 326.0           18.0               0.07                           ok
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               22            1.02              1.33        186.00                31.02            True
   WDC           96.67               30            2.79              7.14        363.16                85.18            True
   WMT           94.44               18            1.21              1.06        124.60                26.20            True
  ALNY           93.48               46            0.51              1.20        338.89                42.77            True
   AEP           92.59               27            0.52              0.49        135.25                19.01            True
   LIN           92.31               13            1.41              4.94        497.57                19.38            True
  MPWR           91.67               36            0.76              7.28       1360.30                58.76            True
  FAST           91.67               12            2.11              0.66         44.34                38.71            True
  VRTX           89.19               37            0.70              2.17        443.35                27.91            True
   MAR           88.24               34            0.84              2.16        365.77                29.18            True
   BKR           86.49               37            0.54              0.23         61.39                34.10            True
  KLAC           85.71               14            3.45             43.42       1777.30                50.02            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-15T09:40:04.895647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T09:30:03.712505-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T00:00:03.433834-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-14T16:10:06.446292-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:05:03.434274-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:00:06.433014-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:55:03.439674-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:40:03.444191-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:35:03.436506-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:30:05.437858-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415094004)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415094004)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415094004)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415094004)

</details>
