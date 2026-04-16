# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 10:05:06 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$7,327.92`
- Equity: `$15,067.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$720.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  7740.0          3.9            4.3      231.34        231.79           720.0                  10.26         100.0               22              0.82         27.49           31.84                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NFLX           95.00               40            0.60              0.46        107.51                27.27            True
  MRVL           94.74               19            3.18              2.99        133.32                70.04            True
  NVDA           91.67               36            0.76              1.06        198.41                36.33            True
  ALNY           91.43               35            1.37              3.20        332.02                43.40            True
  ASML           90.91               11            3.72             38.63       1465.22                53.24            True
  SOXL           86.11               36            0.54              0.32         85.82               129.54            True
  KLAC           85.19               27            1.73             21.13       1739.05                51.26            True
  PLTR           83.87               31            1.56              1.55        141.48                63.23            True
  ISRG           83.33               12            2.41              7.92        464.97                23.09            True
  PYPL           82.35               34            0.79              0.27         49.45                36.71            True
  TSLA           82.14               28            1.71              4.70        389.94                50.86            True
  IDXX           81.82               44            0.52              2.11        579.85                25.44            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-16T10:05:06.442845-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T10:00:05.433710-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T09:55:01.387641-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-16T09:40:05.435541-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-16T09:35:04.828747-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-16T09:30:06.428916-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-16T09:25:06.428686-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-16T00:00:03.899170-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-15T16:10:06.073164-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
2026-04-15T16:05:06.125049-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416100506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416100506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416100506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416100506)

</details>
