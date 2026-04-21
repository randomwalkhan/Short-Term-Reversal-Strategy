# Reversal 3.2.3 Live Paper Test

Latest checkpoint (ET): `2026-04-21 15:35:05 EDT`
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

- Cash: `$6,100.20`
- Equity: `$11,959.30`
- Realized PnL: `$1,973.99`
- Unrealized PnL: `$-14.69`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct                  option_liquidity_status
  ROST      share share_fallback       ROST       2026-04-21                   0     26     5873.79                  5859.1       225.91         225.35      225.91        225.35          -14.69                  -0.25         95.24               21              1.02           NaN             NaN                  25.78                  88.0            6.0               0.17 low_open_interest,low_volume,wide_spread
```

## Today's Closed Trades (2026-04-21)

```text
ticker asset_type execution_mode instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price        pnl  return_pct           exit_reason
   HON      share share_fallback        HON     23          2026-04-20         2026-04-21   229.925003  222.725006 -165.59993   -3.131455 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
   AEP           94.74               19            0.66              0.62        133.02                13.52            True
  ROST           93.75               16            1.21              1.93        227.42                25.78            True
  SHOP           93.33               30            1.78              1.69        134.42                55.61            True
  NVDA           91.89               37            0.63              0.89        201.68                32.81            True
  CHTR           91.67               36            1.13              1.94        243.86                38.05            True
  UPRO           91.67               36            0.84              0.73        124.18                53.04            True
  ALNY           90.91               33            1.48              3.21        309.56                46.90            True
   LIN           90.48               21            0.86              2.98        496.87                19.90            True
  SBUX           90.00               20            1.31              0.91         98.56                31.75            True
  NFLX           90.00               10            2.29              1.52         94.18                46.83            True
  GILD           90.00               10            1.98              1.88        135.06                18.88            True
   MAR           89.19               37            0.61              1.62        378.03                30.20            True
```

## Recent Events

```text
                    timestamp_et        slot   event_type                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-04-21T15:35:05.716188-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T15:30:05.732127-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T15:25:01.726215-04:00 manage_1530 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T15:10:05.707514-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T15:05:05.718333-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T15:00:05.722865-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T14:55:05.717229-04:00  entry_1500 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T14:50:05.712479-04:00  entry_1500        entry {"allocated_cash": 5873.79, "asset_type": "share", "contract_symbol": "ROST", "contracts": 26, "entry_option_price": 225.915, "execution_mode": "share_fallback", "matched_signals": 21, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 88.0, "option_spread_pct": 17.04, "option_volume": 6.0, "success_rate": 95.24, "ticker": "ROST"}
2026-04-21T14:40:05.707420-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-04-21T14:35:05.698088-04:00 manage_1430 slot_skipped                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.2.3 Live Equity Overall](../../assets/reversal_3_2_1_live_equity_overall.png?v=20260421153505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.2.3 Live Equity 1D](../../assets/reversal_3_2_1_live_equity_1d.png?v=20260421153505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.2.3 Live Equity 1W](../../assets/reversal_3_2_1_live_equity.png?v=20260421153505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.2.3 Live Equity 1M](../../assets/reversal_3_2_1_live_equity_1m.png?v=20260421153505)

</details>
