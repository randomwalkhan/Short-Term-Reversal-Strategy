# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 09:40:05 EDT`
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

- Cash: `$7,327.92`
- Equity: `$14,887.92`
- Realized PnL: `$4,347.92`
- Unrealized PnL: `$540.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   HON     option         option HON260515C00240000       2026-04-15                   1     18      7020.0                  7560.0          3.9            4.2      231.34        233.17           540.0                   7.69         100.0               22              0.82         27.49            3.13                  23.78                2322.0          110.0               0.05                      ok
```

## Today's Closed Trades (2026-04-16)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  MRVL           96.15               26            2.34              2.21        133.65                70.04            True
  NFLX           94.12               34            0.87              0.65        107.43                27.27            True
  ASML           92.86               14            3.03             31.48       1468.28                53.24            True
  ALNY           92.68               41            0.96              2.24        332.43                43.40            True
  NVDA           91.67               36            0.72              1.00        198.44                36.33            True
  MDLZ           88.89               18            0.69              0.27         56.46                20.45            True
  KLAC           85.00               20            2.23             27.28       1736.42                51.26            True
  INSM           84.38               32            1.45              1.49        146.10                55.95            True
  ISRG           83.33               36            0.89              2.92        467.11                23.09            True
  AAPL           83.33               18            1.45              2.70        265.27                21.71            True
  AMZN           82.86               35            0.71              1.24        247.97                37.83            True
  AMAT           82.76               29            1.54              4.25        392.44                56.17            True
```

## Recent Events

```text
                    timestamp_et         slot   event_type                                                                                                                                                           detail
2026-04-16T09:40:05.435541-04:00  manage_0930 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-16T09:35:04.828747-04:00  manage_0930 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-16T09:30:06.428916-04:00  manage_0930 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-16T09:25:06.428686-04:00  manage_0930 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-16T00:00:03.899170-04:00 data_refresh data_refresh                                                                                                                                                    {'saved': 99}
2026-04-15T16:10:06.073164-04:00  manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T16:05:06.125049-04:00  manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T16:00:04.897355-04:00  manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:55:00.685389-04:00  manage_1600 slot_skipped                                                                                                                                  {"reason": "already_processed"}
2026-04-15T15:50:05.921508-04:00  manage_1600         exit {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 754.24, "pnl": 117.92, "reason": "time_exit_at_4pm_scan", "return_pct": 1.99, "ticker": "REGN"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416094005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416094005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416094005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416094005)

</details>
