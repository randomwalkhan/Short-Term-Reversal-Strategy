# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 11:00:05 EDT`
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
- Equity: `$13,006.16`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$-138.84`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                 5952.16        739.5         744.02      739.50        744.02           36.16                   0.61         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                 5985.00          8.8           8.55      186.41        187.50         -175.00                  -2.84         100.0               20              1.42         38.05           36.44                  30.53                 326.0           18.0               0.07                           ok
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               22            1.46              7.73        752.20                24.04            True
   HON          100.00               14            1.27              2.08        232.35                23.78            True
   WDC           96.88               32            2.40              6.15        363.58                85.18            True
  SBUX           94.74               38            0.54              0.37         98.31                40.64            True
  FTNT           94.12               34            1.28              0.70         78.40                37.90            True
   AEP           92.59               27            0.52              0.49        135.25                19.01            True
  FAST           92.31               13            2.02              0.63         44.35                38.71            True
  GILD           91.67               12            1.37              1.35        139.87                21.91            True
  MPWR           91.43               35            1.00              9.52       1359.34                58.76            True
   WMT           90.91               22            1.02              0.90        124.67                26.20            True
   LIN           90.00               20            0.90              3.15        498.34                19.38            True
   XEL           90.00               10            1.05              0.59         79.58                20.57            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-15T11:00:05.898328-04:00  manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-15T10:55:05.902096-04:00  manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-15T10:40:05.814047-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T10:35:04.887046-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T10:25:06.545831-04:00  manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-15T09:40:04.895647-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T09:30:03.712505-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T00:00:03.433834-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-14T16:10:06.446292-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:05:03.434274-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415110005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415110005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415110005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415110005)

</details>
