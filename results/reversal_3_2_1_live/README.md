# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 23:20:01 EDT`
Last processed slot: `share_ext_2320`

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
- Equity: `$13,607.80`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$462.80`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  FANG     option         option FANG260515C00185000       2026-04-14                   0      7      6160.0                  6510.0          8.8            9.3      186.41        186.02           350.0                   5.68         100.0               20              1.42         38.05           40.42                  30.53                 326.0           18.0               0.07                           ok
  REGN      share share_fallback                REGN       2026-04-13                   1      8      5916.0                  6028.8        739.5          753.6      739.50        753.60           112.8                   1.91         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

_None_

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T16:10:06.446292-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:05:03.434274-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T16:00:06.433014-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:55:03.439674-04:00 manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-14T15:40:03.444191-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:35:03.436506-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:30:05.437858-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:25:01.440627-04:00 manage_1530 slot_skipped {"reason": "already_processed"}
2026-04-14T15:10:01.444585-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
2026-04-14T15:05:06.434435-04:00  entry_1500 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414232001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414232001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414232001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414232001)

</details>
