# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-15 09:30:03 EDT`
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
- Equity: `$13,565.00`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$420.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   1      7      6160.0                  6440.0          8.8            9.2      186.41        186.02           280.0                   4.55         100.0               20              1.42         38.05             0.0                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   2      8      5916.0                  6056.0        739.5          757.0      739.50        757.00           140.0                   2.37         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-15)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               19            1.04              1.69        232.51                23.78            True
   WDC           97.06               34            1.39              3.56        364.69                85.18            True
  NFLX           93.94               33            0.85              0.63        105.97                27.68            True
   WMT           93.75               16            1.24              1.08        124.59                26.20            True
   STX           92.31               26            3.03             11.32        528.59                74.84            True
   LIN           92.31               13            1.39              4.86        497.60                19.38            True
   XEL           92.31               13            0.91              0.51         79.61                20.57            True
  MPWR           91.67               36            0.75              7.20       1360.33                58.76            True
  COST           90.62               32            0.62              4.21        972.99                19.02            True
  ORLY           88.89               36            0.76              0.50         93.31                24.04            True
  FAST           87.50               16            1.65              0.51         44.40                38.71            True
  SOXL           86.11               36            0.61              0.36         85.23               129.42            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-15T09:30:03.712505-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-15T00:00:03.433834-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-14T16:10:06.446292-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:05:03.434274-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:00:06.433014-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:55:03.439674-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:40:03.444191-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:35:03.436506-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:30:05.437858-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:25:01.440627-04:00  manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260415093003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260415093003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260415093003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260415093003)

</details>
