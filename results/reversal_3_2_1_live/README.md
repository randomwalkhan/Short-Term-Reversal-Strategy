# Reversal 3.2.2 Live Paper Test

Latest checkpoint (ET): `2026-04-16 15:55:05 EDT`
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

- Cash: `$6,636.99`
- Equity: `$13,356.48`
- Realized PnL: `$3,357.92`
- Unrealized PnL: `$-1.44`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   0      9     6720.93                 6719.49       746.77         746.61      746.77        746.61           -1.44                  -0.02         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-16)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct           exit_reason
   HON     option         option HON260515C00240000     18          2026-04-15         2026-04-16          3.9        3.35 -990.0  -14.102564 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               29            0.97              5.12        751.73                24.02            True
   HON          100.00               14            1.28              2.08        231.30                23.34            True
   WDC           97.14               35            0.85              2.18        364.06                79.90            True
  MRVL           96.67               30            1.32              1.25        134.07                70.04            True
  ROST           90.91               22            0.99              1.55        223.49                24.88            True
  BKNG           89.74               39            0.52              0.68        185.40                37.56            True
  VRTX           88.46               26            1.29              3.98        440.00                27.87            True
  GILD           86.96               23            0.92              0.90        139.39                21.89            True
  ORLY           86.67               30            0.98              0.64         93.32                23.50            True
   EXC           86.36               22            0.57              0.19         47.80                22.11            True
  KLAC           85.71               35            1.04             12.69       1742.67                51.26            True
  AMAT           83.87               31            1.31              3.61        392.71                56.17            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                        detail
2026-04-16T15:55:05.424408-04:00 manage_1600 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T15:40:06.417370-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T15:35:06.621941-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T15:30:06.430926-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T15:25:06.542766-04:00 manage_1530 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T15:20:06.408935-04:00 manage_1530         exit {"asset_type": "option", "contract_symbol": "HON260515C00240000", "fill_price": 3.35, "pnl": -990.0, "reason": "stop_loss_hit_at_scan", "return_pct": -14.1, "ticker": "HON"}
2026-04-16T15:10:06.430073-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T15:05:05.470311-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T15:00:05.944863-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
2026-04-16T14:55:06.168816-04:00  entry_1500 slot_skipped                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.2 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260416155505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.2 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260416155505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.2 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260416155505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.2 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260416155505)

</details>
