# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 10:50:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$12,946.80`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$-198.20`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                  5962.8        739.5         745.35      739.50        745.35            46.8                   0.79         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                  5915.0          8.8           8.45      186.41        187.42          -245.0                  -3.98         100.0               20              1.42         38.05           36.18                  30.53                 326.0           18.0               0.07                           ok
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               22            1.36              7.20        752.43                24.04            True
   HON          100.00               22            0.93              1.52        232.59                23.78            True
   WDC           97.06               34            1.25              3.21        364.84                85.18            True
  FTNT           92.86               28            1.56              0.86         78.33                37.90            True
   XEL           92.31               13            0.93              0.52         79.61                20.57            True
   WMT           92.00               25            0.89              0.78        124.72                26.20            True
   STX           90.91               22            3.53             13.19        527.79                74.84            True
  ALNY           90.62               32            1.48              3.52        337.90                42.77            True
   LIN           90.00               20            0.94              3.30        498.27                19.38            True
   MAR           89.66               29            0.97              2.49        365.63                29.18            True
  VRTX           88.00               25            1.32              4.10        442.52                27.91            True
  FAST           86.67               15            1.68              0.53         44.39                38.71            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-15T10:40:05.814047-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T10:35:04.887046-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T10:25:06.545831-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T09:40:04.895647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T09:30:03.712505-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T00:00:03.433834-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-14T16:10:06.446292-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:05:03.434274-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:00:06.433014-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:55:03.439674-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415105005)

</details>
