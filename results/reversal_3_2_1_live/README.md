# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-20 10:50:05 EDT`
Last processed slot: `manage_1100`

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
- Equity: `$12,166.41`
- Realized PnL: `$2,120.42`
- Unrealized PnL: `$45.99`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-16                   2      9     6720.93                 6766.92       746.77         751.88      746.77        751.88           45.99                   0.68         100.0               30              0.95           NaN             NaN                  24.02                  51.0            3.0               0.15 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-20)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  INTC     option         option INTC260529C00068000      9          2026-04-17         2026-04-20        6.775         5.4 -1237.5  -20.295203 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   WDC           97.14               35            1.40              3.66        370.95                78.62            True
  INTC           95.24               21            3.60              1.73         67.76                74.75            True
  NFLX           93.33               15            1.89              1.29         96.76                45.70            True
   STX           92.59               27            2.49              9.54        543.66                70.39            True
  AVGO           92.00               25            1.74              4.96        404.42                45.93            True
  NVDA           92.00               25            1.29              1.83        200.90                35.90            True
  SBUX           90.91               22            1.17              0.82         99.65                34.23            True
  GILD           90.32               31            0.55              0.53        137.41                20.86            True
  BKNG           90.00               40            0.57              0.77        191.68                38.41            True
  UPRO           89.66               29            1.39              1.22        124.71                56.64            True
   MAR           89.19               37            0.55              1.46        377.31                31.36            True
  PLTR           86.84               38            1.17              1.20        145.87                63.50            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                          detail
2026-04-20T10:40:00.901789-04:00 manage_1030 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T10:35:00.907804-04:00 manage_1030 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T10:30:01.916831-04:00 manage_1030 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T10:25:03.898715-04:00 manage_1030 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T10:20:05.896862-04:00 manage_1030         exit {"asset_type": "option", "contract_symbol": "INTC260529C00068000", "fill_price": 5.4, "pnl": -1237.5, "reason": "stop_loss_hit_at_scan", "return_pct": -20.3, "ticker": "INTC"}
2026-04-20T10:10:00.900486-04:00 manage_1000 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T10:05:01.895753-04:00 manage_1000 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T10:00:02.779107-04:00 manage_1000 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T09:55:05.914542-04:00 manage_1000 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
2026-04-20T09:40:05.897388-04:00 manage_0930 slot_skipped                                                                                                                                                 {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260420105005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260420105005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260420105005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260420105005)

</details>
