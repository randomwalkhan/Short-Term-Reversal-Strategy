# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-23 15:00:02 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$917.70`
- Equity: `$13,045.50`
- Realized PnL: `$2,953.99`
- Unrealized PnL: `$91.51`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  NVDA     option         option NVDA260618C00200000       2026-04-23                   0      5     6162.50                  6237.5        12.32          12.48      198.79        198.41           75.00                   1.22         95.24               21              1.83          41.3           42.54                  33.17              111167.0         4613.0               0.00                                       ok
  ROST      share share_fallback                ROST       2026-04-21                   2     26     5873.79                  5890.3       225.91         226.55      225.91        226.55           16.51                   0.28         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-23)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price   pnl  return_pct                  exit_reason
  INTC     option         option INTC260618C00065000      8          2026-04-22         2026-04-23         7.45       8.675 980.0   16.442953 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  UPRO           92.59               27            1.70              1.50        125.05                53.56            True
  AMAT           85.71               35            0.88              2.49        402.41                55.83            True
  KLAC           86.49               37            0.60              7.58       1808.81                51.27            True
  AVGO           91.67               36            0.63              1.85        421.85                44.55            True
  CSCO           86.36               22            1.09              0.69         89.51                27.83            True
    MU           81.25               32            2.59              8.84        483.69                79.49            True
  NVDA           94.44               18            2.00              2.84        201.28                33.17            True
  META           68.75               16            2.50             11.78        669.67                51.97           False
  NFLX           97.78               45            0.20              0.13         93.18                46.34           False
  ASML           78.95               19            2.66             26.92       1432.12                53.38           False
   WBD           78.57               14            1.02              0.20         27.25                 7.69           False
   HON          100.00                3            2.61              4.02        218.25                25.23           False
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                        detail
2026-04-23T15:00:02.837489-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:55:05.925620-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:50:05.228027-04:00  entry_1500        entry {"allocated_cash": 6162.5, "asset_type": "option", "contract_symbol": "NVDA260618C00200000", "contracts": 5, "entry_option_price": 12.325, "execution_mode": "option", "matched_signals": 21, "option_liquidity_status": "ok", "option_open_interest": 111167.0, "option_spread_pct": 0.41, "option_volume": 4613.0, "success_rate": 95.24, "ticker": "NVDA"}
2026-04-23T14:40:04.065338-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:35:04.153865-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:30:04.173942-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:25:01.235972-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:10:04.443812-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:05:01.396383-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
2026-04-23T14:00:03.244541-04:00 manage_1400 slot_skipped                                                                                                                                                                                                                                                                                                                               {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260423150002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260423150002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260423150002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260423150002)

</details>
