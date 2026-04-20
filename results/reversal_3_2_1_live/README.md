# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 15:50:06 EDT`
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
- Equity: `$12,131.54`
- Realized PnL: `$2,139.59`
- Unrealized PnL: `$-8.05`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
   HON      share share_fallback        HON       2026-04-20                   0     23     5288.28                 5280.22       229.93         229.57      229.93        229.57           -8.05                  -0.15         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
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
   STX           94.29               35            1.72              6.60        544.92                70.39            True
   XEL           94.12               17            0.81              0.46         80.88                22.98            True
  INTC           92.31               13            4.42              2.12         67.59                74.75            True
  FAST           91.67               36            0.60              0.19         45.70                38.81            True
  SBUX           91.67               24            1.09              0.76         99.67                34.23            True
  UPRO           90.91               33            0.89              0.78        124.89                56.64            True
  AVGO           90.91               22            1.92              5.46        404.20                45.93            True
  GILD           90.91               11            1.53              1.48        137.01                20.86            True
  NFLX           90.00               10            2.37              1.61         96.62                45.70            True
  ORLY           88.24               34            0.82              0.54         93.48                22.78            True
  PLTR           87.50               40            0.53              0.54        146.16                63.50            True
   ROP           87.10               31            0.69              1.74        361.69                23.20            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-04-20T15:50:06.460350-04:00 manage_1600         exit                                                                                                                                                                                                                         {"asset_type": "share", "contract_symbol": "REGN", "fill_price": 748.9, "pnl": 19.17, "reason": "time_exit_at_4pm_scan", "return_pct": 0.29, "ticker": "REGN"}
2026-04-20T15:40:03.007489-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:35:05.448312-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:30:05.898034-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:25:06.452583-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:10:06.433548-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:05:06.429713-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:00:06.434401-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:55:06.431094-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:50:06.432200-04:00  entry_1500        entry {"allocated_cash": 5288.28, "asset_type": "share", "contract_symbol": "HON", "contracts": 23, "entry_option_price": 229.925, "execution_mode": "share_fallback", "matched_signals": 11, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 32.0, "option_spread_pct": 16.77, "option_volume": 3.0, "success_rate": 100.0, "ticker": "HON"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420155006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420155006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420155006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420155006)

</details>
