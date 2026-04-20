# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 15:40:03 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$111.21`
- Equity: `$12,145.79`
- Realized PnL: `$2,120.42`
- Unrealized PnL: `$25.37`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   2      9     6720.93                 6749.64       746.77         749.96      746.77        749.96           28.71                   0.43         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
   HON      share share_fallback        HON       2026-04-20                   0     23     5288.28                 5284.94       229.93         229.78      229.93        229.78           -3.34                  -0.06         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20        6.775         5.4 -1237.5  -20.295203 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               11            1.58              2.59        232.44                24.45            True
   STX           94.29               35            1.71              6.56        544.94                70.39            True
   XEL           93.75               16            0.83              0.47         80.88                22.98            True
  SBUX           93.33               30            0.93              0.65         99.72                34.23            True
  INTC           92.86               14            4.21              2.02         67.63                74.75            True
  FAST           92.11               38            0.56              0.18         45.70                38.81            True
  GILD           91.67               12            1.40              1.35        137.06                20.86            True
  AVGO           91.30               23            1.83              5.21        404.31                45.93            True
  UPRO           90.62               32            0.97              0.85        124.87                56.64            True
  VRTX           90.00               40            0.52              1.61        440.51                26.94            True
  ORLY           88.89               36            0.79              0.52         93.49                22.78            True
   ROP           88.24               34            0.60              1.51        361.79                23.20            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-04-20T15:40:03.007489-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:35:05.448312-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:30:05.898034-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:25:06.452583-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:10:06.433548-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:05:06.429713-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T15:00:06.434401-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:55:06.431094-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:50:06.432200-04:00  entry_1500        entry {"allocated_cash": 5288.28, "asset_type": "share", "contract_symbol": "HON", "contracts": 23, "entry_option_price": 229.925, "execution_mode": "share_fallback", "matched_signals": 11, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 32.0, "option_spread_pct": 16.77, "option_volume": 3.0, "success_rate": 100.0, "ticker": "HON"}
2026-04-20T14:40:06.422017-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420154003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420154003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420154003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420154003)

</details>
