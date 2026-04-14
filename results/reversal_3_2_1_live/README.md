# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 11:20:06 EDT`
Last processed slot: `manage_1130`

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

- Cash: `$7,229.00`
- Equity: `$13,280.60`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$135.60`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                  6051.6        739.5         756.45       739.5        756.45           135.6                   2.29         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  FANG          100.00               16            1.67              2.21        188.15                30.53            True
  INTC           95.24               21            3.41              1.56         64.53                75.15            True
   XEL           94.12               17            0.75              0.42         80.27                20.44            True
  COST           91.67               12            1.08              7.42        977.67                19.04            True
  MPWR           91.43               35            0.88              8.41       1368.63                58.48            True
  DDOG           87.80               41            0.65              0.50        109.86                53.71            True
  TMUS           87.50               24            1.02              1.37        191.84                20.34            True
  PCAR           85.71               28            1.03              0.92        126.99                27.21            True
  ADBE           81.82               44            0.52              0.88        239.73                37.72            True
   BKR           81.48               27            0.99              0.43         62.37                33.24            True
  PAYX           81.08               37            0.56              0.35         89.17                30.62            True
  CSCO           80.00               20            0.61              0.35         82.20                28.38            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-14T11:10:06.425817-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-14T11:05:06.519402-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-14T11:00:06.430912-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-14T10:55:06.431637-04:00 manage_1100 slot_skipped {"reason": "already_processed"}
2026-04-14T10:40:06.436642-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:35:06.425929-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:30:06.433815-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:25:06.434099-04:00 manage_1030 slot_skipped {"reason": "already_processed"}
2026-04-14T10:10:06.430685-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-14T10:05:06.431814-04:00 manage_1000 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414112006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414112006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414112006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414112006)

</details>
