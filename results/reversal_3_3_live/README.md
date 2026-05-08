# Reversal 3.3.2 Live Paper Test

Latest checkpoint (ET): `2026-05-08 15:50:02 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$15,258.50`
- Equity: `$31,598.50`
- Realized PnL: `$19,983.50`
- Unrealized PnL: `$1,615.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TEAM     option         option TEAM260618C00090000       2026-05-08                   0     19     14725.0                 16340.0         7.75            8.6       89.62         91.67          1615.0                  10.97         83.33               30              2.98         65.54           63.05                 115.49                2469.0          138.0               0.04                      ok
```

## Today's Closed Trades (2026-05-08)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   TXN     option         option TXN260618C00290000     10          2026-05-07         2026-05-08         13.1        15.5 2400.0   18.320611 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate
  TEAM           86.67               45            0.75              0.48         92.16               115.49         0.662          pass               28.13              3.606                                 ok            True
   XEL           92.86               14            1.12              0.63         80.16                27.43         0.555          pass                0.48              0.145                                 ok            True
  FAST           96.43               28            0.51              0.16         44.29                33.68         0.554          pass               -0.72             -0.062                                 ok            True
    ZS           83.78               37            1.06              1.13        152.30                60.77         0.513          pass               11.56              1.191                                 ok            True
   ADP           88.89               27            0.73              1.09        213.62                38.09         0.509          pass                8.14              0.721                                 ok            True
   HON           83.33               18            1.37              2.08        215.18                24.51         0.504          pass               -0.03              0.086                                 ok            True
  CHTR           69.23               13            3.05              3.42        158.77               119.32         0.763          pass              -13.76             -1.264            downtrend_blocked_slope           False
 CMCSA           75.00                4            3.03              0.56         26.00                61.43         0.633          pass               -7.67             -0.675 downtrend_blocked_slope_and_streak           False
  SHOP           90.00               30            1.99              1.56        111.07                82.33         0.592          pass              -12.97             -1.585 downtrend_blocked_slope_and_streak           False
  ORLY           78.57               14            1.55              1.03         94.14                34.97         0.542          pass               -0.02              0.208                                 ok           False
  MSFT           78.95               19            1.45              4.28        419.09                34.38         0.537          pass               -2.31             -0.284            downtrend_blocked_slope           False
  NFLX           88.24               34            0.93              0.57         88.02                43.15         0.535          pass               -5.40             -0.611            downtrend_blocked_slope           False
```

## Recent Events

```text
                    timestamp_et        slot     event_type                                                                                                                                                                                                                                                                                                                                                                            detail
2026-05-08T15:40:02.063692-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T15:35:05.923584-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T15:30:06.082521-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T15:25:06.105856-04:00 manage_1530   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T15:10:02.102478-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T15:05:03.959571-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T15:00:03.172365-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:55:02.174561-04:00  entry_1500   slot_skipped                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-05-08T14:50:08.791874-04:00  entry_1500          entry {"allocated_cash": 14725.0, "asset_type": "option", "contract_symbol": "TEAM260618C00090000", "contracts": 19, "entry_option_price": 7.75, "execution_mode": "option", "matched_signals": 30, "option_liquidity_status": "ok", "option_open_interest": 2469.0, "option_spread_pct": 3.87, "option_volume": 138.0, "success_rate": 83.33, "ticker": "TEAM", "timing_score": 0.621}
2026-05-08T14:50:08.791874-04:00  entry_1500 timing_overlay                                                                                                                                                                                                                                                                      {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-08", "training_samples": 5000, "window": 5}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260508155002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260508155002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260508155002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260508155002)

</details>
