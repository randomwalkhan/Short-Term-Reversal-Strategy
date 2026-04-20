# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 15:00:06 EDT`
Last processed slot: `entry_1500`

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
- Equity: `$12,164.15`
- Realized PnL: `$2,120.42`
- Unrealized PnL: `$43.73`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   2      9     6720.93                 6763.05       746.77         751.45      746.77        751.45           42.12                   0.63         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
   HON      share share_fallback        HON       2026-04-20                   0     23     5288.28                 5289.88       229.93         229.99      229.93        229.99            1.61                   0.03         100.0               11              1.55           NaN             NaN                  24.45                  32.0            3.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20        6.775         5.4 -1237.5  -20.295203 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   HON          100.00               11            1.55              2.53        232.47                24.45            True
   STX           94.29               35            1.40              5.38        545.44                70.39            True
  INTC           94.12               17            3.96              1.90         67.69                74.75            True
  UPRO           91.89               37            0.73              0.64        124.96                56.64            True
  AVGO           90.48               21            2.07              5.90        404.01                45.93            True
  BKNG           89.74               39            0.65              0.88        191.63                38.41            True
  GILD           89.66               29            0.61              0.59        137.39                20.86            True
  PLTR           87.50               40            0.68              0.70        146.09                63.50            True
   PEP           87.50               24            0.71              0.78        157.33                20.25            True
  ORLY           87.10               31            0.95              0.62         93.44                22.78            True
  INSM           86.96               46            0.52              0.53        144.25                56.82            True
   ROP           86.67               30            0.84              2.14        361.52                23.20            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                                 detail
2026-04-20T15:00:06.434401-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:55:06.431094-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:50:06.432200-04:00  entry_1500        entry {"allocated_cash": 5288.28, "asset_type": "share", "contract_symbol": "HON", "contracts": 23, "entry_option_price": 229.925, "execution_mode": "share_fallback", "matched_signals": 11, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 32.0, "option_spread_pct": 16.77, "option_volume": 3.0, "success_rate": 100.0, "ticker": "HON"}
2026-04-20T14:40:06.422017-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:35:06.440002-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:30:06.428079-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:25:01.454961-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:10:06.433539-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:05:06.440826-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
2026-04-20T14:00:06.434380-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                                                        {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420150006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420150006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420150006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420150006)

</details>
