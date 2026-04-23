# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 14:55:05 EDT`
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

- Cash: `$917.70`
- Equity: `$12,963.07`
- Realized PnL: `$2,953.99`
- Unrealized PnL: `$9.08`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                 5895.37       225.91         226.74      225.91        226.74           21.58                   0.37         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
  NVDA     option         option NVDA260618C00200000       2026-04-23                   0      5     6162.50                 6150.00        12.32          12.30      198.79        198.68          -12.50                  -0.20         95.24               21              1.83          41.3           41.38                  33.17              111167.0         4613.0               0.00                                       ok
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23         7.45       8.675 980.0   16.442953 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  NVDA           95.24               21            1.85              2.62        201.38                33.17            True
  TSLA           90.91               11            3.79             10.27        383.11                48.19            True
  VRTX           90.00               40            0.62              1.91        436.85                26.82            True
  UPRO           89.66               29            1.41              1.24        125.16                53.56            True
  ABNB           87.50               24            1.73              1.75        143.43                37.26            True
  DDOG           86.96               23            3.14              2.91        130.89                58.97            True
  AMAT           86.84               38            0.59              1.68        402.76                55.83            True
  ORLY           86.67               30            0.99              0.65         93.64                22.27            True
  CSCO           86.36               22            1.00              0.63         89.53                27.83            True
  DXCM           85.71               35            1.41              0.63         63.14                37.31            True
  BKNG           85.19               27            1.74              2.19        178.46                44.00            True
  ISRG           83.78               37            0.74              2.51        482.54                37.51            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                        detail
2026-04-23T14:55:05.925620-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:50:05.228027-04:00  entry_1500        entry {"allocated_cash": 6162.5, "asset_type": "option", "contract_symbol": "NVDA260618C00200000", "contracts": 5, "entry_option_price": 12.325, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 111167.0, "option_spread_pct": 0.41, "option_volume": 4613.0, "success_rate": 95.24, "ticker": "NVDA"}
2026-04-23T14:40:04.065338-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:35:04.153865-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:30:04.173942-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:25:01.235972-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:10:04.443812-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:05:01.396383-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:00:03.244541-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T13:55:06.322619-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260423145505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260423145505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260423145505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260423145505)

</details>
