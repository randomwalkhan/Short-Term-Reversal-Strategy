# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-13 14:50:05 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Fallback execution: buy shares when the option fails the liquidity gate; use `+3% / -3%` for common-stock fallback and `+5% / -5%` for leveraged-ETF shares
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,229.00`
- Equity: `$13,142.52`
- Realized PnL: `$3,145.00`
- Unrealized PnL: `$-2.48`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct      option_liquidity_status
  REGN      share share_fallback       REGN       2026-04-13                   0      8      5916.0                 5913.52        739.5         739.19       739.5        739.19           -2.48                  -0.04         100.0               24              1.25           NaN             NaN                  24.22                  89.0            1.0               0.07 low_open_interest,low_volume
```

## Today's Closed Trades (2026-04-13)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  PLTR     option         option PLTR260522C00125000      5          2026-04-10         2026-04-13        12.06       13.88 910.0   15.091211 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  REGN          100.00               24            1.25              6.56        746.06                24.22            True
   HON          100.00               17            1.00              1.64        234.36                23.73            True
  ROST           92.86               28            0.56              0.86        220.79                24.81            True
   PEP           85.00               20            0.78              0.86        156.69                20.42            True
   EXC           83.33               12            0.93              0.32         48.43                21.28            True
  ODFL           82.86               35            0.65              0.95        207.94                24.62            True
  AMAT           81.48               27            1.80              5.02        397.34                55.88            True
  CSCO           80.95               21            0.74              0.43         82.04                28.42            True
   BKR           80.00               25            1.06              0.47         62.63                35.55            True
   XEL          100.00                2            1.94              1.12         81.90                18.59           False
  NVDA           92.11               38            0.23              0.30        188.62                35.03           False
  GILD           91.18               34            0.39              0.38        138.87                21.48           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                  detail
2026-04-13T14:50:05.902241-04:00  entry_1500        entry {"allocated_cash": 5916.0, "asset_type": "share", "contract_symbol": "REGN", "contracts": 8, "entry_option_price": 739.5, "execution_mode": "share_fallback", "matched_signals": 24, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 89.0, "option_spread_pct": 6.64, "option_volume": 1.0, "success_rate": 100.0, "ticker": "REGN"}
2026-04-13T14:40:01.908593-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T14:35:05.900098-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T14:30:05.902792-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T14:25:05.905782-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T13:40:03.882273-04:00 manage_1330 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T13:35:04.710153-04:00 manage_1330 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T13:30:01.722483-04:00 manage_1330 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T13:25:03.704935-04:00 manage_1330 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
2026-04-13T13:10:04.705330-04:00 manage_1300 slot_skipped                                                                                                                                                                                                                                                                                                                                         {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_2_live_equity_overall.png?v=20260413145005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_2_live_equity_1d.png?v=20260413145005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_2_live_equity.png?v=20260413145005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_2_live_equity_1m.png?v=20260413145005)

</details>
