# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 10:35:04 EDT`
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

- Cash: `$1,069.00`
- Equity: `$12,815.52`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$-329.48`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5971.52        739.5         746.44      739.50        746.44           55.52                   0.94         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 5775.00          8.8           8.25      186.41        186.30         -385.00                  -6.25         100.0               20              1.42         38.05           39.08                  30.53                 326.0           18.0               0.07                           ok
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               25            1.20              6.35        752.79                24.04            True
   HON          100.00               14            1.29              2.11        232.34                23.78            True
   WDC           97.06               34            1.54              3.94        364.53                85.18            True
   AEP           95.65               23            0.60              0.57        135.22                19.01            True
  FTNT           94.74               38            0.98              0.54         78.47                37.90            True
   WMT           94.44               18            1.18              1.03        124.61                26.20            True
  ALNY           92.31               39            1.05              2.50        338.34                42.77            True
  MPWR           91.18               34            1.15             11.00       1358.71                58.76            True
  ASML           90.91               11            3.44             36.58       1502.62                52.27            True
  VRTX           89.29               28            1.23              3.83        442.64                27.91            True
   STX           88.89               18            4.21             15.71        526.71                74.84            True
   MAR           88.46               26            1.12              2.88        365.47                29.18            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-15T10:35:04.887046-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T10:25:06.545831-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T09:40:04.895647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T09:30:03.712505-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T00:00:03.433834-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-14T16:10:06.446292-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:05:03.434274-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:00:06.433014-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:55:03.439674-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:40:03.444191-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415103504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415103504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415103504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415103504)

</details>
