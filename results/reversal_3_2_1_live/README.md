# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 15:55:06 EDT`
Last processed slot: `manage_1600`

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

- Cash: `$6,851.31`
- Equity: `$12,135.22`
- Realized PnL: `$2,139.59`
- Unrealized PnL: `$-4.37`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
   HON      share share_fallback        HON       2026-04-20                   0     23     5288.28                 5283.91       229.93         229.74      229.93        229.74           -4.37                  -0.08         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price          pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20      6.77500    5.400000 -1237.500000  -20.295203 stop_loss_hit_at_scan
  REGN      share share_fallback                REGN      9          2026-04-16         2026-04-20    746.77002  748.900024    19.170044    0.285229 time_exit_at_4pm_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               10            1.61              2.63        232.42                24.45            True
   STX           94.12               34            1.78              6.84        544.82                70.39            True
  INTC           92.86               14            4.29              2.06         67.62                74.75            True
  FAST           92.11               38            0.50              0.16         45.71                38.81            True
  SBUX           91.67               24            1.06              0.74         99.68                34.23            True
   XEL           91.67               12            1.02              0.58         80.83                22.98            True
  UPRO           91.43               35            0.83              0.73        124.92                56.64            True
  AVGO           91.30               23            1.86              5.31        404.27                45.93            True
  ORLY           87.10               31            0.99              0.65         93.43                22.78            True
   ROP           86.67               30            0.88              2.22        361.49                23.20            True
  ISRG           84.62               39            0.79              2.60        468.10                25.69            True
   AMD           84.38               32            1.31              2.56        277.29                54.39            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                         detail
2026-04-20T15:55:06.432735-04:00 manage_1600 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:50:06.460350-04:00 manage_1600         exit {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 748.9, "pnl": 19.17, "reason": "time_exit_at_4pm_scan", "return_pct": 0.29, "ticker": "REGN"}
2026-04-20T15:40:03.007489-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:35:05.448312-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:30:05.898034-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:25:06.452583-04:00 manage_1530 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:10:06.433548-04:00  entry_1500 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:05:06.429713-04:00  entry_1500 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T15:00:06.434401-04:00  entry_1500 slot_skipped                                                                                                                                {"reason": "already_processed"}
2026-04-20T14:55:06.431094-04:00  entry_1500 slot_skipped                                                                                                                                {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420155506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420155506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420155506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420155506)

</details>
