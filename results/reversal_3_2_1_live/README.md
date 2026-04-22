# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-22 14:55:01 EDT`
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

- Cash: `$140.20`
- Equity: `$11,990.11`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$16.12`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback                ROST       2026-04-21                   1     26     5873.79                 5889.91       225.91         226.54      225.91        226.54           16.12                   0.27         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
  INTC     option         option INTC260618C00065000       2026-04-22                   0      8     5960.00                 5960.00         7.45           7.45       65.32         65.32            0.00                   0.00        100.00               34              1.42         70.65           70.59                  73.47               19823.0          361.0               0.01                                       ok
```

## Today's Closed Trades (2026-04-22)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  INTC          100.00               34            1.45              0.67         65.97                73.47            True
  REGN          100.00               33            0.68              3.55        745.84                22.93            True
   HON          100.00               23            0.89              1.39        221.62                25.07            True
  PCAR           89.19               37            0.66              0.58        125.93                27.36            True
   PEP           86.96               23            0.76              0.83        154.56                19.79            True
   CSX           86.36               22            0.97              0.29         43.24                16.22            True
  PAYX           85.00               40            0.64              0.42         93.50                30.98            True
  FAST           84.62               13            2.11              0.68         45.41                37.98            True
  DASH           83.33               42            0.59              0.76        182.12                52.99            True
   MAR           83.33               12            1.98              5.19        373.22                30.40            True
  CTAS           82.61               23            1.25              1.55        175.60                25.46            True
  MDLZ           82.61               23            0.56              0.22         56.04                19.49            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                    detail
2026-04-22T14:55:01.681230-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T14:50:03.700065-04:00  entry_1500        entry {"allocated_cash": 5960.0, "asset_type": "option", "contract_symbol": "INTC260618C00065000", "contracts": 8, "entry_option_price": 7.45, "execution_mode": "option", "matched_signals": 34, "option_liquidity_status": "ok", "option_open_interest": 19823.0, "option_spread_pct": 1.34, "option_volume": 361.0, "success_rate": 100.0, "ticker": "INTC"}
2026-04-22T14:40:00.880828-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T14:35:01.668405-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T14:30:00.682982-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T14:25:05.683900-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T14:10:00.707134-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T14:05:03.677671-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T14:00:03.862138-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
2026-04-22T13:55:04.717401-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                           {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260422145501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260422145501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260422145501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260422145501)

</details>
