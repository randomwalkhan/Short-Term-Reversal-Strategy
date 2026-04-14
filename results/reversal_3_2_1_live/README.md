# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-14 09:35:06 EDT`
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

- Cash: `$7,229.00`
- Equity: `$13,250.08`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$105.08`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   1      8      5916.0                 6021.08        739.5         752.64       739.5        752.64          105.08                   1.78         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-14)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.06               34            1.15              2.81        348.95                85.45            True
  INTC           96.55               29            2.33              1.06         64.74                75.15            True
   STX           94.44               36            1.03              3.69        511.70                74.84            True
  ROST           93.10               29            0.53              0.82        220.60                24.81            True
   WMT           92.86               14            1.39              1.21        124.04                26.19            True
  FAST           91.67               12            2.21              0.71         45.50                37.61            True
  MPWR           91.43               35            0.78              7.54       1369.00                58.48            True
  COST           90.91               11            1.14              7.81        977.50                19.04            True
   AEP           90.91               11            0.96              0.90        134.07                18.89            True
 CMCSA           90.00               20            0.55              0.11         28.00                24.19            True
   CSX           85.71               21            0.97              0.29         42.23                21.75            True
   PEP           85.71               21            0.74              0.81        155.53                20.56            True
```

## Recent Events

```text
                    timestamp_et           slot   event_type                          detail
2026-04-14T09:35:06.430444-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:30:06.428322-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T09:25:06.428256-04:00    manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-14T01:39:11.037721-04:00 share_ext_0135 slot_skipped {"reason": "already_processed"}
2026-04-14T01:38:52.650663-04:00 share_ext_0135 slot_skipped {"reason": "already_processed"}
2026-04-14T00:08:05.269990-04:00 share_ext_0005 slot_skipped {"reason": "already_processed"}
2026-04-13T23:54:15.718712-04:00 share_ext_2350 slot_skipped {"reason": "already_processed"}
2026-04-13T16:00:05.899443-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-13T15:55:05.891523-04:00    manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-13T15:40:00.935651-04:00    manage_1530 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260414093506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260414093506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260414093506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260414093506)

</details>
