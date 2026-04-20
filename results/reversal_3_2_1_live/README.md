# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 14:45:06 EDT`
Last processed slot: `manual`

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

- Cash: `$5,399.49`
- Equity: `$12,163.62`
- Realized PnL: `$2,120.42`
- Unrealized PnL: `$43.20`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   2      9     6720.93                 6764.13       746.77         751.57      746.77        751.57            43.2                   0.64         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20        6.775         5.4 -1237.5  -20.295203 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  SBUX           94.87               39            0.51              0.36         99.85                34.23            True
   STX           94.29               35            1.58              6.04        545.16                70.39            True
  INTC           92.86               14            4.24              2.03         67.63                74.75            True
  UPRO           91.89               37            0.79              0.69        124.93                56.64            True
  AVGO           90.48               21            2.13              6.05        403.95                45.93            True
  CTAS           89.47               38            0.52              0.65        178.89                25.79            True
  BKNG           89.19               37            0.84              1.13        191.53                38.41            True
  GILD           88.89               27            0.79              0.76        137.31                20.86            True
   ROP           87.10               31            0.72              1.83        361.66                23.20            True
   PEP           86.96               23            0.76              0.84        157.31                20.25            True
   BKR           86.11               36            0.65              0.27         59.66                28.32            True
   EXC           85.71               21            0.72              0.24         46.92                20.08            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                          detail
2026-04-20T14:40:06.422017-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-20T14:35:06.440002-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-20T14:30:06.428079-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-20T14:25:01.454961-04:00 manage_1430 slot_skipped {"reason": "already_processed"}
2026-04-20T14:10:06.433539-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-20T14:05:06.440826-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-20T14:00:06.434380-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-20T13:55:06.437344-04:00 manage_1400 slot_skipped {"reason": "already_processed"}
2026-04-20T13:40:06.437809-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
2026-04-20T13:35:06.428825-04:00 manage_1330 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420144506)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420144506)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420144506)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420144506)

</details>
