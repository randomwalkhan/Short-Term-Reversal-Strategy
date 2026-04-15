# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 11:15:03 EDT`
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
- Equity: `$13,679.72`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$534.72`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 6650.00          8.8           9.50      186.41        187.77          490.00                   7.95         100.0               20              1.42         38.05           38.05                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5960.72        739.5         745.09      739.50        745.09           44.72                   0.76         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               22            1.36              7.20        752.42                24.04            True
   HON          100.00               17            1.23              2.01        232.38                23.78            True
   WDC           96.88               32            2.45              6.28        363.53                85.18            True
  FTNT           94.74               38            0.98              0.54         78.47                37.90            True
   WMT           94.74               19            1.15              1.01        124.62                26.20            True
   AEP           94.44               18            0.71              0.67        135.17                19.01            True
  FAST           92.31               13            2.06              0.64         44.34                38.71            True
  MPWR           91.67               36            0.78              7.43       1360.23                58.76            True
  ALNY           91.30               23            1.92              4.57        337.45                42.77            True
  VRTX           90.00               30            1.15              3.58        442.74                27.91            True
   STX           89.47               19            4.01             14.97        527.02                74.84            True
   EXC           89.47               19            0.73              0.25         48.51                21.52            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-15T11:10:01.922344-04:00  manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-15T11:05:03.774531-04:00  manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-15T11:00:05.898328-04:00  manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-15T10:55:05.902096-04:00  manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-15T10:40:05.814047-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T10:35:04.887046-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T10:25:06.545831-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T09:40:04.895647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T09:30:03.712505-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T00:00:03.433834-04:00 data_refresh data_refresh                   {'saved': 99}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415111503)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415111503)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415111503)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415111503)

</details>
